import traceback
from typing import *
from .fileUtil import *
import numpy as np




class EskArmature:
    def __init__(self, file_name: str, hlist=None):
        self.name       = \
            (file_name.replace(".esk","") if ".esk" in file_name else file_name)    #type: str
        self.bones      = []                                                        #type: List[EskBone]
        
        self.header     = None                                                      #type: None or ESK_Header
        self.skeleton   = None                                                      #type: None or ESK_Skeleton_Section
        
        if hlist is not None:
            self.header = ESK_Header(hlist=hlist)
            self.skeleton = self.header.SkeleSect
            
            for boneInd in range(0, self.skeleton.number_bones):
                BoneRelativeTransform = self.skeleton.RelativeTransforms[boneInd]
                BoneAbsoluteMatrix = self.skeleton.AbsoluteMatrices[boneInd]
                
                newBone = EskBone()
                newBone.name = self.skeleton.BoneNames[boneInd]
                newBone.XYZ = BoneRelativeTransform.position
                newBone.ORI = BoneRelativeTransform.orientation
                newBone.SCA = BoneRelativeTransform.scale
                
                newBone.AbsoluteBoneMatrixL1 = BoneAbsoluteMatrix.m0
                newBone.AbsoluteBoneMatrixL2 = BoneAbsoluteMatrix.m1
                newBone.AbsoluteBoneMatrixL3 = BoneAbsoluteMatrix.m2
                newBone.AbsoluteBoneMatrixL4 = BoneAbsoluteMatrix.m3
                
                self.bones.append(newBone)
            self.generate_hierarchy(self.skeleton.BoneHierCatalog)

    def generate_hierarchy(self, HierRef):
        if HierRef[0] == 65535:
            print("HIERARCHY STARTS WITH 65535")
            HierValues = HierRef[1:]
        else:
            print("HIERARCHY DOESN'T START WITH 65535")
            HierValues = HierRef

        for ind in range(0, len(HierValues), 4):
            tempHierVals = HierValues[ind:ind + 4]
            if len(tempHierVals) == 4:
                #print("REFER:\t", HierRef[ind:ind + 4])
                #print("VALUES:\t", HierValues[ind:ind + 4])
                if tempHierVals[0] == 65535:
                    if tempHierVals[1] != 65535:
                        self.bones[tempHierVals[1]].parent = self.bones[tempHierVals[3]]
                        #print("Parent: ",self.bones[tempHierVals[3]].name)
                        #print("Child:  ",self.bones[tempHierVals[1]].name)
                        #print()
                else:
                    self.bones[tempHierVals[0]].parent = self.bones[tempHierVals[3]]
                    #print("Parent: ", tempHierVals[3])
                    #print("Child:  ", tempHierVals[0])
                    #print()
                    if tempHierVals[1] != 65535:
                        self.bones[tempHierVals[1]].parent = self.bones[tempHierVals[3]].parent
                        #print("Parent: ", str(tempHierVals[3])+"'s parent")
                        #print("Child:  ", tempHierVals[1])
                        #print()
        pass

class EskBone:
    def __init__(self):
        self.name                   = ''            #type: str
        self.XYZ                    = []            #type: List[np.float32]*3
        self.ORI                    = []            #type: List[np.float32]*3
        self.SCA                    = []            #type: List[np.float32]*3
        #self.ATM                    = ()            #type: List[List[np.float32]*4]*4
        self.AbsoluteBoneMatrixL1   = []            #type: List[np.float32]*4
        self.AbsoluteBoneMatrixL2   = []            #type: List[np.float32]*4
        self.AbsoluteBoneMatrixL3   = []            #type: List[np.float32]*4
        self.AbsoluteBoneMatrixL4   = []            #type: List[np.float32]*4
        self.parent                 = None          #type: EskBone or None

class LocationCloud:
    def __init__(self):
        self.cloud = []
        self.offset = 0
        self.padding = 52

class ESK_Header:
    def __init__(self,hlist):       
        self.signature          = hex2str(hlist[0x00:0x04])
        print("signature:\t\t",self.signature)
        self.endian             = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x04:0x06],keepSpaces=False)),np.uint16)
        print("endian:\t\t\t",self.endian)
        self.header_size        = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x06:0x08],keepSpaces=False)),np.uint16)[0]
        print("header_size:\t\t",self.header_size)
        self.version            = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x08:0x0c],keepSpaces=False)),np.uint8)
        print("version:\t\t",self.version)
        self.unknow_0           = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x0c:0x10],keepSpaces=False)),np.uint32)
        print("unknow_0:\t\t",self.unknow_0)
        self.offset_skeleton    = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x10:0x14],keepSpaces=False)),np.uint32)[0]
        print("offset_skeleton:\t",self.offset_skeleton)
        self.offset_nextPart    = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x14:0x18],keepSpaces=False)),np.uint32)[0]
        print("offset_nextPart:\t",self.offset_nextPart)
        self.unknow_1           = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x18:0x1c],keepSpaces=False)),np.uint32)
        print("unknow_1:\t\t",self.unknow_1)
        self.unknow_2           = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x1c:0x20],keepSpaces=False)),np.uint32)
        print("unknow_2:\t\t",self.unknow_2)
        
        self.SkeleSect          = ESK_Skeleton_Section(hlist[self.offset_skeleton:])    #type: ESK_Skeleton_Section
        #print("offset_nextPart:\t", self.offset_nextPart)
        #self.NextPart           = 

