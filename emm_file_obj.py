import traceback
from typing import *
from .fileUtil import *
import numpy as np
#from parameter_types import Parameter, params

class mat_paras:
    materials = {
        'TOON_UNIF_STAIN3d2_XVM_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN1_DFD': ['AlphaBlend', 'AlphaBlendType', 'Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_EYE_MUT1_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1', 'TexScrl0'],
        'TOON_UNIF_DFD': ['AlphaBlend', 'AlphaBlendType', 'Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatOffset1', 'MatScale0', 'MatScale1', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff', 'TexScrl0'],
        'TOON_UNIF_STAIN2_DFD': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'Glare', 'MatC', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN3_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_EYE_MUT2_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1', 'TexScrl0'],
        'TOON_UNIF_EYE_MUT0_DFD': ['Glare', 'MatCol0', 'MatCol3', 'MatScale0', 'MatScale1', 'TexScrl0'],
        'TOON_UNIF_EYE_MUT1d3_DFD': ['MatCol0', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1', 'TexScrl0'],
        'TOON_UNIF_EYE_MUT3_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1', 'TexScrl0'],
        'TOON_UNIF_HAIR_DFD': ['Glare', 'MatCol0', 'MatOffset0', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN2_DFDaa': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN3_DFDaa': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_ENV': ['AlphaBlend', 'AlphaBlendType', 'Glare', 'MatOffset1', 'MatScale0', 'MatScale1', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff'],
        'TOON0002_UNIF_STAIN2_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN2d2_XVM_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN3_DFDAth': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN2_DFDAth': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_ENV_ADD': ['Glare', 'MatOffset1', 'MatScale0', 'MatScale1', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff'],
        'TOON_UNIF_STAIN1_DFDaa': ['Glare', 'MatCol0', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN1_MSK_DFD': ['Glare', 'MatCol0', 'MatScale0', 'MatScale1'],
        'AGE_TOON_UNIF_STAIN3_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1', 'RimCoeff', 'RimPower', 'SpcCoeff', 'SpcPower'],
        'AGE_TEST_TOON_UNIF_DFD': ['Glare', 'MatScale0', 'MatScale1', 'RimCoeff', 'RimPower', 'SpcCoeff', 'SpcPower'],
        'AGE_TOON_UNIF_ENV': ['Glare', 'MatScale0', 'MatScale1', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff', 'RimCoeff', 'RimPower', 'SpcCoeff', 'SpcPower'],
        'AGE_TOON_UNIF_EYE_MUT1_DFD': ['Glare', 'MatCol0', 'MatCol3', 'MatScale0', 'MatScale1', 'RimCoeff', 'RimPower', 'SpcCoeff', 'SpcPower', 'TexScrl0'],
        'AGE_TOON_UNIF_STAIN3_DFDaa': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1', 'RimCoeff', 'RimPower', 'SpcCoeff', 'SpcPower'],
        'TOON_UNIF_SIMPLIFIED': ['MatCol0'],
        'TOON_DFD': ['MarkSamplerAddress', 'MatScale0', 'ToonSamplerAddress', 'gLightAmb', 'gLightDif', 'gLightDir', 'gLightSpc', 'gToonTextureHeight', 'gToonTextureWidth'],
        'TOON_STAIN1_DFD': ['AlphaBlend', 'AlphaBlendType', 'Glare', 'MatCol0', 'MatScale0', 'MatScale1'],
        'TOON_STAIN1_DFD_STN': ['BackFace', 'MatCol0', 'MatOffset1', 'MatScale0', 'MatScale1'],
        'TOON_STAIN2_DFD': ['AlphaBlend', 'AlphaBlendType', 'Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'TOON_ENV': ['Glare', 'MatOffset1', 'MatScale0', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff'],
        'TOON_UNIF_STAIN3_MSK_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale0', 'MatScale1'],
        'AGE_TOON_UNIF_HAIR_DFD': ['Glare', 'MatCol0', 'MatOffset0', 'MatScale0', 'MatScale1'],
        'TOON_DECAL_DC': ['Glare', 'MatCol1', 'MatCol2', 'MatOffset0', 'MatOffset1', 'MatScale0'],
        'TOON_UNIF_STAIN1_DFDAth': ['AlphaTest', 'Glare', 'MatCol0', 'MatScale0', 'MatScale1', 'NoEdge'],
        'TOON_UNIF_HAIR_DFDAth': ['Glare', 'MatCol0', 'MatOffset0', 'MatScale0', 'MatScale1'],
        'TOON_HAIR_DFD': ['gToonTextureHeight', 'gToonTextureWidth', 'g_MaterialOffset0_VS'],
        'TOON_STAIN1_DFDaa': ['Glare', 'MatCol0', 'MatScale0', 'MatScale1'],
        'TOON0002_UNIF_STAIN2d2_XVM_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'AGE_TOON_UNIF_EYE_MUT2_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1', 'TexScrl0'],
        'TOON_UNIF_STAIN2d2_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'AGE_TOON_UNIF_STAIN2_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'AGE_TOON_STAIN1_DFD': ['Glare', 'MatCol0', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_HAIR_DFD_STN': ['BackFace', 'Glare', 'MatCol0', 'MatOffset0', 'MatOffset1', 'MatScale0', 'MatScale1'],
        'TOON_UNIF_STAIN1d2_XVM_DFD': ['Glare', 'MatCol0', 'MatCol1', 'MatCol3', 'MatScale0', 'MatScale1'],
        'ParticleDecal': ['AlphaBlend', 'AlphaBlendType', 'AlphaTest', 'BackFace', 'Glare', 'GlareCol', 'LowRez', 'LowRezSmoke', 'ZWriteMask'],
        'T1_VFX_TRC_RI': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'CustomFlag', 'Glare', 'GlareCol', 'IncidenceAlphaBias', 'IncidencePower', 'MatScale0', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'T1_VFX_MTN': ['AlphaBlend', 'AlphaBlendType', 'AlphaSortMask', 'AlphaTest', 'AnimationChannel', 'BackFace', 'Billboard', 'BillboardType', 'Glare', 'GlareCol', 'IncidenceAlphaBias', 'IncidencePower', 'LowRez', 'LowRezSmoke', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'TexScrl0', 'TexScrl1', 'TwoSidedRender', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'T1_VFX_MTN_DIS_ALPHA': ['AlphaBlend', 'AlphaBlendType', 'AnimationChannel', 'BackFace', 'Glare', 'GlareCol', 'IncidenceAlphaBias', 'IncidencePower', 'LowRez', 'LowRezSmoke', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'TexScrl0', 'TexScrl1', 'TwoSidedRender', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'DecalColor': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'LowRez', 'ZWriteMask'],
        'T1_VFX_PRLX_MTN': ['AlphaBlend', 'AlphaBlendType', 'AnimationChannel', 'Glare', 'GlareCol', 'IncidenceAlphaBias', 'IncidencePower', 'LowRez', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale1', 'TexScrl0', 'TexScrl1', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'ScreenRefractAdjust': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'GlareCol', 'LowRez', 'MatScale0', 'ZWriteMask'],
        'SoftParticleDecal': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'Glare', 'GlareCol', 'LowRez', 'LowRezSmoke', 'MatOffset0', 'ZWriteMask'],
        'U2_MUV_L_SM_S': ['MatSpc', 'SpcCoeff', 'SpcPower'],
        'GLASS': ['AlphaBlend', 'AlphaBlendType', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff'],
        'U2_MUV_L_SM': ['MatSpc', 'SpcCoeff', 'SpcPower'],
        'T1_ScrollShimmerBias': ['CustomFlag', 'Glare', 'MipMapLod0', 'TexScrl0'],
        'T1_Scroll': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'Glare', 'MipMapLod0', 'NoEdge', 'TexScrl0', 'TwoSidedRender', 'ZWriteMask'],
        'U2_MUV_BUMP_SM': ['MatSpc', 'SpcCoeff', 'SpcPower'],
        'T1_VFX_PRLX_MTN_DIS_ALPHA': ['AlphaBlend', 'AlphaBlendType', 'AnimationChannel', 'Glare', 'GlareCol', 'IncidenceAlphaBias', 'IncidencePower', 'LowRez', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'MatScale1', 'TexScrl0', 'TexScrl1', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'T2_MUV_STKR_Scrl_NF': ['MatSpc', 'SpcCoeff', 'SpcPower', 'TexScrl0', 'TexScrl1'],
        'T1_Scroll_Emission_NoFog': ['AlphaBlend', 'AlphaBlendType', 'Glare', 'MatScale0', 'TexScrl0', 'ZWriteMask'],
        'U3spua_BM_BUMP_SM': ['Glare', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'U3_BM_BUMP_SM_DYN': ['Glare', 'MatAmb', 'MatAmbScale', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'U3spua_BM_SM': ['Glare', 'MatSpc', 'MipMapLod1', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2'],
        'U3_SUV_SM_ALPHA_BLEND_S': ['Glare', 'MatSpc', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2'],
        'U3spua_BM_SM_S': ['Glare', 'MatSpc', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2'],
        'U3_MUV_SM_BLEND': ['MatSpc', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2'],
        'U3_SUV_SM_BLEND': ['MatSpc', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2'],
        'U3_BM': [],
        'T1_C_NoFog_PT': ['AlphaTest'],
        'U2_SUV_SM_BLEND_MOD_S': ['Glare', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'U2_SUV_SM_BLEND_S': ['MatSpc', 'SpcCoeff', 'SpcPower'],
        'VdotN_Alpha': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'TexScrl0', 'ZWriteMask'],
        'T1_S': ['AlphaTest', 'BackFace'],
        'GI_GrassSimulation_L_S': ['AlphaTest', 'BackFace', 'CustomFlag', 'MatCol0', 'MatCol1', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'T1_BUMP_SM_DYN_MTN_S': ['Glare', 'MatAmb', 'MatAmbScale', 'MatCol0', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'T1_SM_DYN_MTN_S': ['Glare', 'MatAmb', 'MatAmbScale', 'MatCol0', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower', 'TexScrl0'],
        'T1_BUMP_SM_DYN_S': ['Glare', 'MatAmb', 'MatAmbScale', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'U3spua_BM_BUMP_SM_DYN_S': ['Glare', 'MatAmb', 'MatAmbScale', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'ParticleDecalPT': ['AlphaBlend', 'AlphaBlendType', 'AlphaTest', 'Glare', 'GlareCol', 'ZWriteMask'],
        'T1_VFX_MTN_W_DIS_ALPHA': ['AlphaBlend', 'AlphaBlendType', 'AnimationChannel', 'BackFace', 'Glare', 'GlareCol', 'IncidenceAlphaBias', 'IncidencePower', 'LowRez', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'TexScrl0', 'TexScrl1', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'T1_VFX_MTN_PT_DIS_ALPHA': ['AlphaBlend', 'AlphaBlendType', 'AlphaTest', 'AnimationChannel', 'BackFace', 'Glare', 'GlareCol', 'IncidenceAlphaBias', 'IncidencePower', 'LowRez', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'TexScrl0', 'TexScrl1', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'T1_VFX_MTN_REFRACT': ['AlphaBlend', 'AlphaBlendType', 'AnimationChannel', 'BackFace', 'CustomFlag', 'GlareCol', 'MatCol0', 'MatCol1', 'TexScrl0', 'TexScrl1', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'TOON_UNIFfx_VFX_DFDna_FCM': ['MatCol0', 'MatScale0', 'MatScale1'],
        'T1_VFX_TRC_I': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'Glare', 'GlareCol', 'IncidenceAlphaBias', 'IncidencePower', 'ZWriteMask'],
        'ParticleRandomColor': [],
        'T1_VFX': ['AlphaBlend', 'AlphaBlendType', 'BackFace', 'FadeInit', 'FadeSpeed', 'Glare', 'GlareCol', 'GradientInit', 'GradientSpeed', 'IncidenceAlphaBias', 'IncidencePower', 'MatCol0', 'MatCol1', 'MatCol2', 'MatCol3', 'TexScrl0', 'TexScrl1', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'ParticleRefract': ['AlphaBlend', 'AlphaBlendType', 'GlareCol', 'LowRez', 'MatScale0', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'ShadowModelAlphaKill': ['BackFace', 'CustomFlag'],
        'SHADOWMAP_ALPHAKILL': ['BackFace', 'CustomFlag'],
        'T1_VFX_MTN_REFRACT_ADJUST_DA': ['AlphaBlend', 'AlphaBlendType', 'AnimationChannel', 'BackFace', 'GlareCol', 'LowRez', 'MatCol0', 'MatCol1', 'TexScrl0', 'TexScrl1', 'TwoSidedRender', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'ZWriteMask'],
        'T1_C_Scroll_Emission': ['AlphaBlend', 'AlphaBlendType', 'Glare', 'MatScale0', 'TexScrl0', 'ZWriteMask'],
        'T1_SM_DYN_S': ['Glare', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'T2_MUV_L_SM': ['MatSpc', 'SpcCoeff', 'SpcPower'],
        'T2_MUV_C_L_SM': ['Glare', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'T1': [],
        'T1_L_PT': ['AlphaBlend', 'AlphaBlendType', 'MatSpc', 'SpcCoeff', 'SpcPower', 'ZWriteMask'],
        'T2_MUV_C': [],
        'T1_Emission_NoFog': ['AlphaBlend', 'AlphaBlendType', 'Glare', 'MatScale0', 'ZWriteMask'],
        'T1_C_Scroll': ['AlphaBlend', 'AlphaBlendType', 'TexScrl0', 'ZWriteMask'],
        'T1_BUMP_SM_DYN_MTN': ['MatAmb', 'MatAmbScale', 'MatCol0', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'T1_BUMP_SM_DYN': ['MatAmb', 'MatAmbScale', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'T2_MUV_BUMP_SM_BLEND_DYN_MTN_S': ['MatAmb', 'MatAmbScale', 'MatCol0', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'T2_MUV_BUMP_SM_BLEND_DYN_S': ['MatAmb', 'MatAmbScale', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'GI_T1_BUMP_SM_DYN': ['MatAmb', 'MatAmbScale', 'MatDif', 'MatDifScale', 'MatSpc', 'SpcCoeff', 'SpcPower'],
        'GI_T1_L_SM_S': ['MatSpc', 'SpcCoeff', 'SpcPower']
    }

    validParameters = []
    pass

class EMM:
    def __init__(self,hexList: List[str]):
        self.header = EMM_Header(hexList)
        self.materials = [EMM_Material_Section(
            hexList[self.header.header_size+self.header.mat_pointers[point]:])
            for point in range(0, int(self.header.material_count))]
        for mat in self.materials:
            if mat.shaderProgName.replace('\x00','') not in mat_paras.validParameters:
                #print(mat.shaderProgName.replace('\x00',''))
                mat_paras.validParameters.append(mat.shaderProgName.replace('\x00',''))
            if mat.shaderProgName.replace('\x00','') not in mat_paras.materials.keys():
                #print('Material Name    :', mat.name)
                print('ShaderProgName   :', mat.shaderProgName.replace('\x00',''))
                oof = tuple([str(mat.shaderProgName.replace('\x00','')),[]])
                #print(oof)
                mat_paras.materials.__setitem__(mat.shaderProgName.replace('\x00',''),[])
                #print('Number_parameters:', mat.number_parameters)
            if mat.shaderProgName.replace('\x00','') in mat_paras.materials.keys():
                for parameter in mat.parameters:
                    if parameter.name.replace('\x00','') not in mat_paras.materials[mat.shaderProgName.replace('\x00','')]:
                        mat_paras.materials[mat.shaderProgName.replace('\x00','')].\
                            append(parameter.name.replace('\x00',''))
                    #print(parameter.name.replace('\x00',''))
                #    print('Parameter Type :', parameter.type)
                #    print('Parameter Level:', parameter.level)
                #    print('Parameter Value:', parameter.value)
                #    print()
        pass

class EMM_Header:
    def __init__(self, hlist: list):
        self.signature        = hex2str(hlist[0x00:0x04])
        self.endian           = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x04:0x06],keepSpaces=False)),np.uint16)[0]
        self.header_size      = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x06:0x08],keepSpaces=False)),np.uint16)[0]
        self.version          = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x08:0x0c],keepSpaces=False)),np.uint8)
        self.offset_materials = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x0c:0x10],keepSpaces=False)),np.uint32)[0]
        self.sub = EMM_Header_Sub(hlist[0x10:])

        self.material_count: np.uint32 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[self.offset_materials:self.offset_materials + 4], keepSpaces=False)), np.uint32)[0]
        self.mat_pointers = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[self.offset_materials+4:(self.offset_materials+4)+(4*self.material_count)], keepSpaces=False)), np.uint32)


        pass

class EMM_Header_Sub:
    def __init__(self, hlist: list):
        self.offset_unknowValues = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x04],keepSpaces=False)),np.uint32)[0]
        self.unknow_0            = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x04:0x08],keepSpaces=False)),np.uint32)[0]
        self.unknow_1            = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x08:0x0c],keepSpaces=False)),np.uint32)[0]
        self.unknow_2            = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x0c:0x10],keepSpaces=False)),np.uint32)[0]

        #print('Header Sub Unknown: ', self.offset_unknowValues  )
        #print('Header Sub Unknown: ', self.unknow_0             )
        #print('Header Sub Unknown: ', self.unknow_1             )
        #print('Header Sub Unknown: ', self.unknow_2             )

        pass

