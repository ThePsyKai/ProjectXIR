import bpy
import re
import os

from .node_templates import Parameter

class XenoverseNodes_PT_panel(bpy.types.Panel):
    """Creates a Panel in the Node properties window"""
    bl_label = "Xenoverse Parameters"
    bl_idname = "XenoverseNodes_PT_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "XeNodes"

    def draw(self, context):
        layout = self.layout

        ParaNodes = layout.box()
        ParaNodes.label(text="Parameter Nodes")
        oof = ParaNodes.row()

        ParaNodes.operator('node.matcol0')
        ParaNodes.operator('node.matcol1')
        ParaNodes.operator('node.matcol2')
        ParaNodes.operator('node.matcol3')
        ParaNodes.operator('node.texscrl0')
        ParaNodes.operator('node.matscale0')
        ParaNodes.operator('node.matscale1')





        other_nodes = layout.box()
        other_nodes.label(text="Other Nodes")
        other_nodes.operator('node.lighting')
        other_nodes.operator('node.combine_matcol')
        other_nodes.operator('node.dyt_strip_assigner')
        other_nodes.operator('node.merge_dyt')
        other_nodes.operator('node.xenoverse_shader_out')
        other_nodes.operator('node.matcol_plus_dyt')
        other_nodes.operator('node.combine_matcol_shadever')


        other_nodes.operator('node.line_work_image')
        other_nodes.operator('node.dyt_image')
        
        #other_nodes.operator('node.misc')



