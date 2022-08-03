import os
from pathlib import Path

NO_BPY = int(os.environ.get('NO_BPY', '0'))

bl_info = {
    "name": "Project XIR",
    "author": "Angzarr Psyco",
    "version": (0,0,6),
    "blender": (2, 92, 0),
    "description": "Import Dragon Ball Xenoverse 1/2 Assets (.emd, .emb, .esk, .emm)",
    "category": "Import-Export"}
import bpy

#from .Game_Engines import
from .xeno_import_operators import (EMDImport_OT_operator,
                                    EANImport_OT_operator,
                                    EMBImport_OT_operator,
                                    DYTImport_OT_operator,
                                    ESKImport_OT_operator,
                                    NSKImport_OT_operator,
                                    EMMImport_OT_operator,
                                    PLACEHOLDER_OT_operator, 
                                    )

from .XenoMaterial_utils import (MaterialUtils_PT_panel,
                                 DYT_OT_MoveUp,
                                 DYT_OT_MoveDown,
                                 DYT_OT_Add,
                                 DYT_OT_Remove,
                                 EMB_OT_MoveUp,
                                 EMB_OT_MoveDown,
                                 EMB_OT_Add,
                                 EMB_OT_Remove,
                                 SharedXenoPropertiesEnum,
                                 DYTImageList_UL,
                                 EMBImageList_UL,
                                 )

from .xeno_export_operators import (EMBExport_OT_operator, 
                                    EXPORTING_UL_embs,
                                    EmbToExport_OT_Add,
                                    EmbToExport_OT_Remove,

                                    EXPORTING_UL_dyts,
                                    DytToExport_OT_Add,
                                    DytToExport_OT_Remove,
                                    )

from .shared_operators import (XenoverseIRUtils_PT_panel,
                               XenoProperties_PT_panel,
                               SkinMesh_OT_operator,
                               SkinSCD_OT_operator,
                               MergeMesh_OT_operator,
                               SplitMesh_OT_operator,
                               #SharedXenoPropertiesEnum,
                               SharedXenoPropertiesCollections,)

from .shared_operators import (XenoImageProperty,
                               FakeEMBUser,
                               EMB_Image,
                               FakeDYTUser,
                               DYT_Image,
                               )
                               

from .parameter_nodes import *
from .node_templates import (UI_Testing,
                             )
from .material_types import *


#╔═ProjectXIR Import Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class ProjectXIRImport_MT_Menu(bpy.types.Menu):
    bl_label    = "Project XIR"
    bl_idname   = "IMPORT_MT_projectxir"

    def draw(self, context):
        self.layout.menu('IMPORT_MT_xenoverseir')
        #self.layout.menu('IMPORT_MT_mineimatorir')
        #self.layout.menu('IMPORT_MT_heroesir')
        #self.layout.menu('IMPORT_MT_creationir')
        #self.layout.menu('IMPORT_MT_unrealir')

#╔═ProjectXIR Export Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class ProjectXIRExport_MT_Menu(bpy.types.Menu):
    bl_label    = "Project XIR"
    bl_idname   = "EXPORT_MT_projectxir"

    def draw(self, context):
        self.layout.menu('EXPORT_MT_xenoverseir')
        #self.layout.menu('EXPORT_MT_mineimatorir')
        #self.layout.menu('EXPORT_MT_heroesir')
        #self.layout.menu('EXPORT_MT_creationir')
        #self.layout.menu('EXPORT_MT_unrealir')


#╔═Xenoverse Import Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class XenoverseIR_MT_Menu(bpy.types.Menu):
    bl_label    = "Xenoverse"
    bl_idname   = "IMPORT_MT_xenoverseir"

    def draw(self, context):
        layout = self.layout
        layout.operator(EMDImport_OT_operator.bl_idname, text="Xenoverse Models (.emd)")
        layout.operator(EMBImport_OT_operator.bl_idname, text="Xenoverse Textures (.emb)")
        layout.operator(DYTImport_OT_operator.bl_idname, text="Xenoverse DYT (.dyt.emb)")
        layout.operator(EMMImport_OT_operator.bl_idname, text="Xenoverse Materials (.emm)")
        layout.operator(ESKImport_OT_operator.bl_idname, text="Xenoverse Armatures (.esk)")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Animations (.ean)")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Stages (.nsk)")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Effects (.emp)")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Skills (.emo)")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Animated Mats (.ema)")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Trail Effects (.etr)")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse HC Figure Pose (.fpf)")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Physics Model (.scd)")
        # layout.separator()
