import os
from pathlib import Path

from .import_XenoModel import (import_model,
                               )
from .import_rig import (import_armature,
                         )
from .import_material import (import_image,
                              import_static_material,)
from .custom_error_reporter import XIR_ERROR_REPORT

import bpy
from bpy.props import StringProperty, BoolProperty, CollectionProperty, EnumProperty, FloatProperty

#╔══════════════════════════════════════════════════════════════╗#
#║                         EMD Operator                         ║#
#║       ================================================       ║#
#║                     EMD Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class EMDImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine EMD meshes"""
    bl_idname = "xenoverse_ir.emd"
    bl_label = "Import Xenoverse EMD file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    esk_option:         BoolProperty(name="Import Parent Esk", default=False, subtype='UNSIGNED')
    emm_option:         BoolProperty(name="Import Assosiated Emm", default=False, subtype='UNSIGNED')
    emb_option:         BoolProperty(name="Import Assosiated Emb", default=False, subtype='UNSIGNED')
    smoothing_option:   BoolProperty(name="Smooth Shading", default=False, subtype='UNSIGNED')

    filter_glob: StringProperty(default="*.emd", options={'HIDDEN'})

    def execute(self, context):
        if Path(self.filepath).is_file():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()


        for file in self.files:
            emd_path = directory / file.name

            print(self.esk_option)
            print('Importing',file.name)
            import_model(emd_file=emd_path.open('rb'),
                         file_name=file.name,
                         file_directory=directory,
                         smooth=self.smoothing_option,
                         Import_ESK=self.esk_option)
        self.report({'INFO'}, "Imported " + str(len(self.files)) + " EMDs")
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
#╔══════════════════════════════════════════════════════════════╗#
#║                         ESK Operator                         ║#
#║       ================================================       ║#
#║                     ESK Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class ESKImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine ESK Armatures"""
    bl_idname = "xenoverse_ir.esk"
    bl_label = "Import Xenoverse ESK file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    filter_glob: StringProperty(default="*.esk", options={'HIDDEN'})

    def execute(self, context):

        if Path(self.filepath).is_file():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()

        for file in self.files:
            esk_path = directory / file.name
            import_armature(esk_file=esk_path.open('rb'),file_name=file.name)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
#╔══════════════════════════════════════════════════════════════╗#
#║                         EMB Operator                         ║#
#║       ================================================       ║#
#║                     EMB Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class EMBImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine EMB Textures"""
    bl_idname = "xenoverse_ir.emb"
    bl_label = "Import Xenoverse EMB file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    filter_glob: StringProperty(default="*.emb", options={'HIDDEN'})

    def execute(self, context):
        if Path(self.filepath).is_file():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()

        files_imported = 0
        denied_file_count = 0
        for file in self.files:
            if '.dyt.emb' not in file.name:
                emb_path = directory / file.name

                print('Importing',file.name)
                import_image(image_file=emb_path.open('rb'),
                             imageType="EMB",
                             file_directory=directory,
                             file_name=file.name)
                files_imported+=1
            else:
                denied_file_count+=1
                XIR_ERROR_REPORT(
                    "Xenoverse", 
                    "File Rejected: %s\n\tReason: %s" % (file.name, "DYT File"),
                    "Please Use the DYT Importer for DYT Files"
                    )
        self.report({'INFO'}, "%s Imported | %s Rejected" % (files_imported, denied_file_count))
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
#╔══════════════════════════════════════════════════════════════╗#
#║                         DYT Operator                         ║#
#║       ================================================       ║#
#║                     DYT Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class DYTImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine DYT Textures"""
    bl_idname = "xenoverse_ir.dyt"
    bl_label = "Import Xenoverse DYT.EMB file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    filter_glob: StringProperty(default="*.dyt.emb", options={'HIDDEN'})

    dyt_method: BoolProperty(name="New Ramp Method", default=False, subtype='UNSIGNED')

    def execute(self, context):
        if Path(self.filepath).is_file():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()

        files_imported = 0
        denied_file_count = 0
        for file in self.files:
            if '.dyt.emb' in file.name:
                emb_path = directory / file.name
    
                print('Importing',file.name)
                import_image(image_file=emb_path.open('rb'),
                             imageType="DYT",
                             file_directory=directory,
                             file_name=file.name,
                             NewDYTMethod=self.dyt_method)
                files_imported += 1
            else:
                denied_file_count+=1
                XIR_ERROR_REPORT(
                    "Xenoverse", 
                    "File Rejected: %s\n\tReason: %s" % (file.name, "DYT File"),
                    "Please Use the DYT Importer for DYT Files"
                    )
            
            
        self.report({'INFO'}, "%s Imported | %s Rejected" % (files_imported, denied_file_count))
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

