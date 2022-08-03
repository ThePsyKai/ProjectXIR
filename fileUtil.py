import os
from binascii import b2a_hex
from typing import *

def hexList2hexStrList(HEXList: List[str],keepSpaces:bool=True,endian=False) -> str:
    temp = ''
    if type(HEXList) == list:
        if endian:
            HEXList.reverse()
        for x in HEXList:
            temp += x
            if keepSpaces:
                temp += ' '
    return temp

def str2hex(STR: str):
    return hexify(bytes(STR,'charmap'))

def hex2str(HEX) -> str:
    temp = ''
    if type(HEX) == str:
        if ' ' in HEX:
            temp = HEX.replace(' ','')
        else:
            temp = HEX
            pass
    elif type(HEX) == list:
        for x in HEX:
            temp += x
    return str(bytes.fromhex(temp).decode('charmap'))

def hexify(data: bytes, KeepSpaces: bool = True) -> str:
    "Hex (XX XX XX XX) representation of bytes"
    a = [b2a_hex(p.to_bytes(1,'little')).decode() for p in data]
    if KeepSpaces:
        return " ".join(a)
    else:
        return "".join(a)
    
def fileReader(path,fileName):
    if path[len(path)-1] == '/':
        fileBytes = open(path + fileName, mode='rb').read()
    else:
        fileBytes = open(path + '/' + fileName, mode='rb').read()
    return fileBytes

def fileWriter(pathing, name, data, overwrite=False):
    if not overwrite:
        try:
            open(pathing + '/' + name)
            fileName = name + '1'
        except:
            fileName = name
    else:
        fileName = name
    if not os.path.exists(pathing + '/' + fileName):
        try:
            print('writing')
            fi = open(pathing + '/' + fileName, 'wb')
            fi.write(data)
            fi.close()
        except PermissionError as err:
            print(err)
    else:
        print("File already exists")
    pass


