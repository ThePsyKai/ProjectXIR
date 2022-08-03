from .fileUtil import *
import numpy as np

class globalVals:
    Full_Hex = None


class EmdModel:
    """
	This is the model from the file as a whole
	"""

    def __init__(self):
        self.name = None
        self.groups = []  #type: List[EmdGroup]     #"Model" section list

class EmdGroup:
    """
	EMD Group is what is refered to as a 'Model' and consists of 'Submeshes'
	"""

    def __init__(self, group_name):
        self.name = group_name
        print(self.name)
        self.meshes = []            # type: List[EmdMesh]
        print(self.meshes)
        self.meshCount = 0
        print(self.meshCount)

        self.subMeshes = []
        print(self.subMeshes)

class EmdMesh:
    """
	EMDMesh is effectively what is refered to as the 'Submesh'"""

    def __init__(self):
        self.MeshName = ''  #type: str								        #Name of mesh
        self.vertices = []  #type: List[EMDVertex]					        #
        self.faces = []  #type: List[np.uint32]					            #
        self.edges = []  #type: List[Set[int,int]]				            #
        self.UVs = []  #type: List[Set[float,float]]			            #
        self.normals = []  #type: List[Set[float,float,float]]		        #

        self.vertex_group_names = []  #type: List[str]					    #
        self.vertex_groups = {}  #type: Dict[('*VGName*',List[Vertex])]	    #

        self.texture_define = []                                            #Mesh's EMB Texture Index

        self.color_ramp = None  #type:									    #
        self.details = None  #type:									        #
        self.average_center = []  #type: List[float,float,float]			#

    def create_edges(self, faceList):
        edgeList = []
        for i in faceList:
            edgeList.append(tuple((i[0], i[1])))
            edgeList.append(tuple((i[0], i[2])))
            edgeList.append(tuple((i[1], i[2])))
        self.edges = edgeList
class Vertex:
    """
	Self explainatory, the vertices of a mesh"""

    def __init__(self):
        self.location = [0.0, 0.0, 0.0]  ##type: List[float,float,float]
        self.normal = [0.0, 0.0, 0.0]  ##type: List[float,float,float]
        self.weight = 0.0  ##type: float
        self.UV = [0.0, 0.0]  ##type: List[float,float]
        self.vertex_groups = {}  ##type: {'VGName 1': float,'VGName 2': float,'VGName 3': float,'VGName 4': float}
        self.boneGroup = 0
        
class EMD:
    """
	The EMD's byte sections together as one object
	"""

    def __init__(self, Hexadecimal):
        globalVals.Full_Hex = "".join(Hexadecimal)
        self.Header = EMD_Header(Hexadecimal)
        self.Section = EMD_Section(Hexadecimal)
        self.Models = [Model_Section(Hexadecimal[
                                     self.Section.mod_pointers[ind]:],
                                     self.Section.mod_names[ind])
                       for ind in range(0, self.Section.number_models)]
        self.Meshes = [ind.Meshes for ind in self.Models]
        self.SubMeshes = [[ind.SubMeshes for ind in mes] for mes in self.Meshes]
        #for mes in self.Meshes:
        #    SubList = [ind.SubMeshes for ind in mes]
        #    self.SubMeshes.append(SubList)
        self.TextureDefs = {}
        for mesh in self.SubMeshes:
            for sub in mesh:
                for tex in sub:
                    self.TextureDefs.__setitem__(tex.name, tex.TextureDefs)
        self.Triangles = [[[ind2.Triangles for ind2 in ind] for ind in sub] for sub in self.SubMeshes]
        print(self.Triangles)
        #for sub in self.SubMeshes:
        #    TriList = [[ind2.Triangles for ind2 in ind] for ind in sub]
        #    self.Triangles.append(TriList)
        self.Vertices = [[[ind2.Verts for ind2 in ind] for ind in sub] for sub in self.SubMeshes]
        print(self.Vertices)
        #for sub in self.SubMeshes:
        #    VertList = [[ind2.Verts for ind2 in ind] for ind in sub]
        #    self.Vertices.append(VertList)

class NewEMD:
    def __init__(self, EMD_Hex):
        globalVals.Full_Hex = "".join(EMD_Hex)
        self.Header         = EMD_Header(EMD_Hex)
        self.Section        = EMD_Section(EMD_Hex)
        self.Models         = [Model_Section(EMD_Hex[self.Section.mod_pointers[ind]:], self.Section.mod_names[ind]) for ind in range(0, self.Section.number_models)]
    pass

