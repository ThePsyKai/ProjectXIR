import bpy

class MaterialTypeClothing_OT_operator(bpy.types.Operator):
    bl_label = "Type Clothing"
    bl_idname = "material.material_type_clothing"

class SelectMaterialProperties(bpy.types.PropertyGroup):

    material_type : bpy.props.EnumProperty(
        name="Type",
        items=[
            ('OP1', "Clothing", "Includes Scratch effects"),
            ('OP2', "Skin", "Includes Scratches and Blood effects"),
            ('OP3', "Reflective", ""),
            ('OP4', "Hair", ""),
            ('OP5', "Eye", ""),
            ('OP6', "Dual EMB", ""),
            ('OP7', "Mouth/Teeth", ""),
            ('OP8', "Other", ""),
            ('OP9', "Unorganized", ""),
        ]
    )

#class MaterialProperty_OT_operator(bpy.types.Operator):
#    bl_label = 'Operator'
#    bl_idname = 'material.material_property'
#
#    def execute(self,context):
#        scene = context.scene
#        materialTool = scene.material_tool
#        if materialTool.material_type == "OP1":
#
#        return {'FINISHED'}

class XenoverseMaterials_PT_panel(bpy.types.Panel):
    bl_label = "Xenoverse Materials"
    bl_idname = "XenoverseMaterials_PT_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "XeNodes"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        materialTool = scene.material_tool

        layout.prop(materialTool,"material_type")

        types = layout.box()
        types.label(text="Material Types")
        if materialTool.material_type == "OP1":     #Clothing
            pass
        elif materialTool.material_type == "OP2":   #Skin
            pass
        elif materialTool.material_type == "OP3":   #Reflective
            pass
        elif materialTool.material_type == "OP4":   #Hair
            pass
        elif materialTool.material_type == "OP5":   #Eye
            pass
        elif materialTool.material_type == "OP6":   #Dual EMB
            ###TOON_UNIF_STAIN1d2_XVM_DFD
            ###TOON_UNIF_STAIN2d2_XVM_DFD
            ###TOON_UNIF_STAIN3d2_XVM_DFD
            pass
        elif materialTool.material_type == "OP7":   #Mouth/Teeth
            pass
        elif materialTool.material_type == "OP8":   #Other
            pass
        elif materialTool.material_type == "OP9":   #Undocumented
            types.operator('material.atetou_dfd')
            types.operator('material.atos1_dfd')
            types.operator('material.atou_env')
            types.operator('material.atou_eye_m1_dfd')
            types.operator('material.atou_eye_m2_dfd')
            types.operator('material.atou_hair_dfd')
            types.operator('material.atous2_dfd')
            types.operator('material.atous3_dfd')
            types.operator('material.atous3_dfd_aa')
            types.operator('material.to0002_u_s2_dfd')
            types.operator('material.to0002_u_s2_d2_xvm_dfd')
            types.operator('material.to_decal_dc')
            types.operator('material.to_dfd')
            types.operator('material.to_env')
            types.operator('material.to_hair_dfd')
            types.operator('material.tos1_dfd')
            types.operator('material.tos1_dfd_stn')
            types.operator('material.tos1_dfd_aa')
            types.operator('material.tos2_dfd')
            types.operator('material.tou_dfd')
            types.operator('material.tou_env')
            types.operator('material.tou_env_add')
            types.operator('material.tou_eye_m0_dfd')
            types.operator('material.tou_eye_m1_dfd')
            types.operator('material.tou_eye_m1_d3_dfd')
            types.operator('material.tou_eye_m2_dfd')
            types.operator('material.tou_eye_m3_dfd')
            types.operator('material.tou_hair_dfd')
            types.operator('material.tou_hair_dfd_ath')
            types.operator('material.tou_hair_dfd_stn')
            types.operator('material.tou_simplified')
            types.operator('material.tous1_dfd')
            types.operator('material.tous1_dfd_ath')
            types.operator('material.tous1_dfd_aa')
            types.operator('material.tous1msk_dfd')
            types.operator('material.tous1_d2_xvm_dfd')
            types.operator('material.tous2_dfd')
            types.operator('material.tous2_dfd_ath')
            types.operator('material.tous2_dfd_aa')
            types.operator('material.tous2_d2_dfd')
            types.operator('material.tous2_d2_xvm_dfd')
            types.operator('material.tous3_dfd')
            types.operator('material.tous3_dfd_ath')
            types.operator('material.tous3_dfd_aa')
            types.operator('material.tous3msk_dfd')
            types.operator('material.tous3_d2_xvm_dfd')



