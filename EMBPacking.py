from typing import List
from itertools import permutations
import numpy as np
from .fileUtil import *
import struct

def float32_to_hex(input_int: float or List[float]):
    hex_item = hex(struct.unpack('<I', struct.pack('<f', input_int))[0])
    final_hex = [hex_item[2:][0:2], hex_item[2:][2:4], hex_item[2:][4:6], hex_item[2:][6:8]]
    for item in range(0, len(final_hex)):
        if final_hex[item] == '':
            final_hex[item] = '00'
        if 2 - len(final_hex[item]):
            final_hex[item] = '0' + final_hex[item]
    if not np.frombuffer(bytes.fromhex(hexList2hexStrList(final_hex, keepSpaces=False)), np.float32)[0] == input_int:
        option_list = list(permutations(final_hex))
        for ind in option_list:
            final_hex = list(ind)
            if np.frombuffer(bytes.fromhex(hexList2hexStrList(final_hex, keepSpaces=False)), np.float32)[0] == input_int:
                break
    return final_hex

def uint8_to_hex(input_int: int or List[int]):
    hex_item = hex(struct.unpack('<I', struct.pack('<l', input_int))[0])
    final_hex = hex_item[2:][0:2]
    if 2-len(final_hex):
        final_hex = '0'+final_hex
    return final_hex

def uint16_to_hex(input_int: int or List[int]):
    hex_item = hex(struct.unpack('<I', struct.pack('<l', input_int))[0])
    hex_item = '0' * (4 - len(hex_item[2:])) + hex_item[2:]
    final_hex = [hex_item[0:2], hex_item[2:4]]
    potential        = [list(ite) for ite in list(permutations(final_hex))]
    potential_vals = [np.frombuffer(bytes.fromhex(hexList2hexStrList(list(ite), keepSpaces=False, endian=False)), np.uint16)[0] for ite in potential]
    if input_int in potential_vals:
        final_hex = potential[potential_vals.index(input_int)]
    return final_hex

def uint32_to_hex(input_int: int or List[int]):
    hex_item = hex(struct.unpack('<I', struct.pack('<l', input_int))[0])
    hex_item = '0'*(8-len(hex_item[2:]))+hex_item[2:]
    final_hex = hexList2hexStrList([hex_item[0:2],hex_item[2:4],hex_item[4:6],hex_item[6:8]], keepSpaces=True, endian=True)
    final_hex = final_hex.split(' ')[:-1]
    return final_hex

def Write_EMB(Location, EMBName, DDSImages:List[bytes], DYT:bool=False):
    print()
    if DYT:
        EMBName += '.dyt'
    print("Save Name:\t", EMBName)
    hex_out_list = []
    signature = str2hex('#EMB').split(' ')
    endian = uint16_to_hex(65534)
    header_size = uint16_to_hex(32)
    version = [uint8_to_hex(item) for item in [132, 146, 0, 0]]
    image_count = uint32_to_hex(len(DDSImages))
    unknow_0 = [uint8_to_hex(item) for item in [0, 0, 0, 0]]
    unknow_1 = [uint8_to_hex(item) for item in [0, 0, 0, 0]]
    unknow_2 = uint32_to_hex(32)
    unknow_3 = [uint8_to_hex(item) for item in [0, 0, 0, 0]]

    image_offsets = []
    for item in range(0,len(DDSImages)):
        if len(image_offsets):
            image_offsets.append(32+(8*len(DDSImages))+(len(DDSImages[item])*item))
        else:
            image_offsets.append(32 + (8 * len(DDSImages)))
        image_offsets.append(len(DDSImages[item]))
    for item in range(0,len(image_offsets),2):
        image_offsets[item] -= int(((item/2)*8)+8)
        pass
    offsets = []
    
    [offsets.extend(it) for it in [uint32_to_hex(ite) for ite in image_offsets]]
    
    temp = image_offsets[0]+32
    image_offsets = offsets
    hex_out_list.extend(signature)
    hex_out_list.extend(endian)
    hex_out_list.extend(header_size)
    hex_out_list.extend(version)
    hex_out_list.extend(image_count)
    hex_out_list.extend(unknow_0)
    hex_out_list.extend(unknow_1)
    hex_out_list.extend(unknow_2)
    hex_out_list.extend(unknow_3)
    hex_out_list.extend(image_offsets)

    hex_out_list.extend(['00']*(temp-len(hex_out_list)))
    for DDS_item in DDSImages:
        hex_out_list.extend(hexify(DDS_item).split(' '))
    
    with open(str(Location)+
              str(EMBName)+
              '.emb', 'wb') as emb:
        emb.write(bytes.fromhex(hexList2hexStrList(hex_out_list,False)))
    emb.close()