#╔═Xenoverse Export Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class XenoverseER_MT_Menu(bpy.types.Menu):
    bl_label    = "Xenoverse"
    bl_idname   = "EXPORT_MT_xenoverseir"

    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Export Not Yet Supported")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Models (.emd)")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Armatures (.esk)")
        #layout.separator()
        #layout.operator(EMBExport_OT_operator.bl_idname, text="Xenoverse Textures (.emb)")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Materials (.emm)")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Animated Mats (.ema)")
        #layout.separator()
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Animations (.ean)")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse HC Figure Pose (.fpf)")
        #layout.separator()
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Physics Model (.scd)")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Stages (.nsk)")
        #layout.separator()
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Effects (.emp)")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Skills (.emo)")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Xenoverse Trail Effects (.etr)")

        # layout.separator()

#╔═Minecraft Import Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class MineimatorIR_MT_Menu(bpy.types.Menu):
    bl_label = "Minecraft/Mineimator"
    bl_idname = "IMPORT_MT_mineimatorir"

    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Block")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Rigged Block")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Mob")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Entity")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Structure")
        #layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft ")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft ")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft ")
        # layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft ")
        # layout.separator()
#╔═Minecraft Export Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class MineimatorER_MT_Menu(bpy.types.Menu):
    bl_label    = "Minecraft/Mineimator"
    bl_idname   = "EXPORT_MT_mineimatorir"

    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Block")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Rigged Block")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Mob")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Entity")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Minecraft Structure")

#╔═SDBH Import Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class HeroesIR_MT_Menu(bpy.types.Menu):
    bl_label    = "Super Dragon Ball Heros"
    bl_idname   = "IMPORT_MT_heroesir"

    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Options To Be Determined")

        # layout.separator()
#╔═SDBH Export Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class HeroesER_MT_Menu(bpy.types.Menu):
    bl_label    = "Super Dragon Ball Heros"
    bl_idname   = "EXPORT_MT_heroesir"

    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Options To Be Determined")

        # layout.separator()

#╔═Creation Import Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class CreationIR_MT_Menu(bpy.types.Menu):
    bl_label    = "Creation Engine"
    bl_idname   = "IMPORT_MT_creationir"

    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Options To Be Determined")
        # layout.separator()
#╔═Creation Export Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class CreationER_MT_Menu(bpy.types.Menu):
    bl_label    = "Creation Engine"
    bl_idname   = "EXPORT_MT_creationir"

    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Options To Be Determined")

        # layout.separator()

#╔═Unreal Import Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class UnrealIR_MT_Menu(bpy.types.Menu):
    bl_label = "Unreal Engine (4.25+)"
    bl_idname = "IMPORT_MT_unrealir"
    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Unreal Engine Rigged/Static Models (.psk/.pskx)")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Unreal Engine Maps (.umap)")
#╔═Unreal Export Menu═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
class UnrealER_MT_Menu(bpy.types.Menu):
    bl_label = "Unreal Engine (4.25+)"
    bl_idname = "EXPORT_MT_unrealir"
    def draw(self, context):
        layout = self.layout
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Unreal Engine Rigged/Static Models (.psk/.pskx)")
        layout.operator(PLACEHOLDER_OT_operator.bl_idname, text="Unreal Engine Maps (.umap)")


def menu_func_import(self, context):
    self.layout.menu(ProjectXIRImport_MT_Menu.bl_idname)

def menu_func_export(self, context):
    self.layout.menu(ProjectXIRExport_MT_Menu.bl_idname)

classes = []

