import math
from pathlib import Path

import bpy
#from bpy.app.handlers import persistent
from typing import List
from bpy.props import StringProperty, BoolProperty, CollectionProperty, EnumProperty, FloatProperty, IntProperty
import time


class storage:
    emb_selecting = {}
    emb_dds = {}
    dyt_selecting = {}
    dyt_dds = {}

    all_images = []
    EMB_Initialize = True
    DYT_Initialize = True

    femb_selecting = {}

class UITools:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "XenoIR"
    bl_context = "objectmode"
    
class operator_methods:
    @classmethod
    def split_mesh(cls, current_context, ctx, mesh_objects=None, parent_mesh=None):
        if parent_mesh is None:
            parent_mesh = current_context.object['Xeno_Properties']['Parent']


        objs = [mat.name for mat in current_context.object['Xeno_Properties']['Materials']]
        objs.sort()
        mesh_collection = bpy.data.collections.new(current_context.object.name)
        mesh_collection['Xeno_Properties'] = {'Name': current_context.object.name,
                                              'Parent': parent_mesh,
                                              'Mesh Index': current_context.object['Xeno_Properties']['Mesh Index'],
                                              'XenoState': 'XenoMeshGroup'}

        bpy.data.collections[current_context.object['Xeno_Properties']['Parent'].name].children.link(mesh_collection)
        bpy.ops.mesh.separate(type='MATERIAL')
        if mesh_objects is None:
            mesh_list = bpy.context.selected_objects
            for item in mesh_list:
                item.name = item.data.materials[0].name
                mesh_collection.objects.link(item)
                bpy.data.collections[item['Xeno_Properties']['Parent'].name].objects.unlink(item)

                item['Xeno_Properties'] = {'Name': item.name,
                                           'Parent': mesh_collection,
                                           'Sub Index': objs.index(item.name),
                                           'XenoState': 'XenoSubmesh'}
        else:
            for item in mesh_objects:
                mesh_collection.objects.link(item)
                bpy.data.collections[current_context.object['Xeno_Properties']['Parent'].name].objects.unlink(item)
                item.name = item.data.materials[0].name

    @classmethod
    def split_model(cls, current_context, ctx, mesh_objects=None, parent_model=None):
        materials_per_mesh = current_context.object['Xeno_Properties']['MatsPerMesh']
        meshList = current_context.object['Xeno_Properties']['Meshes']
        model_collection = bpy.data.collections.new(current_context.object.name)
        bpy.context.scene.collection.children.link(model_collection)
        model_collection['Xeno_Properties'] = {'CharCode'    : current_context.object['Xeno_Properties']['CharCode'],
                                               'CharCode #'  : current_context.object['Xeno_Properties']['CharCode #'],
                                               'Model Type'  : current_context.object['Xeno_Properties']['Model Type'],
                                               'XenoState'   : 'XenoModelGroup'}

        bpy.ops.mesh.separate(type='MATERIAL')

        for item in meshList:
            selected = []

            for obj in bpy.context.selected_objects:
                if obj.data.materials[0].name in [mat.name for mat in materials_per_mesh[item.name]]:
                    selected.append(obj)
                    selected[0].name = item.name
            try:
                ctx['active_object'] = selected[0]
            except BaseException as err:
                print("ERROR")
                print(err.__traceback__)

            ctx['selected_editable_objects'] = selected

            selected[0]['Xeno_Properties'] = {'Name': item.name,
                                              'Parent': model_collection,
                                              'Mesh Index': meshList.index(item),
                                              'Materials': materials_per_mesh[item.name],
                                              'XenoState': 'XenoMeshGroup'}

            bpy.ops.object.join(ctx)

            model_collection.objects.link(ctx['active_object'])
            bpy.context.scene.collection.objects.unlink(ctx['active_object'])
        pass
    
