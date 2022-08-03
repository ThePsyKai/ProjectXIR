from .fileUtil import (str2hex,hex2str,hexify,fileReader,hexList2hexStrList,)
import re
from .handlingHex import vertHex2Float,hex2float,hexToHalfFloat,hexToShort
from .esk_file_obj import *


def get_rig_hirearchy(HEX,tempArm):
    searchIn = HEX[:HEX.index('45 58 50 5f ')].lower()
    startFrom = searchIn.index('ff ff ') - searchIn.index('ff ff ')%(16*3)
    searchIn = searchIn[startFrom:]
    spare = None
    justInCase = None
    for x in range(0,len(searchIn),16*3):
        line = searchIn[x:x+(16*3)].split(' ')[:-1]
        print(line)
        if line[3] == '00' and line[5] == '00' and line[11] == '00' and line[13] == '00' and x != 0:
            print('Line 1+')
            print(spare)
            if spare is not None:
                child = spare
                parent = hexToShort(line[4:6], True)
                if tempArm.bones[child].parent is None and child > parent:
                    print("Spare  :",child, 'is a child of', parent)
                    tempArm.bones[child].parent = parent

            print(line[4:6],line[8:10])
            if line[4:6] != ['ff','ff'] and line[8:10] != ['ff','ff']:
                child = hexToShort(line[8:10], True)
                parent = hexToShort(line[4:6], True)
                if tempArm.bones[child].parent is None and child > parent:
                    print("First  :",child, 'is a child of', parent)
                    tempArm.bones[child].parent = parent

            print(line[6:8],line[12:14])
            if line[6:8] != ['ff','ff'] and line[12:14] != ['ff','ff']:
                child =hexToShort(line[6:8],True)
                parent = hexToShort(line[12:14], True)
                if tempArm.bones[child].parent is None and child > parent:
                    print("Second :",child, 'is a child of', parent)
                    tempArm.bones[child].parent = parent

            print(line[6:8],line[8:10])
            if line[6:8] == ['ff','ff'] and line[8:10] != ['ff','ff']:
                child =hexToShort(line[8:10], True)
                parent = hexToShort(line[12:14], True)
                if tempArm.bones[child].parent is None and child > parent:
                    print("Third  :",child, 'is a child of', parent)
                    tempArm.bones[child].parent = parent

            print(line[0:2])
            print(justInCase)
            if line[0:2] != ['ff','ff']:
                child = hexToShort(line[0:2], True)
                parent = justInCase
                if tempArm.bones[child].parent is None and child > parent:
                    print('JIC    :',child, 'is a child of', parent)
                    tempArm.bones[child].parent = parent

            justInCase = hexToShort(line[12:14], True)
            if line[14:16] != ['ff','ff']:
                spare = hexToShort(line[14:16], True)
            else:
                spare = None
        elif x == 0:
            print('Line 0')
            if line[6:8] != ['ff','ff'] and line[12:14] != ['ff','ff']:
                child = hexToShort(line[6:8], True)
                parent = hexToShort(line[12:14], True)
                print(child, 'is a child of', parent)
                tempArm.bones[child].parent = parent
            justInCase = hexToShort(line[12:14], True)
            if line[14:16] != ['ff','ff']:
                spare = hexToShort(line[14:16], True)
            else:
                spare = None
        else:
            break

    #for bone2 in tempArm.bones:
    #    if bone2.parent is not None:
    #        print(tempArm.bones.index(bone2), bone2.name,'\t\t' + ' '*(30-(len(str(tempArm.bones.index(bone2)))+1+len(bone2.name))), bone2.parent, tempArm.bones[bone2.parent].name)
    #    else:
    #        print(tempArm.bones.index(bone2), bone2.name, '\t\t' + ' '*(30-(len(str(tempArm.bones.index(bone2)))+1+len(bone2.name))), bone2.parent)
    pass

def get_bone_names(HEX: str):
    hexList = HEX.split(' ')
    boneKeys = ['5f 78 5f ', '5f 4c 5f', '5f 52 5f', '5f 43 5f', '53 43 44 5f', '45 58 50 5f ', '30 30 30 5f ',
                '5f 54 5f ']
    boneOffset = int(HEX.index("45 58 50 5f ") / 3)
    tList = hexList[boneOffset:]
    tempWords = []
    word = ''
    for CurIndex in range(0, len(tList)):
        if tList[CurIndex] != '00':
            word += tList[CurIndex] + ' '
            pass
        else:
            if CurIndex + 1 < len(tList):
                if tList[CurIndex + 1] != '00':
                    for item in boneKeys:
                        if item in word:
                            tempWords.append(hex2str(word))
                            word = ''
                            break
                    pass
                else:
                    for item in boneKeys:
                        if item in word:
                            tempWords.append(hex2str(word))
                            break
                    break
    return tempWords