class EMD_Header:
    """
	EMD File Header
	"""
    def __init__(self, hexList):
        #╔═4 characters to confirm the file type═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.signature = hex2str(hexList[0x00:0x04])
        #╔═Number to determine the endian type (big or little)═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.endian = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x04:0x06], keepSpaces=False)), np.uint16)
        #╔═Size of Header═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.header_size = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x06:0x08], keepSpaces=False)), np.uint16)
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.version = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x08:0x0c], keepSpaces=False)), np.uint8)
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x0c:0x10], keepSpaces=False)), np.uint32)       
    pass
class EMD_Section:
    """
	Section right after the header, contains data about all 'models'(main meshes) in the model
	"""
    def __init__(self, hexList):
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x10:0x12], keepSpaces=False)), np.uint16)[0]
        #╔═Number of Models in EMD═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.number_models = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x12:0x14], keepSpaces=False)), np.uint16)[0]
        #╔═Offset for Model Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_models = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x14:0x18], keepSpaces=False)), np.uint32)[0]
        #╔═Offset for Model Names═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_models_name = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x18:0x1c], keepSpaces=False)), np.uint32)[0]
        #╔═Model Name Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.name_pointers = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[self.offset_models_name:self.offset_models_name + (4 * self.number_models)], keepSpaces=False)), np.uint32)
        #╔═Model Names═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.mod_names = self.get_names(hexList, self.name_pointers)
        #╔═Model Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.mod_pointers = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[self.offset_models:self.offset_models + (4 * self.number_models)], keepSpaces=False)), np.uint32)

    def get_names(self, hList, NamePointers):
        names = []
        for NameOffset in NamePointers:
            decodeThis = ''.join(hList[NameOffset:NameOffset + hList[NameOffset:].index('00')])
            names.append(str(bytes.fromhex(decodeThis).decode('charmap')))
        return names
    pass
class Model_Section:
    """"""
    def __init__(self, hexList, Name=None):
        #╔═Model Name═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓ ║#
        self.name = Name
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x00:0x02], keepSpaces=False)), np.uint16)[0]
        #╔═Number of Meshes═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.number_meshs = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x02:0x04], keepSpaces=False)), np.uint16)[0]
        #╔═Offset Mesh Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_meshs = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x04:0x08], keepSpaces=False)), np.uint32)[0]
        #╔═Mesh Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.mes_pointers = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[self.offset_meshs:self.offset_meshs + (4 * self.number_meshs)], keepSpaces=False)), np.uint32)
        #╔═Hex Arrays for Meshes═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.meshHexes = self.get_MeshHexes(hexList, self.mes_pointers)
        #╔═Collection of EMD Mesh Objects═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.Meshes = [Mesh_Section(mHex) for mHex in self.meshHexes]
        
    def get_MeshHexes(self, hList, pointers):
        ReturnMeshes = []
        for point in range(0, len(pointers)):
            if point + 1 < len(pointers):
                ReturnMeshes.append(hList[pointers[point]:pointers[point + 1]][:-1])
            else:
                ReturnMeshes.append(hList[pointers[point]:][:-1])
        return ReturnMeshes
    pass
class Mesh_Section:
    """"""
    def __init__(self, hexList: list):
        #╔═Mesh Center Point═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.aabb_center_x = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x00:0x04], keepSpaces=False)), np.float32)[0]
        self.aabb_center_y = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x04:0x08], keepSpaces=False)), np.float32)[0]
        self.aabb_center_z = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x08:0x0c], keepSpaces=False)), np.float32)[0]
        self.aabb_center_w = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x0c:0x10], keepSpaces=False)), np.float32)[0]
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.aabb_min_x = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x10:0x14], keepSpaces=False)), np.float32)[0]
        self.aabb_min_y = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x14:0x18], keepSpaces=False)), np.float32)[0]
        self.aabb_min_z = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x18:0x1c], keepSpaces=False)), np.float32)[0]
        self.aabb_min_w = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x1c:0x20], keepSpaces=False)), np.float32)[0]
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.aabb_max_x = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x20:0x24], keepSpaces=False)), np.float32)[0]
        self.aabb_max_y = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x24:0x28], keepSpaces=False)), np.float32)[0]
        self.aabb_max_z = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x28:0x2c], keepSpaces=False)), np.float32)[0]
        self.aabb_max_w = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x2c:0x30], keepSpaces=False)), np.float32)[0]
        #╔═Mesh Name Offset═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_mesh_name = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x30:0x34], keepSpaces=False)), np.uint32)[0]
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x34:0x36], keepSpaces=False)), np.uint16)[0]
        #╔═ Number of Submeshes═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.number_submeshs = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x36:0x38], keepSpaces=False)), np.uint16)[0]
        #╔═Offset Submesh Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_submeshs = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x38:0x3c], keepSpaces=False)), np.uint32)[0]

        #╔═Mesh Name═╗#
        #║ ↓↓↓↓↓↓↓↓↓ ║#
        self.name = self.get_name(hexList, self.offset_mesh_name)
        #╔═Submesh Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.sub_pointers = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[self.offset_submeshs:self.offset_submeshs + (4 * self.number_submeshs)], keepSpaces=False)), np.uint32)
        #╔═List of Submesh Hexes═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.submeshHex = self.get_subHex(hexList, self.sub_pointers)
        #╔═List of Submeshes═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.SubMeshes = [SubMesh_Section(ind) for ind in self.submeshHex]

    def get_subHex(self, hList, pointers):
        SubMeshes = []
        for k in range(0, len(pointers)):
            if k + 1 < len(pointers):
                SubMeshes.append(hList[pointers[k]:pointers[k + 1]][:-1])
            else:
                SubMeshes.append(hList[pointers[k]:][:-1])
        return SubMeshes
    def get_name(self, hList, NameOffset):
        decodeThis = ''.join(hList[NameOffset:NameOffset + hList[NameOffset:].index('00')])
        return str(bytes.fromhex(decodeThis).decode('charmap'))

    pass
