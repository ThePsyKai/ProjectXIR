from pathlib import Path
from typing import BinaryIO, Iterable, Sized, Union
from typing import *
import os

from .emd_file_obj import EmdModel
from .esk_file_obj import EskArmature
from .emd_file_obj import NewEMD

from .handlingHex import hexToHalfFloat

import bpy
import bmesh
import numpy as np
from mathutils import Vector, Matrix, Euler
import re
from math import *

#╔══════════════════════════════════════════════════════════════╗#
#║                      Quaterion -> Euler                      ║#
#║       ================================================       ║#
#║           Converts Quaterion (XYZW) to Euler (XYZ)           ║#
#╚══════════════════════════════════════════════════════════════╝#
def quaterion_to_euler(x,y,z,w):
    import math
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)

    X = math.degrees(math.atan2(t0,t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    Y = math.degrees(math.asin(t2))

    t3 = +2.0 * (w*z + x*y)
    t4 = +1.0 - 2.0 * (y*y + z*z)
    Z = math.degrees(math.atan2(t3,t4))

    return X, Y, Z

#╔═════════════════════════════════════════════════════════════╗#
#║                         Finds ESK 📁                        ║#
#║       ===============================================       ║#
#║           Checks and Grabs ESK Rig File for Model           ║#
#╚═════════════════════════════════════════════════════════════╝#
def esk_Locator(pathing, fileName):
    print()
    if 'scd.emd' in fileName:
        esk_file = pathing / (fileName[:-4] + '.esk')
        print(fileName)
        print(esk_file)
        if os.path.isfile(esk_file):
            return [esk_file ,fileName[:-4] + '.esk']
    else:
        esk_file = pathing / (fileName[:7] + '.esk')
        print(fileName)
        print(esk_file)
        if os.path.isfile(esk_file):
            return [esk_file ,fileName[:7] + '.esk']

#╔══════════════════════════════════════════════════════════════╗#
#║                       Import EMD Model                       ║#
#║       ================================================       ║#
#║       Reads Selected EMD File(s) and Generates Objects       ║#
#╚══════════════════════════════════════════════════════════════╝#
def import_model(emd_file: BinaryIO, file_directory, smooth, parent_collection=None, file_name=None, Import_ESK=False):
    from .emd_reader import Reader2 as Read_emd

    if parent_collection is None:
        parent_collection = bpy.context.scene.collection
    if file_name is None:
        file_name = 'new_EMD'

    esk_bytes = esk_Locator(file_directory,file_name)

    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode="OBJECT", toggle=False)

    emd = EmdModel()
    ModelFile = Read_emd(emd_file.read())
    objectList = []
    
    
    if ModelFile is not None:
        
        current_emd_count = len([[collect.name, collect] for collect in bpy.data.collections if
                                 collect.name != 'Collection' and '.emd' in collect.name])
        File_Collection = bpy.data.collections.new(file_name)
        File_Collection['XenoState'] = "XenoFile"
        File_Collection['Xeno_Properties'] = {'Name' : {'FileCode_Char' : file_name[:3],
                                                        'FileCode_Num'  : file_name[4:7],
                                                        'FileCode_Desc' : file_name[8:file_name.rindex('.')]
                                                        },
                                              'XenoModelList'           : []}
        bpy.context.scene.collection.children.link(File_Collection)
        core_object_list = []
        for i in bpy.context.selected_objects:
            print(i.name)
            i.select = False
        for Model in ModelFile.Models:
            Model_Collection = bpy.data.collections.new(Model.name)
            #Model_Collection.original
            Model_Collection['XenoState'] = "XenoModel"
            Model_Collection['Xeno_Properties'] = {'Name'           : Model.name,
                                                   'Parent'         : File_Collection,
                                                   'Index'          : ModelFile.Models.index(Model),
                                                   'XenoMeshList'   : []}
            File_Collection.children.link(Model_Collection)
            for Mesh in Model.Meshes:
                print(Mesh.name)
                objectList = []
                Mesh_Collection = bpy.data.collections.new(Mesh.name)
                Mesh_Collection['XenoState'] = "XenoMesh"
                Mesh_Collection['Xeno_Properties'] = {'Name'            : Mesh.name,
                                                      'Parent'          : Model_Collection,
                                                      'Index'           : Model.Meshes.index(Mesh),
                                                      
                                                      'XenoSubmeshList' : []}
                
                Model_Collection.children.link(Mesh_Collection)
                for CurrentSub in Mesh.SubMeshes:
                    print(CurrentSub.name)
                    current_submesh = bpy.data.meshes.new(name=CurrentSub.name)
                    new_SubMesh = bmesh.new()
                    allNormals = []

                    #╔═Create Vertices═╗#
                    for V in range(0, len(CurrentSub.Verts)):
                        new_SubMesh.verts.new()
                    new_SubMesh.verts.ensure_lookup_table()
                    #╔═Assign XYZ and Normals to Vertices═╗#
                    for V in range(0, len(CurrentSub.Verts)):
                        new_SubMesh.verts[V].co = CurrentSub.Verts[V].location
                        #new_SubMesh.verts[V].normal = CurrentSub.Verts[V].normal
                        allNormals.append(CurrentSub.Verts[V].normal)
                        
                    for Tris in CurrentSub.Triangles:
                        for faceInd in range(0, len(Tris.Faces)):
                            face = (new_SubMesh.verts[Tris.Faces[faceInd][0]], 
                                    new_SubMesh.verts[Tris.Faces[faceInd][1]],
                                    new_SubMesh.verts[Tris.Faces[faceInd][2]])
                            try:
                                new_SubMesh.faces.new(face)
                            except BaseException as ERR:
                                print(ERR)
                                pass

                    new_SubMesh.to_mesh(current_submesh)
                    new_object = bpy.data.objects.new(CurrentSub.name, current_submesh)
                    
                    new_object['XenoState'] = "XenoSubmesh"
                    
                    tempTexDefs = {}
                    for TD in CurrentSub.TextureDefs:
                        key = CurrentSub.TextureDefs.index(TD)
                        values = {'Flag0': int(TD.flag0), 
                                  'TexInd': int(TD.textureIndex), 
                                  'AddressMode_uv': int(TD.adressMode_uv), 
                                  'Filtering_minMag': int(TD.filtering_minMag), 
                                  'TexScaleU': float(TD.texture_scale_u), 
                                  'TexScaleV': float(TD.texture_scale_v)}
                        tempTexDefs.__setitem__(str("TexDef_"+str(key)), values)

                    new_object['Xeno_Properties'] = {'Name': CurrentSub.name,
                                                     'Parent': Mesh_Collection,
                                                     'Index': 0,
                                                     'TexDefs': tempTexDefs}
                    
                    #new_object['Xeno_Properties'].TexDefs   = [XenoTexDef()]*len(CurrentSub.TextureDefs)
                    #[new_object['Xeno_Properties'].TexDefs[TD].assignTexDefVals(CurrentSub.TextureDefs[TD]) for TD in range(0,len(CurrentSub.TextureDefs))]
                    
                    objectList.append(new_object)
                    core_object_list.append(new_object)

                    #╔═════════════════Submesh UV═════════════════╗#
                    if True:
                        submeshData = new_object.data #bpy.data.objects[new_object.name].data
                        NewMaterial = bpy.data.materials.new(new_object.name)

                        submeshData.materials.append(NewMaterial)
                        submeshData.uv_layers.new()
                        uv_data = submeshData.uv_layers[0].data
                        vertexInds = np.zeros((len(submeshData.loops)), dtype=np.uint32)
                        submeshData.loops.foreach_get('vertex_index', vertexInds)
                        
                        UVs = [v.UV for v in CurrentSub.Verts]
                        try:
                            UVcoors = [UVs[vertexInds[k]] for k in range(0, len(vertexInds))]
                            for loop in range(0, len(uv_data)):
                                uv_data[loop].uv = UVcoors[loop]
                        except BaseException as err:
                            print('UV Error for '+ submeshData.name)
                            print(err)
                            pass
                        pass
                    #╔═════════════════Vertex Groups═════════════════╗#
                    if True:
                        VG_Names = []
                        
                        faces = []
                        faceRange = []
                        for Tris in CurrentSub.Triangles:
                            [faces.append([F[0], F[1], F[2]]) for F in Tris.Faces]
                            newRange = []
                            for F in faces:
                                for FI in F:
                                    if FI not in newRange:
                                        newRange.append(FI)
                            print("RANGE:",newRange)
                            newRange.sort()
                            faceRange.append(newRange)
                            print("Face Range:", faceRange)
                            faces, newRange  = [], []
                            VG_Names.append(Tris.bone_names)
                            #for groupName in Tris.bone_names:
                            #    if groupName not in VG_Names:
                            #        VG_Names.append(groupName)
                            
                        print("VG_Names:", VG_Names)
                        for Group in VG_Names:
                            for GroupName in range(0,len(Group)):
                                if Group[GroupName] not in new_object.vertex_groups:
                                    new_object.vertex_groups.new(name=Group[GroupName])

                        
                        for CurRange in range(0,len(faceRange)):
                            print("[DEBUG] | Range Index:", CurRange)
                            for VertInd in faceRange[CurRange]:
                                #print("Vertex Index: " + str(VertInd), end="Angzarr")
                                CurVertex = CurrentSub.Verts[VertInd]
                                
                                vgInds = CurVertex.vgIndexes
                                weights = CurVertex.weights

                                printWeights = "["+str(VG_Names[CurRange][vgInds[0]])+","+str(vgInds[0])+","+str(weights[0])+"] "+\
                                               "["+str(VG_Names[CurRange][vgInds[1]])+","+str(vgInds[1])+","+str(weights[1])+"] "+\
                                               "["+str(VG_Names[CurRange][vgInds[2]])+","+str(vgInds[2])+","+str(weights[2])+"] "+\
                                               "["+str(VG_Names[CurRange][vgInds[3]])+","+str(vgInds[3])+","+str(weights[3])+"]"
                                #print(printWeights.split(" "))

                                for w in range(0, 4):
                                    try:
                                        new_object.vertex_groups[VG_Names[CurRange][vgInds[w]]].add(
                                            [int(VertInd)],
                                            weights[w],
                                            'ADD')
                                    except KeyError as err:
                                        print(err)
                        pass
                    
                    print(allNormals)
                    print(len(allNormals))
                    new_object.data.normals_split_custom_set_from_vertices(allNormals)
                    
                for i in range(0,len(objectList)):
                    Mesh_Collection.objects.link(objectList[i])
                    objectList[i]['Xeno_Properties']['Index'] = i
                #print("CORE OBJECT LIST:",core_object_list)
                for obj in core_object_list:
                    print("=====================\n", obj.name)
                    print("=====================")
                    bpy.data.objects[obj.name].rotation_euler[0] = 1.5708
                    bpy.data.objects[obj.name].rotation_euler[2] = -1.5708*2
                    bpy.data.objects[obj.name].scale.x = -1
                    bpy.data.objects[obj.name].select = True
                    
            if smooth:
                bpy.ops.object.shade_smooth()
            for i in bpy.context.selected_objects:
                i.select = False
            objectList = core_object_list
                
        if Import_ESK:
            esk_Locator(file_directory,file_name)
            parent_esk_file = esk_Locator(file_directory,file_name)#file_directory / file_name
            parent_esk_name = parent_esk_file[1]
            import_armature(esk_file=parent_esk_file[0].open('rb'), file_name=parent_esk_file[1], emd_objects=objectList)

def rot_edit_bone(bone,quaterion: np.array):
    #print(bone.name)
    #print(quaterion)
    #print(len(quaterion))
    euler = quaterion_to_euler(x=quaterion[0],
                               y=quaterion[1],
                               z=quaterion[2],
                               w=quaterion[3])
    #print(euler)
    old_head = bone.head.copy()

    R = Matrix.Rotation(radians(euler[0]),4,bone.x_axis.normalized())
    bone.transform(R,roll=True)

    R = Matrix.Rotation(radians(euler[1]), 4, bone.y_axis.normalized())
    bone.transform(R, roll=True)

    R = Matrix.Rotation(radians(euler[2]), 4, bone.z_axis.normalized())
    bone.transform(R, roll=True)

    offset_vec = -(bone.head - old_head)
    bone.head += offset_vec
    bone.tail += offset_vec
    pass
#╔═════════════════════════════════════════════════════════════╗#
#║                     Import ESK Armature                     ║#
#║       ===============================================       ║#
#║        Reads Selected ESK File(s) and Generates Rig         ║#
#╚═════════════════════════════════════════════════════════════╝#
def import_armature(esk_file: BinaryIO, parent_collection=None, file_name=None,emd_objects=None):
    from .import_rig import Reader as Read_esk
    if parent_collection is None:
        parent_collection = bpy.context.scene.collection
    if file_name is None:
        file_name = 'new_armature'

    esk = Read_esk(esk_file.read(), name=file_name)
    esk.name = file_name
    new_collection = bpy.data.collections.new(file_name)
    bpy.context.scene.collection.children.link(new_collection)
    new_arm = bpy.data.armatures.new(esk.name)
    arm_object = bpy.data.objects.new(esk.name,new_arm)

    for i in bpy.context.selected_objects:
        i.select = False

    new_collection.objects.link(arm_object)

    bpy.context.view_layer.objects.active = bpy.data.objects[esk.name]
    bpy.data.objects[esk.name].select = True

    arm = bpy.context.active_object
    bpy.ops.object.mode_set(mode="EDIT",toggle=False)

    for item in esk.bones:
        new_bone = arm.data.edit_bones.new(item.name)
        if item.parent is not None:
            new_bone.parent = arm.data.edit_bones[item.parent.name]
        else:
            new_bone.parent = None

        itemMatrix = [item.ATML1,
                      item.ATML2,
                      item.ATML3,
                      item.ATML4]

        itemMatrix = [tuple(itemMatrix[0]       ),
                      tuple([0.0, 0.0, 0.0, 0.0]),
                      tuple(itemMatrix[2]       ),
                      tuple(itemMatrix[3]       )]
        print("=========Absolute Matrix=========")
        print(item.name)
        print([keyItem for keyItem in item.ATML1])
        print([keyItem for keyItem in item.ATML2])
        print([keyItem for keyItem in item.ATML3])
        print([keyItem for keyItem in item.ATML4])
        print("=================================")

        #new_bone.matrix = tuple(itemMatrix)
        #new_bone.tail.y = -item.XYZ[1] + .1
        #print('===========================')

        if new_bone.parent is not None:

            new_bone.head.x = item.XYZ[0] + new_bone.parent.head.x
            new_bone.head.y = item.XYZ[1] + new_bone.parent.head.y
            new_bone.head.z = item.XYZ[2] + new_bone.parent.head.z

            if 'h_' in new_bone.name:
                new_bone.tail = (new_bone.head.x,
                                 new_bone.head.y,
                                 new_bone.head.z + .1)
                if 'Thumb' in new_bone.name:
                    pass
                    #print('Absolute:', [(Abs * -Abs) for Abs in item.ATML1])
                    #print('Absolute:', [(Abs * -Abs) for Abs in item.ATML2])
                    #print('Absolute:', [(Abs * -Abs) for Abs in item.ATML3])
                    #print('Absolute:', [(item.ATML4[Abs] * -abs(new_bone.parent.head[Abs])) for Abs in range(0,3)])
                    #print(new_bone.head)
                    #print()

                    #print(item.XYZ)

            elif re.search('b_\w_Hand',new_bone.name) is not None:
                new_bone.tail = (new_bone.head.x,
                                 new_bone.head.y,
                                 new_bone.head.z + .1)
                new_bone.tail.z -= 0.2
            else:
                new_bone.tail = (new_bone.head.x,
                                 new_bone.head.y + .1,
                                 new_bone.head.z)
        else:
            new_bone.head.x = item.XYZ[0]
            new_bone.head.y = item.XYZ[1]
            new_bone.head.z = item.XYZ[2]
            new_bone.tail = (new_bone.head.x,
                             new_bone.head.y + .1,
                             new_bone.head.z)

        ###rot_edit_bone(new_bone,item.ORI)
        
    bpy.ops.object.mode_set(mode="OBJECT", toggle=False)
    bpy.ops.object.mode_set(mode="OBJECT", toggle=False)
    for i in arm.pose.bones:
        pass
    print([i.name for i in arm.pose.bones])
    
    ###for item in esk.bones:
    ###    current_Bone = arm.pose.bones[item.name]
    ###    if "Hand" in item.name:
    ###        current_Bone.rotation_quaternion.w = -0.707106
    ###        current_Bone.rotation_quaternion.x = 0.707108
    
    bpy.data.objects[esk.name].rotation_euler[0] = 1.5708
    print(bpy.data.objects[esk.name].rotation_euler[0])
    bpy.data.objects[esk.name].rotation_euler[2] = -1.5708 * 2
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    
    if emd_objects is not None:
        for mesh in emd_objects:
            ArmModName = 'Skin'
            mesh.modifiers.new(name=ArmModName,type='ARMATURE')
            mesh.modifiers[ArmModName].object = bpy.data.objects[esk.name]
            mesh.parent = bpy.data.objects[esk.name]
            mesh.rotation_euler[0], mesh.rotation_euler[1], mesh.rotation_euler[2] = 0.0, 0.0, 0.0
    pass




class XenoFile:
    def __init__(self):
        self.FileCode_Char  = ""	#type: str
        self.FileCode_Num	= ""	#type: str
        self.FileCode_Desc	= ""	#type: str
        self.Name           = self.FileCode_Char+"_"+\
                              self.FileCode_Num+"_"+\
                              self.FileCode_Desc+".emd"
        self.XenoModelList	= []	#type: List[XenoModel]  #Only used when All XenoModels are merged
        pass
    pass


class XenoModel:
    def __init__(self):
        self.Name           = ""    #type: str
        self.Parent         = ""    #type: str
        self.Index          = 0     #type: int
        self.XenoMeshList   = []    #type: List[XenoMesh]
        pass
    pass

class XenoMesh:
    def __init__(self):
        self.Name               = ""    #type: str
        self.Parent             = ""    #type: str
        self.Index              = 0     #type: int
        self.XenoSubmeshList    = []    #type: List[XenoSubmesh]
        pass
    pass

class XenoSubmesh:
    def __init__(self):
        self.Name           = ""    #type: str
        self.Parent         = ""    #type: str
        self.Index          = 0     #type: int
        self.TexDefs        = []    #type: List[XenoTexDef]
    pass

class XenoTexDef:
    def __init__(self):
        self.Flag0              = []    #type: List
        self.TexIndex           = 0     #type: int
        self.AddressMode_uv     = []    #type: List
        self.Filtering_minMag   = []    #type: List
        self.TexScaleU          = []    #type: List
        self.TexScaleV          = []    #type: List
        
    def assignTexDefVals(self, TexDefSect):
        self.Flag0              = TexDefSect.flag0
        self.TexIndex           = TexDefSect.textureIndex
        self.AddressMode_uv     = TexDefSect.adressMode_uv
        self.Filtering_minMag   = TexDefSect.filtering_minMag
        self.TexScaleU          = TexDefSect.texture_scale_u
        self.TexScaleV          = TexDefSect.texture_scale_v
        pass
    pass
