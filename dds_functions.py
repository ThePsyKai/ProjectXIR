from typing import *

from . import PIL_Installer
PIL_Installer.install_Pillow()
from PIL import Image
import bpy
import numpy as np
import os
from .node_templates import Parameter

import math


def generate_color_ramps(filepath):
	###bpy.data.materials[bpy.context.object.material_slots[0].name].node_tree.nodes.new('ShaderNodeValToRGB')
	#bpy.data.materials[**Material Name**].node_tree.nodes[**Node Index**].color_ramp.elements[**Color Key**].color[0]	R
	#bpy.data.materials[**Material Name**].node_tree.nodes[**Node Index**].color_ramp.elements[**Color Key**].color[1]	G
	#bpy.data.materials[**Material Name**].node_tree.nodes[**Node Index**].color_ramp.elements[**Color Key**].color[2]	B
	#bpy.data.materials[**Material Name**].node_tree.nodes[**Node Index**].color_ramp.elements[**Color Key**].color[3]	A
	pass


#bpy.ops.node.add_node(type="ShaderNodeValToRGB", use_transform=True)

def srgb_to_linearrgb(c):
	if c < 0:
		return 0
	elif c < 0.04045:
		return c / 12.92
	else:
		return ((c + 0.055) / 1.055) ** 2.4
def hex_to_rgb(h, alpha=1):
	r = (h & 0xff0000) >> 16
	g = (h & 0x00ff00) >> 8
	b = (h & 0x0000ff)
	return tuple([srgb_to_linearrgb(c / 0xff) for c in (r, g, b)] + [alpha])

def generate_ramp_node(nodeNumber, material_slot, startFrom:int):
	newRamp = bpy.data.materials[bpy.context.object.material_slots[0].name].node_tree.nodes.new('ShaderNodeValToRGB')
	newRamp.name = "XenoRamp_%s" % nodeNumber
	for currentItem in range(startFrom,128):
		try:
			newRamp.color_ramp.elements.new(currentItem*(1/128))
			newRamp.color_ramp.elements[-1].color[0] = 0.0
			newRamp.color_ramp.elements[-1].color[1] = 0.0
			newRamp.color_ramp.elements[-1].color[2] = 0.0
			newRamp.color_ramp.elements[-1].color[3] = 1.0
		except RuntimeError:
			pass
	return newRamp


class Color_Ramp:
	def __init__(self, rampName):
		self.color_tags = []  #type: List[Color_Tag]
		self.name = rampName
		
	def add_tag(self, pix, ind):
		newTag = Color_Tag(pix, ind)
		self.color_tags.append(newTag)
		del newTag

class Color_Tag:
	def __init__(self, pixel, pixel_ind: int):
		self.hexColor = "".join(['0' * (2 - len(hex(val)[2:])) + hex(val)[2:] for val in pixel][:3])
		#print(self.hexColor)
		self.RGBVal = pixel
		self.colorRGB = hex_to_rgb(int(self.hexColor, 16))
		self.alphaVal = pixel[-1] / 255
		self.position = pixel_ind * (1 / 128) if pixel_ind != 128 else 1.0

class ColorOption:
	def __init__(self):
		self.color 	= Color_Ramp("COLOR")
		self.rim	= Color_Ramp("RIM")
		self.shine	= Color_Ramp("SHINE")
		self.fourth	= Color_Ramp("FOURTH")

def read_pixel_row(ARRAY, ACTIVE_OPTION, line_Ind, diff=None):
	Active = ACTIVE_OPTION
	ind_keys = ["color", "rim", "shine", "fourth"]
	#print("CURRENT ",ind_keys[line_Ind])
	#print(len(ARRAY))
	#print(line_Ind)
	Ramp = eval("Active.%s" % ind_keys[line_Ind])
	#print()
	
	line1 = [pix for pix in ARRAY[line_Ind*4]]
	print("LENGTH OF LINE 1:",len(line1))
	
	if diff is None:
		diff_limit = 5
	else:
		diff_limit = diff
	print("PIXEL DIFFERENCE:",diff_limit)
	#print()
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
					print("PRIOR PIXEL PASS & PRIOR DIFF IS NONE:", prior_pixel, itm - 1)
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
	print("### COLOR LIST LENGTH",len(Ramp.color_tags))
	return Ramp

def apply_ramp(node, RPL):
	for tagInd in range(0, len(RPL.color_tags)):
		if not tagInd:
			node.color_ramp.elements[0].position = RPL.color_tags[tagInd].position
			node.color_ramp.elements[0].color[0] = RPL.color_tags[tagInd].colorRGB[0]
			node.color_ramp.elements[0].color[1] = RPL.color_tags[tagInd].colorRGB[1]
			node.color_ramp.elements[0].color[2] = RPL.color_tags[tagInd].colorRGB[2]
			node.color_ramp.elements[0].color[3] = RPL.color_tags[tagInd].alphaVal
		elif tagInd != len(RPL.color_tags) - 1:
			newElement = node.color_ramp.elements.new(RPL.color_tags[tagInd].position)
			newElement.color[0] = RPL.color_tags[tagInd].colorRGB[0]
			newElement.color[1] = RPL.color_tags[tagInd].colorRGB[1]
			newElement.color[2] = RPL.color_tags[tagInd].colorRGB[2]
			newElement.color[3] = RPL.color_tags[tagInd].alphaVal

def read_dyt(MaterialName, FileAndPath, file_name, current_Y):
	#print(os.path.exists(FileAndPath))
	curImg = Image.open(FileAndPath)
	Array = np.asarray(curImg)
	ind_keys = ["color", "rim", "shine", "fourth"]
	curX = 0
	curSectID = 0
	for rmp in range(0, len(Array), 16):
		newOption = ColorOption()	#creates new Color Ramp section object
		newPara = Parameter.new("DYT_Ramps", bpy.data.materials[MaterialName].node_tree, True)	#creates new Parameter Node for DYT Ramps
		newPara.frame.label = FileAndPath[FileAndPath.rindex("_._")+3:]+" "+"0"*(3-len(str(curSectID)))+str(curSectID)
		newPara.frame.location = (curX,current_Y)
		curArray = Array[rmp:rmp+16]
		for row in range(0, 4):
			print()
			rampPixelList = read_pixel_row(curArray, newOption, line_Ind=row)
			test_len = len(rampPixelList.color_tags)
			#print("TAG LIST LENGTH:",test_len)
			altered_difference = 6
			if len(rampPixelList.color_tags) > 31:
				while True:
					print("DIFFERENCE",altered_difference)
					if altered_difference == 255:
						print("ERROR: DIFFERENCE EXCEEDED")
						break
						
					#print(len(curArray))
					#print(newOption)
					#print(row)
					#print(altered_difference)
					rampPixelList = read_pixel_row(curArray, newOption, line_Ind=row, diff=altered_difference)
					print("New TAG LIST LENGTH", len(rampPixelList.color_tags))
					if test_len < len(rampPixelList.color_tags):
						print("ERROR: PIXEL LIST INCREASE")
						break
					if len(rampPixelList.color_tags) <= 31:
						break
					else:
						altered_difference+=1
						
			ramp_Node = newPara.nodes["ramp%s" % (row+1)]
			
			apply_ramp(node=ramp_Node, RPL=rampPixelList)
			
		curX+=300
		curSectID+=1
	