def get_rel_and_abs_transforms(HEX, tempRig):
    nema = str2hex(tempRig.bones[-1].name)
    HexRow = int((int((HEX.index(nema) + len(nema)) / 3) + 1) / 16)
    StartPos = (HexRow + 1) * 16
    print()
    rowCount = 1
    relTrans = []
    for i in range(StartPos, len(HEX.split(' ')[StartPos:]), 16 * 3):
        if rowCount > len(tempRig.bones):
            break
        posline = HEX.split(' ')[i:i + (16 * 1)]
        XYZ = [hex2float(posline[0:4]), hex2float(posline[4:8]), hex2float(posline[8:12])]
        oriline = HEX.split(' ')[i + 16:i + (16 * 2)]
        ORI = tuple([hex2float(oriline[12:16]), hex2float(oriline[0:4]), hex2float(oriline[4:8]),
                             hex2float(oriline[8:12])])
        scaline = HEX.split(' ')[i + (16 * 2):i + (16 * 3)]
        SCA = tuple([hex2float(scaline[0:4]), hex2float(scaline[4:8]), hex2float(scaline[8:12])])
        relTrans.append([XYZ,ORI,SCA])
        rowCount += 1

    StartPos += rowCount * (16 * 3)
    rowCount = 1
    absTrans = []
    for i in range(StartPos, len(HEX.split(' ')), 16 * 4):
        if rowCount > len(tempRig.bones):
            break
        Line1 = HEX.split(' ')[i:i + (16 * 1)]
        line_1 = [hex2float(Line1[0:4]), hex2float(Line1[4:8]), hex2float(Line1[8:12]), hex2float(Line1[12:16])]
        Line2 = HEX.split(' ')[i + 16:i + (16 * 2)]
        line_2 = [hex2float(Line2[0:4]), hex2float(Line2[4:8]), hex2float(Line2[8:12]), hex2float(Line2[12:16])]
        Line3 = HEX.split(' ')[i + (16 * 2):i + (16 * 3)]
        line_3 = [hex2float(Line3[0:4]), hex2float(Line3[4:8]), hex2float(Line3[8:12]), hex2float(Line3[12:16])]
        Line4 = HEX.split(' ')[i + (16 * 3):i + (16 * 4)]
        line_4 = [hex2float(Line4[0:4]), hex2float(Line4[4:8]), hex2float(Line4[8:12]), hex2float(Line4[12:16])]
        rowCount += 1
        absTrans.append([line_1,line_2,line_3,line_4])
    return [relTrans,absTrans]

    #for item in tempRig.bones:
    #    print(item.name)
    #    print(item.XYZ, '\n' + str(item.ORI) + '\n' + str(item.scale))
    #    print()
    #    print(item.ATML1, '\n' + str(item.ATML2) + '\n' + str(item.ATML3) + '\n' + str(item.ATML4))
    #    print()


def get_hierarchy(hlist,current_arm):
    if np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[0:2], keepSpaces=False)), np.uint16)[0] == 65535:
        startFrom = 2
    else:
        startFrom = 0
    for ind in range(0,len(hlist[startFrom:]),8):
        check_temp = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[startFrom:][ind:ind + 8], keepSpaces=False)), np.uint16)
        if check_temp[0] == 65535:
            if check_temp[1] != 65535:
                display_temp = np.frombuffer(
                    bytes.fromhex(hexList2hexStrList(hlist[startFrom:][ind:ind + 8], keepSpaces=False)), np.uint16)

                current_arm.bones[display_temp[1]].parent = current_arm.bones[display_temp[3]]
                #print(current_arm.bones[display_temp[1]].name,': child')
                #print(display_temp[2],'unknown')
                #print(current_arm.bones[display_temp[1]].parent.name,': parent')
                #print()
                pass
            else:
                #print(hlist[startFrom:][ind:ind + 8])
                #print('65535 error')
                #print()
                pass
        else:
            display_temp = np.frombuffer(bytes.fromhex(hexList2hexStrList(hlist[startFrom:][ind:ind+8],keepSpaces=False)),np.uint16)
            current_arm.bones[display_temp[0]].parent = current_arm.bones[display_temp[3]]
            #
            #print(current_arm.bones[display_temp[0]].name,': child')
            if display_temp[1] != 65535:
                current_arm.bones[display_temp[1]].parent = current_arm.bones[display_temp[3]].parent
                #print(display_temp[1],'uncle')
            else:
                #print('.', 'uncle')
                pass
            #print(display_temp[2],'unknown')
            #print(current_arm.bones[display_temp[0]].parent.name,': parent')
            #print()
    pass