#╔═Core Menu Operators═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
menus_mainOps = [SelectMaterialProperties,
                 SharedXenoPropertiesEnum,
                 #====Menus====#
                 ProjectXIRImport_MT_Menu,
                 ProjectXIRExport_MT_Menu,
                 #====Xenoverse Menus====#
                 XenoverseIR_MT_Menu,
                 XenoverseER_MT_Menu,
                 #====Minecraft Menus====#
                 MineimatorIR_MT_Menu,
                 MineimatorER_MT_Menu,
                 #====SDBH Menus====#
                 HeroesIR_MT_Menu,
                 HeroesER_MT_Menu,
                 #====Creation Menues====#
                 CreationIR_MT_Menu,
                 CreationER_MT_Menu,
                 #====Unreal Menues====#
                 UnrealIR_MT_Menu,
                 UnrealER_MT_Menu,

                 #====Misc Operators====#
                 PLACEHOLDER_OT_operator,

                 #====Xenoverse Operators====#
                 EMDImport_OT_operator,
                 EMBImport_OT_operator,
                 DYTImport_OT_operator,
                 ESKImport_OT_operator,
                 EANImport_OT_operator,
                 NSKImport_OT_operator,
                 EMMImport_OT_operator,
                 EMBExport_OT_operator,
                 
                 EXPORTING_UL_embs,
                 EmbToExport_OT_Add,
                 EmbToExport_OT_Remove,
                 
                 EXPORTING_UL_dyts,
                 DytToExport_OT_Add,
                 DytToExport_OT_Remove,

                 #====Minecraft Operators====#

                 #====SDBH Operators====#

                 #====Creation Operators====#

                 ]
classes.extend(menus_mainOps)

#╔═Tool Panels/Operators═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
Tools = [MaterialUtils_PT_panel,
         XenoProperties_PT_panel,
         XenoverseIRUtils_PT_panel,
         SkinMesh_OT_operator,
         SkinSCD_OT_operator,
         MergeMesh_OT_operator,
         SplitMesh_OT_operator,
        ]
classes.extend(Tools)

#╔═XenoShader Node Operators═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
Nodes = [XenoverseMaterials_PT_panel,
         XenoverseNodes_PT_panel,
         MatCol0Node_OT_operator,
         MatCol1Node_OT_operator,
         MatCol2Node_OT_operator,
         MatCol3Node_OT_operator,
         LightingNode_OT_operator,
         ColorStripNode_OT_operator,
         ShineNode_OT_operator,
         TexScrl0Node_OT_operator,
         CombineMatColNode_OT_operator,
         LineWorkNode_OT_operator,
         DYTNode_OT_operator,
         DYTStripAssignerNode_OT_operator,
         MergeDYTNode_OT_operator,
         XenoverseShaderOutNode_OT_operator,
         CombineMatColShadeVerNode_OT_operator,
         MatColPlusDYTNode_OT_operator,
         MatScale0Node_OT_operator,
         MatScale1Node_OT_operator,
         ####################
         MiscNode_OT_operator,]
classes.extend(Nodes)

#╔═XenoShader Node Panels/Operators═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
Materials = [ATeToUDFD_OT_operator,
             AToS1DFD_OT_operator,
             AToUEnv_OT_operator,
             AToUEyeM1DFD_OT_operator,
             AToUEyeM2DFD_OT_operator,
             AToUHairDFD_OT_operator,
             AToUS2DFD_OT_operator,
             AToUS3DFD_OT_operator,
             AToUS3DFDaa_OT_operator,
             To0002US2DFD_OT_operator,
             To0002US2d2XVMDFD_OT_operator,
             ToDecalDC_OT_operator,
             ToDFD_OT_operator,
             ToEnv_OT_operator,
             ToHairDFD_OT_operator,
             ToS1DFD_OT_operator,
             ToS1DFDSTN_OT_operator,
             ToS1DFDaa_OT_operator,
             ToS2DFD_OT_operator,
             ToUDFD_OT_operator,
             ToUEnv_OT_operator,
             ToUEnvADD_OT_operator,
             ToUEyeM0DFD_OT_operator,
             ToUEyeM1DFD_OT_operator,
             ToUEyeM1d3DFD_OT_operator,
             ToUEyeM2DFD_OT_operator,
             ToUEyeM3DFD_OT_operator,
             ToUHairDFD_OT_operator,
             ToUHairDFDAth_OT_operator,
             ToUHairDFDSTN_OT_operator,
             ToUSIMPLIFIED_OT_operator,
             ToUS1DFD_OT_operator,
             ToUS1DFDAth_OT_operator,
             ToUS1DFDaa_OT_operator,
             ToUS1MskDFD_OT_operator,
             ToUS1d2XVMDFD_OT_operator,
             ToUS2DFD_OT_operator,
             ToUS2DFDAth_OT_operator,
             ToUS2DFDaa_OT_operator,
             ToUS2d2DFD_OT_operator,
             ToUS2d2XVMDFD_OT_operator,
             ToUS3DFD_OT_operator,
             ToUS3DFDAth_OT_operator,
             ToUS3DFDaa_OT_operator,
             ToUS3MskDFD_OT_operator,
             ToUS3d2XVMDFD_OT_operator]
