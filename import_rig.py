from typing import BinaryIO
from .esk_file_obj import *
import bpy
import bmesh
import numpy as np
from mathutils import Vector, Matrix, Euler
import re
import math

import os

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

def rot_edit_bone(bone, rig, quaterion: np.array):
    euler = quaterion_to_euler(x=quaterion[0],
                               y=quaterion[1],
                               z=quaterion[2],
                               w=quaterion[3])
    #print(euler)
    edit = rig.data.edit_bones[bone.name]
    if edit:
        #x, y, z = edit.parent.matrix.to_3x3().col
        #print(edit.name)
        #if "Hand" in edit.name:
        #    print("HAND")
        #    R = (Matrix.Translation(edit.head) @
        #         Matrix.Rotation(math.radians(euler[0]), 4, edit.x_axis.normalized()) @
        #         Matrix.Translation(-edit.head))
        #    edit.transform(R, roll=True)  #applying active ORI.x to active bone
        #    #print("###################")
        #    #print(Matrix.Translation(edit.head))
        #    #print(Matrix.Rotation(math.radians(euler[0]), 4, edit.x_axis.normalized()))
        #    #print(Matrix.Translation(-edit.head))
        #    #print("===================")
        #    #print(Matrix.Translation(edit.head) @
        #    #      Matrix.Rotation(math.radians(euler[0]), 4, edit.x_axis.normalized()) @
        #    #      Matrix.Translation(-edit.head))
        #    #print("###################")
        #    pass
        #else:
        R = (Matrix.Translation(edit.head) @
             Matrix.Rotation(math.radians(euler[0]), 4, edit.x_axis.normalized()) @
             Matrix.Translation(-edit.head))
        edit.transform(R, roll=True)  #applying active ORI.x to active bone
        R = (Matrix.Translation(edit.head) @
             Matrix.Rotation(math.radians(euler[1]), 4, edit.y_axis.normalized()) @
             Matrix.Translation(-edit.head))
        edit.transform(R, roll=True)  #applying active ORI.y to active bone
        R = (Matrix.Translation(edit.head) @
             Matrix.Rotation(math.radians(euler[2]), 4, edit.z_axis.normalized()) @
             Matrix.Translation(-edit.head))
        edit.transform(R, roll=True)  #applying active ORI.z to active bone
        ##if edit.parent is not None and not ("Hand" in edit.name):
        ##    print("PARENT RELATION")
        ##    R = (Matrix.Translation(edit.head) @
        ##         Matrix.Rotation(edit.parent.x_axis.normalized()[0], 4, x) @
        ##         Matrix.Translation(-edit.parent.head))
        ##    edit.transform(R, roll=True)  #applying parent's ORI.x to active bone
        ##    
        ##    R = (Matrix.Translation(edit.head) @
        ##         Matrix.Rotation(edit.parent.y_axis.normalized()[0], 4, y) @
        ##         Matrix.Translation(-edit.parent.head))
        ##    edit.transform(R, roll=True)  #applying parent's ORI.y to active bone
        ##    
        ##    R = (Matrix.Translation(edit.head) @
        ##         Matrix.Rotation(edit.parent.z_axis.normalized()[0], 4, z) @
        ##         Matrix.Translation(-edit.head))
        ##    print("###################")
        ##    print(Matrix.Translation(edit.head))
        ##    print(Matrix.Rotation(edit.parent.z_axis.normalized()[0], 4, z))
        ##    print(Matrix.Translation(-edit.head))
        ##    print("===================")
        ##    print(Matrix.Translation(edit.head) @
        ##          Matrix.Rotation(edit.parent.z_axis.normalized()[0], 4, z) @
        ##          Matrix.Translation(-edit.head))
        ##    print("###################")
        ##    
        ##    edit.transform(R, roll=True)  #applying parent's ORI.z to active bone
        
            
    #R = Matrix.Rotation(math.radians(euler[0]),4,bone.x_axis.normalized())
    #bone.transform(R,roll=True)

    #R = Matrix.Rotation(math.radians(euler[1]), 4, bone.y_axis.normalized())
    #bone.transform(R, roll=True)

    #R = Matrix.Rotation(math.radians(euler[2]), 4, bone.z_axis.normalized())
    #bone.transform(R, roll=True)

    #offset_vec = -(bone.head - old_head)
    #bone.head += offset_vec
    #bone.tail += offset_vec
    pass


