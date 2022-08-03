import bpy
from typing import List
from .EMBPacking import Write_EMB
import os

class dds_prep:
	@classmethod
	def temporary_method(cls):
		print('OPERATOR PROCESSED')
		pass

	@classmethod
	def new_gather_dds(cls, TBH=None):
		print("##GATHERING IMAGES##")
		dds_list = []  # List of images to append to and return
		
		return dds_list
	
	#@classmethod
	#def new_gather_dds(cls, TBD = None):
	#	print("##GATHERING IMAGES##")
	#	dds_list = []		#List of images to append to and return
	#	
	#	
	#	return dds_list

	@classmethod
	def gather_meshes(cls, context):
		print("GATHERING MESHES")
		meshes = []
		if context.object['Xeno_Properties']['XenoState'] == 'XenoSubmesh':
			meshes.extend(context.object['Xeno_Properties']['Parent']['Xeno_Properties']['Parent'].objects)
			for child in context.object['Xeno_Properties']['Parent']['Xeno_Properties']['Parent'].children:
				meshes.extend(child.objects)
		elif context.object['Xeno_Properties']['XenoState'] == 'XenoMeshGroup':
			meshes.extend(context.object['Xeno_Properties']['Parent'].objects)
			for child in context.object['Xeno_Properties']['Parent'].children:
				meshes.extend(child.objects)
		else:
			meshes = [context.object]
		meshes = [mesh.data for mesh in meshes]
		return meshes

	@classmethod
	def gather_mats(cls, meshList):
		print("GATHERING MATERIALS")
		materials = []
		for item in meshList:
			materials.extend(item.materials)
		return materials

	@classmethod
	def gather_dds(cls, current_material):
		print("GATHERING IMAGES")
		DYT_List = []
		Detail_List = []
		FinalFileName = None
		tempDict = {} #stores node name as key and image as value
		for node in current_material.node_tree.nodes:
			if node.type=='TEX_IMAGE':
				tempDict.__setitem__(node.name, node.image)
		if "DYT" in current_material.name:
			DYT_List = [tempDict[item].name[:tempDict[item].name.index('.dds')+4]
						for item in sorted(tempDict)]
		elif "EMB" in current_material.name:
			Detail_List = [tempDict[item].name[:tempDict[item].name.index('.dds')+4]
						   for item in sorted(tempDict)]
		
		#[print(item+" : "+str(tempDict[item])) for item in tempDict.keys()]
		for item in [node.image for node in current_material.node_tree.nodes if node.type=='TEX_IMAGE']:
			if ".dyt" in item.name and ".dds" in item.name:
				if item not in DYT_List:
					item.unpack(method='WRITE_ORIGINAL')
					item.pack()
			elif ".dds" in item.name:
				if item not in Detail_List:
					item.unpack(method='WRITE_ORIGINAL')
					item.pack()
			if FinalFileName is None:
				FinalFileName = item.name[:item.name.index('_._')]
		return [FinalFileName, DYT_List, Detail_List]

def packing_emb(context, direct, pack_this):
	XIR_Directory = str(os.getcwd()).replace('\\','/') \
					+'/2.92/scripts/addons/XenoverseIR/temp_dds_storage'
	print(pack_this)
	exportImageList = [img.image.name for img in pack_this.images]
	for img in pack_this.images:
		img.image.unpack(method="WRITE_ORIGINAL")
		img.image.pack()
	Write_EMB(Location=str(direct)[:str(direct).rindex('\\') + 1],
			  EMBName=pack_this.name,
			  DDSImages=[open(XIR_Directory + '/' + dds, 'rb').read() for dds in exportImageList],
			  DYT=False)
			
	
def packing_dyt(context, direct, pack_this):
	XIR_Directory = str(os.getcwd()).replace('\\','/') \
					+'/2.92/scripts/addons/XenoverseIR/temp_dds_storage'

	print(pack_this)
	exportImageList = [img.image.name for img in pack_this.images]
	for img in pack_this.images:
		img.image.unpack(method="WRITE_ORIGINAL")
		img.image.pack()
	Write_EMB(Location=str(direct)[:str(direct).rindex('\\') + 1],
			  EMBName=pack_this.name,
			  DDSImages=[open(XIR_Directory + '/' + dds, 'rb').read() for dds in exportImageList],
			  DYT=True)
