from .fileUtil import (str2hex,hex2str,hexify,fileReader,hexList2hexStrList,)
import re
from .handlingHex import vertHex2Float,hex_to_float,hexToHalfFloat,hexToShort,hex2float
from .emd_file_obj import *
import time

from .esk_reader import get_bone_names

def reader_debug(*text_string):
    debugText = "[DEBUG] | "
    print(debugText+"".join([str(string)+" " for string in text_string]))

#╔═════════════════════════════════════════════════════════════╗#
#║                       EMD File Reader                       ║#
#║       ===============================================       ║#
#║                     Original EMD Reader                     ║#
#║                Does Not Have TexDef Working                 ║#
#╚═════════════════════════════════════════════════════════════╝#
def Reader(fileBytes):
    emdfileHex = hexify(fileBytes)      # File hex grabbed from file bytes
    hexList = emdfileHex.split(' ')     # File hex split apart from each other into a list
    EMDData = EMD(hexList)              # Run File Hex through File Type "filter" (Generate that 
    returnGroups = []
    for ModelInd in range(0, len(EMDData.Models)):
        
        newGroup = EmdGroup(EMDData.Models[ModelInd].name)
        newGroup.meshes = EMDData.Models[ModelInd].Meshes
        newGroup.subMeshes = [mes.SubMeshes for mes in EMDData.Models[ModelInd].Meshes]
        groupVertClusters = []
        for VertexInd in EMDData.Vertices[ModelInd]:
            groupVertClusters.append(VertexInd)

        groupTrianClusters = []
        for TriInd in EMDData.Triangles[ModelInd]:
            groupTrianClusters.append(TriInd)


        # print(tempVerts)
        for ind in range(0, len(newGroup.subMeshes)):
            newGroup.meshCount = len(newGroup.subMeshes[ind])
            for SubMeshInd in range(0,len(newGroup.subMeshes[ind])):
                newMesh = EmdMesh()
                newMesh.MeshName = newGroup.subMeshes[ind][SubMeshInd].name
                newMesh.vertices = groupVertClusters[ind][SubMeshInd]
                TriCluster = groupTrianClusters[ind][SubMeshInd]

                tempFaces = []
                if len(TriCluster) == 1:
                    tempFaces.extend(groupTrianClusters[ind][SubMeshInd][0].Faces)
                    bones = groupTrianClusters[ind][SubMeshInd][0].bone_names
                    for vertexItem in newMesh.vertices:
                        vertexItem.vgNames = [bones[vertexItem.vgIndexes[0]],
                                              bones[vertexItem.vgIndexes[1]],
                                              bones[vertexItem.vgIndexes[2]],
                                              bones[vertexItem.vgIndexes[3]]]
                    newMesh.vertex_group_names = bones

                elif len(TriCluster) > 1:
                    tempBones = []
                    for clustInd in groupTrianClusters[ind][SubMeshInd]:
                        tempFaces.extend(clustInd.Faces)
                        bones = clustInd.bone_names
                        tempBones.extend(bones)
                        for face in clustInd.Faces:
                            Vert1_vgIndexes = newMesh.vertices[face[0]].vgIndexes
                            Vert2_vgIndexes = newMesh.vertices[face[1]].vgIndexes
                            Vert3_vgIndexes = newMesh.vertices[face[2]].vgIndexes
                            if not len(newMesh.vertices[face[0]].vgNames):
                                newMesh.vertices[face[0]].vgNames = [bones[Vert1_vgIndexes[0]], bones[Vert1_vgIndexes[1]],
                                                                 bones[Vert1_vgIndexes[2]], bones[Vert1_vgIndexes[3]]]
                            if not len(newMesh.vertices[face[1]].vgNames):
                                newMesh.vertices[face[1]].vgNames = [bones[Vert2_vgIndexes[0]], bones[Vert2_vgIndexes[1]],
                                                                 bones[Vert2_vgIndexes[2]], bones[Vert2_vgIndexes[3]]]
                            if not len(newMesh.vertices[face[2]].vgNames):
                                newMesh.vertices[face[2]].vgNames = [bones[Vert3_vgIndexes[0]], bones[Vert3_vgIndexes[1]],
                                                                 bones[Vert3_vgIndexes[2]], bones[Vert3_vgIndexes[3]]]

                    newMesh.vertex_group_names = tempBones

                for vertexItem in newMesh.vertices:
                    for vgItem in range(0, len(vertexItem.vgNames)):
                        if vertexItem.location[0] > 0.0 and '_R_' in vertexItem.vgNames[vgItem]:
                            vertexItem.vgNames[vgItem] = vertexItem.vgNames[vgItem].replace('_R_', '_L_')
                        
                        elif vertexItem.location[0] < 0.0 and '_L_' in vertexItem.vgNames[vgItem]:
                            vertexItem.vgNames[vgItem] = vertexItem.vgNames[vgItem].replace('_L_', '_R_')

                newMesh.faces = tempFaces
                newGroup.meshes.append(newMesh)
        returnGroups.append(newGroup)
    print("════════════RETURN VALUES FROM EMD READER════════════")
    print(returnGroups)
    for grp in returnGroups:
        for msh in grp.meshes:
            print(msh)
    print("═════════════════════════════════════════════════════")
    return returnGroups