def rot_bone_poseMethod(bone, rig, quaternion: np.array):
    #print(bone.name)
    rig.pose.bones[bone.name].rotation_quaternion.x = quaternion[0]
    rig.pose.bones[bone.name].rotation_quaternion.y = quaternion[1]
    rig.pose.bones[bone.name].rotation_quaternion.z = quaternion[2]
    rig.pose.bones[bone.name].rotation_quaternion.w = quaternion[3]


def get_hierarchy(hlist,current_arm, Skel):
    hierlist = Skel.BoneHierarchy
    
    value = 0
    if np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0:2], keepSpaces=False)), np.uint16)[0] == 65535:
        startFrom = 2
        #print("FIRST 16 OOF18:\t", hlist[2:16 + 2])
        #print("FIRST 16 HIERA:\t", Skel.tempcall[Skel.offset_bonesHierarchy:][2:16 + 2])
    else:
        startFrom = 0
    for ind in range(0,len(hlist[startFrom:]),8):
        if not ind:
            #print(hlist[startFrom:][ind:ind + 8])
            pass
        check_temp = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[startFrom:][ind:ind + 8], keepSpaces=False)), np.uint16)
        if check_temp[0] == 65535:
            if check_temp[1] != 65535:
                display_temp = np.frombuffer(
                    bytes.fromhex(hexList2hexStrList(hlist[startFrom:][ind:ind + 8], keepSpaces=False)), np.uint16)
                print()
                print("HIERARCHY ACTIVE METHOD",display_temp)
                print("HIERARCHY OBJECT METHOD",hierlist[value].HierList)
                current_arm.bones[display_temp[1]].parent = current_arm.bones[display_temp[3]]
                pass
            else:
                pass
            value += 1
        else:
            display_temp = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[startFrom:][ind:ind+8],keepSpaces=False)),np.uint16)
            current_arm.bones[display_temp[0]].parent = current_arm.bones[display_temp[3]]
            if display_temp[1] != 65535:
                print()
                print("HIERARCHY ACTIVE METHOD",display_temp)
                #print("\t", "Parent: " + str(current_arm.bones.index(display_temp[3])),
                #            "Child:  " + str(current_arm.bones.index(display_temp[1])))
                print("HIERARCHY OBJECT METHOD",hierlist[value].HierList)
                current_arm.bones[display_temp[1]].parent = current_arm.bones[display_temp[3]].parent
            else:
                print()
                print("HIERARCHY ACTIVE METHOD", display_temp)
                #print("\t","Parent: "+str(current_arm.bones.index(display_temp[3])),
                #           "Child:  "+str(current_arm.bones.index(display_temp[0])))
                print("HIERARCHY OBJECT METHOD", hierlist[value].HierList)
                #print("\t", "Parent: " + str(),
                #            "Child:  " + str())
                pass
            value += 1
        #print()
    pass

def Reader(fileBytes, name):
    fileHex = hexify(fileBytes).split(' ')
    ESK = EskArmature(name, hlist=fileHex)
    return ESK

