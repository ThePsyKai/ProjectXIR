import bpy

class frame_node:
    def __init__(self,frm,ins:list,outs:list, node_refs:dict):
        self.frame = frm
        
        self.inputs = ins
        self.outputs = outs
        
        self.nodes = node_refs

#class ImageTemplate:
#    image : bpy.props.PointerProperty(type=bpy.data.Image)
#
#    def draw(self, context):
#        layout = self.layout
#        layout.template_ID(self, "image", new="image.new", open="image.open")

class AlphaBlend:
    def __init__(self,tree):
        pass
    pass

class AlphaBlendType:
    def __init__(self,tree):
        pass
    pass

class AlphaSortMask:
    def __init__(self,tree):
        pass
    pass

class AlphaTest:
    def __init__(self,tree):
        pass
    pass

class AnimationChannel:
    def __init__(self,tree):
        pass
    pass

class BackFace:
    def __init__(self,tree):
        pass
    pass

class Billboard:
    def __init__(self,tree):
        pass
    pass

class BillboardType:
    def __init__(self,tree):
        pass
    pass

class CustomFlag:
    def __init__(self,tree):
        pass
    pass

class FadeInit:
    def __init__(self,tree):
        pass
    pass

class FadeSpeed:
    def __init__(self,tree):
        pass
    pass

class GlareCol:
    def __init__(self,tree):

        pass
    pass

class GradientInit:
    def __init__(self,tree):
        pass
    pass

class GradientSpeed:
    def __init__(self,tree):
        pass
    pass

class IncidenceAlphaBias:
    def __init__(self,tree):
        pass
    pass

class IncidencePower:
    def __init__(self,tree):
        pass
    pass

class LowRez:
    def __init__(self,tree):
        pass
    pass

class LowRezSmoke:
    def __init__(self,tree):
        pass
    pass

class MarkSamplerAddress:
    def __init__(self,tree):


        U = 0
        V = 0
        pass
    pass

class MatAmb:
    def __init__(self,tree):
        if 'MatAmb' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatAmb', 'ShaderNodeTree')

            # ======Nodes======#
            group_in = test_group.nodes.new('NodeGroupInput')
            group_out = test_group.nodes.new('NodeGroupOutput')

            # =================#

            # ======Inputs======#
            test_group.inputs.new('NodeSocketFloat', 'R')
            test_group.inputs.new('NodeSocketFloat', 'G')
            test_group.inputs.new('NodeSocketFloat', 'B')
            test_group.inputs.new('NodeSocketFloat', 'A')
            # ==================#

            # ======Outputs======#

            # ===================#

            # =========Arrangement=========#
            group_in.location = (-200, 0)
            group_out.location = (400, 0)

            # =============================#

            # ===========Linking===========#

            # =============================#

            # ===========Defaults==========#

            # =============================#
        else:
            test_group = bpy.data.node_groups['MatAmb']
        

        # ======Parameter Node======#
        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatAmb'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 180.0
        # ==========================#

        self.__node = node
        pass

    def node(self):
        return self.__node
        pass
    pass

class MatAmbScale:
    def __init__(self,tree):

        pass
    pass

class MatC:
    def __init__(self,tree):
        pass
    pass

class MatDif:
    def __init__(self,tree):
        if 'MatDif' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatDif', 'ShaderNodeTree')

            # ======Nodes======#
            group_in = test_group.nodes.new('NodeGroupInput')
            group_out = test_group.nodes.new('NodeGroupOutput')

            # =================#

            # ======Inputs======#
            test_group.inputs.new('NodeSocketFloat', 'R')
            test_group.inputs.new('NodeSocketFloat', 'G')
            test_group.inputs.new('NodeSocketFloat', 'B')
            test_group.inputs.new('NodeSocketFloat', 'A')
            # ==================#

            # ======Outputs======#

            # ===================#

            # =========Arrangement=========#
            group_in.location = (-200, 0)
            group_out.location = (400, 0)

            # =============================#

            # ===========Linking===========#

            # =============================#

            # ===========Defaults==========#

            # =============================#
        else:
            test_group = bpy.data.node_groups['MatDif']
        

        # ======Parameter Node======#
        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatDif'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 180.0
        # ==========================#

        self.__node = node
        pass

    def node(self):
        return self.__node
    pass

class MatDifScale:
    def __init__(self,tree):
        pass
    pass

class MatOffset0:
    def __init__(self, tree):
        if 'MatOffset0' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatOffset0', 'ShaderNodeTree')

            # ======Nodes======#
            group_in = test_group.nodes.new('NodeGroupInput')
            group_out = test_group.nodes.new('NodeGroupOutput')

            # =================#

            # ======Inputs======#
            test_group.inputs.new('NodeSocketFloat', 'X')
            test_group.inputs.new('NodeSocketFloat', 'Y')
            test_group.inputs.new('NodeSocketFloat', 'Z')
            test_group.inputs.new('NodeSocketFloat', 'W')
            # ==================#

            # ======Outputs======#

            # ===================#

            # =========Arrangement=========#
            group_in.location = (-200, 0)
            group_out.location = (400, 0)

            # =============================#

            # ===========Linking===========#

            # =============================#

            # ===========Defaults==========#

            # =============================#
        else:
            test_group = bpy.data.node_groups['MatOffset0']

        # ======Parameter Node======#
        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatOffset0'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 180.0
        # ==========================#

        self.__node = node
        pass

    def node(self):
        return self.__node
    pass

class MatOffset1:
    def __init__(self, tree):
        if 'MatOffset1' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatOffset1', 'ShaderNodeTree')

            # ======Nodes======#
            group_in = test_group.nodes.new('NodeGroupInput')
            group_out = test_group.nodes.new('NodeGroupOutput')

            # =================#

            # ======Inputs======#
            test_group.inputs.new('NodeSocketFloat', 'X')
            test_group.inputs.new('NodeSocketFloat', 'Y')
            test_group.inputs.new('NodeSocketFloat', 'Z')
            test_group.inputs.new('NodeSocketFloat', 'W')
            # ==================#

            # ======Outputs======#

            # ===================#

            # =========Arrangement=========#
            group_in.location = (-200, 0)
            group_out.location = (400, 0)

            # =============================#

            # ===========Linking===========#

            # =============================#

            # ===========Defaults==========#

            # =============================#
        else:
            test_group = bpy.data.node_groups['MatOffset1']

        # ======Parameter Node======#
        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatOffset1'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 180.0
        # ==========================#

        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MatSpc:
    def __init__(self, tree):
        if 'MatSpc' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatSpc', 'ShaderNodeTree')

            # ======Nodes======#
            group_in = test_group.nodes.new('NodeGroupInput')
            group_out = test_group.nodes.new('NodeGroupOutput')

            # =================#

            # ======Inputs======#
            test_group.inputs.new('NodeSocketFloat', 'R')
            test_group.inputs.new('NodeSocketFloat', 'G')
            test_group.inputs.new('NodeSocketFloat', 'B')
            test_group.inputs.new('NodeSocketFloat', 'A')
            # ==================#

            # ======Outputs======#

            # ===================#

            # =========Arrangement=========#
            group_in.location = (-200, 0)
            group_out.location = (400, 0)

            # =============================#

            # ===========Linking===========#

            # =============================#

            # ===========Defaults==========#

            # =============================#
        else:
            test_group = bpy.data.node_groups['MatSpc']

        # ======Parameter Node======#
        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatSpc'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 180.0
        # ==========================#

        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MipMapLod0:
    def __init__(self,tree):
        pass
    pass

class MipMapLod1:
    def __init__(self,tree):
        pass
    pass

class NoEdge:
    def __init__(self,tree):
        pass
    pass

class ReflectCoeff:
    def __init__(self,tree):
        pass
    pass

class ReflectFresnelBias:
    def __init__(self,tree):
        pass
    pass

class ReflectFresnelCoeff:
    def __init__(self,tree):
        pass
    pass

class RimCoeff:
    def __init__(self,tree):
        pass
    pass

class RimPower:
    def __init__(self,tree):
        pass
    pass

class SpcCoeff:
    def __init__(self,tree):
        pass
    pass

class SpcPower:
    def __init__(self,tree):
        pass
    pass

class TexScrl1:
    def __init__(self,tree):


        U = 0
        V = 0
        pass
    pass

class TextureFilter0:
    def __init__(self,tree):
        pass
    pass

class TextureFilter1:
    def __init__(self,tree):
        pass
    pass

class TextureFilter2:
    def __init__(self,tree):
        pass
    pass

class ToonSamplerAddress:
    def __init__(self,tree):


        U     = 0
        V     = 0
        pass
    pass

class TwoSidedRender:
    def __init__(self,tree):
        pass
    pass

class VsFlag0:
    def __init__(self,tree):
        pass
    pass

class VsFlag1:
    def __init__(self,tree):
        pass
    pass

class VsFlag2:
    def __init__(self,tree):
        pass
    pass

class VsFlag3:
    def __init__(self,tree):
        pass
    pass

class ZWriteMask:
    def __init__(self,tree):
        pass
    pass

class gLightAmb:
    def __init__(self,tree):
        pass
    pass

class gLightDif:
    def __init__(self,tree):
        pass
    pass

class gLightDir:
    def __init__(self,tree):
        pass
    pass

class gLightSpc:
    def __init__(self,tree):
        pass
    pass

class gToonTextureHeight:
    def __init__(self,tree):
        pass
    pass

class gToonTextureWidth:
    def __init__(self,tree):
        pass
    pass

class g_MaterialOffset0_VS:
    def __init__(self,tree):
        pass
    pass


#Misc Nodes

