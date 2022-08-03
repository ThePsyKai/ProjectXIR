from pathlib import Path
from typing import BinaryIO, Iterable, Sized, Union
import os

from .fileUtil import *
#from .emb_file_obj import EMB
from .emm_file_obj import EMM, mat_paras
from .emb_reader import Reader
from .custom_error_reporter import XIR_ERROR_REPORT
from . import dds_functions

from .material_node_arrangement import arrange

import bpy
import bmesh
import numpy as np
from mathutils import Vector, Matrix, Euler
from math import *

class new_color_ramp:
    def __init__(self):
        self.color_tags = []  #type: List[Color_Tag]

    def add_tag(self, pix, ind):
        newTag = Color_Tag(pix, ind)
        self.color_tags.append(newTag)
        
class Color_Tag:
    def __init__(self, pixel, pixel_ind: int):
        self.hexColor = ['0' * (2 - len(hex(val)[2:])) + hex(val)[2:] for val in pixel][:3]
        self.colorRGB = [val for val in pixel][:3]
        self.alphaVal = pixel[-1] / 255
        self.position = pixel_ind * (1 / 128) if pixel_ind != 128 else 1.0
        
        
def read_pixel_row(ARRAY, PIXELROW):
    line1, line2, line3, line4 = [], [], [], []
    Ramp = new_color_ramp()
    for pxl in range(0, len(ARRAY[PIXELROW])):
        line1.append(ARRAY[PIXELROW + 0][pxl])
        line2.append(ARRAY[PIXELROW + 1][pxl])
        line3.append(ARRAY[PIXELROW + 2][pxl])
        line4.append(ARRAY[PIXELROW + 3][pxl])
        
    diff_limit = 3
    prior_pixel = None
    prior_diff = None
    for itm in range(0, len(line1)):
        if prior_pixel is not None:
            difference = [abs(int(prior_pixel[item1]) - int(line1[itm][item1])) 
                          for item1 in range(0, 4)]
            if difference != [0, 0, 0, 0] \
                    and difference != prior_diff \
                    or prior_diff is None:
                if prior_diff is None:
                    Ramp.add_tag(prior_pixel, itm - 1)
                if difference[0] > diff_limit or difference[1] > diff_limit \
                        or difference[2] > diff_limit or difference[3] > diff_limit:
                    Ramp.add_tag(prior_pixel, itm - 1)
                    pass
                pass
            prior_diff = difference
            pass
        prior_pixel = line1[itm]
        pass
    Ramp.add_tag(line1[len(line1) - 1], len(line1) - 1)

    #for tag in Ramp.color_tags:
    #    print("".join(tag.hexColor), "\t", tag.alphaVal, "\t", tag.position)
    
    return Ramp
    