def import_armature(esk_file: BinaryIO, parent_collection=None, file_name=None, emd_objects=None):
    if parent_collection is None:
        parent_collection = bpy.context.scene.collection
    if file_name is None:
        file_name = 'new_armature'

    esk = Reader(esk_file.read(),file_name)
    new_collection = bpy.data.collections.new(file_name)
    bpy.context.scene.collection.children.link(new_collection)
    new_arm = bpy.data.armatures.new(esk.name)
    arm_object = bpy.data.objects.new(esk.name, new_arm)

    print(esk.skeleton.RelativeTransforms)

    for i in bpy.context.selected_objects:
        i.select = False

    new_collection.objects.link(arm_object)

    bpy.context.view_layer.objects.active = bpy.data.objects[esk.name]
    bpy.data.objects[esk.name].select = True

    arm = bpy.context.active_object
    bpy.ops.object.mode_set(mode="EDIT", toggle=False)

    for item in esk.bones:
        new_bone = arm.data.edit_bones.new(item.name)
        if item.parent is not None:
            new_bone.parent = arm.data.edit_bones[item.parent.name]
        else:
            new_bone.parent = None

        itemMatrix = [item.AbsoluteBoneMatrixL1,
                      item.AbsoluteBoneMatrixL2,
                      item.AbsoluteBoneMatrixL3,
                      item.AbsoluteBoneMatrixL4]
        ###itemMatrix = [tuple(itemMatrix[0]),
        ###              tuple([0.0, 0.0, 0.0, 0.0]),
        ###              tuple(itemMatrix[2]),
        ###              tuple(itemMatrix[3])]
        ######print("=========Absolute Matrix=========")
        ######print(item.name)
        ######print([keyItem for keyItem in item.ATML1])
        ######print([keyItem for keyItem in item.ATML2])
        ######print([keyItem for keyItem in item.ATML3])
        ######print([keyItem for keyItem in item.ATML4])
        ######print("=================================")
        if new_bone.parent is not None:
            new_bone.head.x = item.XYZ[0]*-1 + new_bone.parent.head.x
            new_bone.head.y = item.XYZ[1]    + new_bone.parent.head.y
            new_bone.head.z = item.XYZ[2]    + new_bone.parent.head.z
            if 'h_' in new_bone.name:
                new_bone.tail = (new_bone.head.x, 
                                 new_bone.head.y, 
                                 new_bone.head.z + 0.1)

            elif re.search('b_\w_Hand', new_bone.name) is not None:
                new_bone.tail = (new_bone.head.x,
                                 new_bone.head.y,
                                 new_bone.head.z - 0.1)
            else:
                new_bone.tail = (new_bone.head.x,
                                 new_bone.head.y + 0.1,
                                 new_bone.head.z)
        else:
            new_bone.head.x = item.XYZ[0]*-1
            new_bone.head.y = item.XYZ[1]
            new_bone.head.z = item.XYZ[2]
            new_bone.tail = (new_bone.head.x,
                             new_bone.head.y + 0.1,
                             new_bone.head.z)
        
        #rot_edit_bone(item, arm, item.ORI)
    bpy.ops.object.mode_set(mode="POSE", toggle=False)
    for item in esk.bones:
        print(item.name+":\t", quaterion_to_euler(x=item.ORI[0],
                                                  y=item.ORI[1],
                                                  z=item.ORI[2],
                                                  w=item.ORI[3]))
        rot_bone_poseMethod(item, arm, item.ORI)
        bpy.ops.pose.armature_apply(selected=False)
        if item.name == "h_R_Thumb1":
            rot_bone_poseMethod(item, arm, [0.5077766180038452, 0.4805839955806732, -0.10583944618701935, 0.7071067690849304])
            pass
        if item.name == "h_L_Thumb1":
            rot_bone_poseMethod(item, arm, [0.5077781081199646, -0.48058435320854187, 0.10583050549030304, 0.7071070075035095])
            pass
        bpy.ops.pose.armature_apply(selected=False)
        pass

    bpy.ops.object.mode_set(mode="OBJECT", toggle=False)
    #print([i.name for i in arm.pose.bones])

    ###for item in esk.bones:
    ###    current_Bone = arm.pose.bones[item.name]
    ###    if "Hand" in item.name:
    ###        current_Bone.rotation_quaternion.w = -0.707106
    ###        current_Bone.rotation_quaternion.x = 0.707108

    bpy.data.objects[esk.name].rotation_euler[0] = 1.5708
    #print(bpy.data.objects[esk.name].rotation_euler[0])
    bpy.data.objects[esk.name].rotation_euler[2] = -1.5708 * 2

    if emd_objects is not None:
        for i in emd_objects:
            ArmModName = 'Skin'
            i.modifiers.new(name=ArmModName, type='ARMATURE')
            i.modifiers[ArmModName].object = bpy.data.objects[esk.name]
    pass