class GlobalPropertyVals:
    @classmethod
    def pl3(cls, layout):
        File_Box = layout.box()
        Model_Box = layout.box()
        Mesh_Box = layout.box()
        Submesh_Box = layout.box()
        
        File_Coll = None
        Model_Coll = None
        Mesh_Coll = bpy.context.object.users_collection[0]
        Submesh = bpy.context.object
        for coll in bpy.data.collections:
            if bpy.context.object.users_collection[0] in list(coll.children):
                Model_Coll = coll
        for coll in bpy.data.collections:
            if Model_Coll in list(coll.children):
                File_Coll = coll

        File_Box.label(text='Xeno Properties - File')
        GlobalPropertyVals.__DisplayProperties(box=File_Box, obj=File_Coll)

        Model_Box.label(text='Xeno Properties - Model')
        GlobalPropertyVals.__DisplayProperties(box=Model_Box, obj=Model_Coll)

        Mesh_Box.label(text='Xeno Properties - Mesh')
        GlobalPropertyVals.__DisplayProperties(box=Mesh_Box, obj=Mesh_Coll)

        Submesh_Box.label(text='Xeno Properties - Submesh')
        GlobalPropertyVals.__DisplayProperties(box=Submesh_Box, obj=Submesh)

    @classmethod
    def pl2(cls, layout):
        File_Box = layout.box()
        Model_Box = layout.box()
        Mesh_Box = layout.box()

        File_Coll = bpy.context.object
        for coll in bpy.data.collections:
            if bpy.context.object.users_collection[0] in list(coll.children):
                File_Coll = coll
        Model_Coll = bpy.context.object.users_collection[0]
        Mesh_Coll = bpy.context.object

        File_Box.label(text='Xeno Properties - File')
        GlobalPropertyVals.__DisplayProperties(box=File_Box, obj=File_Coll)
        Model_Box.label(text='Xeno Properties - Model')
        GlobalPropertyVals.__DisplayProperties(box=Model_Box, obj=Model_Coll)
        Mesh_Box.label(text='Xeno Properties - Mesh')
        GlobalPropertyVals.__DisplayProperties(box=Mesh_Box, obj=Mesh_Coll)

    @classmethod
    def pl1(cls, layout):
        File_Box = layout.box()
        Model_Box = layout.box()
        
        File_Coll = bpy.context.object
        Model_Coll = bpy.context.object

        File_Box.label(text='Xeno Properties - File')
        GlobalPropertyVals.__DisplayProperties(box=File_Box, obj=File_Coll)
        Model_Box.label(text='Xeno Properties - Model')
        GlobalPropertyVals.__DisplayProperties(box=Model_Box,obj=Model_Coll)
    
    @classmethod
    def pl0 (cls, layout):
        File_Box = layout.box()
        File_Coll = bpy.context.object
        print(File_Coll['Xeno_Properties'])
        File_Box.label(text='Xeno Properties - File')
        GlobalPropertyVals.__DisplayProperties(box=File_Box, obj=File_Coll)
        pass

    @classmethod
    def __DisplayProperties(cls, box, obj):
        col = box.column()
        DontDisplay = ['XenoModelList', 'MatsPerMesh', 'XenoState', 'XenoMeshList', 'XenoSubmeshList']
        print('Object Properties:', obj['Xeno_Properties'])
        for item in obj['Xeno_Properties'].keys():
            if item not in DontDisplay:
                row = col.split(factor=0.4)
                row.label(text=item)
                item_Type = ""
                try:
                    obj['Xeno_Properties'][item].items()
                    item_Type = dict
                except AttributeError:
                    pass
                if item == "Name" and item_Type == dict:
                    row.label(text=obj['Xeno_Properties'][item]["FileCode_Char"]+"_"+
                                   obj['Xeno_Properties'][item]["FileCode_Num"]+"_"+
                                   obj['Xeno_Properties'][item]["FileCode_Desc"]+".emd")
                elif type(obj['Xeno_Properties'][item]) == dict or \
                        type(obj['Xeno_Properties'][item]) == list or \
                        type(obj['Xeno_Properties'][item]) == tuple:
                    subCol = row.column()
                    print(type(obj['Xeno_Properties'][item]))
                    if type(obj['Xeno_Properties'][item]) == list:
                        if item == 'Materials':
                            for mat in obj['Xeno_Properties']['Materials']:
                                subCol.label(text=str(mat.name))
                        elif item == 'Meshes':
                            for mat in obj['Xeno_Properties']['Meshes']:
                                subCol.label(text=str(mat.name))
                    else:
                        for mat in obj['Xeno_Properties'][item]:
                            subCol.label(text=str(mat))
                elif item == "TexDefs":
                    subCol = row.column()
                    for TexDef in list(obj['Xeno_Properties']['TexDefs'].keys()):
                        TexDefRow = subCol.split(factor=0.7)
                        TexDefRow.label(text=TexDef+": ")
                        TexDefRow.label(text=str(obj['Xeno_Properties']['TexDefs'][TexDef]['TexInd']))
                    
                    pass
                elif "Parent" == item:
                    row.label(text=str(obj['Xeno_Properties'][item].name))
                else:
                    row.label(text=str(obj['Xeno_Properties'][item]))