oof={'TOON_UNIF_STAIN3d2_XVM_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN1_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'AlphaBlend', 'AlphaBlendType', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A'],
     'TOON_UNIF_EYE_MUT1_DFD': ['TexScrl0U', 'TexScrl0V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A'],
     'TOON_UNIF_DFD': ['MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'AlphaBlend', 'AlphaBlendType', 'MatOffset1X', 'MatOffset1Y', 'MatOffset1Z', 'MatOffset1W', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'TexScrl0U', 'TexScrl0V'],
     'TOON_UNIF_STAIN2_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatC'],
     'TOON_UNIF_STAIN3_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_EYE_MUT2_DFD': ['TexScrl0U', 'TexScrl0V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_EYE_MUT0_DFD': ['TexScrl0U', 'TexScrl0V', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A'],
     'TOON_UNIF_EYE_MUT1d3_DFD': ['TexScrl0U', 'TexScrl0V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W'],
     'TOON_UNIF_EYE_MUT3_DFD': ['TexScrl0U', 'TexScrl0V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_HAIR_DFD': ['MatOffset0X', 'MatOffset0Y', 'MatOffset0Z', 'MatOffset0W', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN2_DFDaa': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN3_DFDaa': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_ENV': ['MatOffset1X', 'MatOffset1Y', 'MatOffset1Z', 'MatOffset1W', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'AlphaBlend', 'AlphaBlendType'],
     'TOON0002_UNIF_STAIN2_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN2d2_XVM_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN3_DFDAth': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN2_DFDAth': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_ENV_ADD': ['MatOffset1X', 'MatOffset1Y', 'MatOffset1Z', 'MatOffset1W', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN1_DFDaa': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN1_MSK_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TOON_UNIF_STAIN3_DFD': ['SpcCoeff', 'SpcPower', 'RimCoeff', 'RimPower', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TEST_TOON_UNIF_DFD': ['SpcCoeff', 'SpcPower', 'RimCoeff', 'RimPower', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TOON_UNIF_ENV': ['ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff', 'SpcCoeff', 'SpcPower', 'RimCoeff', 'RimPower', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TOON_UNIF_EYE_MUT1_DFD': ['TexScrl0U', 'TexScrl0V', 'SpcCoeff', 'SpcPower', 'RimCoeff', 'RimPower', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TOON_UNIF_STAIN3_DFDaa': ['SpcCoeff', 'SpcPower', 'RimCoeff', 'RimPower', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_SIMPLIFIED': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A'],
     'TOON_DFD': ['gToonTextureWidth', 'gToonTextureHeight', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'gLightDir', 'gLightDif', 'gLightSpc', 'gLightAmb', 'ToonSamplerAddressU', 'ToonSamplerAddressV', 'MarkSamplerAddressU', 'MarkSamplerAddressV'],
     'TOON_STAIN1_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'AlphaBlend', 'AlphaBlendType'],
     'TOON_STAIN1_DFD_STN': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'MatOffset1X', 'MatOffset1Y', 'MatOffset1Z', 'MatOffset1W', 'BackFace'],
     'TOON_STAIN2_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'AlphaBlend', 'AlphaBlendType', 'Glare'],
     'TOON_ENV': ['MatOffset1X', 'MatOffset1Y', 'MatOffset1Z', 'MatOffset1W', 'ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'Glare'],
     'TOON_UNIF_STAIN3_MSK_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TOON_UNIF_HAIR_DFD': ['MatOffset0X', 'MatOffset0Y', 'MatOffset0Z', 'MatOffset0W', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_DECAL_DC': ['MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatOffset0X', 'MatOffset0Y', 'MatOffset0Z', 'MatOffset0W', 'MatOffset1X', 'MatOffset1Y', 'MatOffset1Z', 'MatOffset1W', 'Glare'],
     'TOON_UNIF_STAIN1_DFDAth': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'AlphaTest', 'NoEdge'],
     'TOON_UNIF_HAIR_DFDAth': ['MatOffset0X', 'MatOffset0Y', 'MatOffset0Z', 'MatOffset0W', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_HAIR_DFD': ['gToonTextureWidth', 'gToonTextureHeight', 'g_MaterialOffset0_VS'],
     'TOON_STAIN1_DFDaa': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON0002_UNIF_STAIN2d2_XVM_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TOON_UNIF_EYE_MUT2_DFD': ['TexScrl0U', 'TexScrl0V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_STAIN2d2_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TOON_UNIF_STAIN2_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'AGE_TOON_STAIN1_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare'],
     'TOON_UNIF_HAIR_DFD_STN': ['MatOffset0X', 'MatOffset0Y', 'MatOffset0Z', 'MatOffset0W', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'MatOffset1X', 'MatOffset1Y', 'MatOffset1Z', 'MatOffset1W', 'BackFace', 'Glare'],
     'TOON_UNIF_STAIN1d2_XVM_DFD': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'Glare', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A'],
     'ParticleDecal': ['GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask', 'Glare', 'BackFace', 'LowRez', 'LowRezSmoke', 'AlphaTest'],
     'T1_VFX_TRC_RI': ['MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'IncidencePower', 'IncidenceAlphaBias', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'CustomFlag', 'Glare'],
     'T1_VFX_MTN': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'IncidencePower', 'IncidenceAlphaBias', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'Glare', 'LowRez', 'AnimationChannel', 'TwoSidedRender', 'AlphaSortMask', 'LowRezSmoke', 'AlphaTest', 'Billboard', 'BillboardType'],
     'T1_VFX_MTN_DIS_ALPHA': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'IncidencePower', 'IncidenceAlphaBias', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'Glare', 'LowRez', 'AnimationChannel', 'LowRezSmoke', 'TwoSidedRender'],
     'DecalColor': ['AlphaBlend', 'AlphaBlendType', 'ZWriteMask', 'BackFace', 'LowRez'],
     'T1_VFX_PRLX_MTN': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'IncidencePower', 'IncidenceAlphaBias', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask', 'Glare', 'LowRez', 'AnimationChannel'],
     'ScreenRefractAdjust': ['GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'LowRez'],
     'SoftParticleDecal': ['GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'MatOffset0X', 'MatOffset0Y', 'MatOffset0Z', 'MatOffset0W', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask', 'BackFace', 'Glare', 'LowRez', 'LowRezSmoke'],
     'U2_MUV_L_SM_S': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'GLASS': ['ReflectCoeff', 'ReflectFresnelBias', 'ReflectFresnelCoeff', 'AlphaBlend', 'AlphaBlendType'],
     'U2_MUV_L_SM': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'T1_ScrollShimmerBias': ['TexScrl0U', 'TexScrl0V', 'MipMapLod0', 'Glare', 'CustomFlag'],
     'T1_Scroll': ['TexScrl0U', 'TexScrl0V', 'MipMapLod0', 'AlphaBlend', 'AlphaBlendType', 'Glare', 'BackFace', 'TwoSidedRender', 'ZWriteMask', 'NoEdge'],
     'U2_MUV_BUMP_SM': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'T1_VFX_PRLX_MTN_DIS_ALPHA': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'IncidencePower', 'IncidenceAlphaBias', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask', 'LowRez', 'AnimationChannel', 'Glare'],
     'T2_MUV_STKR_Scrl_NF': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'T1_Scroll_Emission_NoFog': ['TexScrl0U', 'TexScrl0V', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask', 'Glare'],
     'U3spua_BM_BUMP_SM': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'U3_BM_BUMP_SM_DYN': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'U3spua_BM_SM': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'MipMapLod1', 'Glare', 'TextureFilter0', 'TextureFilter2'],
     'U3_SUV_SM_ALPHA_BLEND_S': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2', 'Glare'],
     'U3spua_BM_SM_S': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2', 'Glare'],
     'U3_MUV_SM_BLEND': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2'],
     'U3_SUV_SM_BLEND': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'TextureFilter0', 'TextureFilter2'],
     'U3_BM': [],'T1_C_NoFog_PT': ['AlphaTest'],
     'U2_SUV_SM_BLEND_MOD_S': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'U2_SUV_SM_BLEND_S': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'VdotN_Alpha': ['TexScrl0U', 'TexScrl0V', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask'],
     'T1_S': ['AlphaTest', 'BackFace'],
     'GI_GrassSimulation_L_S': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'AlphaTest', 'BackFace', 'CustomFlag'],
     'T1_BUMP_SM_DYN_MTN_S': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'T1_SM_DYN_MTN_S': ['MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'TexScrl0U', 'TexScrl0V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'T1_BUMP_SM_DYN_S': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'U3spua_BM_BUMP_SM_DYN_S': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'ParticleDecalPT': ['GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaTest', 'AlphaBlend', 'AlphaBlendType', 'Glare', 'ZWriteMask'],
     'T1_VFX_MTN_W_DIS_ALPHA': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'IncidencePower', 'IncidenceAlphaBias', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'Glare', 'LowRez', 'AnimationChannel'],
     'T1_VFX_MTN_PT_DIS_ALPHA': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'IncidencePower', 'IncidenceAlphaBias', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaTest', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'Glare', 'LowRez', 'AnimationChannel'],
     'T1_VFX_MTN_REFRACT': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'CustomFlag', 'AnimationChannel'],
     'TOON_UNIFfx_VFX_DFDna_FCM': ['MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'MatScale1X', 'MatScale1Y', 'MatScale1Z', 'MatScale1W'],
     'T1_VFX_TRC_I': ['IncidencePower', 'IncidenceAlphaBias', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'Glare'],
     'ParticleRandomColor': [],'T1_VFX': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'MatCol2R', 'MatCol2G', 'MatCol2B', 'MatCol2A', 'MatCol3R', 'MatCol3G', 'MatCol3B', 'MatCol3A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'FadeInit', 'FadeSpeed', 'IncidencePower', 'IncidenceAlphaBias', 'GradientInit', 'GradientSpeed', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'ZWriteMask', 'Glare'],
     'ParticleRefract': ['MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask', 'LowRez'],
     'ShadowModelAlphaKill': ['BackFace', 'CustomFlag'],
     'SHADOWMAP_ALPHAKILL': ['BackFace', 'CustomFlag'],
     'T1_VFX_MTN_REFRACT_ADJUST_DA': ['TexScrl0U', 'TexScrl0V', 'TexScrl1U', 'TexScrl1V', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatCol1R', 'MatCol1G', 'MatCol1B', 'MatCol1A', 'VsFlag0', 'VsFlag1', 'VsFlag2', 'VsFlag3', 'GlareColR', 'GlareColG', 'GlareColB', 'GlareColA', 'AlphaBlend', 'AlphaBlendType', 'BackFace', 'TwoSidedRender', 'ZWriteMask', 'LowRez', 'AnimationChannel'],
     'T1_C_Scroll_Emission': ['TexScrl0U', 'TexScrl0V', 'MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'Glare', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask'],
     'T1_SM_DYN_S': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'T2_MUV_L_SM': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'T2_MUV_C_L_SM': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'Glare'],
     'T1': [],'T1_L_PT': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask'],
     'T2_MUV_C': [],'T1_Emission_NoFog': ['MatScale0X', 'MatScale0Y', 'MatScale0Z', 'MatScale0W', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask', 'Glare'],
     'T1_C_Scroll': ['TexScrl0U', 'TexScrl0V', 'AlphaBlend', 'AlphaBlendType', 'ZWriteMask'],
     'T1_BUMP_SM_DYN_MTN': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'T1_BUMP_SM_DYN': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'T2_MUV_BUMP_SM_BLEND_DYN_MTN_S': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower', 'MatCol0R', 'MatCol0G', 'MatCol0B', 'MatCol0A'],
     'T2_MUV_BUMP_SM_BLEND_DYN_S': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'GI_T1_BUMP_SM_DYN': ['MatAmbR', 'MatAmbG', 'MatAmbB', 'MatAmbScale', 'MatDifR', 'MatDifG', 'MatDifB', 'MatDifScale', 'MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower'],
     'GI_T1_L_SM_S': ['MatSpcR', 'MatSpcG', 'MatSpcB', 'SpcCoeff', 'SpcPower']}