class Combine_MatCol_ShadeVer:
    def __init__(self, tree):
        if 'Combine_MatCol_ShadeVer' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('Combine_MatCol_ShadeVer', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('ShaderNodeBsdfPrincipled')
            inner_node_1 = test_group.nodes.new('ShaderNodeBsdfPrincipled')
            inner_node_2 = test_group.nodes.new('ShaderNodeBsdfPrincipled')
            inner_node_3 = test_group.nodes.new('ShaderNodeBsdfPrincipled')
            inner_node_4 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_5 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_6 = test_group.nodes.new('NodeGroupInput')
            inner_node_7 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_8 = test_group.nodes.new('ShaderNodeVectorMath')
            inner_node_9 = test_group.nodes.new('ShaderNodeMath')
            inner_node_10 = test_group.nodes.new('ShaderNodeMath')
            inner_node_11 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_12 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_13 = test_group.nodes.new('ShaderNodeMath')
            inner_node_14 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_15 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_16 = test_group.nodes.new('NodeGroupInput')
            inner_node_17 = test_group.nodes.new('ShaderNodeMath')
            inner_node_18 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_19 = test_group.nodes.new('ShaderNodeMath')
            inner_node_20 = test_group.nodes.new('ShaderNodeMath')
            inner_node_21 = test_group.nodes.new('ShaderNodeMath')
            inner_node_22 = test_group.nodes.new('ShaderNodeMath')
            inner_node_23 = test_group.nodes.new('ShaderNodeMath')
            inner_node_24 = test_group.nodes.new('ShaderNodeMath')
            inner_node_25 = test_group.nodes.new('ShaderNodeMath')
            inner_node_26 = test_group.nodes.new('NodeGroupInput')
            inner_node_27 = test_group.nodes.new('ShaderNodeMath')
            inner_node_28 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_29 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_30 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_31 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_32 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_33 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_34 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_35 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_36 = test_group.nodes.new('NodeGroupOutput')
            inner_node_37 = test_group.nodes.new('ShaderNodeVectorMath')
            inner_node_38 = test_group.nodes.new('ShaderNodeVectorMath')
            inner_node_39 = test_group.nodes.new('ShaderNodeMath')
            inner_node_40 = test_group.nodes.new('ShaderNodeMath')
            inner_node_41 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_42 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_43 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_44 = test_group.nodes.new('ShaderNodeMath')

            test_group.inputs.new('NodeSocketColor', 'MatCol0')
            test_group.inputs.new('NodeSocketColor', 'Lines')
            test_group.inputs.new('NodeSocketColor', 'MatCol1')
            test_group.inputs.new('NodeSocketColor', 'Red Channel')
            test_group.inputs.new('NodeSocketColor', 'MatCol2')
            test_group.inputs.new('NodeSocketColor', 'Green Channel')
            test_group.inputs.new('NodeSocketColor', 'MatCol3')
            test_group.inputs.new('NodeSocketColor', 'Blue Channel')
            test_group.inputs.new('NodeSocketFloatFactor', 'Scratches?')
            test_group.inputs['Scratches?'].min_value = 0.0
            test_group.inputs['Scratches?'].max_value = 1.0
            test_group.inputs['Scratches?'].hide_value = False
            test_group.inputs.new('NodeSocketFloatFactor', 'Blood?')
            test_group.inputs['Blood?'].min_value = 0.0
            test_group.inputs['Blood?'].max_value = 1.0
            test_group.inputs['Blood?'].hide_value = False
            test_group.inputs.new('NodeSocketFloatFactor', 'Use Blue Channel?')
            test_group.inputs['Use Blue Channel?'].min_value = 0.0
            test_group.inputs['Use Blue Channel?'].max_value = 1.0
            test_group.inputs['Use Blue Channel?'].hide_value = False

            test_group.outputs.new('NodeSocketShader', 'MatCol')
            test_group.outputs.new('NodeSocketFloat', 'Value')

            inner_node_0.location = (-220.0, -220.0)
            inner_node_1.location = (-220.0, -60.0)
            inner_node_2.location = (-220.0, 100.0)
            inner_node_3.location = (-220.0, 260.0)
            inner_node_4.location = (820.0, 240.0)
            inner_node_5.location = (480.0, 240.0)
            inner_node_6.location = (-700.0, 20.0)
            inner_node_7.location = (-960.0, 1580.0)
            inner_node_8.location = (-500.0, 1440.0)
            inner_node_9.location = (-680.0, 1000.0)
            inner_node_10.location = (-680.0, 1320.0)
            inner_node_11.location = (-960.0, 1420.0)
            inner_node_12.location = (-960.0, 1500.0)
            inner_node_13.location = (-680.0, 1160.0)
            inner_node_14.location = (-960.0, 1660.0)
            inner_node_15.location = (160.0, 240.0)
            inner_node_16.location = (-1460.0, 920.0)
            inner_node_17.location = (1160.0, 1820.0)
            inner_node_18.location = (600.0, 1200.0)
            inner_node_19.location = (1460.0, 1820.0)
            inner_node_20.location = (1780.0, 1820.0)
            inner_node_21.location = (-1160.0, 540.0)
            inner_node_22.location = (-1160.0, 680.0)
            inner_node_23.location = (-1160.0, 400.0)
            inner_node_24.location = (240.0, 2000.0)
            inner_node_25.location = (240.0, 2140.0)
            inner_node_26.location = (-120.0, 1980.0)
            inner_node_27.location = (240.0, 1860.0)
            inner_node_28.location = (1020.0, 1480.0)
            inner_node_29.location = (1200.0, 1480.0)
            inner_node_30.location = (1020.0, 1280.0)
            inner_node_31.location = (1020.0, 1080.0)
            inner_node_32.location = (1400.0, 1540.0)
            inner_node_33.location = (1580.0, 1540.0)
            inner_node_34.location = (1400.0, 1340.0)
            inner_node_35.location = (1400.0, 1140.0)
            inner_node_36.location = (2360.0, 1120.0)
            inner_node_37.location = (-300.0, 1440.0)
            inner_node_38.location = (-100.0, 1440.0)
            inner_node_39.location = (-280.0, 1000.0)
            inner_node_40.location = (160.0, 1000.0)
            inner_node_41.location = (600.0, 1020.0)
            inner_node_42.location = (600.0, 1420.0)
            inner_node_43.location = (780.0, 1420.0)
            inner_node_44.location = (-60.0, 1000.0)

            test_group.links.new(inner_node_8.inputs[0], inner_node_14.outputs[0])
            test_group.links.new(inner_node_10.inputs[0], inner_node_7.outputs[0])
            test_group.links.new(inner_node_8.inputs[1], inner_node_10.outputs[0])
            test_group.links.new(inner_node_3.inputs[19], inner_node_6.outputs[1])
            test_group.links.new(inner_node_3.inputs[0], inner_node_6.outputs[0])
            test_group.links.new(inner_node_2.inputs[0], inner_node_6.outputs[2])
            test_group.links.new(inner_node_15.inputs[2], inner_node_2.outputs[0])
            test_group.links.new(inner_node_5.inputs[1], inner_node_15.outputs[0])
            test_group.links.new(inner_node_1.inputs[0], inner_node_6.outputs[4])
            test_group.links.new(inner_node_1.inputs[19], inner_node_6.outputs[5])
            test_group.links.new(inner_node_0.inputs[0], inner_node_6.outputs[6])
            test_group.links.new(inner_node_0.inputs[19], inner_node_6.outputs[7])
            test_group.links.new(inner_node_4.inputs[1], inner_node_5.outputs[0])
            test_group.links.new(inner_node_5.inputs[2], inner_node_1.outputs[0])
            test_group.links.new(inner_node_4.inputs[2], inner_node_0.outputs[0])
            test_group.links.new(inner_node_13.inputs[0], inner_node_12.outputs[0])
            test_group.links.new(inner_node_9.inputs[0], inner_node_11.outputs[0])
            test_group.links.new(inner_node_2.inputs[19], inner_node_6.outputs[3])
            test_group.links.new(inner_node_37.inputs[1], inner_node_13.outputs[0])
            test_group.links.new(inner_node_37.inputs[0], inner_node_8.outputs[0])
            test_group.links.new(inner_node_38.inputs[1], inner_node_9.outputs[0])
            test_group.links.new(inner_node_38.inputs[0], inner_node_37.outputs[0])
            test_group.links.new(inner_node_5.inputs[0], inner_node_44.outputs[0])
            test_group.links.new(inner_node_40.inputs[0], inner_node_38.outputs[0])
            test_group.links.new(inner_node_4.inputs[0], inner_node_40.outputs[0])
            test_group.links.new(inner_node_14.inputs[1], inner_node_16.outputs[1])
            test_group.links.new(inner_node_7.inputs[1], inner_node_16.outputs[3])
            test_group.links.new(inner_node_12.inputs[1], inner_node_16.outputs[5])
            test_group.links.new(inner_node_11.inputs[1], inner_node_16.outputs[7])
            test_group.links.new(inner_node_15.inputs[1], inner_node_3.outputs[0])
            test_group.links.new(inner_node_39.inputs[0], inner_node_8.outputs[0])
            test_group.links.new(inner_node_15.inputs[0], inner_node_39.outputs[0])
            test_group.links.new(inner_node_44.inputs[0], inner_node_37.outputs[0])
            test_group.links.new(inner_node_36.inputs[0], inner_node_4.outputs[0])
            test_group.links.new(inner_node_36.inputs[1], inner_node_20.outputs[0])
            test_group.links.new(inner_node_20.inputs[0], inner_node_19.outputs[0])
            test_group.links.new(inner_node_17.inputs[0], inner_node_14.outputs[0])
            test_group.links.new(inner_node_19.inputs[0], inner_node_17.outputs[0])
            test_group.links.new(inner_node_41.inputs[0], inner_node_15.outputs[0])
            test_group.links.new(inner_node_31.inputs[0], inner_node_5.outputs[0])
            test_group.links.new(inner_node_35.inputs[0], inner_node_4.outputs[0])
            test_group.links.new(inner_node_34.inputs[1], inner_node_35.outputs[1])
            test_group.links.new(inner_node_43.inputs[0], inner_node_42.outputs[0])
            test_group.links.new(inner_node_42.inputs[1], inner_node_39.outputs[0])
            test_group.links.new(inner_node_42.inputs[2], inner_node_18.outputs[0])
            test_group.links.new(inner_node_17.inputs[1], inner_node_43.outputs[0])
            test_group.links.new(inner_node_29.inputs[0], inner_node_28.outputs[0])
            test_group.links.new(inner_node_28.inputs[1], inner_node_44.outputs[0])
            test_group.links.new(inner_node_28.inputs[2], inner_node_30.outputs[0])
            test_group.links.new(inner_node_19.inputs[1], inner_node_29.outputs[0])
            test_group.links.new(inner_node_33.inputs[0], inner_node_32.outputs[0])
            test_group.links.new(inner_node_32.inputs[2], inner_node_34.outputs[0])
            test_group.links.new(inner_node_32.inputs[1], inner_node_40.outputs[0])
            test_group.links.new(inner_node_20.inputs[1], inner_node_33.outputs[0])
            test_group.links.new(inner_node_22.inputs[0], inner_node_16.outputs[8])
            test_group.links.new(inner_node_21.inputs[0], inner_node_16.outputs[9])
            test_group.links.new(inner_node_23.inputs[0], inner_node_16.outputs[10])
            test_group.links.new(inner_node_10.inputs[1], inner_node_22.outputs[0])
            test_group.links.new(inner_node_13.inputs[1], inner_node_21.outputs[0])
            test_group.links.new(inner_node_9.inputs[1], inner_node_23.outputs[0])
            test_group.links.new(inner_node_39.inputs[1], inner_node_22.outputs[0])
            test_group.links.new(inner_node_44.inputs[1], inner_node_21.outputs[0])
            test_group.links.new(inner_node_40.inputs[1], inner_node_23.outputs[0])
            test_group.links.new(inner_node_25.inputs[0], inner_node_26.outputs[8])
            test_group.links.new(inner_node_24.inputs[0], inner_node_26.outputs[9])
            test_group.links.new(inner_node_27.inputs[0], inner_node_26.outputs[10])
            test_group.links.new(inner_node_42.inputs[0], inner_node_25.outputs[0])
            test_group.links.new(inner_node_28.inputs[0], inner_node_24.outputs[0])
            test_group.links.new(inner_node_32.inputs[0], inner_node_27.outputs[0])
            test_group.links.new(inner_node_30.inputs[1], inner_node_31.outputs[1])
            test_group.links.new(inner_node_18.inputs[1], inner_node_41.outputs[1])

            inner_node_0.inputs[0].default_value = (0.0012069722870364785, 0.0, 0.8000000715255737, 1.0)
            inner_node_0.inputs[1].default_value = 0.0
            inner_node_0.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            inner_node_0.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_0.inputs[4].default_value = 0.0
            inner_node_0.inputs[5].default_value = 0.0
            inner_node_0.inputs[6].default_value = 0.0
            inner_node_0.inputs[7].default_value = 1.0
            inner_node_0.inputs[8].default_value = 0.0
            inner_node_0.inputs[9].default_value = 0.0
            inner_node_0.inputs[10].default_value = 0.0
            inner_node_0.inputs[11].default_value = 0.5
            inner_node_0.inputs[12].default_value = 0.0
            inner_node_0.inputs[13].default_value = 0.029999999329447746
            inner_node_0.inputs[14].default_value = 1.4500000476837158
            inner_node_0.inputs[15].default_value = 0.0
            inner_node_0.inputs[16].default_value = 0.0
            inner_node_0.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_0.inputs[18].default_value = 1.0
            inner_node_0.inputs[19].default_value = 1.0
            inner_node_0.inputs[20].default_value = (0.0, 0.0, 0.0)
            inner_node_0.inputs[21].default_value = (0.0, 0.0, 0.0)
            inner_node_0.inputs[22].default_value = (0.0, 0.0, 0.0)

            inner_node_1.inputs[0].default_value = (0.0012069722870364785, 0.0, 0.8000000715255737, 1.0)
            inner_node_1.inputs[1].default_value = 0.0
            inner_node_1.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            inner_node_1.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_1.inputs[4].default_value = 0.0
            inner_node_1.inputs[5].default_value = 0.0
            inner_node_1.inputs[6].default_value = 0.0
            inner_node_1.inputs[7].default_value = 1.0
            inner_node_1.inputs[8].default_value = 0.0
            inner_node_1.inputs[9].default_value = 0.0
            inner_node_1.inputs[10].default_value = 0.0
            inner_node_1.inputs[11].default_value = 0.5
            inner_node_1.inputs[12].default_value = 0.0
            inner_node_1.inputs[13].default_value = 0.029999999329447746
            inner_node_1.inputs[14].default_value = 1.4500000476837158
            inner_node_1.inputs[15].default_value = 0.0
            inner_node_1.inputs[16].default_value = 0.0
            inner_node_1.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_1.inputs[18].default_value = 1.0
            inner_node_1.inputs[19].default_value = 1.0
            inner_node_1.inputs[20].default_value = (0.0, 0.0, 0.0)
            inner_node_1.inputs[21].default_value = (0.0, 0.0, 0.0)
            inner_node_1.inputs[22].default_value = (0.0, 0.0, 0.0)

            inner_node_2.inputs[0].default_value = (0.0012069722870364785, 0.0, 0.8000000715255737, 1.0)
            inner_node_2.inputs[1].default_value = 0.0
            inner_node_2.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            inner_node_2.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_2.inputs[4].default_value = 0.0
            inner_node_2.inputs[5].default_value = 0.0
            inner_node_2.inputs[6].default_value = 0.0
            inner_node_2.inputs[7].default_value = 1.0
            inner_node_2.inputs[8].default_value = 0.0
            inner_node_2.inputs[9].default_value = 0.0
            inner_node_2.inputs[10].default_value = 0.0
            inner_node_2.inputs[11].default_value = 0.5
            inner_node_2.inputs[12].default_value = 0.0
            inner_node_2.inputs[13].default_value = 0.029999999329447746
            inner_node_2.inputs[14].default_value = 1.4500000476837158
            inner_node_2.inputs[15].default_value = 0.0
            inner_node_2.inputs[16].default_value = 0.0
            inner_node_2.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_2.inputs[18].default_value = 1.0
            inner_node_2.inputs[19].default_value = 1.0
            inner_node_2.inputs[20].default_value = (0.0, 0.0, 0.0)
            inner_node_2.inputs[21].default_value = (0.0, 0.0, 0.0)
            inner_node_2.inputs[22].default_value = (0.0, 0.0, 0.0)

            inner_node_3.inputs[0].default_value = (0.0012069722870364785, 0.0, 0.8000000715255737, 1.0)
            inner_node_3.inputs[1].default_value = 0.0
            inner_node_3.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            inner_node_3.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_3.inputs[4].default_value = 0.0
            inner_node_3.inputs[5].default_value = 0.0
            inner_node_3.inputs[6].default_value = 0.0
            inner_node_3.inputs[7].default_value = 1.0
            inner_node_3.inputs[8].default_value = 0.0
            inner_node_3.inputs[9].default_value = 0.0
            inner_node_3.inputs[10].default_value = 0.0
            inner_node_3.inputs[11].default_value = 0.5
            inner_node_3.inputs[12].default_value = 0.0
            inner_node_3.inputs[13].default_value = 0.029999999329447746
            inner_node_3.inputs[14].default_value = 1.4500000476837158
            inner_node_3.inputs[15].default_value = 0.0
            inner_node_3.inputs[16].default_value = 0.0
            inner_node_3.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_3.inputs[18].default_value = 1.0
            inner_node_3.inputs[19].default_value = 1.0
            inner_node_3.inputs[20].default_value = (0.0, 0.0, 0.0)
            inner_node_3.inputs[21].default_value = (0.0, 0.0, 0.0)
            inner_node_3.inputs[22].default_value = (0.0, 0.0, 0.0)

            inner_node_4.inputs[0].default_value = 0.0

            inner_node_5.inputs[0].default_value = 1.0

            inner_node_7.inputs[0].default_value = 1.0
            inner_node_7.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_7.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_8.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[1].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[3].default_value = 1.0
            inner_node_8.outputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_8.outputs[1].default_value = 0.0

            inner_node_9.inputs[0].default_value = 0.5
            inner_node_9.inputs[1].default_value = 0.5
            inner_node_9.inputs[2].default_value = 0.0
            inner_node_9.outputs[0].default_value = 0.0

            inner_node_10.inputs[0].default_value = 0.5
            inner_node_10.inputs[1].default_value = 0.5
            inner_node_10.inputs[2].default_value = 0.0
            inner_node_10.outputs[0].default_value = 0.0

            inner_node_11.inputs[0].default_value = 1.0
            inner_node_11.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_11.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_12.inputs[0].default_value = 1.0
            inner_node_12.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_12.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_13.inputs[0].default_value = 0.5
            inner_node_13.inputs[1].default_value = 0.5
            inner_node_13.inputs[2].default_value = 0.0
            inner_node_13.outputs[0].default_value = 0.0

            inner_node_14.inputs[0].default_value = 1.0
            inner_node_14.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_14.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_15.inputs[0].default_value = 0.0

            inner_node_17.inputs[0].default_value = 0.5
            inner_node_17.inputs[1].default_value = 0.5
            inner_node_17.inputs[2].default_value = 0.0
            inner_node_17.outputs[0].default_value = 0.0

            inner_node_18.inputs[0].default_value = 0.0
            inner_node_18.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_18.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_19.inputs[0].default_value = 0.5
            inner_node_19.inputs[1].default_value = 0.5
            inner_node_19.inputs[2].default_value = 0.0
            inner_node_19.outputs[0].default_value = 0.0

            inner_node_20.inputs[0].default_value = 0.5
            inner_node_20.inputs[1].default_value = 0.5
            inner_node_20.inputs[2].default_value = 0.0
            inner_node_20.outputs[0].default_value = 0.0

            inner_node_21.inputs[0].default_value = 0.5
            inner_node_21.inputs[1].default_value = 0.5
            inner_node_21.inputs[2].default_value = 0.0
            inner_node_21.outputs[0].default_value = 0.0

            inner_node_22.inputs[0].default_value = 0.5
            inner_node_22.inputs[1].default_value = 0.5
            inner_node_22.inputs[2].default_value = 0.0
            inner_node_22.outputs[0].default_value = 0.0

            inner_node_23.inputs[0].default_value = 0.5
            inner_node_23.inputs[1].default_value = 0.5
            inner_node_23.inputs[2].default_value = 0.0
            inner_node_23.outputs[0].default_value = 0.0

            inner_node_24.inputs[0].default_value = 0.5
            inner_node_24.inputs[1].default_value = 0.5
            inner_node_24.inputs[2].default_value = 0.0
            inner_node_24.outputs[0].default_value = 0.0

            inner_node_25.inputs[0].default_value = 0.5
            inner_node_25.inputs[1].default_value = 0.5
            inner_node_25.inputs[2].default_value = 0.0
            inner_node_25.outputs[0].default_value = 0.0

            inner_node_27.inputs[0].default_value = 0.5
            inner_node_27.inputs[1].default_value = 0.5
            inner_node_27.inputs[2].default_value = 0.0
            inner_node_27.outputs[0].default_value = 0.0

            inner_node_28.inputs[0].default_value = 0.0

            inner_node_29.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_29.outputs[1].default_value = 0.0

            inner_node_30.inputs[0].default_value = 0.0
            inner_node_30.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_30.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_31.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_31.outputs[1].default_value = 0.0

            inner_node_32.inputs[0].default_value = 0.0

            inner_node_33.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_33.outputs[1].default_value = 0.0

            inner_node_34.inputs[0].default_value = 0.0
            inner_node_34.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_34.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_35.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_35.outputs[1].default_value = 0.0

            inner_node_37.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_37.inputs[1].default_value = (0.0, 0.0, 0.0)
            inner_node_37.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_37.inputs[3].default_value = 1.0
            inner_node_37.outputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_37.outputs[1].default_value = 0.0

            inner_node_38.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_38.inputs[1].default_value = (0.0, 0.0, 0.0)
            inner_node_38.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_38.inputs[3].default_value = 1.0
            inner_node_38.outputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_38.outputs[1].default_value = 0.0

            inner_node_39.inputs[0].default_value = 0.5
            inner_node_39.inputs[1].default_value = 0.5
            inner_node_39.inputs[2].default_value = 0.0
            inner_node_39.outputs[0].default_value = 0.0

            inner_node_40.inputs[0].default_value = 0.5
            inner_node_40.inputs[1].default_value = 0.5
            inner_node_40.inputs[2].default_value = 0.0
            inner_node_40.outputs[0].default_value = 0.0

            inner_node_41.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_41.outputs[1].default_value = 0.0

            inner_node_42.inputs[0].default_value = 0.0

            inner_node_43.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_43.outputs[1].default_value = 0.0

            inner_node_44.inputs[0].default_value = 0.5
            inner_node_44.inputs[1].default_value = 0.5
            inner_node_44.inputs[2].default_value = 0.0
            inner_node_44.outputs[0].default_value = 0.0

            inner_node_0.location = (-220.0, -220.0)
            inner_node_0.width = 240.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Principled BSDF.007'
            inner_node_1.location = (-220.0, -60.0)
            inner_node_1.width = 240.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Principled BSDF.008'
            inner_node_2.location = (-220.0, 100.0)
            inner_node_2.width = 240.0
            inner_node_2.width_hidden = 42.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Principled BSDF.006'
            inner_node_3.location = (-220.0, 260.0)
            inner_node_3.width = 240.0
            inner_node_3.width_hidden = 42.0
            inner_node_3.height = 100.0
            inner_node_3.name = 'Principled BSDF.005'
            inner_node_4.location = (820.0, 240.0)
            inner_node_4.width = 140.0
            inner_node_4.width_hidden = 42.0
            inner_node_4.height = 100.0
            inner_node_4.name = 'Mix Shader.002'
            inner_node_5.location = (480.0, 240.0)
            inner_node_5.width = 140.0
            inner_node_5.width_hidden = 42.0
            inner_node_5.height = 100.0
            inner_node_5.name = 'Mix Shader.001'
            inner_node_6.location = (-700.0, 20.0)
            inner_node_6.width = 140.0
            inner_node_6.width_hidden = 42.0
            inner_node_6.height = 100.0
            inner_node_6.name = 'Group Input'
            inner_node_7.location = (-960.0, 1580.0)
            inner_node_7.width = 140.0
            inner_node_7.width_hidden = 42.0
            inner_node_7.height = 100.0
            inner_node_7.name = 'Invert.004'
            inner_node_8.location = (-500.0, 1440.0)
            inner_node_8.width = 140.0
            inner_node_8.width_hidden = 42.0
            inner_node_8.height = 100.0
            inner_node_8.name = 'Vector Math'
            inner_node_9.location = (-680.0, 1000.0)
            inner_node_9.width = 140.0
            inner_node_9.width_hidden = 42.0
            inner_node_9.height = 100.0
            inner_node_9.name = 'Math.002'
            inner_node_9.operation = 'MULTIPLY'
            inner_node_9.use_clamp = True
            inner_node_10.location = (-680.0, 1320.0)
            inner_node_10.width = 140.0
            inner_node_10.width_hidden = 42.0
            inner_node_10.height = 100.0
            inner_node_10.name = 'Math'
            inner_node_10.operation = 'MULTIPLY'
            inner_node_10.use_clamp = True
            inner_node_11.location = (-960.0, 1420.0)
            inner_node_11.width = 140.0
            inner_node_11.width_hidden = 42.0
            inner_node_11.height = 100.0
            inner_node_11.name = 'Invert.006'
            inner_node_12.location = (-960.0, 1500.0)
            inner_node_12.width = 140.0
            inner_node_12.width_hidden = 42.0
            inner_node_12.height = 100.0
            inner_node_12.name = 'Invert.005'
            inner_node_13.location = (-680.0, 1160.0)
            inner_node_13.width = 140.0
            inner_node_13.width_hidden = 42.0
            inner_node_13.height = 100.0
            inner_node_13.name = 'Math.001'
            inner_node_13.operation = 'MULTIPLY'
            inner_node_13.use_clamp = True
            inner_node_14.location = (-960.0, 1660.0)
            inner_node_14.width = 140.0
            inner_node_14.width_hidden = 42.0
            inner_node_14.height = 100.0
            inner_node_14.name = 'Invert.003'
            inner_node_15.location = (160.0, 240.0)
            inner_node_15.width = 140.0
            inner_node_15.width_hidden = 42.0
            inner_node_15.height = 100.0
            inner_node_15.name = 'Mix Shader'
            inner_node_16.location = (-1460.0, 920.0)
            inner_node_16.width = 140.0
            inner_node_16.width_hidden = 42.0
            inner_node_16.height = 100.0
            inner_node_16.name = 'Group Input.001'
            inner_node_17.location = (1160.0, 1820.0)
            inner_node_17.width = 140.0
            inner_node_17.width_hidden = 42.0
            inner_node_17.height = 100.0
            inner_node_17.name = 'Math.008'
            inner_node_18.location = (600.0, 1200.0)
            inner_node_18.width = 140.0
            inner_node_18.width_hidden = 42.0
            inner_node_18.height = 100.0
            inner_node_18.name = 'Invert'
            inner_node_19.location = (1460.0, 1820.0)
            inner_node_19.width = 140.0
            inner_node_19.width_hidden = 42.0
            inner_node_19.height = 100.0
            inner_node_19.name = 'Math.006'
            inner_node_20.location = (1780.0, 1820.0)
            inner_node_20.width = 140.0
            inner_node_20.width_hidden = 42.0
            inner_node_20.height = 100.0
            inner_node_20.name = 'Math.007'
            inner_node_21.location = (-1160.0, 540.0)
            inner_node_21.width = 140.0
            inner_node_21.width_hidden = 42.0
            inner_node_21.height = 100.0
            inner_node_21.name = 'Math.010'
            inner_node_21.operation = 'CEIL'
            inner_node_22.location = (-1160.0, 680.0)
            inner_node_22.width = 140.0
            inner_node_22.width_hidden = 42.0
            inner_node_22.height = 100.0
            inner_node_22.name = 'Math.009'
            inner_node_22.operation = 'CEIL'
            inner_node_23.location = (-1160.0, 400.0)
            inner_node_23.width = 140.0
            inner_node_23.width_hidden = 42.0
            inner_node_23.height = 100.0
            inner_node_23.name = 'Math.011'
            inner_node_23.operation = 'CEIL'
            inner_node_24.location = (240.0, 2000.0)
            inner_node_24.width = 140.0
            inner_node_24.width_hidden = 42.0
            inner_node_24.height = 100.0
            inner_node_24.name = 'Math.012'
            inner_node_24.operation = 'CEIL'
            inner_node_25.location = (240.0, 2140.0)
            inner_node_25.width = 140.0
            inner_node_25.width_hidden = 42.0
            inner_node_25.height = 100.0
            inner_node_25.name = 'Math.013'
            inner_node_25.operation = 'CEIL'
            inner_node_26.location = (-120.0, 1980.0)
            inner_node_26.width = 140.0
            inner_node_26.width_hidden = 42.0
            inner_node_26.height = 100.0
            inner_node_26.name = 'Group Input.002'
            inner_node_27.location = (240.0, 1860.0)
            inner_node_27.width = 140.0
            inner_node_27.width_hidden = 42.0
            inner_node_27.height = 100.0
            inner_node_27.name = 'Math.014'
            inner_node_27.operation = 'CEIL'
            inner_node_28.location = (1020.0, 1480.0)
            inner_node_28.width = 140.0
            inner_node_28.width_hidden = 42.0
            inner_node_28.height = 100.0
            inner_node_28.name = 'Mix Shader.004'
            inner_node_29.location = (1200.0, 1480.0)
            inner_node_29.width = 140.0
            inner_node_29.width_hidden = 42.0
            inner_node_29.height = 100.0
            inner_node_29.name = 'Shader to RGB.004'
            inner_node_30.location = (1020.0, 1280.0)
            inner_node_30.width = 140.0
            inner_node_30.width_hidden = 42.0
            inner_node_30.height = 100.0
            inner_node_30.name = 'Invert.001'
            inner_node_31.location = (1020.0, 1080.0)
            inner_node_31.width = 140.0
            inner_node_31.width_hidden = 42.0
            inner_node_31.height = 100.0
            inner_node_31.name = 'Shader to RGB.001'
            inner_node_32.location = (1400.0, 1540.0)
            inner_node_32.width = 140.0
            inner_node_32.width_hidden = 42.0
            inner_node_32.height = 100.0
            inner_node_32.name = 'Mix Shader.005'
            inner_node_33.location = (1580.0, 1540.0)
            inner_node_33.width = 140.0
            inner_node_33.width_hidden = 42.0
            inner_node_33.height = 100.0
            inner_node_33.name = 'Shader to RGB.005'
            inner_node_34.location = (1400.0, 1340.0)
            inner_node_34.width = 140.0
            inner_node_34.width_hidden = 42.0
            inner_node_34.height = 100.0
            inner_node_34.name = 'Invert.002'
            inner_node_35.location = (1400.0, 1140.0)
            inner_node_35.width = 140.0
            inner_node_35.width_hidden = 42.0
            inner_node_35.height = 100.0
            inner_node_35.name = 'Shader to RGB.002'
            inner_node_36.location = (2360.0, 1120.0)
            inner_node_36.width = 140.0
            inner_node_36.width_hidden = 42.0
            inner_node_36.height = 100.0
            inner_node_36.name = 'Group Output'
            inner_node_36.is_active_output = True
            inner_node_37.location = (-300.0, 1440.0)
            inner_node_37.width = 140.0
            inner_node_37.width_hidden = 42.0
            inner_node_37.height = 100.0
            inner_node_37.name = 'Vector Math.001'
            inner_node_38.location = (-100.0, 1440.0)
            inner_node_38.width = 140.0
            inner_node_38.width_hidden = 42.0
            inner_node_38.height = 100.0
            inner_node_38.name = 'Vector Math.002'
            inner_node_39.location = (-280.0, 1000.0)
            inner_node_39.width = 140.0
            inner_node_39.width_hidden = 42.0
            inner_node_39.height = 100.0
            inner_node_39.name = 'Math.005'
            inner_node_39.operation = 'MULTIPLY'
            inner_node_39.use_clamp = True
            inner_node_40.location = (160.0, 1000.0)
            inner_node_40.width = 140.0
            inner_node_40.width_hidden = 42.0
            inner_node_40.height = 100.0
            inner_node_40.name = 'Math.004'
            inner_node_40.operation = 'MULTIPLY'
            inner_node_40.use_clamp = True
            inner_node_41.location = (600.0, 1020.0)
            inner_node_41.width = 140.0
            inner_node_41.width_hidden = 42.0
            inner_node_41.height = 100.0
            inner_node_41.name = 'Shader to RGB'
            inner_node_42.location = (600.0, 1420.0)
            inner_node_42.width = 140.0
            inner_node_42.width_hidden = 42.0
            inner_node_42.height = 100.0
            inner_node_42.name = 'Mix Shader.003'
            inner_node_43.location = (780.0, 1420.0)
            inner_node_43.width = 140.0
            inner_node_43.width_hidden = 42.0
            inner_node_43.height = 100.0
            inner_node_43.name = 'Shader to RGB.003'
            inner_node_44.location = (-60.0, 1000.0)
            inner_node_44.width = 140.0
            inner_node_44.width_hidden = 42.0
            inner_node_44.height = 100.0
            inner_node_44.name = 'Math.003'
            inner_node_44.operation = 'MULTIPLY'
            inner_node_44.use_clamp = True
        else:
            test_group = bpy.data.node_groups['Combine_MatCol_ShadeVer']

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'Combine MatCol ShadeVer'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 198.359

        node.location = (-540.0, 780.0)

        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class DYT_Strip_Assigner:
    def __init__(self, tree):
        if 'DYT_Strip_Assigner' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('DYT_Strip_Assigner', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupOutput')  #Output
            inner_node_1 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_2 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_3 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_4 = test_group.nodes.new('ShaderNodeCombineRGB')  #
            inner_node_5 = test_group.nodes.new('ShaderNodeMapping')  #
            inner_node_6 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_7 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_8 = test_group.nodes.new('ShaderNodeCombineRGB')  #
            inner_node_9 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_10 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_11 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_12 = test_group.nodes.new('ShaderNodeMapping')  #
            inner_node_13 = test_group.nodes.new('ShaderNodeCombineRGB')  #
            inner_node_14 = test_group.nodes.new('ShaderNodeMath')  #
            inner_node_15 = test_group.nodes.new('ShaderNodeMapping')  #
            inner_node_16 = test_group.nodes.new('NodeGroupInput')  #
            inner_node_17 = test_group.nodes.new('NodeGroupInput')  #
            inner_node_18 = test_group.nodes.new('NodeGroupInput')  #

            test_group.inputs.new('NodeSocketVector', 'Light Tracking')
            test_group.inputs[0].min_value = -3.4028234663852886e+38
            test_group.inputs[0].max_value = 3.4028234663852886e+38
            test_group.inputs[0].hide_value = True
            test_group.inputs.new('NodeSocketFloat', 'MatScale1X')
            test_group.inputs[1].min_value = -10000.0
            test_group.inputs[1].max_value = 10000.0
            test_group.inputs[1].hide_value = True
            test_group.inputs.new('NodeSocketFloatUnsigned', 'Color Strip Strength')
            test_group.inputs[2].min_value = 0.0
            test_group.inputs[2].max_value = 1.0
            test_group.inputs[2].hide_value = False
            test_group.inputs.new('NodeSocketFloatUnsigned', 'Rim Light Strength')
            test_group.inputs[3].min_value = 0.0
            test_group.inputs[3].max_value = 1.0
            test_group.inputs[3].hide_value = False
            test_group.inputs.new('NodeSocketFloatUnsigned', 'Shine Strength')
            test_group.inputs[4].min_value = 0.0
            test_group.inputs[4].max_value = 1.0
            test_group.inputs[4].hide_value = False
            test_group.inputs.new('NodeSocketVectorXYZ', 'Color Scale')
            test_group.inputs[5].min_value = -3.4028234663852886e+38
            test_group.inputs[5].max_value = 3.4028234663852886e+38
            test_group.inputs[5].hide_value = False
            test_group.inputs.new('NodeSocketVectorXYZ', 'Rim Scale')
            test_group.inputs[6].min_value = -3.4028234663852886e+38
            test_group.inputs[6].max_value = 3.4028234663852886e+38
            test_group.inputs[6].hide_value = False
            test_group.inputs.new('NodeSocketVectorXYZ', 'Shine Scale')
            test_group.inputs[7].min_value = -3.4028234663852886e+38
            test_group.inputs[7].max_value = 3.4028234663852886e+38
            test_group.inputs[7].hide_value = False

            test_group.outputs.new('NodeSocketVector', 'Color Strip')
            test_group.outputs.new('NodeSocketVector', 'Rim Light')
            test_group.outputs.new('NodeSocketVector', 'Shine')

            inner_node_0.location = (520.0, 20.0)
            inner_node_1.location = (-160.0, 340.0)
            inner_node_2.location = (0.0, 340.0)
            inner_node_3.location = (-320.0, 340.0)
            inner_node_4.location = (160.0, 340.0)
            inner_node_5.location = (320.0, 340.0)
            inner_node_6.location = (0.0, -340.0)
            inner_node_7.location = (-160.0, -340.0)
            inner_node_8.location = (160.0, -340.0)
            inner_node_9.location = (0.0, 0.0)
            inner_node_10.location = (-160.0, 0.0)
            inner_node_11.location = (-320.0, 0.0)
            inner_node_12.location = (320.0, 0.0)
            inner_node_13.location = (160.0, 0.0)
            inner_node_14.location = (-320.0, -340.0)
            inner_node_15.location = (320.0, -340.0)
            inner_node_16.location = (-520.0, -240.0)
            inner_node_17.location = (-520.0, 100.0)
            inner_node_18.location = (-520.0, 440.0)

            test_group.links.new(inner_node_1.inputs[0], inner_node_3.outputs[0])
            test_group.links.new(inner_node_2.inputs[1], inner_node_1.outputs[0])
            test_group.links.new(inner_node_5.inputs[1], inner_node_4.outputs[0])
            test_group.links.new(inner_node_4.inputs[1], inner_node_2.outputs[0])
            test_group.links.new(inner_node_10.inputs[0], inner_node_11.outputs[0])
            test_group.links.new(inner_node_9.inputs[1], inner_node_10.outputs[0])
            test_group.links.new(inner_node_13.inputs[1], inner_node_9.outputs[0])
            test_group.links.new(inner_node_12.inputs[1], inner_node_13.outputs[0])
            test_group.links.new(inner_node_7.inputs[0], inner_node_14.outputs[0])
            test_group.links.new(inner_node_6.inputs[1], inner_node_7.outputs[0])
            test_group.links.new(inner_node_8.inputs[1], inner_node_6.outputs[0])
            test_group.links.new(inner_node_15.inputs[1], inner_node_8.outputs[0])
            test_group.links.new(inner_node_12.inputs[0], inner_node_17.outputs[0])
            test_group.links.new(inner_node_11.inputs[0], inner_node_17.outputs[1])
            test_group.links.new(inner_node_0.inputs[0], inner_node_5.outputs[0])
            test_group.links.new(inner_node_0.inputs[1], inner_node_12.outputs[0])
            test_group.links.new(inner_node_0.inputs[2], inner_node_15.outputs[0])
            test_group.links.new(inner_node_13.inputs[0], inner_node_17.outputs[3])
            test_group.links.new(inner_node_3.inputs[0], inner_node_18.outputs[1])
            test_group.links.new(inner_node_4.inputs[0], inner_node_18.outputs[2])
            test_group.links.new(inner_node_5.inputs[0], inner_node_18.outputs[0])
            test_group.links.new(inner_node_14.inputs[0], inner_node_16.outputs[1])
            test_group.links.new(inner_node_8.inputs[0], inner_node_16.outputs[4])
            test_group.links.new(inner_node_15.inputs[0], inner_node_16.outputs[0])
            test_group.links.new(inner_node_15.inputs[3], inner_node_16.outputs[7])
            test_group.links.new(inner_node_12.inputs[3], inner_node_17.outputs[6])
            test_group.links.new(inner_node_5.inputs[3], inner_node_18.outputs[5])

            inner_node_1.inputs[0].default_value = 0.5
            inner_node_1.inputs[1].default_value = 0.015625
            inner_node_1.inputs[2].default_value = 0.0
            inner_node_1.outputs[0].default_value = 0.0

            inner_node_2.inputs[0].default_value = 1.0
            inner_node_2.inputs[1].default_value = -1.0
            inner_node_2.inputs[2].default_value = 0.0
            inner_node_2.outputs[0].default_value = 0.0

            inner_node_3.inputs[0].default_value = 0.5
            inner_node_3.inputs[1].default_value = 0.125
            inner_node_3.inputs[2].default_value = 0.046875
            inner_node_3.outputs[0].default_value = 0.0

            inner_node_4.inputs[0].default_value = 0.0
            inner_node_4.inputs[1].default_value = 0.0
            inner_node_4.inputs[2].default_value = 0.0
            inner_node_4.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_5.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_5.inputs[1].default_value = (0.0, 0.171875, 0.0)
            inner_node_5.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_5.inputs[3].default_value = (1.0, 0.03125, 0.0)
            inner_node_5.outputs[0].default_value = (0.0, 0.0, 0.0)

            inner_node_6.inputs[0].default_value = 1.0
            inner_node_6.inputs[1].default_value = -1.0
            inner_node_6.inputs[2].default_value = 0.0
            inner_node_6.outputs[0].default_value = 0.0

            inner_node_7.inputs[0].default_value = 0.5
            inner_node_7.inputs[1].default_value = 0.078125
            inner_node_7.inputs[2].default_value = 0.0
            inner_node_7.outputs[0].default_value = 0.0

            inner_node_8.inputs[0].default_value = 0.0
            inner_node_8.inputs[1].default_value = 0.0
            inner_node_8.inputs[2].default_value = 0.0
            inner_node_8.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_9.inputs[0].default_value = 1.0
            inner_node_9.inputs[1].default_value = -1.0
            inner_node_9.inputs[2].default_value = 0.0
            inner_node_9.outputs[0].default_value = 0.0

            inner_node_10.inputs[0].default_value = 0.5
            inner_node_10.inputs[1].default_value = 0.046875
            inner_node_10.inputs[2].default_value = 0.0
            inner_node_10.outputs[0].default_value = 0.0

            inner_node_11.inputs[0].default_value = 0.5
            inner_node_11.inputs[1].default_value = 0.125
            inner_node_11.inputs[2].default_value = 0.046875
            inner_node_11.outputs[0].default_value = 0.0

            inner_node_12.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_12.inputs[1].default_value = (0.0, 0.171875, 0.0)
            inner_node_12.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_12.inputs[3].default_value = (1.0, 0.03125, 0.0)
            inner_node_12.outputs[0].default_value = (0.0, 0.0, 0.0)

            inner_node_13.inputs[0].default_value = 0.0
            inner_node_13.inputs[1].default_value = 0.0
            inner_node_13.inputs[2].default_value = 0.0
            inner_node_13.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_14.inputs[0].default_value = 0.5
            inner_node_14.inputs[1].default_value = 0.125
            inner_node_14.inputs[2].default_value = 0.046875
            inner_node_14.outputs[0].default_value = 0.0

            inner_node_15.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_15.inputs[1].default_value = (0.0, 0.171875, 0.0)
            inner_node_15.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_15.inputs[3].default_value = (1.0, 0.03125, 0.0)
            inner_node_15.outputs[0].default_value = (0.0, 0.0, 0.0)

            inner_node_0.location = (520.0, 20.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 80.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Output'
            inner_node_0.is_active_output = True
            inner_node_1.location = (-160.0, 340.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 100.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Math.009'
            inner_node_2.location = (0.0, 340.0)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 100.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Math.010'
            inner_node_2.operation = 'SUBTRACT'
            inner_node_3.location = (-320.0, 340.0)
            inner_node_3.width = 140.0
            inner_node_3.width_hidden = 100.0
            inner_node_3.height = 100.0
            inner_node_3.name = 'Math'
            inner_node_3.operation = 'MULTIPLY'
            inner_node_4.location = (160.0, 340.0)
            inner_node_4.width = 140.0
            inner_node_4.width_hidden = 100.0
            inner_node_4.height = 100.0
            inner_node_4.name = 'Combine RGB.003'
            inner_node_4.use_custom_color = True
            inner_node_5.location = (320.0, 340.0)
            inner_node_5.width = 140.0
            inner_node_5.width_hidden = 100.0
            inner_node_5.height = 100.0
            inner_node_5.name = 'Mapping.001'
            inner_node_6.location = (0.0, -340.0)
            inner_node_6.width = 140.0
            inner_node_6.width_hidden = 100.0
            inner_node_6.height = 100.0
            inner_node_6.name = 'Math.012'
            inner_node_6.operation = 'SUBTRACT'
            inner_node_7.location = (-160.0, -340.0)
            inner_node_7.width = 140.0
            inner_node_7.width_hidden = 100.0
            inner_node_7.height = 100.0
            inner_node_7.name = 'Math.007'
            inner_node_8.location = (160.0, -340.0)
            inner_node_8.width = 140.0
            inner_node_8.width_hidden = 100.0
            inner_node_8.height = 100.0
            inner_node_8.name = 'Combine RGB.005'
            inner_node_8.use_custom_color = True
            inner_node_9.location = (0.0, 0.0)
            inner_node_9.width = 140.0
            inner_node_9.width_hidden = 100.0
            inner_node_9.height = 100.0
            inner_node_9.name = 'Math.011'
            inner_node_9.operation = 'SUBTRACT'
            inner_node_10.location = (-160.0, 0.0)
            inner_node_10.width = 140.0
            inner_node_10.width_hidden = 100.0
            inner_node_10.height = 100.0
            inner_node_10.name = 'Math.004'
            inner_node_11.location = (-320.0, 0.0)
            inner_node_11.width = 140.0
            inner_node_11.width_hidden = 100.0
            inner_node_11.height = 100.0
            inner_node_11.name = 'Math.003'
            inner_node_11.operation = 'MULTIPLY'
            inner_node_12.location = (320.0, 0.0)
            inner_node_12.width = 140.0
            inner_node_12.width_hidden = 100.0
            inner_node_12.height = 100.0
            inner_node_12.name = 'Mapping.002'
            inner_node_13.location = (160.0, 0.0)
            inner_node_13.width = 140.0
            inner_node_13.width_hidden = 100.0
            inner_node_13.height = 100.0
            inner_node_13.name = 'Combine RGB.004'
            inner_node_13.use_custom_color = True
            inner_node_14.location = (-320.0, -340.0)
            inner_node_14.width = 140.0
            inner_node_14.width_hidden = 100.0
            inner_node_14.height = 100.0
            inner_node_14.name = 'Math.006'
            inner_node_14.operation = 'MULTIPLY'
            inner_node_15.location = (320.0, -340.0)
            inner_node_15.width = 140.0
            inner_node_15.width_hidden = 100.0
            inner_node_15.height = 100.0
            inner_node_15.name = 'Mapping.003'
            inner_node_16.location = (-520.0, -240.0)
            inner_node_16.width = 140.0
            inner_node_16.width_hidden = 80.0
            inner_node_16.height = 100.0
            inner_node_16.name = 'Group Input.002'
            inner_node_17.location = (-520.0, 100.0)
            inner_node_17.width = 140.0
            inner_node_17.width_hidden = 80.0
            inner_node_17.height = 100.0
            inner_node_17.name = 'Group Input'
            inner_node_18.location = (-520.0, 440.0)
            inner_node_18.width = 140.0
            inner_node_18.width_hidden = 80.0
            inner_node_18.height = 100.0
            inner_node_18.name = 'Group Input.001'
        else:
            test_group = bpy.data.node_groups['DYT_Strip_Assigner']

        

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'DYT Strip Assigner'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 220.82861328125

        node.inputs[2].default_value = 0.515
        node.inputs[3].default_value = 0.000
        node.inputs[4].default_value = 0.250
        node.inputs[5].default_value = (0.96, 0.02000, 0.0)
        node.inputs[6].default_value = (0.96, 0.03125, 0.0)
        node.inputs[7].default_value = (0.96, 0.02400, 0.0)

        node.location = (-840.0, 120.0)

        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MatCol_Plus_DYT:
    def __init__(self, tree):
        if 'MatCol_Plus_DYT' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatCol_Plus_DYT', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_1 = test_group.nodes.new('NodeGroupInput')
            inner_node_2 = test_group.nodes.new('NodeGroupOutput')
            inner_node_3 = test_group.nodes.new('ShaderNodeEmission')

            test_group.inputs.new('NodeSocketShader', 'MatCol')
            test_group.inputs.new('NodeSocketFloatFactor', 'Value')
            test_group.inputs['Value'].min_value = 0.0
            test_group.inputs['Value'].max_value = 1.0
            test_group.inputs['Value'].hide_value = False
            test_group.inputs.new('NodeSocketColor', 'DYT')
            test_group.inputs.new('NodeSocketFloat', 'Strength')
            test_group.inputs['Strength'].min_value = 0.0
            test_group.inputs['Strength'].max_value = 1000000.0
            test_group.inputs['Strength'].hide_value = False

            test_group.outputs.new('NodeSocketShader', 'Shader')

            inner_node_0.location = (80.0, 74.1959228515625)
            inner_node_1.location = (-280.0, -0.0)
            inner_node_2.location = (270.0, -0.0)
            inner_node_3.location = (-80.0, -74.196044921875)

            test_group.links.new(inner_node_0.inputs[1], inner_node_1.outputs[0])
            test_group.links.new(inner_node_0.inputs[0], inner_node_1.outputs[1])
            test_group.links.new(inner_node_2.inputs[0], inner_node_0.outputs[0])
            test_group.links.new(inner_node_3.inputs[0], inner_node_1.outputs[2])
            test_group.links.new(inner_node_0.inputs[2], inner_node_3.outputs[0])
            test_group.links.new(inner_node_3.inputs[1], inner_node_1.outputs[3])

            inner_node_0.inputs[0].default_value = 0.5

            inner_node_3.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            inner_node_3.inputs[1].default_value = 1.0

            inner_node_0.location = (80.0, 74.1959228515625)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Mix Shader'
            inner_node_1.location = (-280.0, -0.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Group Input'
            inner_node_2.location = (270.0, -0.0)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 42.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Group Output'
            inner_node_2.is_active_output = True
            inner_node_3.location = (-80.0, -74.196044921875)
            inner_node_3.width = 140.0
            inner_node_3.width_hidden = 42.0
            inner_node_3.height = 100.0
            inner_node_3.name = 'Emission'
        else:
            test_group = bpy.data.node_groups['MatCol_Plus_DYT']

        

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatCol Plus DYT'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 140.0

        node.inputs[-1].default_value = 1.0

        node.location = (120.0, 300.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class Combine_MatCol:
    def __init__(self, tree):
        if 'Combine_MatCol' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('Combine_MatCol', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('ShaderNodeBsdfPrincipled')
            inner_node_1 = test_group.nodes.new('ShaderNodeBsdfPrincipled')
            inner_node_2 = test_group.nodes.new('ShaderNodeBsdfPrincipled')
            inner_node_3 = test_group.nodes.new('ShaderNodeBsdfPrincipled')
            inner_node_4 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_5 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_6 = test_group.nodes.new('NodeGroupInput')
            inner_node_7 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_8 = test_group.nodes.new('ShaderNodeVectorMath')
            inner_node_9 = test_group.nodes.new('ShaderNodeMath')
            inner_node_10 = test_group.nodes.new('ShaderNodeMath')
            inner_node_11 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_12 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_13 = test_group.nodes.new('ShaderNodeMath')
            inner_node_14 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_15 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_16 = test_group.nodes.new('NodeGroupInput')
            inner_node_17 = test_group.nodes.new('ShaderNodeMath')
            inner_node_18 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_19 = test_group.nodes.new('ShaderNodeMath')
            inner_node_20 = test_group.nodes.new('ShaderNodeMath')
            inner_node_21 = test_group.nodes.new('ShaderNodeMath')
            inner_node_22 = test_group.nodes.new('ShaderNodeMath')
            inner_node_23 = test_group.nodes.new('ShaderNodeMath')
            inner_node_24 = test_group.nodes.new('ShaderNodeMath')
            inner_node_25 = test_group.nodes.new('ShaderNodeMath')
            inner_node_26 = test_group.nodes.new('NodeGroupInput')
            inner_node_27 = test_group.nodes.new('ShaderNodeMath')
            inner_node_28 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_29 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_30 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_31 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_32 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_33 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_34 = test_group.nodes.new('ShaderNodeInvert')
            inner_node_35 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_36 = test_group.nodes.new('NodeGroupOutput')
            inner_node_37 = test_group.nodes.new('ShaderNodeVectorMath')
            inner_node_38 = test_group.nodes.new('ShaderNodeVectorMath')
            inner_node_39 = test_group.nodes.new('ShaderNodeMath')
            inner_node_40 = test_group.nodes.new('ShaderNodeMath')
            inner_node_41 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_42 = test_group.nodes.new('ShaderNodeMixShader')
            inner_node_43 = test_group.nodes.new('ShaderNodeShaderToRGB')
            inner_node_44 = test_group.nodes.new('ShaderNodeMath')

            test_group.inputs.new('NodeSocketColor', 'MatCol0')
            test_group.inputs.new('NodeSocketColor', 'Lines')
            test_group.inputs.new('NodeSocketColor', 'MatCol1')
            test_group.inputs.new('NodeSocketColor', 'Red Channel')
            test_group.inputs.new('NodeSocketColor', 'MatCol2')
            test_group.inputs.new('NodeSocketColor', 'Green Channel')
            test_group.inputs.new('NodeSocketColor', 'MatCol3')
            test_group.inputs.new('NodeSocketColor', 'Blue Channel')
            test_group.inputs.new('NodeSocketFloatFactor', 'Scratches?')
            test_group.inputs['Scratches?'].min_value = 0.0
            test_group.inputs['Scratches?'].max_value = 1.0
            test_group.inputs['Scratches?'].hide_value = False
            test_group.inputs.new('NodeSocketFloatFactor', 'Blood?')
            test_group.inputs['Blood?'].min_value = 0.0
            test_group.inputs['Blood?'].max_value = 1.0
            test_group.inputs['Blood?'].hide_value = False
            test_group.inputs.new('NodeSocketFloatFactor', 'Use Blue Channel?')
            test_group.inputs['Use Blue Channel?'].min_value = 0.0
            test_group.inputs['Use Blue Channel?'].max_value = 1.0
            test_group.inputs['Use Blue Channel?'].hide_value = False

            test_group.outputs.new('NodeSocketShader', 'Shader')
            test_group.outputs.new('NodeSocketFloat', 'Value')

            inner_node_0.location = (-220.0, -220.0)
            inner_node_1.location = (-220.0, -60.0)
            inner_node_2.location = (-220.0, 100.0)
            inner_node_3.location = (-220.0, 260.0)
            inner_node_4.location = (820.0, 240.0)
            inner_node_5.location = (480.0, 240.0)
            inner_node_6.location = (-700.0, 20.0)
            inner_node_7.location = (-960.0, 1580.0)
            inner_node_8.location = (-500.0, 1440.0)
            inner_node_9.location = (-680.0, 1000.0)
            inner_node_10.location = (-680.0, 1320.0)
            inner_node_11.location = (-960.0, 1420.0)
            inner_node_12.location = (-960.0, 1500.0)
            inner_node_13.location = (-680.0, 1160.0)
            inner_node_14.location = (-960.0, 1660.0)
            inner_node_15.location = (160.0, 240.0)
            inner_node_16.location = (-1460.0, 920.0)
            inner_node_17.location = (1160.0, 1820.0)
            inner_node_18.location = (600.0, 1200.0)
            inner_node_19.location = (1460.0, 1820.0)
            inner_node_20.location = (1780.0, 1820.0)
            inner_node_21.location = (-1160.0, 540.0)
            inner_node_22.location = (-1160.0, 680.0)
            inner_node_23.location = (-1160.0, 400.0)
            inner_node_24.location = (240.0, 2000.0)
            inner_node_25.location = (240.0, 2140.0)
            inner_node_26.location = (-120.0, 1980.0)
            inner_node_27.location = (240.0, 1860.0)
            inner_node_28.location = (1020.0, 1480.0)
            inner_node_29.location = (1200.0, 1480.0)
            inner_node_30.location = (1020.0, 1280.0)
            inner_node_31.location = (1020.0, 1080.0)
            inner_node_32.location = (1400.0, 1540.0)
            inner_node_33.location = (1580.0, 1540.0)
            inner_node_34.location = (1400.0, 1340.0)
            inner_node_35.location = (1400.0, 1140.0)
            inner_node_36.location = (2360.0, 1120.0)
            inner_node_37.location = (-300.0, 1440.0)
            inner_node_38.location = (-100.0, 1440.0)
            inner_node_39.location = (-280.0, 1000.0)
            inner_node_40.location = (160.0, 1000.0)
            inner_node_41.location = (600.0, 1020.0)
            inner_node_42.location = (600.0, 1420.0)
            inner_node_43.location = (780.0, 1420.0)
            inner_node_44.location = (-60.0, 1000.0)

            test_group.links.new(inner_node_8.inputs[0], inner_node_14.outputs[0])
            test_group.links.new(inner_node_10.inputs[0], inner_node_7.outputs[0])
            test_group.links.new(inner_node_8.inputs[1], inner_node_10.outputs[0])
            test_group.links.new(inner_node_3.inputs[19], inner_node_6.outputs[1])
            test_group.links.new(inner_node_3.inputs[0], inner_node_6.outputs[0])
            test_group.links.new(inner_node_2.inputs[0], inner_node_6.outputs[2])
            test_group.links.new(inner_node_15.inputs[2], inner_node_2.outputs[0])
            test_group.links.new(inner_node_5.inputs[1], inner_node_15.outputs[0])
            test_group.links.new(inner_node_1.inputs[0], inner_node_6.outputs[4])
            test_group.links.new(inner_node_1.inputs[19], inner_node_6.outputs[5])
            test_group.links.new(inner_node_0.inputs[0], inner_node_6.outputs[6])
            test_group.links.new(inner_node_0.inputs[19], inner_node_6.outputs[7])
            test_group.links.new(inner_node_4.inputs[1], inner_node_5.outputs[0])
            test_group.links.new(inner_node_5.inputs[2], inner_node_1.outputs[0])
            test_group.links.new(inner_node_4.inputs[2], inner_node_0.outputs[0])
            test_group.links.new(inner_node_13.inputs[0], inner_node_12.outputs[0])
            test_group.links.new(inner_node_9.inputs[0], inner_node_11.outputs[0])
            test_group.links.new(inner_node_2.inputs[19], inner_node_6.outputs[3])
            test_group.links.new(inner_node_37.inputs[1], inner_node_13.outputs[0])
            test_group.links.new(inner_node_37.inputs[0], inner_node_8.outputs[0])
            test_group.links.new(inner_node_38.inputs[1], inner_node_9.outputs[0])
            test_group.links.new(inner_node_38.inputs[0], inner_node_37.outputs[0])
            test_group.links.new(inner_node_5.inputs[0], inner_node_44.outputs[0])
            test_group.links.new(inner_node_40.inputs[0], inner_node_38.outputs[0])
            test_group.links.new(inner_node_4.inputs[0], inner_node_40.outputs[0])
            test_group.links.new(inner_node_14.inputs[1], inner_node_16.outputs[1])
            test_group.links.new(inner_node_7.inputs[1], inner_node_16.outputs[3])
            test_group.links.new(inner_node_12.inputs[1], inner_node_16.outputs[5])
            test_group.links.new(inner_node_11.inputs[1], inner_node_16.outputs[7])
            test_group.links.new(inner_node_15.inputs[1], inner_node_3.outputs[0])
            test_group.links.new(inner_node_39.inputs[0], inner_node_8.outputs[0])
            test_group.links.new(inner_node_15.inputs[0], inner_node_39.outputs[0])
            test_group.links.new(inner_node_44.inputs[0], inner_node_37.outputs[0])
            test_group.links.new(inner_node_36.inputs[0], inner_node_4.outputs[0])
            test_group.links.new(inner_node_36.inputs[1], inner_node_20.outputs[0])
            test_group.links.new(inner_node_20.inputs[0], inner_node_19.outputs[0])
            test_group.links.new(inner_node_17.inputs[0], inner_node_14.outputs[0])
            test_group.links.new(inner_node_19.inputs[0], inner_node_17.outputs[0])
            test_group.links.new(inner_node_41.inputs[0], inner_node_15.outputs[0])
            test_group.links.new(inner_node_31.inputs[0], inner_node_5.outputs[0])
            test_group.links.new(inner_node_35.inputs[0], inner_node_4.outputs[0])
            test_group.links.new(inner_node_34.inputs[1], inner_node_35.outputs[1])
            test_group.links.new(inner_node_43.inputs[0], inner_node_42.outputs[0])
            test_group.links.new(inner_node_42.inputs[1], inner_node_39.outputs[0])
            test_group.links.new(inner_node_42.inputs[2], inner_node_18.outputs[0])
            test_group.links.new(inner_node_17.inputs[1], inner_node_43.outputs[0])
            test_group.links.new(inner_node_29.inputs[0], inner_node_28.outputs[0])
            test_group.links.new(inner_node_28.inputs[1], inner_node_44.outputs[0])
            test_group.links.new(inner_node_28.inputs[2], inner_node_30.outputs[0])
            test_group.links.new(inner_node_19.inputs[1], inner_node_29.outputs[0])
            test_group.links.new(inner_node_33.inputs[0], inner_node_32.outputs[0])
            test_group.links.new(inner_node_32.inputs[2], inner_node_34.outputs[0])
            test_group.links.new(inner_node_32.inputs[1], inner_node_40.outputs[0])
            test_group.links.new(inner_node_20.inputs[1], inner_node_33.outputs[0])
            test_group.links.new(inner_node_22.inputs[0], inner_node_16.outputs[8])
            test_group.links.new(inner_node_21.inputs[0], inner_node_16.outputs[9])
            test_group.links.new(inner_node_23.inputs[0], inner_node_16.outputs[10])
            test_group.links.new(inner_node_10.inputs[1], inner_node_22.outputs[0])
            test_group.links.new(inner_node_13.inputs[1], inner_node_21.outputs[0])
            test_group.links.new(inner_node_9.inputs[1], inner_node_23.outputs[0])
            test_group.links.new(inner_node_39.inputs[1], inner_node_22.outputs[0])
            test_group.links.new(inner_node_44.inputs[1], inner_node_21.outputs[0])
            test_group.links.new(inner_node_40.inputs[1], inner_node_23.outputs[0])
            test_group.links.new(inner_node_25.inputs[0], inner_node_26.outputs[8])
            test_group.links.new(inner_node_24.inputs[0], inner_node_26.outputs[9])
            test_group.links.new(inner_node_27.inputs[0], inner_node_26.outputs[10])
            test_group.links.new(inner_node_42.inputs[0], inner_node_25.outputs[0])
            test_group.links.new(inner_node_28.inputs[0], inner_node_24.outputs[0])
            test_group.links.new(inner_node_32.inputs[0], inner_node_27.outputs[0])
            test_group.links.new(inner_node_30.inputs[1], inner_node_31.outputs[1])
            test_group.links.new(inner_node_18.inputs[1], inner_node_41.outputs[1])

            inner_node_0.inputs[0].default_value = (0.0012069722870364785, 0.0, 0.8000000715255737, 1.0)
            inner_node_0.inputs[1].default_value = 0.0
            inner_node_0.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            inner_node_0.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_0.inputs[4].default_value = 0.0
            inner_node_0.inputs[5].default_value = 0.0
            inner_node_0.inputs[6].default_value = 0.0
            inner_node_0.inputs[7].default_value = 1.0
            inner_node_0.inputs[8].default_value = 0.0
            inner_node_0.inputs[9].default_value = 0.0
            inner_node_0.inputs[10].default_value = 0.0
            inner_node_0.inputs[11].default_value = 0.5
            inner_node_0.inputs[12].default_value = 0.0
            inner_node_0.inputs[13].default_value = 0.029999999329447746
            inner_node_0.inputs[14].default_value = 1.4500000476837158
            inner_node_0.inputs[15].default_value = 0.0
            inner_node_0.inputs[16].default_value = 0.0
            inner_node_0.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_0.inputs[18].default_value = 1.0
            inner_node_0.inputs[19].default_value = 1.0
            inner_node_0.inputs[20].default_value = (0.0, 0.0, 0.0)
            inner_node_0.inputs[21].default_value = (0.0, 0.0, 0.0)
            inner_node_0.inputs[22].default_value = (0.0, 0.0, 0.0)

            inner_node_1.inputs[0].default_value = (0.0012069722870364785, 0.0, 0.8000000715255737, 1.0)
            inner_node_1.inputs[1].default_value = 0.0
            inner_node_1.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            inner_node_1.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_1.inputs[4].default_value = 0.0
            inner_node_1.inputs[5].default_value = 0.0
            inner_node_1.inputs[6].default_value = 0.0
            inner_node_1.inputs[7].default_value = 1.0
            inner_node_1.inputs[8].default_value = 0.0
            inner_node_1.inputs[9].default_value = 0.0
            inner_node_1.inputs[10].default_value = 0.0
            inner_node_1.inputs[11].default_value = 0.5
            inner_node_1.inputs[12].default_value = 0.0
            inner_node_1.inputs[13].default_value = 0.029999999329447746
            inner_node_1.inputs[14].default_value = 1.4500000476837158
            inner_node_1.inputs[15].default_value = 0.0
            inner_node_1.inputs[16].default_value = 0.0
            inner_node_1.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_1.inputs[18].default_value = 1.0
            inner_node_1.inputs[19].default_value = 1.0
            inner_node_1.inputs[20].default_value = (0.0, 0.0, 0.0)
            inner_node_1.inputs[21].default_value = (0.0, 0.0, 0.0)
            inner_node_1.inputs[22].default_value = (0.0, 0.0, 0.0)

            inner_node_2.inputs[0].default_value = (0.0012069722870364785, 0.0, 0.8000000715255737, 1.0)
            inner_node_2.inputs[1].default_value = 0.0
            inner_node_2.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            inner_node_2.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_2.inputs[4].default_value = 0.0
            inner_node_2.inputs[5].default_value = 0.0
            inner_node_2.inputs[6].default_value = 0.0
            inner_node_2.inputs[7].default_value = 1.0
            inner_node_2.inputs[8].default_value = 0.0
            inner_node_2.inputs[9].default_value = 0.0
            inner_node_2.inputs[10].default_value = 0.0
            inner_node_2.inputs[11].default_value = 0.5
            inner_node_2.inputs[12].default_value = 0.0
            inner_node_2.inputs[13].default_value = 0.029999999329447746
            inner_node_2.inputs[14].default_value = 1.4500000476837158
            inner_node_2.inputs[15].default_value = 0.0
            inner_node_2.inputs[16].default_value = 0.0
            inner_node_2.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_2.inputs[18].default_value = 1.0
            inner_node_2.inputs[19].default_value = 1.0
            inner_node_2.inputs[20].default_value = (0.0, 0.0, 0.0)
            inner_node_2.inputs[21].default_value = (0.0, 0.0, 0.0)
            inner_node_2.inputs[22].default_value = (0.0, 0.0, 0.0)

            inner_node_3.inputs[0].default_value = (0.0012069722870364785, 0.0, 0.8000000715255737, 1.0)
            inner_node_3.inputs[1].default_value = 0.0
            inner_node_3.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            inner_node_3.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_3.inputs[4].default_value = 0.0
            inner_node_3.inputs[5].default_value = 0.0
            inner_node_3.inputs[6].default_value = 0.0
            inner_node_3.inputs[7].default_value = 1.0
            inner_node_3.inputs[8].default_value = 0.0
            inner_node_3.inputs[9].default_value = 0.0
            inner_node_3.inputs[10].default_value = 0.0
            inner_node_3.inputs[11].default_value = 0.5
            inner_node_3.inputs[12].default_value = 0.0
            inner_node_3.inputs[13].default_value = 0.029999999329447746
            inner_node_3.inputs[14].default_value = 1.4500000476837158
            inner_node_3.inputs[15].default_value = 0.0
            inner_node_3.inputs[16].default_value = 0.0
            inner_node_3.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_3.inputs[18].default_value = 1.0
            inner_node_3.inputs[19].default_value = 1.0
            inner_node_3.inputs[20].default_value = (0.0, 0.0, 0.0)
            inner_node_3.inputs[21].default_value = (0.0, 0.0, 0.0)
            inner_node_3.inputs[22].default_value = (0.0, 0.0, 0.0)

            inner_node_4.inputs[0].default_value = 0.0

            inner_node_5.inputs[0].default_value = 1.0

            inner_node_7.inputs[0].default_value = 1.0
            inner_node_7.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_7.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_8.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[1].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[3].default_value = 1.0
            inner_node_8.outputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_8.outputs[1].default_value = 0.0

            inner_node_9.inputs[0].default_value = 0.5
            inner_node_9.inputs[1].default_value = 0.5
            inner_node_9.inputs[2].default_value = 0.0
            inner_node_9.outputs[0].default_value = 0.0

            inner_node_10.inputs[0].default_value = 0.5
            inner_node_10.inputs[1].default_value = 0.5
            inner_node_10.inputs[2].default_value = 0.0
            inner_node_10.outputs[0].default_value = 0.0

            inner_node_11.inputs[0].default_value = 1.0
            inner_node_11.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_11.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_12.inputs[0].default_value = 1.0
            inner_node_12.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_12.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_13.inputs[0].default_value = 0.5
            inner_node_13.inputs[1].default_value = 0.5
            inner_node_13.inputs[2].default_value = 0.0
            inner_node_13.outputs[0].default_value = 0.0

            inner_node_14.inputs[0].default_value = 1.0
            inner_node_14.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_14.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_15.inputs[0].default_value = 0.0

            inner_node_17.inputs[0].default_value = 0.5
            inner_node_17.inputs[1].default_value = 0.5
            inner_node_17.inputs[2].default_value = 0.0
            inner_node_17.outputs[0].default_value = 0.0

            inner_node_18.inputs[0].default_value = 0.0
            inner_node_18.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_18.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_19.inputs[0].default_value = 0.5
            inner_node_19.inputs[1].default_value = 0.5
            inner_node_19.inputs[2].default_value = 0.0
            inner_node_19.outputs[0].default_value = 0.0

            inner_node_20.inputs[0].default_value = 0.5
            inner_node_20.inputs[1].default_value = 0.5
            inner_node_20.inputs[2].default_value = 0.0
            inner_node_20.outputs[0].default_value = 0.0

            inner_node_21.inputs[0].default_value = 0.5
            inner_node_21.inputs[1].default_value = 0.5
            inner_node_21.inputs[2].default_value = 0.0
            inner_node_21.outputs[0].default_value = 0.0

            inner_node_22.inputs[0].default_value = 0.5
            inner_node_22.inputs[1].default_value = 0.5
            inner_node_22.inputs[2].default_value = 0.0
            inner_node_22.outputs[0].default_value = 0.0

            inner_node_23.inputs[0].default_value = 0.5
            inner_node_23.inputs[1].default_value = 0.5
            inner_node_23.inputs[2].default_value = 0.0
            inner_node_23.outputs[0].default_value = 0.0

            inner_node_24.inputs[0].default_value = 0.5
            inner_node_24.inputs[1].default_value = 0.5
            inner_node_24.inputs[2].default_value = 0.0
            inner_node_24.outputs[0].default_value = 0.0

            inner_node_25.inputs[0].default_value = 0.5
            inner_node_25.inputs[1].default_value = 0.5
            inner_node_25.inputs[2].default_value = 0.0
            inner_node_25.outputs[0].default_value = 0.0

            inner_node_27.inputs[0].default_value = 0.5
            inner_node_27.inputs[1].default_value = 0.5
            inner_node_27.inputs[2].default_value = 0.0
            inner_node_27.outputs[0].default_value = 0.0

            inner_node_28.inputs[0].default_value = 0.0

            inner_node_29.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_29.outputs[1].default_value = 0.0

            inner_node_30.inputs[0].default_value = 0.0
            inner_node_30.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_30.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_31.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_31.outputs[1].default_value = 0.0

            inner_node_32.inputs[0].default_value = 0.0

            inner_node_33.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_33.outputs[1].default_value = 0.0

            inner_node_34.inputs[0].default_value = 0.0
            inner_node_34.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            inner_node_34.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_35.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_35.outputs[1].default_value = 0.0

            inner_node_37.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_37.inputs[1].default_value = (0.0, 0.0, 0.0)
            inner_node_37.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_37.inputs[3].default_value = 1.0
            inner_node_37.outputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_37.outputs[1].default_value = 0.0

            inner_node_38.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_38.inputs[1].default_value = (0.0, 0.0, 0.0)
            inner_node_38.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_38.inputs[3].default_value = 1.0
            inner_node_38.outputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_38.outputs[1].default_value = 0.0

            inner_node_39.inputs[0].default_value = 0.5
            inner_node_39.inputs[1].default_value = 0.5
            inner_node_39.inputs[2].default_value = 0.0
            inner_node_39.outputs[0].default_value = 0.0

            inner_node_40.inputs[0].default_value = 0.5
            inner_node_40.inputs[1].default_value = 0.5
            inner_node_40.inputs[2].default_value = 0.0
            inner_node_40.outputs[0].default_value = 0.0

            inner_node_41.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_41.outputs[1].default_value = 0.0

            inner_node_42.inputs[0].default_value = 0.0

            inner_node_43.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_43.outputs[1].default_value = 0.0

            inner_node_44.inputs[0].default_value = 0.5
            inner_node_44.inputs[1].default_value = 0.5
            inner_node_44.inputs[2].default_value = 0.0
            inner_node_44.outputs[0].default_value = 0.0

            inner_node_0.location = (-220.0, -220.0)
            inner_node_0.width = 240.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Principled BSDF.007'
            inner_node_1.location = (-220.0, -60.0)
            inner_node_1.width = 240.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Principled BSDF.008'
            inner_node_2.location = (-220.0, 100.0)
            inner_node_2.width = 240.0
            inner_node_2.width_hidden = 42.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Principled BSDF.006'
            inner_node_3.location = (-220.0, 260.0)
            inner_node_3.width = 240.0
            inner_node_3.width_hidden = 42.0
            inner_node_3.height = 100.0
            inner_node_3.name = 'Principled BSDF.005'
            inner_node_4.location = (820.0, 240.0)
            inner_node_4.width = 140.0
            inner_node_4.width_hidden = 42.0
            inner_node_4.height = 100.0
            inner_node_4.name = 'Mix Shader.002'
            inner_node_5.location = (480.0, 240.0)
            inner_node_5.width = 140.0
            inner_node_5.width_hidden = 42.0
            inner_node_5.height = 100.0
            inner_node_5.name = 'Mix Shader.001'
            inner_node_6.location = (-700.0, 20.0)
            inner_node_6.width = 140.0
            inner_node_6.width_hidden = 42.0
            inner_node_6.height = 100.0
            inner_node_6.name = 'Group Input'
            inner_node_7.location = (-960.0, 1580.0)
            inner_node_7.width = 140.0
            inner_node_7.width_hidden = 42.0
            inner_node_7.height = 100.0
            inner_node_7.name = 'Invert.004'
            inner_node_8.location = (-500.0, 1440.0)
            inner_node_8.width = 140.0
            inner_node_8.width_hidden = 42.0
            inner_node_8.height = 100.0
            inner_node_8.name = 'Vector Math'
            inner_node_9.location = (-680.0, 1000.0)
            inner_node_9.width = 140.0
            inner_node_9.width_hidden = 42.0
            inner_node_9.height = 100.0
            inner_node_9.name = 'Math.002'
            inner_node_9.operation = 'MULTIPLY'
            inner_node_9.use_clamp = True
            inner_node_10.location = (-680.0, 1320.0)
            inner_node_10.width = 140.0
            inner_node_10.width_hidden = 42.0
            inner_node_10.height = 100.0
            inner_node_10.name = 'Math'
            inner_node_10.operation = 'MULTIPLY'
            inner_node_10.use_clamp = True
            inner_node_11.location = (-960.0, 1420.0)
            inner_node_11.width = 140.0
            inner_node_11.width_hidden = 42.0
            inner_node_11.height = 100.0
            inner_node_11.name = 'Invert.006'
            inner_node_12.location = (-960.0, 1500.0)
            inner_node_12.width = 140.0
            inner_node_12.width_hidden = 42.0
            inner_node_12.height = 100.0
            inner_node_12.name = 'Invert.005'
            inner_node_13.location = (-680.0, 1160.0)
            inner_node_13.width = 140.0
            inner_node_13.width_hidden = 42.0
            inner_node_13.height = 100.0
            inner_node_13.name = 'Math.001'
            inner_node_13.operation = 'MULTIPLY'
            inner_node_13.use_clamp = True
            inner_node_14.location = (-960.0, 1660.0)
            inner_node_14.width = 140.0
            inner_node_14.width_hidden = 42.0
            inner_node_14.height = 100.0
            inner_node_14.name = 'Invert.003'
            inner_node_15.location = (160.0, 240.0)
            inner_node_15.width = 140.0
            inner_node_15.width_hidden = 42.0
            inner_node_15.height = 100.0
            inner_node_15.name = 'Mix Shader'
            inner_node_16.location = (-1460.0, 920.0)
            inner_node_16.width = 140.0
            inner_node_16.width_hidden = 42.0
            inner_node_16.height = 100.0
            inner_node_16.name = 'Group Input.001'
            inner_node_17.location = (1160.0, 1820.0)
            inner_node_17.width = 140.0
            inner_node_17.width_hidden = 42.0
            inner_node_17.height = 100.0
            inner_node_17.name = 'Math.008'
            inner_node_18.location = (600.0, 1200.0)
            inner_node_18.width = 140.0
            inner_node_18.width_hidden = 42.0
            inner_node_18.height = 100.0
            inner_node_18.name = 'Invert'
            inner_node_19.location = (1460.0, 1820.0)
            inner_node_19.width = 140.0
            inner_node_19.width_hidden = 42.0
            inner_node_19.height = 100.0
            inner_node_19.name = 'Math.006'
            inner_node_20.location = (1780.0, 1820.0)
            inner_node_20.width = 140.0
            inner_node_20.width_hidden = 42.0
            inner_node_20.height = 100.0
            inner_node_20.name = 'Math.007'
            inner_node_21.location = (-1160.0, 540.0)
            inner_node_21.width = 140.0
            inner_node_21.width_hidden = 42.0
            inner_node_21.height = 100.0
            inner_node_21.name = 'Math.010'
            inner_node_21.operation = 'CEIL'
            inner_node_22.location = (-1160.0, 680.0)
            inner_node_22.width = 140.0
            inner_node_22.width_hidden = 42.0
            inner_node_22.height = 100.0
            inner_node_22.name = 'Math.009'
            inner_node_22.operation = 'CEIL'
            inner_node_23.location = (-1160.0, 400.0)
            inner_node_23.width = 140.0
            inner_node_23.width_hidden = 42.0
            inner_node_23.height = 100.0
            inner_node_23.name = 'Math.011'
            inner_node_23.operation = 'CEIL'
            inner_node_24.location = (240.0, 2000.0)
            inner_node_24.width = 140.0
            inner_node_24.width_hidden = 42.0
            inner_node_24.height = 100.0
            inner_node_24.name = 'Math.012'
            inner_node_24.operation = 'CEIL'
            inner_node_25.location = (240.0, 2140.0)
            inner_node_25.width = 140.0
            inner_node_25.width_hidden = 42.0
            inner_node_25.height = 100.0
            inner_node_25.name = 'Math.013'
            inner_node_25.operation = 'CEIL'
            inner_node_26.location = (-120.0, 1980.0)
            inner_node_26.width = 140.0
            inner_node_26.width_hidden = 42.0
            inner_node_26.height = 100.0
            inner_node_26.name = 'Group Input.002'
            inner_node_27.location = (240.0, 1860.0)
            inner_node_27.width = 140.0
            inner_node_27.width_hidden = 42.0
            inner_node_27.height = 100.0
            inner_node_27.name = 'Math.014'
            inner_node_27.operation = 'CEIL'
            inner_node_28.location = (1020.0, 1480.0)
            inner_node_28.width = 140.0
            inner_node_28.width_hidden = 42.0
            inner_node_28.height = 100.0
            inner_node_28.name = 'Mix Shader.004'
            inner_node_29.location = (1200.0, 1480.0)
            inner_node_29.width = 140.0
            inner_node_29.width_hidden = 42.0
            inner_node_29.height = 100.0
            inner_node_29.name = 'Shader to RGB.004'
            inner_node_30.location = (1020.0, 1280.0)
            inner_node_30.width = 140.0
            inner_node_30.width_hidden = 42.0
            inner_node_30.height = 100.0
            inner_node_30.name = 'Invert.001'
            inner_node_31.location = (1020.0, 1080.0)
            inner_node_31.width = 140.0
            inner_node_31.width_hidden = 42.0
            inner_node_31.height = 100.0
            inner_node_31.name = 'Shader to RGB.001'
            inner_node_32.location = (1400.0, 1540.0)
            inner_node_32.width = 140.0
            inner_node_32.width_hidden = 42.0
            inner_node_32.height = 100.0
            inner_node_32.name = 'Mix Shader.005'
            inner_node_33.location = (1580.0, 1540.0)
            inner_node_33.width = 140.0
            inner_node_33.width_hidden = 42.0
            inner_node_33.height = 100.0
            inner_node_33.name = 'Shader to RGB.005'
            inner_node_34.location = (1400.0, 1340.0)
            inner_node_34.width = 140.0
            inner_node_34.width_hidden = 42.0
            inner_node_34.height = 100.0
            inner_node_34.name = 'Invert.002'
            inner_node_35.location = (1400.0, 1140.0)
            inner_node_35.width = 140.0
            inner_node_35.width_hidden = 42.0
            inner_node_35.height = 100.0
            inner_node_35.name = 'Shader to RGB.002'
            inner_node_36.location = (2360.0, 1120.0)
            inner_node_36.width = 140.0
            inner_node_36.width_hidden = 42.0
            inner_node_36.height = 100.0
            inner_node_36.name = 'Group Output'
            inner_node_36.is_active_output = True
            inner_node_37.location = (-300.0, 1440.0)
            inner_node_37.width = 140.0
            inner_node_37.width_hidden = 42.0
            inner_node_37.height = 100.0
            inner_node_37.name = 'Vector Math.001'
            inner_node_38.location = (-100.0, 1440.0)
            inner_node_38.width = 140.0
            inner_node_38.width_hidden = 42.0
            inner_node_38.height = 100.0
            inner_node_38.name = 'Vector Math.002'
            inner_node_39.location = (-280.0, 1000.0)
            inner_node_39.width = 140.0
            inner_node_39.width_hidden = 42.0
            inner_node_39.height = 100.0
            inner_node_39.name = 'Math.005'
            inner_node_39.operation = 'MULTIPLY'
            inner_node_39.use_clamp = True
            inner_node_40.location = (160.0, 1000.0)
            inner_node_40.width = 140.0
            inner_node_40.width_hidden = 42.0
            inner_node_40.height = 100.0
            inner_node_40.name = 'Math.004'
            inner_node_40.operation = 'MULTIPLY'
            inner_node_40.use_clamp = True
            inner_node_41.location = (600.0, 1020.0)
            inner_node_41.width = 140.0
            inner_node_41.width_hidden = 42.0
            inner_node_41.height = 100.0
            inner_node_41.name = 'Shader to RGB'
            inner_node_42.location = (600.0, 1420.0)
            inner_node_42.width = 140.0
            inner_node_42.width_hidden = 42.0
            inner_node_42.height = 100.0
            inner_node_42.name = 'Mix Shader.003'
            inner_node_43.location = (780.0, 1420.0)
            inner_node_43.width = 140.0
            inner_node_43.width_hidden = 42.0
            inner_node_43.height = 100.0
            inner_node_43.name = 'Shader to RGB.003'
            inner_node_44.location = (-60.0, 1000.0)
            inner_node_44.width = 140.0
            inner_node_44.width_hidden = 42.0
            inner_node_44.height = 100.0
            inner_node_44.name = 'Math.003'
            inner_node_44.operation = 'MULTIPLY'
            inner_node_44.use_clamp = True
        else:
            test_group = bpy.data.node_groups['Combine_MatCol']

        

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'Combine MatCol'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 168.57308959960938

        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class Xenoverse_Shader_Out:
    def __init__(self, tree):
        if 'Xenoverse_Shader_Out' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('Xenoverse_Shader_Out', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupOutput')
            inner_node_1 = test_group.nodes.new('NodeGroupInput')
            inner_node_2 = test_group.nodes.new('ShaderNodeMixRGB')
            inner_node_3 = test_group.nodes.new('ShaderNodeEmission')

            test_group.inputs.new('NodeSocketFloatFactor', 'View Color')
            test_group.inputs['View Color'].min_value = 0.0
            test_group.inputs['View Color'].max_value = 1.0
            test_group.inputs['View Color'].hide_value = False
            test_group.inputs.new('NodeSocketColor', 'MatCol')
            test_group.inputs.new('NodeSocketColor', 'DYT')
            test_group.inputs.new('NodeSocketFloat', 'Strength')
            test_group.inputs['Strength'].min_value = 0.0
            test_group.inputs['Strength'].max_value = 1000000.0
            test_group.inputs['Strength'].hide_value = False

            test_group.outputs.new('NodeSocketShader', 'Emission')

            inner_node_0.location = (270.0, -0.0)
            inner_node_1.location = (-280.0, -0.0)
            inner_node_2.location = (-80.0, 20.0)
            inner_node_3.location = (80.0, -20.0)

            test_group.links.new(inner_node_0.inputs[0], inner_node_3.outputs[0])
            test_group.links.new(inner_node_2.inputs[2], inner_node_1.outputs[2])
            test_group.links.new(inner_node_2.inputs[1], inner_node_1.outputs[1])
            test_group.links.new(inner_node_3.inputs[0], inner_node_2.outputs[0])
            test_group.links.new(inner_node_2.inputs[0], inner_node_1.outputs[0])
            test_group.links.new(inner_node_3.inputs[1], inner_node_1.outputs[3])

            inner_node_2.inputs[0].default_value = 1.0
            inner_node_2.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
            inner_node_2.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
            inner_node_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_3.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            inner_node_3.inputs[1].default_value = 10.0

            inner_node_0.location = (270.0, -0.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Output'
            inner_node_0.is_active_output = True
            inner_node_1.location = (-280.0, -0.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Group Input'
            inner_node_2.location = (-80.0, 20.0)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 42.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Mix.006'
            inner_node_2.blend_type = 'OVERLAY'
            inner_node_2.use_clamp = True
            inner_node_3.location = (80.0, -20.0)
            inner_node_3.width = 140.0
            inner_node_3.width_hidden = 42.0
            inner_node_3.height = 100.0
            inner_node_3.name = 'Emission'
        else:
            test_group = bpy.data.node_groups['Xenoverse_Shader_Out']

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'Xenoverse Shader Out'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 178.3459930419922

        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class Lighting:
    def __init__(self, tree):
        if 'Lighting' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('Lighting', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('ShaderNodeMath')
            inner_node_1 = test_group.nodes.new('ShaderNodeMath')
            inner_node_2 = test_group.nodes.new('NodeGroupInput')
            inner_node_3 = test_group.nodes.new('NodeGroupOutput')
            inner_node_4 = test_group.nodes.new('ShaderNodeVertexColor')
            inner_node_5 = test_group.nodes.new('ShaderNodeNormal')
            inner_node_6 = test_group.nodes.new('ShaderNodeSeparateRGB')
            inner_node_7 = test_group.nodes.new('ShaderNodeTexCoord')
            inner_node_8 = test_group.nodes.new('ShaderNodeVectorMath')

            test_group.inputs.new('NodeSocketFloat', 'Light Tweeking')
            test_group.inputs['Light Tweeking'].min_value = -10000.0
            test_group.inputs['Light Tweeking'].max_value = 10000.0
            test_group.inputs['Light Tweeking'].hide_value = False

            test_group.outputs.new('NodeSocketFloat', 'Light Tracking')

            inner_node_0.location = (63.78546142578125, 22.351207733154297)
            inner_node_1.location = (223.7854766845703, 22.351207733154297)
            inner_node_2.location = (-458.1806640625, -7.648792266845703)
            inner_node_3.location = (413.78546142578125, -7.648792266845703)
            inner_node_4.location = (-257.19757080078125, -187.64878845214844)
            inner_node_5.location = (-277.19757080078125, 32.3512077331543)
            inner_node_6.location = (-97.19757080078125, -107.64878845214844)
            inner_node_7.location = (-277.19757080078125, 312.3511962890625)
            inner_node_8.location = (-96.21453857421875, 102.35121154785156)

            test_group.links.new(inner_node_3.inputs[0], inner_node_1.outputs[0])
            test_group.links.new(inner_node_6.inputs[0], inner_node_4.outputs[0])
            test_group.links.new(inner_node_1.inputs[0], inner_node_0.outputs[0])
            test_group.links.new(inner_node_0.inputs[0], inner_node_8.outputs[1])
            test_group.links.new(inner_node_8.inputs[0], inner_node_7.outputs[1])
            test_group.links.new(inner_node_0.inputs[1], inner_node_6.outputs[0])
            test_group.links.new(inner_node_8.inputs[1], inner_node_5.outputs[0])
            test_group.links.new(inner_node_1.inputs[1], inner_node_2.outputs[0])

            inner_node_0.inputs[0].default_value = 0.0
            inner_node_0.inputs[1].default_value = 0.5
            inner_node_0.inputs[2].default_value = 0.0
            inner_node_0.outputs[0].default_value = 0.0

            inner_node_1.inputs[0].default_value = 0.0
            inner_node_1.inputs[1].default_value = 2.0
            inner_node_1.inputs[2].default_value = 0.0
            inner_node_1.outputs[0].default_value = 0.0

            inner_node_4.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            inner_node_4.outputs[1].default_value = 0.0

            inner_node_5.inputs[0].default_value = (0.0, 0.0, 1.0)
            inner_node_5.outputs[0].default_value = (0.687000036239624, -0.02800000086426735, -0.7260000109672546)
            inner_node_5.outputs[1].default_value = 0.0

            inner_node_6.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            inner_node_6.outputs[0].default_value = 0.0
            inner_node_6.outputs[1].default_value = 0.0
            inner_node_6.outputs[2].default_value = 0.0

            inner_node_7.outputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_7.outputs[1].default_value = (0.0, 0.0, 0.0)
            inner_node_7.outputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_7.outputs[3].default_value = (0.0, 0.0, 0.0)
            inner_node_7.outputs[4].default_value = (0.0, 0.0, 0.0)
            inner_node_7.outputs[5].default_value = (0.0, 0.0, 0.0)
            inner_node_7.outputs[6].default_value = (0.0, 0.0, 0.0)

            inner_node_8.inputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[1].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[2].default_value = (0.0, 0.0, 0.0)
            inner_node_8.inputs[3].default_value = 1.0
            inner_node_8.outputs[0].default_value = (0.0, 0.0, 0.0)
            inner_node_8.outputs[1].default_value = 0.0

            inner_node_0.location = (63.78546142578125, 22.351207733154297)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 100.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Math'
            inner_node_1.location = (223.7854766845703, 22.351207733154297)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 100.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Math.001'
            inner_node_1.operation = 'DIVIDE'
            inner_node_2.location = (-458.1806640625, -7.648792266845703)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 80.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Group Input'
            inner_node_3.location = (413.78546142578125, -7.648792266845703)
            inner_node_3.width = 140.0
            inner_node_3.width_hidden = 80.0
            inner_node_3.height = 100.0
            inner_node_3.name = 'Group Output'
            inner_node_3.is_active_output = True
            inner_node_4.location = (-257.19757080078125, -187.64878845214844)
            inner_node_4.width = 140.0
            inner_node_4.width_hidden = 100.0
            inner_node_4.height = 100.0
            inner_node_4.name = 'Vertex Color'
            inner_node_4.layer_name = 'Col'
            inner_node_5.location = (-277.19757080078125, 32.3512077331543)
            inner_node_5.width = 140.0
            inner_node_5.width_hidden = 100.0
            inner_node_5.height = 100.0
            inner_node_5.name = 'Normal'
            inner_node_6.location = (-97.19757080078125, -107.64878845214844)
            inner_node_6.width = 140.0
            inner_node_6.width_hidden = 100.0
            inner_node_6.height = 100.0
            inner_node_6.name = 'Separate RGB'
            inner_node_7.location = (-277.19757080078125, 312.3511962890625)
            inner_node_7.width = 140.0
            inner_node_7.width_hidden = 100.0
            inner_node_7.height = 100.0
            inner_node_7.name = 'Texture Coordinate'
            inner_node_8.location = (-96.21453857421875, 102.35121154785156)
            inner_node_8.width = 140.0
            inner_node_8.width_hidden = 100.0
            inner_node_8.height = 100.0
            inner_node_8.name = 'Vector Math'
            inner_node_8.operation = 'DOT_PRODUCT'
        else:
            test_group = bpy.data.node_groups['Lighting']

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'Lighting'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 182.883544921875

        node.inputs[0].default_value = 2.0

        node.location = (-1080.0, 180.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class Merge_DYT:
    def __init__(self, tree):
        if 'Merge_DYT' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('Merge_DYT', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupOutput')
            inner_node_1 = test_group.nodes.new('ShaderNodeMixRGB')
            inner_node_2 = test_group.nodes.new('ShaderNodeMixRGB')
            inner_node_3 = test_group.nodes.new('ShaderNodeRGBToBW')
            inner_node_4 = test_group.nodes.new('ShaderNodeRGBToBW')
            inner_node_5 = test_group.nodes.new('NodeGroupInput')

            test_group.inputs.new('NodeSocketColor', 'Color')
            test_group.inputs.new('NodeSocketColor', 'Rim')
            test_group.inputs.new('NodeSocketColor', 'Shine')
            test_group.inputs.new('NodeSocketFloatFactor', 'Show Rim')
            test_group.inputs[3].min_value = 0.0
            test_group.inputs[3].max_value = 1.0
            test_group.inputs[3].hide_value = False
            test_group.inputs.new('NodeSocketFloatFactor', 'Show Shine')
            test_group.inputs[4].min_value = 0.0
            test_group.inputs[4].max_value = 1.0
            test_group.inputs[4].hide_value = False

            test_group.outputs.new('NodeSocketColor', 'DYT')

            inner_node_0.location = (600.0, 60.0)
            inner_node_1.location = (400.0, 40.0)
            inner_node_2.location = (180.0, 160.0)
            inner_node_3.location = (-20.0, -220.0)
            inner_node_4.location = (-20.0, -140.0)
            inner_node_5.location = (-280.0, -0.0)

            test_group.links.new(inner_node_2.inputs[1], inner_node_5.outputs[0])
            test_group.links.new(inner_node_3.inputs[0], inner_node_5.outputs[2])
            test_group.links.new(inner_node_4.inputs[0], inner_node_5.outputs[1])
            test_group.links.new(inner_node_1.inputs[1], inner_node_2.outputs[0])
            test_group.links.new(inner_node_0.inputs[0], inner_node_1.outputs[0])
            test_group.links.new(inner_node_2.inputs[2], inner_node_4.outputs[0])
            test_group.links.new(inner_node_1.inputs[2], inner_node_3.outputs[0])
            test_group.links.new(inner_node_1.inputs[0], inner_node_5.outputs[4])
            test_group.links.new(inner_node_2.inputs[0], inner_node_5.outputs[3])

            inner_node_1.inputs[0].default_value = 1.0
            inner_node_1.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
            inner_node_1.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
            inner_node_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_2.inputs[0].default_value = 1.0
            inner_node_2.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
            inner_node_2.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
            inner_node_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_3.inputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
            inner_node_3.outputs[0].default_value = 0.0

            inner_node_4.inputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
            inner_node_4.outputs[0].default_value = 0.0

            inner_node_0.location = (600.0, 60.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 80.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Output'
            inner_node_0.is_active_output = True
            inner_node_1.location = (400.0, 40.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 100.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Mix.001'
            inner_node_1.blend_type = 'ADD'
            inner_node_2.location = (180.0, 160.0)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 100.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Mix'
            inner_node_2.blend_type = 'ADD'
            inner_node_3.location = (-20.0, -220.0)
            inner_node_3.width = 140.0
            inner_node_3.width_hidden = 100.0
            inner_node_3.height = 100.0
            inner_node_3.name = 'RGB to BW'
            inner_node_4.location = (-20.0, -140.0)
            inner_node_4.width = 140.0
            inner_node_4.width_hidden = 100.0
            inner_node_4.height = 100.0
            inner_node_4.name = 'RGB to BW.001'
            inner_node_5.location = (-280.0, -0.0)
            inner_node_5.width = 140.0
            inner_node_5.width_hidden = 80.0
            inner_node_5.height = 100.0
            inner_node_5.name = 'Group Input'
        else:
            test_group = bpy.data.node_groups['Merge_DYT']

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'Merge DYT'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 140.0

        node.inputs[3].default_value = 0.0
        node.inputs[4].default_value = 1.0

        node.location = (-260.0, -20.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass


class Line_Work_Image:
    def __init__(self,tree):

        frame = tree.nodes.new('NodeFrame')
        frame.label = 'Line Work Image'

        image = tree.nodes.new('ShaderNodeTexImage')
        image.name = "LineWork_This"
        image.location = (-120.0, 0.0)
        image.parent = frame

        sepRGB = tree.nodes.new('ShaderNodeSeparateRGB')
        sepRGB.location = (160.0, -60.0)
        sepRGB.parent = frame

        frame.location = (-1200.0, 700.0)
        tree.links.new(sepRGB.inputs[0],image.outputs[0])

        input_list  = [image.inputs[0]]
        output_list = [image.outputs[0],
                       image.outputs[1],
                       sepRGB.outputs[0],
                       sepRGB.outputs[1],
                       sepRGB.outputs[2]]
        self.__node = frame_node(frame,input_list,output_list, {"image":image, "sepRGB":sepRGB})
    def node(self):
        return self.__node
    pass

class DYT_Image:
    def __init__(self,tree):
        frame = tree.nodes.new('NodeFrame')
        frame.label = 'DYT Image'

        image1 = tree.nodes.new('ShaderNodeTexImage')
        image1.name = "DYT_1"
        image1.location = (0.0, 260.0)
        image1.parent = frame

        image2 = tree.nodes.new('ShaderNodeTexImage')
        image2.name = "DYT_2"
        image2.location = (0.0, 0.0)
        image2.parent = frame

        image3 = tree.nodes.new('ShaderNodeTexImage')
        image3.name = "DYT_3"
        image3.location = (0.0, -260.0)
        image3.parent = frame

        frame.location = (-560.0, -20.0)

        input_list = [image1.inputs[0],
                      image2.inputs[0],
                      image3.inputs[0],]
        output_list = [image1.outputs[0],
                       image1.outputs[1],
                       image2.outputs[0],
                       image2.outputs[1],
                       image3.outputs[0],
                       image3.outputs[1],]
        self.__node = frame_node(frame, input_list, output_list, {"image1":image1, "image2":image2, "image3":image3})
    def node(self):
        return self.__node
    pass

class DYT_Ramps:
    def __init__(self,tree):
        frame = tree.nodes.new('NodeFrame')
        frame.label = 'DYT Ramps'

        ramp1 = tree.nodes.new('ShaderNodeValToRGB')
        ramp1.color_ramp.elements.remove(ramp1.color_ramp.elements[-1])
        ramp1.name = "RAMP_1.0"
        ramp1.label = "Main Color Ramp"
        ramp1.location = (0.0, 220.0)
        ramp1.parent = frame

        ramp2 = tree.nodes.new('ShaderNodeValToRGB')
        ramp2.color_ramp.elements.remove(ramp2.color_ramp.elements[-1])
        ramp2.name = "RAMP_2"
        ramp2.label = "Rim Color Ramp"
        ramp2.location = (0.0, 0.0)
        ramp2.parent = frame

        ramp3 = tree.nodes.new('ShaderNodeValToRGB')
        ramp3.color_ramp.elements.remove(ramp3.color_ramp.elements[-1])
        ramp3.name = "RAMP_3"
        ramp3.label = "Shine Color Ramp"
        ramp3.location = (0.0, -220.0)
        ramp3.parent = frame

        ramp4 = tree.nodes.new('ShaderNodeValToRGB')
        ramp4.color_ramp.elements.remove(ramp4.color_ramp.elements[-1])
        ramp4.name = "RAMP_4"
        ramp4.label = "Fourth Color Ramp"
        ramp4.location = (0.0, -440.0)
        ramp4.parent = frame

        frame.location = (0, 0)

        input_list = [ramp1.inputs[0],          # Factor
                      ramp2.inputs[0],          # Factor
                      ramp3.inputs[0],          # Factor
                      ramp4.inputs[0],]         # Factor
        
        output_list = [ramp1.outputs[0],        # Ramp 1 Color
                       ramp1.outputs[1],        # Ramp 1 Alpha
                       
                       ramp2.outputs[0],        # Ramp 2 Color
                       ramp2.outputs[1],        # Ramp 2 Alpha
                       
                       ramp3.outputs[0],        # Ramp 3 Color
                       ramp3.outputs[1],        # Ramp 3 Alpha
                       
                       ramp4.outputs[0],        # Ramp 4 Color
                       ramp4.outputs[1],]       # Ramp 4 Alpha
        self.__node = frame_node(frame, input_list, output_list, {"ramp1":ramp1, "ramp2":ramp2, "ramp3":ramp3, "ramp4":ramp4})
    def node(self):
        return self.__node
    pass

#Finished Parameter Nodes

class Glare:
    def __init__(self, tree):
        test_group = bpy.data.node_groups.new('Glare', 'ShaderNodeTree')

        inner_node_0 = test_group.nodes.new('NodeGroupInput')
        inner_node_1 = test_group.nodes.new('NodeGroupOutput')

        test_group.inputs.new('NodeSocketFloat', 'Glare')
        test_group.inputs[0].min_value = -3.4028234663852886e+38
        test_group.inputs[0].max_value = 3.4028234663852886e+38
        test_group.inputs[0].hide_value = False

        test_group.outputs.new('NodeSocketFloat', 'Glare')

        inner_node_0.location = (-200.0, -0.0)
        inner_node_1.location = (190.0, -0.0)

        test_group.links.new(inner_node_1.inputs[0], inner_node_0.outputs[0])

        inner_node_0.location = (-200.0, -0.0)
        inner_node_0.width = 140.0
        inner_node_0.width_hidden = 42.0
        inner_node_0.height = 100.0
        inner_node_0.name = 'Group Input'
        inner_node_1.location = (190.0, -0.0)
        inner_node_1.width = 140.0
        inner_node_1.width_hidden = 42.0
        inner_node_1.height = 100.0
        inner_node_1.name = 'Group Output'
        inner_node_1.is_active_output = True

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'Glare'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 140.0

        node.inputs[0].default_value = 1.0

        node.location = (list(tree.nodes['Material Output'].location)[0],
                         list(tree.nodes['Material Output'].location)[1]+(20*7))
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MatCol0:
    def __init__(self, tree):
        if 'MatCol0' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatCol0', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupOutput')
            inner_node_1 = test_group.nodes.new('ShaderNodeCombineRGB')
            inner_node_2 = test_group.nodes.new('ShaderNodeBrightContrast')
            inner_node_3 = test_group.nodes.new('NodeGroupInput')

            test_group.inputs.new('NodeSocketColor', 'Image Alpha')
            test_group.inputs.new('NodeSocketFloat', 'R')
            test_group.inputs[1].min_value = -3.4028234663852886e+38
            test_group.inputs[1].max_value = 3.4028234663852886e+38
            test_group.inputs[1].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'G')
            test_group.inputs[2].min_value = -3.4028234663852886e+38
            test_group.inputs[2].max_value = 3.4028234663852886e+38
            test_group.inputs[2].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'B')
            test_group.inputs[3].min_value = -3.4028234663852886e+38
            test_group.inputs[3].max_value = 3.4028234663852886e+38
            test_group.inputs[3].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'A')
            test_group.inputs[4].min_value = -3.4028234663852886e+38
            test_group.inputs[4].max_value = 3.4028234663852886e+38
            test_group.inputs[4].hide_value = False

            test_group.outputs.new('NodeSocketColor', 'MatCol0')
            test_group.outputs.new('NodeSocketColor', 'Lines')

            inner_node_0.location = (400.0, 0.0)
            inner_node_1.location = (0.0, 80.0)
            inner_node_2.location = (20.0, -140.0)
            inner_node_3.location = (-200.0, 0.0)

            test_group.links.new(inner_node_1.inputs[0], inner_node_3.outputs[1])
            test_group.links.new(inner_node_1.inputs[1], inner_node_3.outputs[2])
            test_group.links.new(inner_node_1.inputs[2], inner_node_3.outputs[3])
            test_group.links.new(inner_node_2.inputs[0], inner_node_3.outputs[0])
            test_group.links.new(inner_node_0.inputs[1], inner_node_2.outputs[0])
            test_group.links.new(inner_node_0.inputs[0], inner_node_1.outputs[0])

            inner_node_1.inputs[0].default_value = 0.0
            inner_node_1.inputs[1].default_value = 0.0
            inner_node_1.inputs[2].default_value = 0.0
            inner_node_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_2.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            inner_node_2.inputs[1].default_value = 0.0
            inner_node_2.inputs[2].default_value = 100.0
            inner_node_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_0.location = (400.0, 0.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Output'
            inner_node_0.is_active_output = True
            inner_node_1.location = (0.0, 80.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Combine RGB'
            inner_node_2.location = (20.0, -140.0)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 42.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Bright/Contrast'
            inner_node_3.location = (-200.0, 0.0)
            inner_node_3.width = 140.0
            inner_node_3.width_hidden = 42.0
            inner_node_3.height = 100.0
            inner_node_3.name = 'Group Input'
            
        else:
            test_group = bpy.data.node_groups['MatCol0']
            
        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatCol0'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 180.0

        node.inputs[1].default_value = 0.0
        node.inputs[2].default_value = 0.0
        node.inputs[3].default_value = 0.0
        node.inputs[4].default_value = 1.0

        node.location = (-800.0, 1040.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MatCol1:
    def __init__(self, tree):
        if 'MatCol1' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatCol1', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupInput')
            inner_node_1 = test_group.nodes.new('NodeGroupOutput')
            inner_node_2 = test_group.nodes.new('ShaderNodeCombineRGB')

            test_group.inputs.new('NodeSocketColor', 'Red Channel')
            test_group.inputs.new('NodeSocketFloat', 'R')
            test_group.inputs[1].min_value = -3.4028234663852886e+38
            test_group.inputs[1].max_value = 3.4028234663852886e+38
            test_group.inputs[1].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'G')
            test_group.inputs[2].min_value = -3.4028234663852886e+38
            test_group.inputs[2].max_value = 3.4028234663852886e+38
            test_group.inputs[2].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'B')
            test_group.inputs[3].min_value = -3.4028234663852886e+38
            test_group.inputs[3].max_value = 3.4028234663852886e+38
            test_group.inputs[3].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'A')
            test_group.inputs[4].min_value = -3.4028234663852886e+38
            test_group.inputs[4].max_value = 3.4028234663852886e+38
            test_group.inputs[4].hide_value = False

            test_group.outputs.new('NodeSocketColor', 'MatCol1')
            test_group.outputs.new('NodeSocketColor', 'Red Channel')

            inner_node_0.location = (-200.0, 0.0)
            inner_node_1.location = (220.0, 0.0)
            inner_node_2.location = (-20.0, -40.0)

            test_group.links.new(inner_node_2.inputs[0], inner_node_0.outputs[1])
            test_group.links.new(inner_node_2.inputs[1], inner_node_0.outputs[2])
            test_group.links.new(inner_node_2.inputs[2], inner_node_0.outputs[3])
            test_group.links.new(inner_node_1.inputs[0], inner_node_2.outputs[0])
            test_group.links.new(inner_node_1.inputs[1], inner_node_0.outputs[0])

            inner_node_2.inputs[0].default_value = 0.0
            inner_node_2.inputs[1].default_value = 0.0
            inner_node_2.inputs[2].default_value = 0.0
            inner_node_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_0.location = (-200.0, 0.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Input'
            inner_node_1.location = (220.0, 0.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Group Output'
            inner_node_1.is_active_output = True
            inner_node_2.location = (-20.0, -40.0)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 42.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Combine RGB'
        else:
            test_group = bpy.data.node_groups['MatCol1']
        
        

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatCol1'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 180.0

        node.inputs[1].default_value = 0.0
        node.inputs[2].default_value = 0.0
        node.inputs[3].default_value = 0.0
        node.inputs[4].default_value = 1.0

        node.location = (-800.0, 820.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MatCol2:
    def __init__(self, tree):
        if 'MatCol2' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatCol2', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupInput')
            inner_node_1 = test_group.nodes.new('NodeGroupOutput')
            inner_node_2 = test_group.nodes.new('ShaderNodeCombineRGB')

            test_group.inputs.new('NodeSocketColor', 'Green Channel')
            test_group.inputs.new('NodeSocketFloat', 'R')
            test_group.inputs[1].min_value = -3.4028234663852886e+38
            test_group.inputs[1].max_value = 3.4028234663852886e+38
            test_group.inputs[1].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'G')
            test_group.inputs[2].min_value = -3.4028234663852886e+38
            test_group.inputs[2].max_value = 3.4028234663852886e+38
            test_group.inputs[2].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'B')
            test_group.inputs[3].min_value = -3.4028234663852886e+38
            test_group.inputs[3].max_value = 3.4028234663852886e+38
            test_group.inputs[3].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'A')
            test_group.inputs[4].min_value = -3.4028234663852886e+38
            test_group.inputs[4].max_value = 3.4028234663852886e+38
            test_group.inputs[4].hide_value = False

            test_group.outputs.new('NodeSocketColor', 'MatCol2')
            test_group.outputs.new('NodeSocketColor', 'Green Channel')

            inner_node_0.location = (-200.0, 0.0)
            inner_node_1.location = (400.0, 0.0)
            inner_node_2.location = (0.0, 80.0)

            test_group.links.new(inner_node_2.inputs[0], inner_node_0.outputs[1])
            test_group.links.new(inner_node_2.inputs[1], inner_node_0.outputs[2])
            test_group.links.new(inner_node_2.inputs[2], inner_node_0.outputs[3])
            test_group.links.new(inner_node_1.inputs[1], inner_node_0.outputs[0])
            test_group.links.new(inner_node_1.inputs[0], inner_node_2.outputs[0])

            inner_node_2.inputs[0].default_value = 0.0
            inner_node_2.inputs[1].default_value = 0.0
            inner_node_2.inputs[2].default_value = 0.0
            inner_node_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_0.location = (-200.0, 0.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Input'
            inner_node_1.location = (400.0, 0.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Group Output'
            inner_node_1.is_active_output = True
            inner_node_2.location = (0.0, 80.0)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 42.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Combine RGB'
        else:
            test_group = bpy.data.node_groups['MatCol2']
        
        

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatCol2'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 180.0

        node.inputs[1].default_value = 0.0
        node.inputs[2].default_value = 0.0
        node.inputs[3].default_value = 0.0
        node.inputs[4].default_value = 1.0

        node.location = (-800.0, 600.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MatCol3:
    def __init__(self, tree):
        if 'MatCol3' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatCol3', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupOutput')
            inner_node_1 = test_group.nodes.new('NodeGroupInput')
            inner_node_2 = test_group.nodes.new('ShaderNodeCombineRGB')

            test_group.inputs.new('NodeSocketColor', 'Blue Channel')
            test_group.inputs.new('NodeSocketFloatUnsigned', 'R')
            test_group.inputs[1].min_value = -3.4028234663852886e+38
            test_group.inputs[1].max_value = 3.4028234663852886e+38
            test_group.inputs[1].hide_value = False
            test_group.inputs.new('NodeSocketFloatUnsigned', 'G')
            test_group.inputs[2].min_value = -3.4028234663852886e+38
            test_group.inputs[2].max_value = 3.4028234663852886e+38
            test_group.inputs[2].hide_value = False
            test_group.inputs.new('NodeSocketFloatUnsigned', 'B')
            test_group.inputs[3].min_value = -3.4028234663852886e+38
            test_group.inputs[3].max_value = 3.4028234663852886e+38
            test_group.inputs[3].hide_value = False
            test_group.inputs.new('NodeSocketFloatUnsigned', 'A')
            test_group.inputs[4].min_value = -3.4028234663852886e+38
            test_group.inputs[4].max_value = 3.4028234663852886e+38
            test_group.inputs[4].hide_value = False

            test_group.outputs.new('NodeSocketColor', 'Color')
            test_group.outputs.new('NodeSocketColor', 'Blue Channel')

            inner_node_0.location = (450.0, -0.0)
            inner_node_1.location = (-460.0, -0.0)
            inner_node_2.location = (-160.0, 120.0)

            test_group.links.new(inner_node_2.inputs[0], inner_node_1.outputs[1])
            test_group.links.new(inner_node_2.inputs[1], inner_node_1.outputs[2])
            test_group.links.new(inner_node_2.inputs[2], inner_node_1.outputs[3])
            test_group.links.new(inner_node_0.inputs[1], inner_node_1.outputs[0])
            test_group.links.new(inner_node_0.inputs[0], inner_node_2.outputs[0])

            inner_node_2.inputs[0].default_value = 0.0
            inner_node_2.inputs[1].default_value = 0.0
            inner_node_2.inputs[2].default_value = 0.0
            inner_node_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            inner_node_0.location = (450.0, -0.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Output'
            inner_node_0.is_active_output = True
            inner_node_1.location = (-460.0, -0.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Group Input'
            inner_node_2.location = (-160.0, 120.0)
            inner_node_2.width = 140.0
            inner_node_2.width_hidden = 42.0
            inner_node_2.height = 100.0
            inner_node_2.name = 'Combine RGB'
        else:
            test_group = bpy.data.node_groups['MatCol3']
        
        

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatCol3'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 177.607421875

        node.inputs[1].default_value = 0.0
        node.inputs[2].default_value = 0.0
        node.inputs[3].default_value = 0.0
        node.inputs[4].default_value = 1.0

        node.location = (-800.0, 380.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MatScale0:
    def __init__(self, tree):
        if 'MatScale0' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatScale0', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupOutput')
            inner_node_1 = test_group.nodes.new('NodeGroupInput')

            test_group.inputs.new('NodeSocketFloat', 'X')
            test_group.inputs[0].min_value = -3.4028234663852886e+38
            test_group.inputs[0].max_value = 3.4028234663852886e+38
            test_group.inputs[0].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'Y')
            test_group.inputs[1].min_value = -3.4028234663852886e+38
            test_group.inputs[1].max_value = 3.4028234663852886e+38
            test_group.inputs[1].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'Z')
            test_group.inputs[2].min_value = -3.4028234663852886e+38
            test_group.inputs[2].max_value = 3.4028234663852886e+38
            test_group.inputs[2].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'W')
            test_group.inputs[3].min_value = -3.4028234663852886e+38
            test_group.inputs[3].max_value = 3.4028234663852886e+38
            test_group.inputs[3].hide_value = False

            test_group.outputs.new('NodeSocketFloat', 'X')
            test_group.outputs.new('NodeSocketFloat', 'Y')
            test_group.outputs.new('NodeSocketFloat', 'Z')
            test_group.outputs.new('NodeSocketFloat', 'W')

            inner_node_0.location = (190.0, -0.0)
            inner_node_1.location = (-200.0, -0.0)

            test_group.links.new(inner_node_0.inputs[0], inner_node_1.outputs[0])
            test_group.links.new(inner_node_0.inputs[1], inner_node_1.outputs[1])
            test_group.links.new(inner_node_0.inputs[2], inner_node_1.outputs[2])
            test_group.links.new(inner_node_0.inputs[3], inner_node_1.outputs[3])

            inner_node_0.location = (190.0, -0.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Output'
            inner_node_0.is_active_output = True
            inner_node_1.location = (-200.0, -0.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Group Input'
        else:
            test_group = bpy.data.node_groups['MatScale0']

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatScale0'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 140.0

        node.inputs[0].default_value = 1.0
        node.inputs[1].default_value = 1.0
        node.inputs[2].default_value = 1.0
        node.inputs[3].default_value = 0.029999999329447746

        node.location = (-1060.0, 60.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class MatScale1:
    def __init__(self, tree):
        if 'MatScale1' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('MatScale1', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('NodeGroupOutput')
            inner_node_1 = test_group.nodes.new('NodeGroupInput')

            test_group.inputs.new('NodeSocketFloat', 'X')
            test_group.inputs[0].min_value = -3.4028234663852886e+38
            test_group.inputs[0].max_value = 3.4028234663852886e+38
            test_group.inputs[0].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'Y')
            test_group.inputs[1].min_value = -3.4028234663852886e+38
            test_group.inputs[1].max_value = 3.4028234663852886e+38
            test_group.inputs[1].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'Z')
            test_group.inputs[2].min_value = -3.4028234663852886e+38
            test_group.inputs[2].max_value = 3.4028234663852886e+38
            test_group.inputs[2].hide_value = False
            test_group.inputs.new('NodeSocketFloat', 'W')
            test_group.inputs[3].min_value = -3.4028234663852886e+38
            test_group.inputs[3].max_value = 3.4028234663852886e+38
            test_group.inputs[3].hide_value = False

            test_group.outputs.new('NodeSocketFloat', 'X')
            test_group.outputs.new('NodeSocketFloat', 'Y')
            test_group.outputs.new('NodeSocketFloat', 'Z')
            test_group.outputs.new('NodeSocketFloat', 'W')

            inner_node_0.location = (190.0, -0.0)
            inner_node_1.location = (-200.0, -0.0)

            test_group.links.new(inner_node_0.inputs[0], inner_node_1.outputs[0])
            test_group.links.new(inner_node_0.inputs[1], inner_node_1.outputs[1])
            test_group.links.new(inner_node_0.inputs[2], inner_node_1.outputs[2])
            test_group.links.new(inner_node_0.inputs[3], inner_node_1.outputs[3])

            inner_node_0.location = (190.0, -0.0)
            inner_node_0.width = 140.0
            inner_node_0.width_hidden = 42.0
            inner_node_0.height = 100.0
            inner_node_0.name = 'Group Output'
            inner_node_0.is_active_output = True
            inner_node_1.location = (-200.0, -0.0)
            inner_node_1.width = 140.0
            inner_node_1.width_hidden = 42.0
            inner_node_1.height = 100.0
            inner_node_1.name = 'Group Input'
        else:
            test_group = bpy.data.node_groups['MatScale1']

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'MatScale1'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 140.0

        node.inputs[0].default_value = 3.0
        node.inputs[1].default_value = 1.0
        node.inputs[2].default_value = 1.0
        node.inputs[3].default_value = 1.0

        node.location = (-1060.0, -180.0)
        self.__node = node
        pass

    def node(self):
        return self.__node

    pass

class TexScrl0:
    def __init__(self, tree):
        if 'TexScrl0' not in list(bpy.data.node_groups.keys()):
            test_group = bpy.data.node_groups.new('TexScrl0', 'ShaderNodeTree')

            inner_node_0 = test_group.nodes.new('ShaderNodeMapping')
            inner_node_1 = test_group.nodes.new('ShaderNodeCombineXYZ')
            inner_node_2 = test_group.nodes.new('ShaderNodeTexCoord')
            inner_node_3 = test_group.nodes.new('NodeGroupInput')
            inner_node_4 = test_group.nodes.new('NodeGroupOutput')

            test_group.inputs.new('NodeSocketFloat', 'U')
            test_group.inputs.new('NodeSocketFloat', 'V')

            test_group.outputs.new('NodeSocketVector', 'Vector')

            inner_node_0.location = (100.0, 30.0)
            inner_node_1.location = (-100.0, -130.0)
            inner_node_2.location = (-100.0, 130.0)
            inner_node_3.location = (-300.0, -0.0)
            inner_node_4.location = (290.0, -0.0)

            test_group.links.new(inner_node_4.inputs['Vector'], inner_node_0.outputs['Vector'])
            test_group.links.new(inner_node_1.inputs['X'], inner_node_3.outputs['U'])
            test_group.links.new(inner_node_1.inputs['Y'], inner_node_3.outputs['V'])
            test_group.links.new(inner_node_0.inputs['Location'], inner_node_1.outputs['Vector'])
            test_group.links.new(inner_node_0.inputs['Vector'], inner_node_2.outputs['UV'])

            inner_node_0.inputs['Vector'].default_value = (0.0, 0.0, 0.0)
            inner_node_0.inputs['Location'].default_value = (0.0, 0.0, 0.0)
            inner_node_0.inputs['Rotation'].default_value = (0.0, 0.0, 0.0)
            inner_node_0.inputs['Scale'].default_value = (1.0, 1.0, 1.0)
            inner_node_0.outputs['Vector'].default_value = (0.0, 0.0, 0.0)

            inner_node_1.inputs['X'].default_value = 0.0
            inner_node_1.inputs['Y'].default_value = 0.0
            inner_node_1.inputs['Z'].default_value = 0.0
            inner_node_1.outputs['Vector'].default_value = (0.0, 0.0, 0.0)

            inner_node_2.outputs['Generated'].default_value = (0.0, 0.0, 0.0)
            inner_node_2.outputs['Normal'].default_value = (0.0, 0.0, 0.0)
            inner_node_2.outputs['UV'].default_value = (0.0, 0.0, 0.0)
            inner_node_2.outputs['Object'].default_value = (0.0, 0.0, 0.0)
            inner_node_2.outputs['Camera'].default_value = (0.0, 0.0, 0.0)
            inner_node_2.outputs['Window'].default_value = (0.0, 0.0, 0.0)
            inner_node_2.outputs['Reflection'].default_value = (0.0, 0.0, 0.0)

            inner_node_0.vector_type = 'TEXTURE'            
        else:
            test_group = bpy.data.node_groups['TexScrl0']

        node = tree.nodes.new('ShaderNodeGroup')
        node.label = 'TexScrl0'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 140.0

        node.location = (-1520.0, 620.0)
        self.__node = node
        pass

    def node(self):
        return self.__node
    pass



class UI_Testing:
    def __init__(self, context):
        print("UI Testing Running")
        
        self.__parent_context = context
        
        test_group = bpy.data.node_groups.new('Testing', 'ShaderNodeTree')
        test_group.name = "Testing"
        self.node_tree = test_group.copy()

        node = bpy.context.object.active_material.node_tree.nodes.new('ShaderNodeGroup')
        node.label = 'Running'
        node.node_tree = bpy.data.node_groups[test_group.name]
        node.width = 140.0
        
        
        node.location = (-200.0, 0)
        self.__node = node
        pass

    def node(self):
        return self.__node
    
    def draw_buttons(self, context, layout):
        box = layout.box()
        env = self.__parent_context.nodes['Testing']
        box.label(text="Environment Map")
        box.template_image(env, "image", env.image_user, compact=False, multiview=True)
        box.prop(env, "interpolation", text="")
        box.prop(env, "projection", text="")
        box.prop(env, "extension", text="")
        pass

class Parameter:
    @classmethod
    def new(cls,parameter_type: str, material, Import:bool=False):
        print(material.name)
        if parameter_type not in [N.name for N in material.node_tree.nodes]:
            if Import:
                print("[DEBUG] | IMPORTING NEW PARAMETER NODE:", parameter_type)
                return eval(parameter_type+'(material.node_tree)').node()
            else:
                print("[DEBUG] | CREATING NEW PARAMETER NODE:", parameter_type)
                exec(parameter_type+'(material.node_tree)')
