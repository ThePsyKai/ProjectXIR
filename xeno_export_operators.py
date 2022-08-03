import os
from pathlib import Path

from bpy_extras.io_utils import ImportHelper, ExportHelper

#from .import_XenoModel import *
#from .export_material import *


import bpy
from bpy.props import StringProperty, BoolProperty, CollectionProperty, EnumProperty, FloatProperty
from .export_material import packing_emb, packing_dyt


class storage:
    emb_selecting = {}
    emb_dds = {}
    dyt_selecting = {}
    dyt_dds = {}

    all_images = []
    EMB_Initialize = True
    DYT_Initialize = True

    femb_selecting = {}
    fdyt_selecting = {}

def FakeUserUnDuper(scene):
    counter = 0
    dupe = False
    #EMBs
    for key in range(0, len(scene.Fake_EMBs.keys())):
        print(key, scene.Fake_EMBs[key])
        print(scene.Fake_EMBs.keys().count(scene.Fake_EMBs.keys()[key]))
        print(scene.Fake_EMBs.keys()[key])
        if scene.Fake_EMBs.keys().count(scene.Fake_EMBs.keys()[key]) - 1:
            print()
            if dupe:
                if scene.Fake_EMBs.keys()[key:].count(scene.Fake_EMBs.keys()[key])-1:
                    print("Oof")
                else:
                    dupe = False
                counter += 1
                #print(scene.Fake_EMBs[key].name + "." + "0" * (3 - len(str(counter))) + str(counter))
                scene.Fake_EMBs[key].name = \
                    scene.Fake_EMBs[key].name+"."+\
                    "0"*(3-len(str(counter)))+str(counter)
            else:
                dupe = True
    #DYTs
    for key in range(0, len(scene.Fake_DYTs.keys())):
        print(key, scene.Fake_DYTs[key])
        print(scene.Fake_DYTs.keys().count(scene.Fake_DYTs.keys()[key]))
        print(scene.Fake_DYTs.keys()[key])
        if scene.Fake_DYTs.keys().count(scene.Fake_DYTs.keys()[key])-1:
            print()
            if dupe:
                if scene.Fake_DYTs.keys()[key:].count(scene.Fake_DYTs.keys()[key])-1:
                    print("Oof")
                else:
                    dupe = False
                counter += 1
                #print(scene.Fake_DYTs[key].name+"."+"0"*(3-len(str(counter)))+str(counter))
                scene.Fake_DYTs[key].name = \
                    scene.Fake_DYTs[key].name+"."+\
                    "0"*(3-len(str(counter)))+str(counter)
            else:
                dupe = True

def femb_callback(context):
    if context.scene:
        FEMBs = context.scene.Fake_EMBs
        for Selection in range(0,len(FEMBs)):
            print("setting " + FEMBs[Selection].name)

            print('OP' + str(Selection+1))
            print()
            storage.femb_selecting.__setitem__('OP' + str(Selection+1), FEMBs[Selection].name)
def fdyt_callback(context):
    if context.scene:
        FDYTs = context.scene.Fake_DYTs
        for Selection in range(0,len(FDYTs)):
            print("setting " + FDYTs[Selection].name)

            print('OP' + str(Selection+1))
            print()
            storage.fdyt_selecting.__setitem__('OP' + str(Selection+1), FDYTs[Selection].name)


