import struct




def hex_to_float(HEXLEN4) -> int:
    tempHex = ''
    if type(HEXLEN4) == list:
        tempStr = ''
        for i in HEXLEN4:
            tempStr += i
        tempHex = tempStr
    elif type(HEXLEN4) == str:
        tempHex = HEXLEN4
    FLOAT = 'f'
    BYTES = bytes.fromhex(tempHex)
    Structure = '<' + FLOAT * (len(BYTES) // struct.calcsize(FLOAT))
    numbers = struct.unpack(Structure, BYTES)
    return numbers[0]

def vertHex2Float(HEX: list):
    vertXYZ = []
    for x in HEX:
        XYZ = []
        for y in x:
            tempHex = ''
            for z in y:
                tempHex += z
            FLOAT = 'f'
            BYTES = bytes.fromhex(tempHex)
            Structure = '<' + FLOAT * (len(BYTES) // struct.calcsize(FLOAT))
            numbers = struct.unpack(Structure, BYTES)
            XYZ.append(numbers[0])

        vertXYZ.append(tuple(XYZ))
    return vertXYZ

def hex2float(HEXLEN4):
    StR = ''
    if type(HEXLEN4) == list:
        for h in HEXLEN4:
            StR += h
    elif type(HEXLEN4) == str:
        if ' ' in HEXLEN4:
            StR = HEXLEN4.replace(' ','')
        else:
            StR = HEXLEN4
    FLOAT = 'f'
    BYTES = bytes.fromhex(StR)
    Structure = '<' + FLOAT * (len(BYTES) // struct.calcsize(FLOAT))
    numbers = struct.unpack(Structure, BYTES)
    #print(numbers)
    return numbers[0]


def hexToHalfFloat(HEXLEN2:list):
    hexInput = HEXLEN2
    tempHex = hexInput[0]+hexInput[1]
    HALF = 'e'
    BYTES = bytes.fromhex(tempHex)
    Structure = '<' + HALF * (len(BYTES) // struct.calcsize(HALF))
    numbers = struct.unpack(Structure, BYTES)
    return numbers[0]



def hexToShort(HEXLEN2: list, intType:int,endian: bool=False):
    if endian:
        tempHex = HEXLEN2[1] + HEXLEN2[0]
    else:
        tempHex = HEXLEN2[0] + HEXLEN2[1]
    validInts = [8,16,32,64]
    if intType in validInts:

        return int(tempHex,16)
    else:
        raise ValueError('intType must be one of the following:\n',  validInts)