#╔══════════════════════════════════════════════════════════════╗#
#║                         EMM Operator                         ║#
#║       ================================================       ║#
#║                     EMM Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class EMMImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine EMM Materials"""
    bl_idname = "xenoverse_ir.emm"
    bl_label = "Import Xenoverse EMM file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)
    importemb: BoolProperty(name='Import Emb?',default=True)
    importdyt: BoolProperty(name='Import DYT?',default=True)

    filter_glob: StringProperty(default="*.emm", options={'HIDDEN'})

    def execute(self, context):
        if Path(self.filepath).is_file():
            directory = Path(self.filepath).parent.absolute()
        else:
            directory = Path(self.filepath).absolute()


        for file in self.files:
            emm_path = directory / file.name
            emb_path = directory / file.name.replace('.emm','.emb')
            dyt_path = directory / file.name.replace('.emm', '.dyt.emb')
            if not os.path.exists(dyt_path):
                self.importdyt = False
            print('Importing',file.name)
            if self.importemb and file.name.replace('.emm','.emb') in os.listdir(directory):
                print('Importing EMB')
                import_image(image_file=emb_path.open('rb'),
                             imageType="EMB",
                             file_directory=directory,
                             file_name=file.name.replace('.emm','.emb'))
            if self.importdyt and file.name.replace('.emm','.dyt.emb') in os.listdir(directory):
                print('Importing DYT')
                import_image(image_file=dyt_path.open('rb'),
                             imageType="DYT",
                             file_directory=directory,
                             file_name=file.name.replace('.emm','.dyt.emb'))
            
            import_static_material(emm_file=emm_path.open('rb'),
                                   file_directory=directory,
                                   file_name=file.name,
                                   IEMB=self.importemb,
                                   IDYT=self.importdyt)
            
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}


#╔══════════════════════════════════════════════════════════════╗#
#║                         EAN Operator                         ║#
#║       ================================================       ║#
#║                     EAN Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class EANImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine EAN Animations"""
    bl_idname = "xenoverse_ir.ean"
    bl_label = "Import Xenoverse EAN file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    filter_glob: StringProperty(default="*.ean", options={'HIDDEN'})

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
#╔══════════════════════════════════════════════════════════════╗#
#║                         EMA Operator                         ║#
#║       ================================================       ║#
#║                     EMA Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class EMAImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine EMA ???"""
    bl_idname = "xenoverse_ir.ema"
    bl_label = "Import Xenoverse EMA file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    filter_glob: StringProperty(default="*.ema", options={'HIDDEN'})

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
#╔══════════════════════════════════════════════════════════════╗#
#║                         NSK Operator                         ║#
#║       ================================================       ║#
#║                     NSK Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class NSKImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine NSK Stages (Mesh and Armature)"""
    bl_idname = "xenoverse_ir.nsk"
    bl_label = "Import Xenoverse NSK file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    filter_glob: StringProperty(default="*.nsk", options={'HIDDEN'})

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
#╔══════════════════════════════════════════════════════════════╗#
#║                         EMO Operator                         ║#
#║       ================================================       ║#
#║                     EMO Import Function                      ║#
#║                Builds VGUI and File Explorer                 ║#
#╚══════════════════════════════════════════════════════════════╝#
class EMOImport_OT_operator(bpy.types.Operator):
    """Load Xenoverse Engine EMO meshes"""
    bl_idname = "xenoverse_ir.emo"
    bl_label = "Import Xenoverse EMO file"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    filter_glob: StringProperty(default="*.emo", options={'HIDDEN'})

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

#╔══════════════════════════════════════════════════════════════╗#
#║                     Placeholder Operator                     ║#
#║       ================================================       ║#
#║       Let's User Know of Feature Yet to be Implemented       ║#
#║                Mainly Used For Laying Out GUI                ║#
#╚══════════════════════════════════════════════════════════════╝#
class PLACEHOLDER_OT_operator(bpy.types.Operator):
    """Place Holder Operator for Visual Menu Testing"""
    bl_idname = "xenoverse_ir.tst"
    bl_label = "Place Holder Import"
    bl_options = {'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")
    files: CollectionProperty(name='File paths', type=bpy.types.OperatorFileListElement)

    filter_glob: StringProperty(default="*.tst", options={'HIDDEN'})

    def execute(self, context):
        self.report({'INFO'}, "Yet To Be Implemented!")
        return {'FINISHED'}
    