class EMM_Material_Section:
    def __init__(self, hlist: list):
        self.name               = hex2str(hlist[0x00:0x20]).replace('\x00','') #0x00
        self.shaderProgName     = hex2str(hlist[0x20:0x40]).replace('\x00','') #0x20
        self.number_parameters  = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x40:0x42],keepSpaces=False)),np.uint16)[0]
        self.unknow_0           = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x42:0x44],keepSpaces=False)),np.uint16)
        #print('Mat Sect Unknown: ', self.unknow_0)
        paraHex = hlist[0x44:]
        self.parameters = [EMM_Parameter_Section(paraHex[0x28*para:])
                           for para in range(0,int(self.number_parameters))]

        self.test = [item for item in self.parameters]
        print(self.name)
        print(self.shaderProgName)
        print(self.number_parameters)
        print(self.unknow_0)
        pass

class EMM_Parameter_Section:
    def __init__(self, hlist: list):
        self.name = hex2str(hlist[0x00:0x20]).replace('\x00','')

        if np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x20:0x22],keepSpaces=False)),np.uint16)[0]:
            self.type = np.uint32
        else:
            self.type = np.float32

        self.level = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x22:0x24],keepSpaces=False)),np.uint16)[0]
        self.value = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x24:0x28],keepSpaces=False)),self.type)[0]
        #print(self.name, hlist[0x24:0x28])
        pass
