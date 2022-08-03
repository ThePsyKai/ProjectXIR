from .fileUtil import *
import re
from .handlingHex import vertHex2Float,hex_to_float,hexToHalfFloat,hexToShort,hex2float

from .emb_file_obj import *

import time

def Reader(fileBytes,Direct):
    fileHex = hexify(fileBytes).split(' ')
    Header = EMB_Header(fileHex)
    ReturnThese = []
    for item in range(0, Header.image_count):
        ImageName = 'DATA' + ('0' * (3 - len(str(item))) + str(item)) + '.dds'

        ImagePath = str(Direct)

        data = bytes.fromhex(
            hexList2hexStrList(
                fileHex[Header.image_pointers[item]:
                        Header.image_pointers[item] + Header.image_length[item]]))
        ReturnThese.append([ImagePath,ImageName,data])
        #fileUtil.fileWriter(name=ImageName, pathing=ImagePath, data=writeThis)
    return ReturnThese