def Reader(fileBytes):
    fileHex = hexify(fileBytes).split(' ')

    ESK = EskArmature()

    header = ESK_Header(fileHex)
    # print(header.signature)
    # print(header.header_size)
    # print('offset skel',header.offset_skeleton)
    # print('offset next',header.offset_nextPart)
    skelSect = ESK_Skeleton_Section(fileHex[header.offset_skeleton:])
    # print('number_bones:         ',skelSect.number_bones)
    # print('unknow_flag:          ',skelSect.unknow_flag)
    # print('offset_bonesHierarchy:',header.offset_skeleton + skelSect.offset_bonesHierarchy)
    # print('offset_boneNames:     ',header.offset_skeleton + skelSect.offset_boneNames)
    # print('offset_relTransforms: ',header.offset_skeleton + skelSect.offset_relTransforms)
    # print('offset_absMatrices:   ',header.offset_skeleton + skelSect.offset_absMatrices)
    print('offset_IKs:           ', header.offset_skeleton + skelSect.offset_IKs)
    # print('offset_boneExtraInfo: ',header.offset_skeleton + skelSect.offset_boneExtraInfo)
    # print('skeletonUniqueId_p1:  ',skelSect.skeletonUniqueId_p1)
    # print('skeletonUniqueId_p2:  ',skelSect.skeletonUniqueId_p2)
    tempLineOffset = (header.offset_skeleton + skelSect.offset_bonesHierarchy - (
                header.offset_skeleton + skelSect.offset_bonesHierarchy) % 16)
    tempLineEndset = header.offset_skeleton + skelSect.offset_boneNames
    ESK.bones = []
    for bone in range(0, skelSect.number_bones):
        newBone = EskBone()
        newBone.name = skelSect.BoneNames[bone]
        BRT = ESK_Bone_Relative_Transform(
            fileHex[header.offset_skeleton + skelSect.offset_relTransforms + (bone * (16 * 3)):])
        newBone.XYZ = BRT.position
        newBone.ORI = BRT.orientation
        newBone.SCA = BRT.scale
        BAM = ESK_Bone_Absolute_Matrix(
            fileHex[header.offset_skeleton + skelSect.offset_absMatrices + (bone * (16 * 4)):])
        #newBone.ATML1 = tuple([BAM.m0[0],BAM.m1[0],BAM.m2[0],BAM.m3[0]])
        #newBone.ATML2 = tuple([BAM.m0[1],BAM.m1[1],BAM.m2[1],BAM.m3[1]])
        #newBone.ATML3 = tuple([BAM.m0[2],BAM.m1[2],BAM.m2[2],BAM.m3[2]])
        #newBone.ATML4 = tuple([BAM.m0[3],BAM.m1[3],BAM.m2[3],BAM.m3[3]])

        newBone.AbsoluteBoneMatrixL1 = BAM.m0
        newBone.AbsoluteBoneMatrixL2 = BAM.m1
        newBone.AbsoluteBoneMatrixL3 = BAM.m2
        newBone.AbsoluteBoneMatrixL4 = BAM.m3


        ESK.bones.append(newBone)

    # IKS = ESK_IK_Section(fileHex[header.offset_skeleton + skelSect.offset_IKs:])
    # print(IKS.number_IkGroups)
    # if IKS.number_IkGroups < skelSect.number_bones:
    #    for group in range(0,IKS.number_IkGroups):
    #        search_num = header.offset_skeleton + skelSect.offset_IKs + 4
    #        IKG = ESK_IK_Group(fileHex[search_num +(group*8) :])
    #        print()
    #        print(IKG.IK.number_relations,IKG.IK.unknow_0)
    #        print(IKG.IK_b.unknow_0,IKG.IK_b.unknow_1)
    #        #EIK = ESK_IK(fileHex[header.offset_skeleton
    #        #                     +skelSect.offset_IKs
    #        #                     +8
    #        #                     +(group*8)
    #        #                     :])
    #        #print(EIK.unknow_0)
    #        #print(EIK.number_relations)
    #        #print(header.offset_skeleton + skelSect.offset_IKs+4+(group*8))
    #        #print(IKG.typeGroup)
    #        #print(IKG.sizeGroup)

    print(header.offset_skeleton + skelSect.offset_boneExtraInfo)
    get_hierarchy(
        fileHex[header.offset_skeleton + skelSect.offset_bonesHierarchy:
                tempLineEndset],
        ESK
    )

    #for item in ESK.bones:
    #    if item.parent is not None:
    #        print(ESK.bones.index(item), item.name, ':', item.parent.name)
    #    else:
    #        print(ESK.bones.index(item), item.name, ':', item.parent)
    return ESK
