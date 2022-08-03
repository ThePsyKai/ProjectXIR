import traceback
from typing import *
from .fileUtil import *
import numpy as np
import time
import multiprocessing as mp

class Emb:
    def __init__(self):
        pass

class EMB_Header:
    def __init__(self,hexList):
        #print(hexList[0x00:0x04])
        self.signature          = hex2str(hexList[0x00:0x04])
        self.endian             = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x04:0x06],keepSpaces=False)), np.uint16)[0]
        self.header_size        = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x06:0x08],keepSpaces=False)), np.uint16)[0]
        self.version            = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x08:0x0c], keepSpaces=False)), np.uint8)
        self.image_count        = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x0c:0x10], keepSpaces=False)), np.uint32)[0]

        self.unknow_0 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x10:0x14], keepSpaces=False)), np.uint8)
        self.unknow_1 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x14:0x18], keepSpaces=False)), np.uint8)
        self.unknow_2 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x18:0x1c], keepSpaces=False)), np.uint32)[0]
        self.unknow_3 = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x1c:0x20], keepSpaces=False)), np.uint8)


        self.image_offsets  = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[self.header_size:self.header_size + (8*self.image_count)],keepSpaces=False)), np.uint32)

        print([self.image_offsets[oop]+self.header_size for oop in range(0, len(self.image_offsets), 2)])
        print([(int(oop/2)*8) for oop in range(0, len(self.image_offsets), 2)])
        self.image_pointers = np.array([self.image_offsets[oop]+self.header_size+(int(oop/2)*8) for oop in range(0, len(self.image_offsets), 2)])
        self.image_length   = np.array([self.image_offsets[oop] for oop in range(1, len(self.image_offsets), 2)])

        imagepointHex       = np.array([hexList[self.header_size + (oop*8):self.header_size + (oop*8) + 4] for oop in range(0, self.image_count)])
        imageLengthHex      = np.array([hexList[self.header_size + 4 + (oop*8):self.header_size + (oop*8) + 8] for oop in range(0, self.image_count)])


        #print(imagepointHex)
        #self.rgba_offset    = np.array([self.image_pointers[oof]+self.unknow_2 for oof in range(0,self.image_count)])
        #print(imageLengthHex)


        print(self.signature)
        print(self.endian)
        print(self.header_size)
        print(self.version)
        print(self.image_count)

        print(self.unknow_0)
        print(self.unknow_1)
        print(self.unknow_2)
        print(self.unknow_3)

        print(self.image_offsets)
        print(self.image_pointers)
        print(self.image_length)

        print()
        print(self.header_size + (8*self.image_count))
        #for h in range(0,len(hexList),16):
        #    print(hexList[h:h+16])

        pass