class SubMesh_Section:
    """"""
    def __init__(self, hexList):
        #╔═Submesh Center Point═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.aabb_center_x = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x00:0x04], keepSpaces=False)), np.float32)[0]  #
        self.aabb_center_y = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x04:0x08], keepSpaces=False)), np.float32)[0]  #
        self.aabb_center_z = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x08:0x0c], keepSpaces=False)), np.float32)[0]  #
        self.aabb_center_w = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x0c:0x10], keepSpaces=False)), np.float32)[0]  #
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.aabb_min_x = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x10:0x14], keepSpaces=False)), np.float32)[0]  #
        self.aabb_min_y = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x14:0x18], keepSpaces=False)), np.float32)[0]  #
        self.aabb_min_z = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x18:0x1c], keepSpaces=False)), np.float32)[0]  #
        self.aabb_min_w = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x1c:0x20], keepSpaces=False)), np.float32)[0]  #
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.aabb_max_x = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x20:0x24], keepSpaces=False)), np.float32)[0]  #
        self.aabb_max_y = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x24:0x28], keepSpaces=False)), np.float32)[0]  #
        self.aabb_max_z = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x28:0x2c], keepSpaces=False)), np.float32)[0]  #
        self.aabb_max_w = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x2c:0x30], keepSpaces=False)), np.float32)[0]  #
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.vertex_type_flag = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x30:0x34], keepSpaces=False)), np.uint32)[0]  #
        #╔═Hex Size of Vertex═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.vertex_size = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x34:0x38], keepSpaces=False)), np.uint32)[0]  #
        #╔═Number of Vertices═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.number_vertex = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x38:0x3c], keepSpaces=False)), np.uint32)[0]  #
        #╔═Offset Vertices═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_vertex = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x3c:0x40], keepSpaces=False)), np.uint32)[0]  #
        #╔═Offset Submesh Name═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_submesh_name = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x40:0x44], keepSpaces=False)), np.uint32)[0]  #
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x44:0x45], keepSpaces=False)), np.uint8)[0]  #***UNKNOWN USE***
        #╔═Number of TextureDefs═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.number_textureDef = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x45:0x46], keepSpaces=False)), np.uint8)[0]  #
        #╔═Number of Triangles═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.number_triangles = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x46:0x48], keepSpaces=False)), np.uint16)[0]  #
        #╔═Offset TextureDefs═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_textureDef = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x48:0x4c], keepSpaces=False)), np.uint32)[0]  #
        #╔═Offset Triangles═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_triangles = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x4c:0x50], keepSpaces=False)), np.uint32)[0]  #

        #╔═Submesh Name═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.name = self.get_name(hexList, self.offset_submesh_name)
        #╔═Triangle Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.tri_pointers = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[self.offset_triangles:self.offset_triangles + (4 * self.number_triangles)], keepSpaces=False)), np.uint32)
        #╔═Triangle Hex═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.TriHex = self.get_TriHex(hexList, self.tri_pointers)

        #╔═List of Triangles═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.Triangles = [EMDTriangles_Section(tri) for tri in self.TriHex]
        #╔═List of TextureDefs═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.TextureDefs = [EMDTextureDef_Section(hexList[self.offset_textureDef + (12 * item):]) for item in range(0, self.number_textureDef)]
        #╔═List of Vertices═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.Verts = [EMDVertex(hexList[self.offset_vertex:][line * 36:]) for line in range(0, self.number_vertex)]

    def get_TriHex(self, hList, pointers: list):
        Triangles = []
        for pointer in range(0, len(pointers)):
            if pointer + 1 < len(pointers):
                Triangles.append(
                    hList[pointers[pointer]:pointers[pointer + 1]][:-1])
            else:
                Triangles.append(hList[pointers[pointer]:][:-1])
        return Triangles
    def get_TexHex(self, hList, pointers: list):
        print(pointers)
        Textures = []
        for point in range(0, len(pointers)):
            if point + 1 < len(pointers):
                Textures.append(hList[pointers[point]:pointers[point + 1]])
            else:
                Textures.append(hList[pointers[point]:])
        return Textures
    def get_name(self, hList, NameOffset):
        decodeThis = ''.join(hList[NameOffset:NameOffset + hList[NameOffset:].index('00')])
        return str(bytes.fromhex(decodeThis).decode('charmap'))

    pass