def get_mat_out(tree):
    for item in tree.nodes:
        if item.type == 'OUTPUT_MATERIAL':
            return item

class ATeToUDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TEST_TOON_UNIF_DFD"""
    bl_label = "AGE_TEST_TOON_UNIF_DFD"
    bl_idname = "material.atetou_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ATeToUDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ATeToUDFD_OT_operator.bl_label)
        return {'FINISHED'}

class AToS1DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TOON_STAIN1_DFD"""
    bl_label = "AGE_TOON_STAIN1_DFD"
    bl_idname = "material.atos1_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = AToS1DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+AToS1DFD_OT_operator.bl_label)
        return {'FINISHED'}

class AToUEnv_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TOON_UNIF_ENV"""
    bl_label = "AGE_TOON_UNIF_ENV"
    bl_idname = "material.atou_env"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = AToUEnv_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+AToUEnv_OT_operator.bl_label)
        return {'FINISHED'}

class AToUEyeM1DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TOON_UNIF_EYE_MUT1_DFD"""
    bl_label = "AGE_TOON_UNIF_EYE_MUT1_DFD"
    bl_idname = "material.atou_eye_m1_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = AToUEyeM1DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+AToUEyeM1DFD_OT_operator.bl_label)
        return {'FINISHED'}

class AToUEyeM2DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TOON_UNIF_EYE_MUT2_DFD"""
    bl_label = "AGE_TOON_UNIF_EYE_MUT2_DFD"
    bl_idname = "material.atou_eye_m2_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = AToUEyeM2DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+AToUEyeM2DFD_OT_operator.bl_label)
        return {'FINISHED'}

class AToUHairDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TOON_UNIF_HAIR_DFD"""
    bl_label = "AGE_TOON_UNIF_HAIR_DFD"
    bl_idname = "material.atou_hair_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = AToUHairDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+AToUHairDFD_OT_operator.bl_label)
        return {'FINISHED'}

class AToUS2DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TOON_UNIF_STAIN2_DFD"""
    bl_label = "AGE_TOON_UNIF_STAIN2_DFD"
    bl_idname = "material.atous2_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = AToUS2DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+AToUS2DFD_OT_operator.bl_label)
        return {'FINISHED'}

class AToUS3DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TOON_UNIF_STAIN3_DFD"""
    bl_label = "AGE_TOON_UNIF_STAIN3_DFD"
    bl_idname = "material.atous3_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = AToUS3DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+AToUS3DFD_OT_operator.bl_label)
        return {'FINISHED'}

class AToUS3DFDaa_OT_operator(bpy.types.Operator):
    """Define Material Type as AGE_TOON_UNIF_STAIN3_DFDaa"""
    bl_label = "AGE_TOON_UNIF_STAIN3_DFDaa"
    bl_idname = "material.atous3_dfd_aa"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = AToUS3DFDaa_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+AToUS3DFDaa_OT_operator.bl_label)
        return {'FINISHED'}

class To0002US2DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON0002_UNIF_STAIN2_DFD"""
    bl_label = "TOON0002_UNIF_STAIN2_DFD"
    bl_idname = "material.to0002_u_s2_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = To0002US2DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+To0002US2DFD_OT_operator.bl_label)
        return {'FINISHED'}

class To0002US2d2XVMDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON0002_UNIF_STAIN2d2_XVM_DFD"""
    bl_label = "TOON0002_UNIF_STAIN2d2_XVM_DFD"
    bl_idname = "material.to0002_u_s2_d2_xvm_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = To0002US2d2XVMDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+To0002US2d2XVMDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToDecalDC_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_DECAL_DC"""
    bl_label = "TOON_DECAL_DC"
    bl_idname = "material.to_decal_dc"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToDecalDC_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToDecalDC_OT_operator.bl_label)
        return {'FINISHED'}

class ToDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_DFD"""
    bl_label = "TOON_DFD"
    bl_idname = "material.to_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToEnv_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_ENV"""
    bl_label = "TOON_ENV"
    bl_idname = "material.to_env"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToEnv_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToEnv_OT_operator.bl_label)
        return {'FINISHED'}

class ToHairDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_HAIR_DFD"""
    bl_label = "TOON_HAIR_DFD"
    bl_idname = "material.to_hair_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToHairDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToHairDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToS1DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_STAIN1_DFD"""
    bl_label = "TOON_STAIN1_DFD"
    bl_idname = "material.tos1_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToS1DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToS1DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToS1DFDSTN_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_STAIN1_DFD_STN"""
    bl_label = "TOON_STAIN1_DFD_STN"
    bl_idname = "material.tos1_dfd_stn"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToS1DFDSTN_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToS1DFDSTN_OT_operator.bl_label)
        return {'FINISHED'}

class ToS1DFDaa_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_STAIN1_DFDaa"""
    bl_label = "TOON_STAIN1_DFDaa"
    bl_idname = "material.tos1_dfd_aa"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToS1DFDaa_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToS1DFDaa_OT_operator.bl_label)
        return {'FINISHED'}

class ToS2DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_STAIN2_DFD"""
    bl_label = "TOON_STAIN2_DFD"
    bl_idname = "material.tos2_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToS2DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToS2DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_DFD"""
    bl_label = "TOON_UNIF_DFD"
    bl_idname = "material.tou_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUEnv_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_ENV"""
    bl_label = "TOON_UNIF_ENV"
    bl_idname = "material.tou_env"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUEnv_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUEnv_OT_operator.bl_label)
        return {'FINISHED'}

class ToUEnvADD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_ENV_ADD"""
    bl_label = "TOON_UNIF_ENV_ADD"
    bl_idname = "material.tou_env_add"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUEnvADD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUEnvADD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUEyeM0DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_EYE_MUT0_DFD"""
    bl_label = "TOON_UNIF_EYE_MUT0_DFD"
    bl_idname = "material.tou_eye_m0_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUEyeM0DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUEyeM0DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUEyeM1DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_EYE_MUT1_DFD"""
    bl_label = "TOON_UNIF_EYE_MUT1_DFD"
    bl_idname = "material.tou_eye_m1_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUEyeM1DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUEyeM1DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUEyeM1d3DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_EYE_MUT1d3_DFD"""
    bl_label = "TOON_UNIF_EYE_MUT1d3_DFD"
    bl_idname = "material.tou_eye_m1_d3_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUEyeM1d3DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUEyeM1d3DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUEyeM2DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_EYE_MUT2_DFD"""
    bl_label = "TOON_UNIF_EYE_MUT2_DFD"
    bl_idname = "material.tou_eye_m2_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUEyeM2DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUEyeM2DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUEyeM3DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_EYE_MUT3_DFD"""
    bl_label = "TOON_UNIF_EYE_MUT3_DFD"
    bl_idname = "material.tou_eye_m3_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUEyeM3DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUEyeM3DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUHairDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_HAIR_DFD"""
    bl_label = "TOON_UNIF_HAIR_DFD"
    bl_idname = "material.tou_hair_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUHairDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUHairDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUHairDFDAth_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_HAIR_DFDAth"""
    bl_label = "TOON_UNIF_HAIR_DFDAth"
    bl_idname = "material.tou_hair_dfd_ath"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUHairDFDAth_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUHairDFDAth_OT_operator.bl_label)
        return {'FINISHED'}