#=================Parameter Nodes=================#
class MatCol0Node_OT_operator(bpy.types.Operator):
    """Add MatCol0 Node (Used for Linework coloring)"""
    bl_label = 'MatCol0'
    bl_idname = 'node.matcol0'

    @classmethod
    def poll(cls,context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'MatCol0' not in nodes

    def execute(self, context):
        Parameter.new('MatCol0',context.object.active_material.node_tree)
        return {'FINISHED'}

class MatCol1Node_OT_operator(bpy.types.Operator):
    bl_label = 'MatCol1'
    bl_idname = 'node.matcol1'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'MatCol1' not in nodes

    def execute(self, context):
        Parameter.new('MatCol1',context.object.active_material.node_tree)
        #self.report({'INFO'}, "Yet To Be Implemented!")
        return {'FINISHED'}

class MatCol2Node_OT_operator(bpy.types.Operator):
    bl_label = 'MatCol2'
    bl_idname = 'node.matcol2'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'MatCol2' not in nodes

    def execute(self, context):
        Parameter.new('MatCol2',context.object.active_material.node_tree)
        return {'FINISHED'}

class MatCol3Node_OT_operator(bpy.types.Operator):
    bl_label = 'MatCol3'
    bl_idname = 'node.matcol3'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'MatCol3' not in nodes

    def execute(self, context):
        Parameter.new('MatCol3',context.object.active_material.node_tree)
        return {'FINISHED'}

class TexScrl0Node_OT_operator(bpy.types.Operator):
    bl_label = 'TexScrl0'
    bl_idname = 'node.texscrl0'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'TexScrl0' not in nodes

    def execute(self, context):
        Parameter.new('TexScrl0', context.object.active_material.node_tree)
        return {'FINISHED'}

class MatScale0Node_OT_operator(bpy.types.Operator):
    bl_label = 'MatScale0'
    bl_idname = 'node.matscale0'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'MatScale0' not in nodes

    def execute(self, context):
        Parameter.new('MatScale0', context.object.active_material.node_tree)
        return {'FINISHED'}

class MatScale1Node_OT_operator(bpy.types.Operator):
    bl_label = 'MatScale1'
    bl_idname = 'node.matscale1'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'MatScale1' not in nodes

    def execute(self, context):
        Parameter.new('MatScale1', context.object.active_material.node_tree)
        return {'FINISHED'}



#=================Misc Nodes=================#
class LightingNode_OT_operator(bpy.types.Operator):
    bl_label = 'Lighting'
    bl_idname = 'node.lighting'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'Lighting' not in nodes

    def execute(self, context):
        Parameter.new('Lighting', context.object.active_material.node_tree)
        return {'FINISHED'}

class ColorStripNode_OT_operator(bpy.types.Operator):
    bl_label = 'Color Strip'
    bl_idname = 'node.color_strip'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'Color Strip' not in nodes

    def execute(self, context):
        Parameter.new('Color Strip', context.object.active_material.node_tree)
        return {'FINISHED'}

class ShineNode_OT_operator(bpy.types.Operator):
    bl_label = 'Shine'
    bl_idname = 'node.shine'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'MatCol0' not in nodes

    def execute(self, context):
        Parameter.new('MatCol0', context.object.active_material.node_tree)
        return {'FINISHED'}

class CombineMatColNode_OT_operator(bpy.types.Operator):
    bl_label = 'Combine MatCol'
    bl_idname = 'node.combine_matcol'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'Combine_MatCol' not in nodes

    def execute(self, context):
        Parameter.new('Combine_MatCol', context.object.active_material.node_tree)
        return {'FINISHED'}

class LineWorkNode_OT_operator(bpy.types.Operator):
    """Add LineWork Node"""
    bl_label = 'Line Work Image'
    bl_idname = 'node.line_work_image'

    @classmethod
    def poll(cls,context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'Line Work Image' not in nodes

    def execute(self, context):
        Parameter.new('Line_Work_Image',context.object.active_material.node_tree)
        return {'FINISHED'}

class DYTNode_OT_operator(bpy.types.Operator):
    """Add DYT Image Node"""
    bl_label = 'DYT Image'
    bl_idname = 'node.dyt_image'

    @classmethod
    def poll(cls,context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'DYT Image' not in nodes

    def execute(self, context):
        Parameter.new('DYT_Image',context.object.active_material.node_tree)
        return {'FINISHED'}

class DYTStripAssignerNode_OT_operator(bpy.types.Operator):
    bl_label = 'DYT Strip Assigner'
    bl_idname = 'node.dyt_strip_assigner'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'DYT Strip Assigner' not in nodes

    def execute(self, context):
        Parameter.new('DYT_Strip_Assigner', context.object.active_material.node_tree)
        return {'FINISHED'}

class MergeDYTNode_OT_operator(bpy.types.Operator):
    bl_label = 'Merge DYT'
    bl_idname = 'node.merge_dyt'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'Merge DYT' not in nodes

    def execute(self, context):
        Parameter.new('Merge_DYT', context.object.active_material.node_tree)
        return {'FINISHED'}

class XenoverseShaderOutNode_OT_operator(bpy.types.Operator):
    bl_label = 'Xenoverse Shader Out'
    bl_idname = 'node.xenoverse_shader_out'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'Xenoverse Shader Out' not in nodes

    def execute(self, context):
        Parameter.new('Xenoverse_Shader_Out', context.object.active_material.node_tree)
        return {'FINISHED'}

class MatColPlusDYTNode_OT_operator(bpy.types.Operator):
    bl_label = 'MatCol Plus DYT'
    bl_idname = 'node.matcol_plus_dyt'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'MatCol Plus DYT' not in nodes

    def execute(self, context):
        Parameter.new('MatCol_Plus_DYT', context.object.active_material.node_tree)
        return {'FINISHED'}

class CombineMatColShadeVerNode_OT_operator(bpy.types.Operator):
    bl_label = 'Combine MatCol ShadeVer'
    bl_idname = 'node.combine_matcol_shadever'

    @classmethod
    def poll(cls, context):
        nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return 'Combine MatCol ShadeVer' not in nodes

    def execute(self, context):
        Parameter.new('Combine_MatCol_ShadeVer', context.object.active_material.node_tree)
        return {'FINISHED'}


class MiscNode_OT_operator(bpy.types.Operator):
    """Add DYT Image Node"""
    bl_label = 'Misc'
    bl_idname = 'node.misc'

    @classmethod
    def poll(cls,context):
        #nodes = [item.label for item in context.object.active_material.node_tree.nodes]
        return True

    def execute(self, context):
        print("Execute Misc Node")
        Parameter.new('UI_Testing',context.object.active_material.node_tree)
        return {'FINISHED'}