class EMDVertex:
    """"""
    def __init__(self, vL: list):
        #╔═XYZ Coords═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓ ║#
        self.location = np.frombuffer(bytes.fromhex(hexList2hexStrList(vL[0:12], keepSpaces=False)), np.float32)  #
        #╔═Normal Val═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓ ║#
        self.normal = np.frombuffer(bytes.fromhex(hexList2hexStrList(vL[12:18], keepSpaces=False)), np.float16)  #
        #╔═UV Coord Temp═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        UV_Temp = np.frombuffer(bytes.fromhex(hexList2hexStrList(vL[20:24], keepSpaces=False)), np.float16)  #
        #╔═UV Coords═╗#
        #║ ↓↓↓↓↓↓↓↓↓ ║#
        self.UV = [UV_Temp[0], -1 * UV_Temp[1]]  #
        #╔═Vertex Group Indexes═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.vgIndexes = np.frombuffer(bytes.fromhex(hexList2hexStrList(vL[24:28], keepSpaces=False)), np.uint8)  #
        #╔═Vertex Group Names═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.vgNames = []  #
        #╔═Vertex Group Weights═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.weights = self.solve_weights(vL)  #

    def solve_weights(self, vLine):
        blends = np.frombuffer(bytes.fromhex(hexList2hexStrList(vLine[28:34], keepSpaces=False)), np.float16)
        weight_4 = 1 - (blends[2] + blends[1] + blends[0])
        weight_1 = blends[0]
        weight_2 = blends[1]
        weight_3 = 1 - (weight_4 + weight_2 + weight_1)
        return np.array([weight_1, weight_2, weight_3, weight_4])
class EMDTextureDef_Section:
    """"""
    def __init__(self, hexList):
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.flag0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x00:0x01], keepSpaces=False)), np.uint8)[0]
        #╔═Int for defining which Detail texture to use═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.textureIndex = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x01:0x02], keepSpaces=False)), np.uint8)[0]
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.adressMode_uv = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x02:0x03], keepSpaces=False)), np.uint8)[0]
        #╔═***USE UNKNOWN***═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.filtering_minMag = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x03:0x04], keepSpaces=False)), np.uint8)[0]
        #╔═U Axis Scale═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.texture_scale_u = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x04:0x08], keepSpaces=False)), np.float32)[0]
        #╔═V Axis Scale═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.texture_scale_v = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x08:0x0c], keepSpaces=False)), np.float32)[0]
    pass
class EMDTriangles_Section:
    """"""
    def __init__(self, hexList):
        #╔═Number of Tri Faces═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.number_faces = int(np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x00:0x04], keepSpaces=False)), np.uint32)[0] / 3)
        #╔═Number of Bones═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.number_bones = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x04:0x08], keepSpaces=False)), np.uint32)[0]
        #╔═Offset Faces═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_faces = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x08:0x0c], keepSpaces=False)), np.uint32)[0]
        #╔═Offset Bone Names═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.offset_bone_names = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x0c:0x10], keepSpaces=False)), np.uint32)[0]
        #╔═Bone Name Pointers═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        pointers = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[self.offset_bone_names:self.offset_bone_names + (4 * self.number_bones)], keepSpaces=False)), np.uint32)
        #╔═List of Bone Names═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.bone_names = [self.get_name(hexList, point) for point in pointers]
        #╔═List of Faces═╗#
        #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
        self.Faces = [np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[self.offset_faces:][curFace * 6:(curFace * 6) + 6], keepSpaces=False)), np.uint16) 
                      for curFace in range(0, self.number_faces)]

    def get_name(self, hList, NameOffset):
        decodeThis = ''
        if '00' in hList[NameOffset:]:
            for hexItem in hList[NameOffset:NameOffset + hList[NameOffset:].index('00')]:
                decodeThis += hexItem
        else:
            for hexItem in hList[NameOffset:]:
                decodeThis += hexItem
        return str(bytes.fromhex(decodeThis).decode('charmap'))
    pass