def import_image(image_file: BinaryIO, imageType:str = None, file_directory=None, file_name=None, NewDYTMethod=False):
    print(file_directory)
    print('THE FILE NAME IN QUESTION:', file_name)
    XIR_Directory = str(os.getcwd()).replace('\\','/')\
                    + '\\2.92\\scripts\\addons\\XenoverseIR\\temp_dds_storage'.replace('\\','/')
    emb_images = Reader(image_file.read(), XIR_Directory) #0 = Image Path  1 = Image Name  2 = file data
    Users = None
    DYTUser = False
    print(imageType)
    MatName = None
    curMat = None
    if imageType.lower() == 'dyt':
        CoreDYTUser = bpy.context.scene.Fake_DYTs.add()
        CoreDYTUser.name = file_name[:file_name.index(".dyt.emb")]
        Users = CoreDYTUser
        DYTUser = "DYTFake_" + file_name[:file_name.index(".dyt.emb")]
        
        if NewDYTMethod:
            MatName = "DYT Ramps for " + file_name
            curMat = bpy.data.materials.new(MatName)
            curMat.use_nodes = True
    elif imageType.lower() == 'emb':
        CoreEMBUser = bpy.context.scene.Fake_EMBs.add()
        CoreEMBUser.name = file_name[:file_name.index(".emb")]
        Users = CoreEMBUser
    else:
        XIR_ERROR_REPORT("Xenoverse",
                         "Unrecognized/Unsupported File Type",
                         "Please only Import Registered Image Types")
    Users.image_count = 0
    for image in emb_images:
        if DYTUser:
            image[1] = file_name[:file_name.index(".dyt.emb")] + '_._' + image[1][:-4] + '.dyt.dds'
        else:
            image[1] = file_name[:file_name.index(".emb")] + "_._" + image[1]
            
        with open(image[0] + '/' + image[1], 'wb') as fi:
            fi.write(image[2])
        curImg = bpy.data.images.load(image[0] + '/' + image[1])
        
        if DYTUser:
            #print("DYT Image Length: ", end=
            if NewDYTMethod:
                curY = 0
                for item in emb_images:
                    try:
                        dds_functions.read_dyt(MatName, XIR_Directory + "/" + item[1], file_name, curY)
                    except FileNotFoundError:
                        pass
                    except RuntimeError as err:
                        print(err)
                        #bpy.data.materials.remove(curMat)
                    curY-=930.0

                
            img = Users.images.add()
            img.name = curImg.name[curImg.name.index("DATA"):]
            img.image = bpy.data.images[curImg.name]
            img.dyt_index = emb_images.index(image)
        else:
            # print("DYT Image Length: ", end='')
            img = Users.images.add()
            img.name = curImg.name[curImg.name.index("DATA"):]
            img.image = bpy.data.images[curImg.name]
            img.emb_index = emb_images.index(image)
            
        curImg.pack()
        os.remove(image[0] + '/' + image[1])
        Users.image_count += 1