classes.extend(Materials)

#╔═UI Functions═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓ ║#
UIList_Stuff = [DYTImageList_UL,
                EMBImageList_UL,
                #XenoTexture_PT_panel,
                XenoImageProperty,
                FakeEMBUser,
                EMB_Image,
                DYT_Image,
                FakeDYTUser,

                DYT_OT_MoveUp,
                DYT_OT_MoveDown,
                DYT_OT_Add,
                DYT_OT_Remove,

                EMB_OT_MoveUp,
                EMB_OT_MoveDown,
                EMB_OT_Add,
                EMB_OT_Remove,
                ]
classes.extend(UIList_Stuff)


classes = tuple(classes)

register_, unregister_ = bpy.utils.register_classes_factory(classes)


#╔═Register ProjectXIR Methods and Functions═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    #register_()
    
    bpy.types.Scene.material_tool = bpy.props.PointerProperty(type=SelectMaterialProperties)        
    bpy.types.Scene.pointer_tools = bpy.props.PointerProperty(type=SharedXenoPropertiesEnum)    #General pointers and enums
    
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)    #add custom menu to the Import menu
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)    #add custom menu to the Export menu
    
    bpy.types.Scene.ActiveEMB = bpy.props.PointerProperty(name="IndexEMB", type=bpy.types.Image)
    bpy.types.Scene.ActiveDYT = bpy.props.PointerProperty(name="IndexDYT", type=bpy.types.Image)

    bpy.types.Scene.FEMBs_For_Export = bpy.props.CollectionProperty(type=FakeEMBUser)
    bpy.types.Scene.FDYTs_For_Export = bpy.props.CollectionProperty(type=FakeDYTUser)
    bpy.types.Scene.FEMB_ID = bpy.props.IntProperty(name="FEMB Index", default=0)
    bpy.types.Scene.FDYT_ID = bpy.props.IntProperty(name="FDYT Index", default=0)
    
    bpy.types.Scene.Fake_EMBs                   = bpy.props.CollectionProperty(type=FakeEMBUser)
    bpy.types.Scene.Fake_EMBs[1]['type'].images = bpy.props.CollectionProperty(type=EMB_Image)
    bpy.types.Scene.EMB_Image_ID                = bpy.props.IntProperty(name="EMB Index", default=0)
    
    bpy.types.Material.Texture_Definition       = bpy.props.IntProperty(name="Texture Def", default=0, 
                                                                        min=0,max=10,step=1)
    
    bpy.types.Scene.Fake_DYTs = bpy.props.CollectionProperty(type=FakeDYTUser)
    bpy.types.Scene.Fake_DYTs[1]['type'].images = bpy.props.CollectionProperty(type=DYT_Image)
    bpy.types.Scene.DYT_Image_ID = bpy.props.IntProperty(name="EMB Index", default=0)

#╔═Unregister ProjectXIR Methods and Functions═╗#
#║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
def unregister():

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    #unregister_()
    #nodeitems_utils.unregister_node_categories('CUSTOM_NODES')
    
    del bpy.types.Scene.material_tool
    del bpy.types.Scene.Fake_EMBs
    del bpy.types.Scene.Fake_DYTs
    del bpy.types.Scene.EMB_Image_ID
    del bpy.types.Scene.DYT_Image_ID
    del bpy.types.Scene.pointer_tools
    #del bpy.types.Scene.ActiveImage
    #del bpy.types.BlendDataImages.Active
    
    

if __name__ == "__main__":
    register()
    