class ESK_Skeleton_Section:
    def __init__(self,hlist):
        self.tempcall = hlist
        self.number_bones               = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x02],keepSpaces=False)),np.uint16)[0]
        print("number_bones:\t\t",self.number_bones)
        self.unknow_flag                = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x02:0x04],keepSpaces=False)),np.uint16)
        print("unknow_flag:\t\t",self.unknow_flag)
        self.offset_bonesHierarchy      = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x04:0x08],keepSpaces=False)),np.uint32)[0]
        print("offset_bonesHierarchy:\t",self.offset_bonesHierarchy)
        self.offset_boneNames           = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x08:0x0c],keepSpaces=False)),np.uint32)[0]
        print("offset_boneNames:\t",self.offset_boneNames)
        self.offset_relTransforms       = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x0c:0x10],keepSpaces=False)),np.uint32)[0]
        print("offset_relTransforms:\t",self.offset_relTransforms)
        self.offset_absMatrices         = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x10:0x14],keepSpaces=False)),np.uint32)[0]
        print("offset_absMatrices:\t",self.offset_absMatrices)
        self.offset_IKs                 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x14:0x18],keepSpaces=False)),np.uint32)[0]
        print("offset_IKs:\t\t",self.offset_IKs)
        self.offset_boneExtraInfo       = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x18:0x1c],keepSpaces=False)),np.uint32)[0]
        print("offset_boneExtraInfo:\t", self.offset_boneExtraInfo)
        self.skeletonUniqueId_p1        = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x1c:0x20],keepSpaces=False)),np.uint32)
        print("skeletonUniqueId_p1:\t", self.skeletonUniqueId_p1)
        self.skeletonUniqueId_p2        = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x20:0x24],keepSpaces=False)),np.uint32)
        print("skeletonUniqueId_p2:\t", self.skeletonUniqueId_p2)

        bone_name_pointers          = np.frombuffer(bytes.fromhex(hexList2hexStrList(
            hlist[self.offset_boneNames:self.offset_boneNames+(4*self.number_bones)],keepSpaces=False)),
            np.uint32)
        if np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[self.offset_bonesHierarchy:self.offset_bonesHierarchy+2], keepSpaces=False)), np.uint16)[0] == 65535:
            bone_hier_pointers = [self.offset_bonesHierarchy+2+(bone*8) for bone in range(0, self.number_bones)]
        else:
            bone_hier_pointers = [self.offset_bonesHierarchy+(bone*8) for bone in range(0, self.number_bones)]
        bone_rela_pointers          = [self.offset_relTransforms+(bone*48) for bone in range(0, self.number_bones)]
        print(self.number_bones, len(bone_rela_pointers))
        bone_abso_pointers          = [self.offset_absMatrices+(bone*64) for bone in range(0, self.number_bones)]
        print(self.number_bones, len(bone_abso_pointers))
        #bone_ik_pointers            = [self.offset_IKs+(bone*(16*4)) for bone in range(0,self.number_bones)]
        self.BoneHierarchy              = [ESK_Bone_Hierarchy(hlist[point:]) for point in bone_hier_pointers]
        
        hierTemp = hlist[self.offset_bonesHierarchy:self.offset_bonesHierarchy+(8*self.number_bones)]
        self.BoneHierCatalog = np.frombuffer(bytes.fromhex(hexList2hexStrList(hierTemp, keepSpaces=False)),np.uint16)
        
        self.BoneNames                  = np.array([hex2str(hlist[point:point+hlist[point:].index('00')]) for point in bone_name_pointers])
        self.RelativeTransforms         = [ESK_Bone_Relative_Transform(hlist[point:], boneName=self.BoneNames[bone_rela_pointers.index(point)]) for point in bone_rela_pointers]
        self.AbsoluteMatrices           = [ESK_Bone_Absolute_Matrix(hlist[point:], boneName=self.BoneNames[bone_abso_pointers.index(point)]) for point in bone_abso_pointers]
        self.IK                         = ESK_IK_Section(hlist[self.offset_IKs:])
        self.BoneExtraInfo              = ESK_Bone_extraInfo(hlist[self.offset_boneExtraInfo:])
        
class ESK_Bone_Hierarchy:
    def __init__(self,hlist):
        
        self.parent_index = None
        self.child_index = None
        self.sibling_index = None
        self.ik_flag = None
        
        Pos0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x02], keepSpaces=False)),np.uint16)[0]
        Pos1 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x02:0x04], keepSpaces=False)),np.uint16)[0]
        Pos2 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x04:0x06], keepSpaces=False)),np.uint16)[0]
        Pos3 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x06:0x08], keepSpaces=False)),np.uint16)[0]
        self.HierList = np.array([Pos0, Pos1, Pos2, Pos3])
        #print(self.HierList)
        
        if Pos0 == 65535:
            if Pos1 != 65535:
                self.parent_index = Pos3
                self.child_index = Pos1
                self.sibling_index = Pos0
                self.ik_flag = Pos2
            else:
                pass
        else:
            self.parent_index = Pos3
            self.child_index = Pos0
            self.sibling_index = None
            self.ik_flag = None
            if Pos1 != 65535:
                self.parent_index = Pos3
                self.child_index = Pos0
                self.sibling_index = Pos1
                self.ik_flag = None
        
        #print("parent_index:\t", self.parent_index)
        #print("child_index:\t", self.child_index)
        #print("sibling_index:\t", self.sibling_index)
        #print("ik_flag:\t", self.ik_flag)

