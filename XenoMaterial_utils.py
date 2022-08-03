import math
from pathlib import Path

import bpy
#from bpy.app.handlers import persistent
from typing import List
from bpy.props import StringProperty, BoolProperty, CollectionProperty, EnumProperty, FloatProperty, IntProperty
from bpy.app.handlers import persistent
import time

class storage:
    emb_selecting = {}
    emb_dds = {}
    dyt_selecting = {}
    dyt_dds = {}
    mat_selecting = {}

    all_images = []
    EMB_Initialize = True
    DYT_Initialize = True

    femb_selecting = {}
    fdyt_selecting = {}

class UITools:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "XenoIR"
    bl_context = "objectmode"

class SharedXenoPropertiesEnum(bpy.types.PropertyGroup):

    def emb_callback(self, context):
        #print("EMB CALLBACK (storage.emb_dds):\t",storage.emb_dds)
        items = []
        if context.scene:
            for Selection in context.scene.Fake_EMBs:
                items.append(('OP' + str(len(items) + 1), Selection.name, ""))

            for it in context.scene.Fake_EMBs:
                for item in it.images:
                    storage.emb_dds.__setitem__(
                        "OP" + str(len(items)),
                        [it.name, [item.image]])

            for it in items:
                storage.emb_selecting.__setitem__(
                    it[0], it[1])
        return items

    emb_selection: EnumProperty(
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
            for it in items:
                storage.mat_selecting.__setitem__(
                    it[0], it[1])

            for m in context.object.data.materials:
                print("MAT CALLBACK:\t","OP" + str(len(items)), m.name)

        return items

    mat_selection: EnumProperty(
        name="",
        items=mat_callback
    )

    def femb_callback(self, context):
        #print(storage.emb_dds)
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
    
    def fdyt_callback(self, context):
        #print(storage.dyt_dds)
        items = []
        if context.scene:
            for Selection in context.scene.Fake_DYTs:
                items.append(('OP' + str(len(items) + 1), Selection.name, ""))
            for it in items:
                storage.fdyt_selecting.__setitem__(
                    it[0], it[1])
        return items

    fdyt_selection: EnumProperty(
        name="",
        items=fdyt_callback
    )

class DYTImageList_UL(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            if item:
                print("DYT ITEM: ", item.name, type(item))
                try:
                    layout.prop(item, "name", text="", emboss=False, icon_value=item.image.preview.icon_id)
                except AttributeError:
                    layout.prop(item, "name", text="", emboss=False, icon="OUTLINER_OB_IMAGE")
            else:
                layout.label(text="", icon="OUTLINER_OB_IMAGE")
class EMBImageList_UL(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            if item:
                print("EMB ITEM: ", item.name, type(item))
                try:
                    layout.prop(item, "name", text="", emboss=False, icon_value=item.image.preview.icon_id)
                except AttributeError:
                    layout.prop(item, "name", text="", emboss=False, icon="OUTLINER_OB_IMAGE")
            else:
                layout.label(text="", icon="OUTLINER_OB_IMAGE")

class EMB_OT_Add(bpy.types.Operator):
    bl_idname = "image.emb_add"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        Active_EMB = scene.Fake_EMBs[storage.emb_selecting[scene.pointer_tools.emb_selection]]
        added = Active_EMB.images.add()
        added.name = ""
        scene.EMB_Image_ID = len(Active_EMB.images) - 1
        return {'FINISHED'}
class EMB_OT_Remove(bpy.types.Operator):
    bl_idname = "image.emb_remove"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        active = scene.EMB_Image_ID
        Active_EMB = scene.Fake_EMBs[storage.emb_selecting[scene.pointer_tools.emb_selection]]
        Active_EMB.images.remove(active)
        scene.EMB_Image_ID -= 1
        return {'FINISHED'}
class EMB_OT_MoveUp(bpy.types.Operator):
    bl_idname = "image.emb_move_up"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        active = scene.EMB_Image_ID

        print('EMB Storage:\t', storage.emb_selecting)
        print('EMB Selection:\t', scene.pointer_tools.emb_selection)

        scene.Fake_EMBs[storage.emb_selecting[
            scene.pointer_tools.emb_selection]].images.move(active, active - 1)
        if active - 1 >= 0:
            scene.EMB_Image_ID -= 1
        return {'FINISHED'}
class EMB_OT_MoveDown(bpy.types.Operator):
    bl_idname = "image.emb_move_down"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        active = scene.EMB_Image_ID

        scene.Fake_EMBs[storage.emb_selecting[
            scene.pointer_tools.emb_selection]].images.move(active, active + 1)
        if active + 1 < len(scene.Fake_EMBs[storage.emb_selecting[
            scene.pointer_tools.emb_selection]].images):
            scene.EMB_Image_ID += 1
        return {'FINISHED'}

class DYT_OT_Add(bpy.types.Operator):
    bl_idname = "image.dyt_add"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        Active_DYT = scene.Fake_DYTs[storage.dyt_selecting[scene.pointer_tools.dyt_selection]]
        Active_DYT.images.add()
        scene.DYT_Image_ID = len(Active_DYT.images) - 1
        return {'FINISHED'}
class DYT_OT_Remove(bpy.types.Operator):
    bl_idname = "image.dyt_remove"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        active = scene.DYT_Image_ID
        Active_DYT = scene.Fake_DYTs[storage.dyt_selecting[scene.pointer_tools.dyt_selection]]
        Active_DYT.images.remove(active)
        return {'FINISHED'}
class DYT_OT_MoveUp(bpy.types.Operator):
    bl_idname = "image.dyt_move_up"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        active = scene.DYT_Image_ID

        print('DYT Storage:\t', storage.dyt_selecting)
        print('DYT Selection:\t', scene.pointer_tools.dyt_selection)

        scene.Fake_DYTs[storage.dyt_selecting[
            scene.pointer_tools.dyt_selection]].images.move(active, active - 1)
        if active - 1 >= 0:
            scene.DYT_Image_ID -= 1
        return {'FINISHED'}
class DYT_OT_MoveDown(bpy.types.Operator):
    bl_idname = "image.dyt_move_down"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        active = scene.DYT_Image_ID
        Active_DYT = scene.Fake_DYTs[storage.dyt_selecting[scene.pointer_tools.dyt_selection]]

        Active_DYT.images.move(active, active + 1)
        if active + 1 < len(Active_DYT.images):
            scene.DYT_Image_ID += 1
        return {'FINISHED'}

class temp_name:
    pass

class MaterialUtils_PT_panel(UITools, bpy.types.Panel):
    bl_label = "XenoverseIR Material"
    bl_idname = "xenoverse_ir.mat_utils"

    @classmethod
    def poll(cls, context):
        if context.active_object is not None:
            return context.active_object.type == "MESH"
        else:
            return False
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        embTool = scene.pointer_tools
        
        MatSel = layout.box()
        MatSel.row().label(text="Active Material:")
        MatSel.prop(embTool, 'mat_selection')
        active_material = bpy.data.materials[storage.mat_selecting[embTool.mat_selection]]
        
        texture_options = layout.box()
        ####EMB####
        texture_options.row().label(text="EMB (Linework)")
        texture_options.prop(embTool, 'emb_selection')
        #print("STORAGE:\t", storage.emb_selecting)
        #print("EMB_SELECTION:\t", scene.pointer_tools.emb_selection)
        #print("RETURN VAL:\t", storage.emb_selecting[scene.pointer_tools.emb_selection])
        if scene.pointer_tools.emb_selection != '':
            EMB_UL_col = texture_options.column()
            EMB = scene.Fake_EMBs[
                storage.emb_selecting[scene.pointer_tools.emb_selection]]
            EMB_UL_row = EMB_UL_col.split(factor=0.9)
            EMB_UL_row.template_list(
                "EMBImageList_UL",  # listtype_name      ##UIList Class
                "",                 # list_id            ##???
                EMB,                # dataptr            ##Where to get property for listing
                "images",           # propname           ##Property Name
                scene,              # active_dataptr     ##Where to get index property
                "EMB_Image_ID"      # active_propname    ##Index Property Name
                )
            EMB_Actions = EMB_UL_row.column()
            EMB_Actions.operator("image.emb_add", icon="ADD")
            EMB_Actions.operator("image.emb_remove", icon="REMOVE")
            EMB_Actions.operator("image.emb_move_up", icon="TRIA_UP")
            EMB_Actions.operator("image.emb_move_down", icon="TRIA_DOWN")

            print()
            print("#################################")
            print("ACTIVE EMB:\t",context.scene.ActiveEMB)
            print("#################################")
            print()


            active_image = EMB.images[bpy.context.scene.EMB_Image_ID]
            EMB_UL_col.template_ID(
                active_image,           # ["AnyType"]     (probably a class object to act as a list)
                "image",                # [String]        (property name, but what property is wanted?)
                new="images.new",       # [String]        (Create new item of listing type)
                open="images.open",     # [String]        (Create new item of listing type by opening file)
                )

            TexDef_row = EMB_UL_col.split(factor=0.9)
            
            EMB_UL_col.prop(scene, 'Texture_Definition')
            #embTool.mat_selection
            
            if context.scene.Texture_Definition >= len(EMB.images):
                context.scene.Texture_Definition = len(EMB.images)-1
            EMB_UL_col.label(text=EMB.images[context.scene.Texture_Definition].name)

            if active_image.image is not None:
                active_image.name = active_image.image.name
            try:
                if (active_image.name == "Render Result"
                    or active_image.name == "Viewer Node"
                    or ".dyt.dds" in active_image.image.name) \
                        and ".dds" not in active_image.image.name:
                    active_image.image = None
                    active_image.name = "INVALID IMAGE"
            except AttributeError as ERROR:
                print("EMB ATTRIBUTE ERROR:\t",ERROR)
                pass

            print("EMB ACTIVE IMAGE:\t",active_image.image)
            act_mat = bpy.context.object.data.materials[0]
            try:
                if active_image.image != act_mat.node_tree.nodes["LineWork_This"].image:
                    #act_mat.node_tree.nodes["LineWork_This"].image = active_image.image
                    pass
            except BaseException as err:
                print("EMB BASE EXCEPTION:\t",err)
                pass
        ###########
        
        ####DYT####
        texture_options.row().label(text="DYT (Colors)")
        texture_options.prop(embTool, 'dyt_selection')
        if scene.pointer_tools.dyt_selection != '':
            DYT_UL_col = texture_options.column()
            DYT = scene.Fake_DYTs[
                storage.dyt_selecting[scene.pointer_tools.dyt_selection]]
            DYT_UL_row = DYT_UL_col.split(factor=0.9)
            DYT_UL_row.template_list(
                "DYTImageList_UL",  #listtype_name      ##UIList Class
                "",                 #list_id            ##???
                DYT,                #dataptr            ##Where to get property for listing
                "images",           #propname           ##Property Name
                scene,              #active_dataptr     ##Where to get index property
                "DYT_Image_ID"      #active_propname    ##Index Property Name
            )
            DYT_Actions = DYT_UL_row.column()
            DYT_Actions.operator("image.dyt_add",icon="ADD")
            DYT_Actions.operator("image.dyt_remove",icon="REMOVE")
            DYT_Actions.operator("image.dyt_move_up", icon="TRIA_UP")
            DYT_Actions.operator("image.dyt_move_down", icon="TRIA_DOWN")

            active_image = DYT.images[bpy.context.scene.DYT_Image_ID]
            DYT_UL_col.template_ID(
                active_image,           # ["AnyType"]     (probably a class object to act as a list)
                "image",                # [String]        (property name, but what property is wanted?)
                new="images.new",       # [String]        (Create new item of listing type)
                open="images.open",     # [String]        (Create new item of listing type by opening file)
            )
            if active_image.image is not None:
                active_image.name = active_image.image.name
            try:
                if (active_image.name == "Render Result"
                        or active_image.name == "Viewer Node"
                        or ".dyt.dds" not in active_image.image.name)\
                        and ".dds" not in active_image.image.name:
                    active_image.image  = None
                    active_image.name   = "INVALID IMAGE"
            except AttributeError as ERROR:
                print("DYT ATTRIBUTE ERROR:\t",ERROR)
                pass
            
            print("DYT ACTIVE IMAGE:\t",active_image.image)
            act_mat = bpy.context.object.data.materials[0]
            try:
                if active_image.image != act_mat.node_tree.nodes["DYT1"].image:
                    act_mat.node_tree.nodes["DYT1"].image = active_image.image
                if active_image.image != act_mat.node_tree.nodes["DYT2"].image:
                    act_mat.node_tree.nodes["DYT2"].image = active_image.image
                if active_image.image != act_mat.node_tree.nodes["DYT3"].image:
                    act_mat.node_tree.nodes["DYT3"].image = active_image.image
            except BaseException as err:
                print("DYT BASE EXCEPTION:\t",err)
                pass
        ###########