class SharedXenoPropertiesEnum(bpy.types.PropertyGroup):
    
    def emb_callback(self, context):
        print(storage.emb_dds)
        items = []
        if context.scene:
            for Selection in context.scene.Fake_EMBs:
                items.append(('OP' + str(len(items) + 1), Selection.name, ""))
            
            for it in context.scene.Fake_EMBs:
                for item in it.images:
                    storage.emb_dds.__setitem__(
                        "OP" + str(len(items)),
                        [it.name,[item.image]])
                    
            for it in items:
                storage.emb_selecting.__setitem__(
                    it[0], it[1])
        return items
    
    emb_selection : EnumProperty(
        name="EMB",
        items=emb_callback
    )
    
    def dyt_callback(self, context):
        items = []
        if context.scene:
            for Selection in context.scene.Fake_DYTs:
                items.append(('OP' + str(len(items) + 1), Selection.name, ""))

            for it in context.scene.Fake_DYTs:
                for item in it.images:
                    storage.dyt_dds.__setitem__(
                        "OP" + str(len(items)),
                        [it.name, [item.image]])

            for it in items:
                storage.dyt_selecting.__setitem__(
                    it[0], it[1])
        return items
    
    dyt_selection: EnumProperty(
        name="DYT",
        items=dyt_callback
    )

    def mat_callback(self, context):
        items = []
        if context.scene:
            for Selection in context.object.data.materials:
                items.append(('OP' + str(len(items) + 1), Selection.name, ""))

            for m in context.object.data.materials:
                print("OP" + str(len(items)), m.name)

        return items

    mat_selection: EnumProperty(
        name="",
        items=mat_callback
    )
    
    def femb_callback(self, context):
        items = []
        if context.scene:
            for Selection in context.scene.Fake_EMBs:
                items.append(('OP' + str(len(items) + 1), Selection.name, ""))

            for it in items:
                storage.femb_selecting.__setitem__(
                    it[0], it[1])
        return items
    
    femb_selection: EnumProperty(
        name="",
        items=femb_callback
    )

class SharedXenoPropertiesCollections(bpy.types.PropertyGroup):
    
    testing: CollectionProperty(
        name="Testing Shit",
        type=BoolProperty
    )