#╔═════════════════════════════════════════════════════════════╗#
#║                         File Reader                         ║#
#║       ===============================================       ║#
#║          Returns EMD Data in more accessible form           ║#
#╚═════════════════════════════════════════════════════════════╝#
def Reader2(fileBytes):
    #╔═File Hex Taken Bytes═╗#
    #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
    emdfileHex = hexify(fileBytes)
    #╔═Hex Split Apart Into List═╗#
    #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
    hexList = emdfileHex.split(' ')
    #╔═Run Hex List Through EMD File Type═╗#
    #║ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ║#
    tab = ">"
    EMDData = NewEMD(hexList)
    for ModelInd in range(0, len(EMDData.Models)):
        reader_debug("========EMD Model========")
        reader_debug("Model Name:", EMDData.Models[ModelInd].name)
        reader_debug("Mesh Count:", EMDData.Models[ModelInd].number_meshs)
        EMDMeshes = EMDData.Models[ModelInd].Meshes
        for MeshInd in range(0, len(EMDMeshes)):
            reader_debug("========EMD Mesh========")
            reader_debug(tab*1+"Mesh Name:", EMDMeshes[MeshInd].name)
            reader_debug(tab*1+"Center: X", EMDMeshes[MeshInd].aabb_center_x, "Y", EMDMeshes[MeshInd].aabb_center_y, "Z", EMDMeshes[MeshInd].aabb_center_z, "W", EMDMeshes[MeshInd].aabb_center_w)
            reader_debug(tab*1+"Min: X", EMDMeshes[MeshInd].aabb_min_x, "Y", EMDMeshes[MeshInd].aabb_min_y, "Z", EMDMeshes[MeshInd].aabb_min_z, "W", EMDMeshes[MeshInd].aabb_min_w)
            reader_debug(tab*1+"Max: X", EMDMeshes[MeshInd].aabb_max_x, "Y", EMDMeshes[MeshInd].aabb_max_y, "Z", EMDMeshes[MeshInd].aabb_max_z, "W", EMDMeshes[MeshInd].aabb_max_w)
            reader_debug(tab*1+"Submesh Count:", EMDMeshes[MeshInd].number_submeshs)
            EMDSubmeshes = EMDMeshes[MeshInd].SubMeshes
            for SubInd in range(0, len(EMDSubmeshes)):
                reader_debug("========EMD Submesh========")
                reader_debug(tab*2+"Mesh Name:", EMDSubmeshes[SubInd].name)
                reader_debug(tab*2+"Center: X", EMDSubmeshes[SubInd].aabb_center_x, "Y", EMDSubmeshes[SubInd].aabb_center_y, "Z", EMDSubmeshes[SubInd].aabb_center_z, "W", EMDSubmeshes[SubInd].aabb_center_w)
                reader_debug(tab*2+"Min: X", EMDSubmeshes[SubInd].aabb_min_x, "Y", EMDSubmeshes[SubInd].aabb_min_y, "Z", EMDSubmeshes[SubInd].aabb_min_z, "W", EMDSubmeshes[SubInd].aabb_min_w)
                reader_debug(tab*2+"Max: X", EMDSubmeshes[SubInd].aabb_max_x, "Y", EMDSubmeshes[SubInd].aabb_max_y, "Z", EMDSubmeshes[SubInd].aabb_max_z, "W", EMDSubmeshes[SubInd].aabb_max_w)
                reader_debug(tab*2+"Vertex Count:", EMDSubmeshes[SubInd].number_vertex)
                reader_debug(tab*2+"Texture Count:", EMDSubmeshes[SubInd].number_textureDef)
                reader_debug(tab*2+"Triangle Count:", EMDSubmeshes[SubInd].number_triangles)
                EMDTextures = EMDSubmeshes[SubInd].TextureDefs
                EMDTriangles = EMDSubmeshes[SubInd].Triangles
                for TexInd in range(0, len(EMDTextures)):
                    reader_debug("========EMD Texture========")
                    reader_debug(tab*3+"Texture Index:", EMDTextures[TexInd].textureIndex)
                    reader_debug(tab*3+"U Scale:", EMDTextures[TexInd].texture_scale_u)
                    reader_debug(tab*3+"V Scale:", EMDTextures[TexInd].texture_scale_v)
                for TriInd in range(0, len(EMDTriangles)):
                    reader_debug("========EMD Triangle========")
                    reader_debug(tab*3+"Face Count:", EMDTriangles[TriInd].number_faces)
                    reader_debug(tab*3+"Bone Count:", EMDTriangles[TriInd].number_bones)
                    reader_debug(tab*3+"Bone Names:", EMDTriangles[TriInd].bone_names)
    print()
    return EMDData
