# 计算modbus的crc的

def modbus_crc(data):
    crc = 0xffff
    for pos in data:
        crc ^= pos
        for i in range(8):
            if ((crc & 1)  != 0):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return ((crc & 0xff) << 8 ) + (crc >> 8)

if __name__ == '__main__':
    s = b'\x01\x03\x01\x89\x00\x02'
    s2 = modbus_crc(s)
    assert s2&0xff == 0x1d
    assert s2>>8&0xff == 0x14
    assert s2 == 0x141d
    print(hex(modbus_crc(s)))