class ESK_Bone_Relative_Transform:
    def __init__(self,hlist, boneName):
        print("\n"+boneName)
        self.position                = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x10],keepSpaces=False)),np.float32)
        print("position:\t",self.position)
        self.orientation             = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x10:0x20],keepSpaces=False)),np.float32)
        print("orientation:\t",self.orientation)
        self.scale                   = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x20:0x30],keepSpaces=False)),np.float32)
        print("scale:\t\t",self.scale)
        
class ESK_Bone_Absolute_Matrix:
    def __init__(self,hlist, boneName):
        print("\n"+boneName+" Absolute Matrix: ")
        self.m0                      = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x10],keepSpaces=False)),np.float32)
        print("m0:\t",self.m0)
        self.m1                      = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x10:0x20],keepSpaces=False)),np.float32)
        print("m1:\t",self.m1)
        self.m2                      = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x20:0x30],keepSpaces=False)),np.float32)
        print("m2:\t",self.m2)
        self.m3                      = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x30:0x40],keepSpaces=False)),np.float32)
        print("m3:\t",self.m3)
        
class ESK_IK_Section:
    def __init__(self, hlist):
        self.number_IkGroups = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x04], keepSpaces=False)), np.uint32)[0]
        print("number_IkGroups:\t", self.number_IkGroups)

        self.IK_Groups = []

        self.the_rest = hlist[0x04:0x04 + (24 * self.number_IkGroups)]
        startAt = 4
        for itm in range(0, self.number_IkGroups):
            if len(self.IK_Groups) == 0:
                self.IK_Groups.append(ESK_IK_Group(hlist[startAt:]))
            elif len(self.IK_Groups) == 10:
                break
            else:
                self.IK_Groups.append(ESK_IK_Group(hlist[startAt:]))
            startAt += self.IK_Groups[itm].groupSize


class ESK_IK_Group:
    def __init__(self, hlist):
        self.groupType = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x02], keepSpaces=False)), np.uint16)[0]
        self.groupSize = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x02:0x04], keepSpaces=False)), np.uint16)[0]
        print("ESK_IK_Group typeGroup:\t", self.groupType)
        print("ESK_IK_Group sizeGroup:\t", self.groupSize)

        self.IK = ESK_IK(hlist[0x04:0x06])
        self.IK_b = ESK_IK_b(hlist[0x06:0x08])
        self.IK_2 = ESK_IK_2(hlist[0x08:self.groupSize])


class ESK_IK:
    def __init__(self, hlist):
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x01], keepSpaces=False)), np.uint8)[0]
        self.number_relations = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x01:0x02], keepSpaces=False)), np.uint8)[0]
        print("ESK_IK unknow_0:\t", self.unknow_0)
        print("ESK_IK number_relations:\t", self.number_relations)


class ESK_IK_b:
    def __init__(self, hlist):
        self.rotation_target = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x01], keepSpaces=False)), np.uint8)[0]
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x01:0x02], keepSpaces=False)), np.uint8)[0]
        print("ESK_IK_b rotation_target:\t", self.rotation_target)
        print("ESK_IK_b unknow_0:\t", self.unknow_0)


class ESK_Bone_extraInfo:
    def __init__(self, hlist):
        #tempglobal.counter += 1
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x02], keepSpaces=False)), np.uint16)[0]  #16
        self.unknow_1 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x02:0x04], keepSpaces=False)), np.uint16)[0]  #16
        self.unknow_2 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x04:0x06], keepSpaces=False)), np.uint16)[0]  #16
        self.unknow_3 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x06:0x08], keepSpaces=False)), np.uint16)[0]  #16
        #oofA = 2 if len("ESK_Bone_extraInfo:\t\tBone %s" % tempglobal.counter) % 3 == 1 \
        #            or len("ESK_Bone_extraInfo:\t\tBone %s" % tempglobal.counter) % 3 == 0 \
        #    else 1
        #print("ESK_Bone_extraInfo:\t\tBone %s" % tempglobal.counter+"\t"*oofA+ str([self.unknow_0, self.unknow_1, self.unknow_2, self.unknow_3]))


class ESK_IK_2:
    def __init__(self, hlist):
        self.number_bones = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x00:0x04], keepSpaces=False)), np.uint32)  #32
        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0x04:0x08], keepSpaces=False)), np.uint32)  #32
        print("ESK_IK_2 number_bones:\t", self.number_bones)
        print("ESK_IK_2 unknow_0:\t", self.unknow_0)
        print(hlist[0x08:])
        