### Work In Progress ###
class XenoItem_PT_panel(UITools, bpy.types.Panel):
    bl_label = "Xeno Texture Panel"
    bl_idname = "xenoverse_ir.textures"

    @classmethod
    def poll(cls,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        
class MakeIntoXeno_OT_operator(bpy.types.Operator):
    bl_label = "Make Xeno Object"
    bl_idname = "xenoverse_ir.make_xenobject"
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.object is not None \
               and 'Xeno_Properties' not in context.object
    
    def execute(self,context):
        if len(context.object.data.materials) > 1:
            
            #operator_methods.split_mesh(context, ctx)
            context.object['Xeno_Properties'] = {'Name'     : context.object.name,
                                                 }
########################
class XenoProperties_PT_panel(UITools, bpy.types.Panel):
    bl_label = "Xeno Properties Panel"
    bl_idname = "xenoverse_ir.props"

    @classmethod
    def poll(cls,context):
        return context.object is not None \
               and 'Xeno_Properties' in context.object

    def draw(self, context):
        print("XenoProperties_PT_panel")
        layout = self.layout
        #print('.emd' in context.object.users_collection[0].name)
        XenoState = context.object['XenoState']
        print(XenoState)
        
        if XenoState == 'XenoFileGroup':
            GlobalPropertyVals.pl0(layout)
        elif XenoState == 'XenoModelGroup':
            GlobalPropertyVals.pl1(layout)
        elif XenoState == 'XenoMeshGroup':
            GlobalPropertyVals.pl2(layout)
        elif XenoState == 'XenoSubmesh':
            GlobalPropertyVals.pl3(layout)

class XenoImageProperty(bpy.types.PropertyGroup):
    emb_fakes = []
    dyt_fakes = []
    
    
class FakeEMBUser(bpy.types.PropertyGroup):
    name: StringProperty(
        name='Name'
    )
    image_count: IntProperty(
        name="Image Count"
    )
class EMB_Image(bpy.types.PropertyGroup):
    name: StringProperty(
        name="Name",
        description="A name for this item"
    )
    
    image: bpy.props.PointerProperty(type=bpy.types.Image)
    
    emd_index: IntProperty(
        name="EMB Index"
    )
    
    is_empty: BoolProperty(default=False)
    
class FakeDYTUser(bpy.types.PropertyGroup):
    name: StringProperty(
        name='Name'
    )
    
    image_count: IntProperty(
        name="Image Count"
    )
class DYT_Image(bpy.types.PropertyGroup):
    name: StringProperty(
        name="Name",
        description="A name for this item"
    )
    
    image: bpy.props.PointerProperty(type=bpy.types.Image)
    
    dyt_index: IntProperty(
        name="DYT Index"
    )



class XenoverseIRUtils_PT_panel(UITools, bpy.types.Panel):
    bl_label = "XenoverseIR Util Panel"
    bl_idname = "xenoverse_ir.utils"
    def draw(self, context):
        print("XenoverseIRUtils_PT_panel")
        
        layout = self.layout
        layout.label(text="XenoverseIR Tools")
        creditsBox = layout.box()
        creditsBox.label(text="Credits")
        scene = context.scene
        #layout.operator('projectxir.force_registering')
        
        embTool = scene.pointer_tools
        
        #texture_options.row().label(text="EMB (Line Work)")
        #texture_options.prop(embTool, 'emb_selection')
        
        #if scene.pointer_tools.emb_selection != '':
        #    EMB_UL_col = texture_options.column()
        #    EMB = scene.Fake_EMBs[
        #        storage.emb_selecting[scene.pointer_tools.emb_selection]]
        #    EMB_UL_row = EMB_UL_col.split(factor=0.9)
        #    EMB_UL_row.template_list(
        #        "EMBImageList_UL",  #listtype_name      ##UIList Class
        #        "",                 #list_id            ##???
        #        EMB,                #dataptr            ##Where to get property for listing
        #        "images",           #propname           ##Property Name
        #        scene,              #active_dataptr     ##Where to get index property
        #        "EMB_Image_ID"      #active_propname    ##Index Property Name
        #    )
        #    EMB_Actions = EMB_UL_row.column()
        #    EMB_Actions.operator("image.emb_add",icon="ADD")
        #    EMB_Actions.operator("image.emb_remove",icon="REMOVE")
        #    EMB_Actions.operator("image.emb_move_up", icon="TRIA_UP")
        #    EMB_Actions.operator("image.emb_move_down", icon="TRIA_DOWN")
        #    
        #    
        #    active_image = EMB.images[bpy.context.scene.EMB_Image_ID]
        #    EMB_UL_col.template_ID(
        #        active_image,           # ["AnyType"]     (probably a class object to act as a list)
        #        "image",                # [String]        (property name, but what property is wanted?)
        #        new="images.new",       # [String]        (Create new item of listing type)
        #        open="images.open",     # [String]        (Create new item of listing type by opening file)
        #        )
        #    if active_image.image is not None:
        #        active_image.name = active_image.image.name
        #    try:
        #        if (active_image.name == "Render Result"
        #                or active_image.name == "Viewer Node"
        #                or ".dyt.dds" in active_image.image.name) \
        #                and ".dds" not in active_image.image.name:
        #            active_image.image = None
        #            active_image.name = "INVALID IMAGE"
        #    except AttributeError:
        #        pass
        #    
        #    print(active_image.image)
        #    act_mat = bpy.context.object.data.materials[0]
        #    try:
        #        if active_image.image != act_mat.node_tree.nodes["LineWork_This"].image:
        #            act_mat.node_tree.nodes["LineWork_This"].image = active_image.image
        #    except:
        #        pass
        #texture_options.row().label(text="DYT (Colors)")
        #texture_options.prop(embTool, 'dyt_selection')
        print()
        #if scene.pointer_tools.dyt_selection != '':
        #    DYT_UL_col = texture_options.column()
        #    DYT = scene.Fake_DYTs[
        #        storage.dyt_selecting[scene.pointer_tools.dyt_selection]]
        #    DYT_UL_row = DYT_UL_col.split(factor=0.9)
        #    DYT_UL_row.template_list(
        #        "DYTImageList_UL",  #listtype_name      ##UIList Class
        #        "",                 #list_id            ##???
        #        DYT,                #dataptr            ##Where to get property for listing
        #        "images",           #propname           ##Property Name
        #        scene,              #active_dataptr     ##Where to get index property
        #        "DYT_Image_ID"      #active_propname    ##Index Property Name
        #    )
        #    DYT_Actions = DYT_UL_row.column()
        #    DYT_Actions.operator("image.dyt_add",icon="ADD")
        #    DYT_Actions.operator("image.dyt_remove",icon="REMOVE")
        #    DYT_Actions.operator("image.dyt_move_up", icon="TRIA_UP")
        #    DYT_Actions.operator("image.dyt_move_down", icon="TRIA_DOWN")

        #    active_image = DYT.images[bpy.context.scene.EMB_Image_ID]
        #    DYT_UL_col.template_ID(
        #        active_image,           # ["AnyType"]     (probably a class object to act as a list)
        #        "image",                # [String]        (property name, but what property is wanted?)
        #        new="images.new",       # [String]        (Create new item of listing type)
        #        open="images.open",     # [String]        (Create new item of listing type by opening file)
        #    )
        #    if active_image.image is not None:
        #        active_image.name = active_image.image.name
        #    try:
        #        if (active_image.name == "Render Result"
        #                or active_image.name == "Viewer Node"
        #                or ".dyt.dds" not in active_image.image.name)\
        #                and ".dds" not in active_image.image.name:
        #            active_image.image  = None
        #            active_image.name   = "INVALID IMAGE"
        #    except AttributeError:
        #        pass        
        #    
        objList = []
        if context.object is not None:
            try:
                if context.object['Xeno_Properties']['XenoState'] != 'XenoModelGroup':
                    for it in context.selected_objects:
                        if it['Xeno_Properties']['Parent'] not in objList:
                            objList.append(it['Xeno_Properties']['Parent'])
                if context.object['Xeno_Properties']['XenoState'] == 'XenoMeshGroup' \
                        or context.object['Xeno_Properties']['XenoState'] == 'XenoSubmesh' \
                        or context.object['Xeno_Properties']['XenoState'] == 'XenoModelGroup':
                    Tools = layout.box()
                    Tools.label(text="Mesh Tools")

                    row = Tools.row()

                    ObjectTools_1 = row.column()
                    ObjectTools_1.label(text="Single")
                    ObjectTools_1.operator("xenoverse_ir.merge_meshes")
                    ObjectTools_1.operator("xenoverse_ir.split_meshes")

                    # ObjectTools_2 = row.column()
                    # ObjectTools_2.label(text="Model")
                    # ObjectTools_2.operator("xenoverse_ir.merge_meshes")
                    # ObjectTools_2.operator("xenoverse_ir.split_meshes")
                    pass
            except:
                pass
            
            

        box = layout.box()
        box.label(text="Skinner")
        box.operator("xenoverse_ir.skin_mesh")
        box.operator("xenoverse_ir.skin_scd")


class MergeMesh_OT_operator(bpy.types.Operator):
    bl_label = "Merge"
    bl_idname = "xenoverse_ir.merge_meshes"
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        #if all('Xeno_Properties' in item.keys() for item in context.selected_objects):
        return all(item['Xeno_Properties']['XenoState'] != 'XenoModelGroup' for item in context.selected_objects) \
               and (all(item['Xeno_Properties']['XenoState'] == 'XenoSubmesh' for item in context.selected_objects)
                    or all(item['Xeno_Properties']['XenoState'] == 'XenoMeshGroup' for item in context.selected_objects))

    def execute(self,context):
        ctx = context.copy()

        parentList = dict([(it['Xeno_Properties']['Parent'], it) for it in context.selected_objects])
        objectList = [parentList[it2] for it2 in parentList]

        for obje in objectList:

            if '.mdl' in obje.name:
                pass
            elif obje['Xeno_Properties']['XenoState'] == 'XenoMeshGroup':
                parent_coll = obje['Xeno_Properties']['Parent']

                for coll in bpy.data.collections.keys():
                    if obje.name in bpy.data.collections[coll].objects.keys():
                        parent_coll = bpy.data.collections[coll]

                objs = parent_coll.objects
                materials = []
                materials.sort()
                mats_per_mesh = dict([(mes.name, mes.data.materials) for mes in objs])
                for mes in objs:
                    materials.extend(mes.data.materials)
                    mes.data.name = mes.name
                objs[0]['Xeno_Properties'] = {'CharCode': parent_coll.name[:3],
                                              'CharCode #': parent_coll.name[
                                                            4:
                                                            parent_coll.name.rindex('_')],

                                              'Model Type': parent_coll.name[
                                                            parent_coll.name.rindex('_')+1:
                                                            parent_coll.name.rindex('.')],
                                              'Meshes': [ob.data for ob in objs],
                                              'Materials': materials,
                                              'MatsPerMesh': mats_per_mesh,
                                              'XenoState': 'XenoModelGroup'}
                objs[0].name = parent_coll.name

                ctx['active_object'] = objs[0]
                ctx['selected_editable_objects'] = objs
                bpy.ops.object.join(ctx)

                bpy.context.scene.collection.objects.link(objs[0])
                bpy.data.collections.remove(parent_coll)
                pass
            elif '.mdl' not in obje.name and obje['Xeno_Properties']['XenoState'] == 'XenoSubmesh':
                objs = [obj for obj in obje['Xeno_Properties']['Parent'].objects]
                Mesh_Object = objs[0]
                parent_coll = Mesh_Object['Xeno_Properties']['Parent']['Xeno_Properties']['Parent']

                material_list = []

                for ob in range(0,len(objs)):
                    for ma in objs[ob].data.materials:
                        material_list.append(ma)
                mesh_collection = Mesh_Object['Xeno_Properties']['Parent']
                Mesh_Object['Xeno_Properties'] = {'Name'        : obje.users_collection[0].name,
                                                  'Parent'      : parent_coll,
                                                  'Mesh Index'  : obje.users_collection[0]['Xeno_Properties']['Mesh Index'],
                                                  'Materials'   : material_list,
                                                  'XenoState'   : 'XenoMeshGroup'}

                Mesh_Object.name = mesh_collection.name #obje.users_collection[0].name

                ctx['active_object'] = Mesh_Object
                ctx['selected_editable_objects'] = objs
                bpy.ops.object.join(ctx)

                parent_coll.objects.link(objs[0])
                bpy.data.collections.remove(mesh_collection)

        del ctx
        return {'FINISHED'}

class SplitMesh_OT_operator(bpy.types.Operator):
    bl_label = "Split"
    bl_idname = "xenoverse_ir.split_meshes"
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.object['Xeno_Properties']['XenoState'] == 'XenoModelGroup' or \
               context.object['Xeno_Properties']['XenoState'] == 'XenoMeshGroup'

    def execute(self, context):
        ctx = context.copy()
        if context.object['Xeno_Properties']['XenoState'] == 'XenoModelGroup':
            operator_methods.split_model(context, ctx)
        elif context.object['Xeno_Properties']['XenoState'] == 'XenoMeshGroup':
            operator_methods.split_mesh(context, ctx)
        return {'FINISHED'}

class SkinMesh_OT_operator(bpy.types.Operator):
    bl_idname = "xenoverse_ir.skin_mesh"
    bl_label = "Skin Mesh to Rig"
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        objectTypes = [obj.type for obj in context.selected_objects]
        selection_valid = 'ARMATURE' in objectTypes \
                          and 'MESH' in objectTypes \
                          and objectTypes.count('ARMATURE') == 1 and \
                          len(context.selected_objects) > 1 and \
                          context.object is not None
        return selection_valid

    def execute(self,context):
        objectTypes = [obj.type for obj in context.selected_objects]
        skinTo = context.selected_objects[objectTypes.index('ARMATURE')]
        for mesh in [obj for obj in context.selected_objects if obj.type != 'ARMATURE']:
            if 'ARMATURE' in [mod.type for mod in mesh.modifiers]:
                mesh.modifiers.remove(mesh.modifiers[
                                          [mod.type for mod in mesh.modifiers].index('ARMATURE')])
            modifier = mesh.modifiers.new('Skinned', 'ARMATURE')
            modifier.object = skinTo
            
            mesh.parent = skinTo
            mesh.rotation_euler[0], mesh.rotation_euler[1], mesh.rotation_euler[2] = 0.0, 0.0, 0.0
        self.report({'INFO'},"Skinned Mesh(es) To Rig!")
        return {'FINISHED'}

class SkinSCD_OT_operator(bpy.types.Operator):
    bl_idname = "xenoverse_ir.skin_scd"
    bl_label = "Skin SCD to Rig"
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        objectTypes = [obj.type for obj in context.selected_objects]
        selection_valid = 'ARMATURE' in objectTypes \
                          and objectTypes.count('ARMATURE') > 1 and \
                          len(context.selected_objects) > 1 and \
                          context.object is not None
        return selection_valid

    def execute(self,context):

        #objectTypes = [obj.type for obj in context.selected_objects]
        #skinTo = context.selected_objects[objectTypes.index('ARMATURE')]
        #for mesh in [obj for obj in context.selected_objects if 'SCD' in obj.name ]:
        #    modifier = mesh.modifiers.new('Skinned', 'ARMATURE')
        #    modifier.object = skinTo
        self.report({'INFO'},"Skinned SCD(s) To Rig!")
        return {'FINISHED'}