class ToUHairDFDSTN_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_HAIR_DFD_STN"""
    bl_label = "TOON_UNIF_HAIR_DFD_STN"
    bl_idname = "material.tou_hair_dfd_stn"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUHairDFDSTN_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUHairDFDSTN_OT_operator.bl_label)
        return {'FINISHED'}

class ToUSIMPLIFIED_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_SIMPLIFIED"""
    bl_label = "TOON_UNIF_SIMPLIFIED"
    bl_idname = "material.tou_simplified"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUSIMPLIFIED_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUSIMPLIFIED_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS1DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN1_DFD"""
    bl_label = "TOON_UNIF_STAIN1_DFD"
    bl_idname = "material.tous1_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS1DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS1DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS1DFDAth_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN1_DFDAth"""
    bl_label = "TOON_UNIF_STAIN1_DFDAth"
    bl_idname = "material.tous1_dfd_ath"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS1DFDAth_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS1DFDAth_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS1DFDaa_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN1_DFDaa"""
    bl_label = "TOON_UNIF_STAIN1_DFDaa"
    bl_idname = "material.tous1_dfd_aa"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS1DFDaa_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS1DFDaa_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS1MskDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN1_MSK_DFD"""
    bl_label = "TOON_UNIF_STAIN1_MSK_DFD"
    bl_idname = "material.tous1msk_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS1MskDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS1MskDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS1d2XVMDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN1d2_XVM_DFD"""
    bl_label = "TOON_UNIF_STAIN1d2_XVM_DFD"
    bl_idname = "material.tous1_d2_xvm_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS1d2XVMDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS1d2XVMDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS2DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN2_DFD"""
    bl_label = "TOON_UNIF_STAIN2_DFD"
    bl_idname = "material.tous2_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS2DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS2DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS2DFDAth_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN2_DFDAth"""
    bl_label = "TOON_UNIF_STAIN2_DFDAth"
    bl_idname = "material.tous2_dfd_ath"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS2DFDAth_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS2DFDAth_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS2DFDaa_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN2_DFDaa"""
    bl_label = "TOON_UNIF_STAIN2_DFDaa"
    bl_idname = "material.tous2_dfd_aa"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS2DFDaa_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS2DFDaa_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS2d2DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN2d2_DFD"""
    bl_label = "TOON_UNIF_STAIN2d2_DFD"
    bl_idname = "material.tous2_d2_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS2d2DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS2d2DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS2d2XVMDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN2d2_XVM_DFD"""
    bl_label = "TOON_UNIF_STAIN2d2_XVM_DFD"
    bl_idname = "material.tous2_d2_xvm_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS2d2XVMDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS2d2XVMDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS3DFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN3_DFD"""
    bl_label = "TOON_UNIF_STAIN3_DFD"
    bl_idname = "material.tous3_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS3DFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS3DFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS3DFDAth_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN3_DFDAth"""
    bl_label = "TOON_UNIF_STAIN3_DFDAth"
    bl_idname = "material.tous3_dfd_ath"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS3DFDAth_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS3DFDAth_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS3DFDaa_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN3_DFDaa"""
    bl_label = "TOON_UNIF_STAIN3_DFDaa"
    bl_idname = "material.tous3_dfd_aa"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS3DFDaa_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS3DFDaa_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS3MskDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN3_MSK_DFD"""
    bl_label = "TOON_UNIF_STAIN3_MSK_DFD"
    bl_idname = "material.tous3msk_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS3MskDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS3MskDFD_OT_operator.bl_label)
        return {'FINISHED'}

class ToUS3d2XVMDFD_OT_operator(bpy.types.Operator):
    """Define Material Type as TOON_UNIF_STAIN3d2_XVM_DFD"""
    bl_label = "TOON_UNIF_STAIN3d2_XVM_DFD"
    bl_idname = "material.tous3_d2_xvm_dfd"

    def execute(self, context):
        mat_out = get_mat_out(context.object.active_material.node_tree)
        mat_out.label = ToUS3d2XVMDFD_OT_operator.bl_label
        self.report({'INFO'}, context.object.active_material.name+" defined as "+ToUS3d2XVMDFD_OT_operator.bl_label)
        return {'FINISHED'}