def import_static_material(emm_file: BinaryIO, file_directory=None, file_name=None, IEMB=False, IDYT=False):
    #import .parameter_types
    from .node_templates import Parameter
    #print(file_name)
    fileHex = hexify(emm_file.read()).split(' ')
    emm = EMM(fileHex)
    for mat in emm.materials:
        NewMat = bpy.data.materials.new(mat.name)
        NewMat.use_nodes = True
        tree = NewMat.node_tree
        tree.nodes.remove(tree.nodes['Principled BSDF'])
        tree.nodes['Material Output'].label = mat.shaderProgName

        paramets = {}
        completed_parameters = ['MatCol0',
                                'MatCol1',
                                'MatCol2',
                                'MatCol3',
                                'TexScrl0',
                                'MatScale0',
                                'MatScale1',]
        master_loc = [300.0,160.00]
        for param in mat.parameters:
            if param.name[-1] in ['R','G','B','A','X','Y','Z','W','U','V'] and param.name[:-1] in completed_parameters:
                if param.name[:-1] not in paramets.keys():
                    print("////////////////////")
                    print("RGBAXYZWUV PARAM CREATION")
                    newParam = Parameter.new(parameter_type=param.name[:-1], material=NewMat, Import=True)
                    paramets.__setitem__(param.name[:-1],newParam)
                    paramets[param.name[:-1]].inputs[param.name[-1]].default_value = param.value
                    print("////////////////////")
                else:
                    paramets[param.name[:-1]].inputs[param.name[-1]].default_value = param.value
            else:
                newNode = tree.nodes.new('ShaderNodeValue')
                newNode.label = param.name
                newNode.outputs[0].default_value = param.value
                newNode.location = tuple(master_loc)
                master_loc[1] -= 80

        LineWork = Parameter.new(parameter_type='Line_Work_Image', material=NewMat, Import=True)
        if IEMB:
            image_int = 0
            ImageNodes = [item for item in tree.nodes if 'LineWork_This' in item.name]
            for item in ImageNodes:
                print(file_name, 'DATA'+ '0'*(3-len(str(image_int))) + str(image_int) + '.dds')
                item.image = bpy.data.images[file_name[:-4]+'_._'+
                    'DATA'+
                    '0'*(3-len(str(image_int))) + str(image_int)
                    +'.dds']
                image_int+=1

        DYT = Parameter.new(parameter_type='DYT_Image', material=NewMat, Import=True)
        if IDYT:
            image_int = 0
            ImageNodes = [item for item in tree.nodes if ('DYT_1' in item.name or 
                                                          'DYT_2' in item.name or
                                                          'DYT_3' in item.name)]
            for item in ImageNodes:
                print(file_name, 'DATA' + '0' * (3 - len(str(image_int))) + str(image_int) + '.dyt.dds')
                item.image = bpy.data.images[file_name[:-4] + '_._' +
                    'DATA' +
                    '0' * (3 - len(str(image_int))) + str(image_int)
                    + '.dyt.dds']

        print("////////////////////")
        print("MatCol_Plus_DYT PARAM CREATION")
        FinalMix = Parameter.new(parameter_type='MatCol_Plus_DYT', material=NewMat, Import=True)
        tree.links.new(tree.nodes['Material Output'].inputs[0], FinalMix.outputs[0])
        print("////////////////////")
        
        if 'MatCol' in [par[:-1] for par in paramets.keys()]:
            print("////////////////////")
            print("Combine_MatCol_ShadeVer PARAM CREATION")
            CombineMatCol = Parameter.new(parameter_type='Combine_MatCol_ShadeVer', material=NewMat, Import=True)
            tree.links.new(FinalMix.inputs[0], CombineMatCol.outputs[0])
            tree.links.new(FinalMix.inputs[1], CombineMatCol.outputs[1])
            print("////////////////////")
            if 'MatCol0' in paramets.keys():
                tree.links.new(paramets['MatCol0'].inputs[0], LineWork.outputs[1])
                tree.links.new(CombineMatCol.inputs[0], paramets['MatCol0'].outputs[0])
                tree.links.new(CombineMatCol.inputs[1], paramets['MatCol0'].outputs[1])

            if 'MatCol1' in paramets.keys():
                tree.links.new(paramets['MatCol1'].inputs[0], LineWork.outputs[2])
                tree.links.new(CombineMatCol.inputs[2], paramets['MatCol1'].outputs[0])
                tree.links.new(CombineMatCol.inputs[3], paramets['MatCol1'].outputs[1])

            if 'MatCol2' in paramets.keys():
                tree.links.new(paramets['MatCol2'].inputs[0], LineWork.outputs[3])
                tree.links.new(CombineMatCol.inputs[4], paramets['MatCol2'].outputs[0])
                tree.links.new(CombineMatCol.inputs[5], paramets['MatCol2'].outputs[1])

            if 'MatCol3' in paramets.keys():
                tree.links.new(paramets['MatCol3'].inputs[0], LineWork.outputs[4])
                tree.links.new(CombineMatCol.inputs[6], paramets['MatCol3'].outputs[0])
                tree.links.new(CombineMatCol.inputs[7], paramets['MatCol3'].outputs[1])

        if 'TexScrl0' in paramets.keys():
            tree.links.new(LineWork.inputs[0], paramets['TexScrl0'].outputs[0])
            pass

        if 'MatScale' in [par[:-1] for par in paramets.keys()]:
            print("////////////////////")
            print("DYT Assigner PARAM CREATION")
            AssignDYT = Parameter.new(parameter_type='DYT_Strip_Assigner', material=NewMat, Import=True)
            print("////////////////////")
            print("////////////////////")
            print("Merge DYT PARAM CREATION")
            MergeDYT = Parameter.new(parameter_type='Merge_DYT', material=NewMat, Import=True)
            print("////////////////////")
            print("////////////////////")
            print("Lighting PARAM CREATION")
            Light = Parameter.new(parameter_type='Lighting', material=NewMat, Import=True)
            tree.links.new(FinalMix.inputs[2], MergeDYT.outputs[0])
            print("////////////////////")

            tree.links.new(DYT.inputs[0], AssignDYT.outputs[0])
            tree.links.new(DYT.inputs[1], AssignDYT.outputs[1])
            tree.links.new(DYT.inputs[2], AssignDYT.outputs[2])
            tree.links.new(MergeDYT.inputs[0], DYT.outputs[0])
            tree.links.new(MergeDYT.inputs[1], DYT.outputs[2])
            tree.links.new(MergeDYT.inputs[2], DYT.outputs[4])
            tree.links.new(AssignDYT.inputs[0], Light.outputs[0])

            if 'MatScale0' in paramets.keys():
                pass
            if 'MatScale1' in paramets.keys():
                tree.links.new(AssignDYT.inputs[1], paramets['MatScale1'].outputs[0])
    pass