class EXPORTING_UL_embs(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            if item:
                layout.prop(item, "name", text="", emboss=False)
class EmbToExport_OT_Add(bpy.types.Operator):
    bl_idname = "export.export_add"
    bl_label = ''
    def execute(self, context):
        scene = context.scene
        sto = storage.femb_selecting
        pt = scene.pointer_tools.femb_selection
        print("Adding POINTER TOOL:\t", pt)
        print("Adding STORAGE:\t\t", sto)
        print("Adding RETRIEVED:\t",str(storage.femb_selecting[scene.pointer_tools.femb_selection]))
        FakeUserUnDuper(scene)
        Export_Ind = len(scene.FEMBs_For_Export)-1
        try:
            if scene.Fake_EMBs[sto[pt]].name not in [item.name for item in scene.FEMBs_For_Export]:
                scene.FEMBs_For_Export.add()
                print(scene.FEMBs_For_Export[Export_Ind])
                item_ref = scene.FEMBs_For_Export[Export_Ind]
                item_ref.name = \
                    scene.Fake_EMBs[sto[pt]].name
                item_ref.image_count = \
                    scene.Fake_EMBs[sto[pt]].image_count
                for item in scene.Fake_EMBs[sto[pt]].images:
                    ind = len(scene.Fake_EMBs[sto[pt]].images)-1
                    print(ind)
                    item_ref.images.add()
                    item_ref.images[-1].name       = item.name
                    item_ref.images[-1].image      = item.image
                    item_ref.images[-1].emd_index  = item.emd_index
                    item_ref.images[-1].is_empty   = item.is_empty
            
        except KeyError:
            print("EmbToExport_OT_Add\tKeyError\tE R R O R:")
            print("POINTER TOOL:\t", scene.pointer_tools.femb_selection)
            print("STORAGE:\t", storage.femb_selecting)
        return {'FINISHED'}
class EmbToExport_OT_Remove(bpy.types.Operator):
    bl_idname = "export.export_remove"
    bl_label = ''
    def execute(self, context):
        scene = context.scene
        active = scene.FEMB_ID
        scene.FEMBs_For_Export.remove(active)
        scene.EMB_Image_ID -= 1
        return {'FINISHED'}
def drawingEMBList(context, layout):
    texture_options = layout
    scene = context.scene
    if scene.FEMB_ID < 0:
        scene.FEMB_ID = 0
    texture_options.label(text="EMBs to Export")
    FakeEMB_UL_col = texture_options.column()
    FakeEMB_UL_row = FakeEMB_UL_col.split(factor=0.9)
    FakeEMB_UL_row.template_list(
        "EXPORTING_UL_embs",    # listtype_name      ##UIList Class
        "",                     # list_id            ##???
        scene,                  # dataptr            ##Where to get property for listing
        "FEMBs_For_Export",     # propname           ##Property Name
        scene,                  # active_dataptr     ##Where to get index property
        "FEMB_ID"               # active_propname    ##Index Property Name
    )
    FakeEMB_Actions = FakeEMB_UL_row.column()
    FakeEMB_Actions.operator("export.export_remove", icon="REMOVE")


class EXPORTING_UL_dyts(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            if item:
                layout.prop(item, "name", text="", emboss=False)
class DytToExport_OT_Add(bpy.types.Operator):
    bl_idname = "export.export_add_dyt"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        sto = storage.fdyt_selecting
        pt = scene.pointer_tools.fdyt_selection
        print("Adding POINTER TOOL:\t", pt)
        print("Adding STORAGE:\t\t", sto)
        print("Adding RETRIEVED:\t", str(storage.fdyt_selecting[scene.pointer_tools.fdyt_selection]))
        FakeUserUnDuper(scene)
        Export_Ind = len(scene.FDYTs_For_Export) - 1
        try:
            if scene.Fake_DYTs[sto[pt]].name not in [item.name for item in scene.FDYTs_For_Export]:
                scene.FDYTs_For_Export.add()
                print(scene.FDYTs_For_Export[Export_Ind])
                item_ref = scene.FDYTs_For_Export[Export_Ind]
                item_ref.name = \
                    scene.Fake_DYTs[sto[pt]].name
                item_ref.image_count = \
                    scene.Fake_DYTs[sto[pt]].image_count
                for item in scene.Fake_DYTs[sto[pt]].images:
                    ind = len(scene.Fake_DYTs[sto[pt]].images) - 1
                    print(ind)
                    item_ref.images.add()
                    item_ref.images[-1].name = item.name
                    item_ref.images[-1].image = item.image
                    item_ref.images[-1].dyt_index = item.dyt_index

        except KeyError:
            print("EmbToExport_OT_Add\tKeyError\tE R R O R:")
            print("POINTER TOOL:\t", scene.pointer_tools.femb_selection)
            print("STORAGE:\t", storage.femb_selecting)
        return {'FINISHED'}
class DytToExport_OT_Remove(bpy.types.Operator):
    bl_idname = "export.export_remove_dyt"
    bl_label = ''

    def execute(self, context):
        scene = context.scene
        active = scene.FDYT_ID
        scene.FDYTs_For_Export.remove(active)
        scene.DYT_Image_ID -= 1
        return {'FINISHED'}
def drawingDYTList(context, layout):
    texture_options = layout
    scene = context.scene
    if scene.FDYT_ID < 0:
        scene.FDYT_ID = 0
    texture_options.label(text="DYTs to Export")
    FakeDYT_UL_col = texture_options.column()
    FakeDYT_UL_row = FakeDYT_UL_col.split(factor=0.9)
    FakeDYT_UL_row.template_list(
        "EXPORTING_UL_dyts",    # listtype_name      ##UIList Class
        "",                     # list_id            ##???
        scene,                  # dataptr            ##Where to get property for listing
        "FDYTs_For_Export",     # propname           ##Property Name
        scene,                  # active_dataptr     ##Where to get index property
        "FDYT_ID"               # active_propname    ##Index Property Name
    )
    FakeDYT_Actions = FakeDYT_UL_row.column()
    FakeDYT_Actions.operator("export.export_remove_dyt", icon="REMOVE")
        

class EMBExport_OT_operator(bpy.types.Operator, ExportHelper):
    """Export Xenoverse Engine EMB Textures"""
    bl_idname = "xenoverse_er.emb"
    bl_label = "Export Xenoverse EMB file"

    filename_ext = ".emb"

    filter_glob: StringProperty(default="*.emb", options={'HIDDEN'})
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)
    
    
    #@classmethod
    #def poll(cls, context):
    #    return True#all('Xeno_Properties' in item for item in context.selected_objects)

    def draw(self, context):
        print(storage.femb_selecting)
        layout = self.layout
        row = layout.row()
        row.label(text="Add EMB to Export List")
        embTool = context.scene.pointer_tools
            
        femb_callback(context)
        fdyt_callback(context)
        
        export_list = layout.box()
        drawingEMBList(context, export_list)
        Col = export_list.column()
        pointer_row = Col.split(factor=0.9)
        pointer_row.prop(embTool, 'femb_selection')
        pointer_row.operator("export.export_add", icon="ADD")

        export_list_dyt = layout.box()
        drawingDYTList(context, export_list)
        Col = export_list_dyt.column()
        pointer_row = Col.split(factor=0.9)
        pointer_row.prop(embTool, 'fdyt_selection')
        pointer_row.operator("export.export_add_dyt", icon="ADD")
        
    
    def execute(self, context):
        if Path(self.filepath).is_dir():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()

        
        if len(context.scene.FEMBs_For_Export):
            for item in context.scene.FEMBs_For_Export:
                packing_emb(bpy.context, directory, item)
        if len(context.scene.FDYTs_For_Export):
            for item in context.scene.FDYTs_For_Export:
                packing_dyt(bpy.context, directory, item)
                    
        storage.femb_selecting = {}
        storage.fdyt_selecting = {}
        
        return {"FINISHED"}


    