class EMB_Image:
    def __init__(self,hexList):
        valid_rgb_formats = ['A8R8G8B8','A1R5G5B5','A4R4G4B4','R8G8B8','R5G5B5']
        valid_FOURCC_formats = ['DXT1','DXT2','DXT3','DXT4','DXT5']

        self.image_type                = hex2str(hexList[0x00:0x04])
        self.header_size               = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x04:0x08], keepSpaces=False)), np.uint32)[0]  #Should equal 124
        self.flags                     = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x08:0x0c], keepSpaces=False)), np.uint32)[0]
        self.height                    = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x0c:0x10], keepSpaces=False)), np.uint32)[0]
        self.width                     = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x10:0x14], keepSpaces=False)), np.uint32)[0]
        self.Pitch_or_LinearSize       = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x14:0x18], keepSpaces=False)), np.uint32)
        self.depth                     = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x18:0x1c], keepSpaces=False)), np.uint32)
        self.MipMap_Count              = np.frombuffer(bytes.fromhex(hexList2hexStrList(hexList[0x1c:0x20], keepSpaces=False)), np.uint32)
        self.unknow_1                  = hexList[0x20:0x20+44]
        self.Pixel_Format              = EMB_Image_Pixel_Format(hexList)

        self.ddsCaps                   = [hexList[(0x20+44+self.Pixel_Format.dwSize)+i:(0x20+44+self.Pixel_Format.dwSize)+i+4]
                                          for i in range(0,20,4)]
        self.ddsCaps = [np.frombuffer(bytes.fromhex(hexList2hexStrList(self.ddsCaps[0], keepSpaces=False)), np.uint32)[0],
                        np.frombuffer(bytes.fromhex(hexList2hexStrList(self.ddsCaps[1], keepSpaces=False)), np.uint8),
                        np.frombuffer(bytes.fromhex(hexList2hexStrList(self.ddsCaps[2], keepSpaces=False)), np.uint8),
                        np.frombuffer(bytes.fromhex(hexList2hexStrList(self.ddsCaps[3], keepSpaces=False)), np.uint8),
                        np.frombuffer(bytes.fromhex(hexList2hexStrList(self.ddsCaps[4], keepSpaces=False)), np.uint8)]  ##0: Unknown Use, 1

        self.unknow_2                  = None

        print('image_type:             ',hexList[0x00:0x04],self.image_type)
        print('header_size:            ',hexList[0x04:0x08],self.header_size)
        print('flags:                  ',hexList[0x08:0x0c],self.flags)
        #print(self.flagging())
        print('height:                 ',hexList[0x0c:0x10],self.height)
        print('width:                  ',hexList[0x10:0x14],self.width)
        print('Pitch_or_LinearSize:    ',hexList[0x14:0x18],self.Pitch_or_LinearSize)
        print('depth:                  ',hexList[0x18:0x1c],self.depth)
        print('MipMap_Count:           ',hexList[0x1c:0x20],self.MipMap_Count)
        #print(self.unknow_1)
        print('Pixel_Format: ',self.Pixel_Format.get())
        print('ddsCaps:      ',self.ddsCaps)
        print()
    def flagging(self):
        active_flags = []
        binary = [k for k in str(bin(self.flags))[2:]]
        binary.reverse()
        DDSD_CAPS = binary[0x00] == '1'  # 0
        DDSD_HEIGHT = binary[0x01] == '1'  # 1
        DDSD_WIDTH = binary[0x02] == '1'  # 2
        DDSD_unknown3 = binary[0x03] == '1'
        DDSD_unknown4 = binary[0x04] == '1'
        DDSD_unknown5 = binary[0x05] == '1'
        DDSD_unknown6 = binary[0x06] == '1'
        DDSD_PITCH = binary[0x07] == '1'  # 7
        DDSD_unknown8 = binary[0x08] == '1'
        DDSD_unknown9 = binary[0x09] == '1'
        DDSD_unknowna = binary[0x0a] == '1'
        DDSD_unknownb = binary[0x0b] == '1'
        DDSD_PIXELFORMAT = binary[0x0c] == '1'  # 12
        DDSD_unknownd = binary[0x0d] == '1'
        DDSD_unknowne = binary[0x0e] == '1'
        DDSD_unknownf = binary[0x0f] == '1'
        DDSD_unknown10 = binary[0x10] == '1'
        DDSD_MIPMAPCOUNT = binary[0x11] == '1'  # 17
        DDSD_unknown12 = binary[0x12] == '1'
        DDSD_LINEARSIZE = binary[0x13] == '1'  # 19
        if len(binary) > 20:
            DDSD_unknown14 = binary[0x14] == '1'
            DDSD_unknown15 = binary[0x15] == '1'
            DDSD_unknown16 = binary[0x16] == '1'
            DDSD_DEPTH = binary[0x17] == '1'  # 23
        else:
            DDSD_unknown14 = False
            DDSD_unknown15 = False
            DDSD_unknown16 = False
            DDSD_DEPTH = False
        if DDSD_CAPS:
            active_flags.append('DDSD_CAPS')
        if DDSD_HEIGHT:
            active_flags.append('DDSD_HEIGHT')
        if DDSD_WIDTH:
            active_flags.append('DDSD_WIDTH')
        if DDSD_unknown3: active_flags.append('DDSD_unknown3')
        if DDSD_unknown4: active_flags.append('DDSD_unknown4')
        if DDSD_unknown5: active_flags.append('DDSD_unknown5')
        if DDSD_unknown6: active_flags.append('DDSD_unknown6')
        if DDSD_PITCH:
            active_flags.append('DDSD_PITCH')
        if DDSD_unknown8: active_flags.append('DDSD_unknown8')
        if DDSD_unknown9: active_flags.append('DDSD_unknown9')
        if DDSD_unknowna: active_flags.append('DDSD_unknowna')
        if DDSD_unknownb: active_flags.append('DDSD_unknownb')
        if DDSD_PIXELFORMAT:
            active_flags.append('DDSD_PIXELFORMAT')
        if DDSD_unknownd: active_flags.append('DDSD_unknownd')
        if DDSD_unknowne: active_flags.append('DDSD_unknowne')
        if DDSD_unknownf: active_flags.append('DDSD_unknownf')
        if DDSD_unknown10: active_flags.append('DDSD_unknown10')
        if DDSD_MIPMAPCOUNT:
            active_flags.append('DDSD_MIPMAPCOUNT')
        if DDSD_unknown12: active_flags.append('DDSD_unknown12')
        if DDSD_LINEARSIZE:
            active_flags.append('DDSD_LINEARSIZE')
        if DDSD_unknown14: active_flags.append('DDSD_unknown14')
        if DDSD_unknown15: active_flags.append('DDSD_unknown15')
        if DDSD_unknown16: active_flags.append('DDSD_unknown16')
        if DDSD_DEPTH:
            active_flags.append('DDSD_DEPTH')
        return active_flags

class EMB_Image_Pixel_Format:
    def __init__(self,hexList):
        self.__splitUp = [hexList[(0x20 + 44) + i:(0x20 + 44) + i + 4] for i in range(0, 32, 4)]

        self.dwSize              = np.frombuffer(bytes.fromhex(hexList2hexStrList(self.__splitUp[0], keepSpaces=False)), np.uint32)[0]
        self.dwFlags             = str(bin(np.frombuffer(bytes.fromhex(hexList2hexStrList(self.__splitUp[1], keepSpaces=False)), np.uint32)[0]))[2:]
        self.dwFourCC            = hex2str(self.__splitUp[2])

        self.dwRGBBitCount       = np.frombuffer(bytes.fromhex(hexList2hexStrList(self.__splitUp[3], keepSpaces=False)), np.uint8)
        self.dwRBitMask          = np.frombuffer(bytes.fromhex(hexList2hexStrList(self.__splitUp[4], keepSpaces=False)), np.uint8)
        self.dwGBitMask          = np.frombuffer(bytes.fromhex(hexList2hexStrList(self.__splitUp[5], keepSpaces=False)), np.uint8)
        self.dwBBitMask          = np.frombuffer(bytes.fromhex(hexList2hexStrList(self.__splitUp[6], keepSpaces=False)), np.uint8)
        self.dwRGBAlphaBitMask   = np.frombuffer(bytes.fromhex(hexList2hexStrList(self.__splitUp[7], keepSpaces=False)), np.uint8)
    def get(self):
        return [self.dwSize,
                self.dwFlags,
                self.dwFourCC,
                self.dwRGBBitCount,
                self.dwRBitMask,
                self.dwGBitMask,
                self.dwBBitMask,
                self.dwRGBAlphaBitMask]

