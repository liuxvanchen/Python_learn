import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def xor_encrypt_decrypt(data,key):
    #判断是否是字节类型，isinstance用来判断指定数据是否是某一类型，not来反转结果进行下一步判断
    if not isinstance(data,bytes):
        data=data.encode()
    if not  isinstance(key,bytes):
        key=key.encode()

    key_length=len(key)#判断密钥是否存在
    if key_length==0:
        raise ValueError("密钥不能为空。")

    result=bytearray()#bytearray 是一个可变的字节序列类型，类似于 bytes，但 bytearray 对象允许你修改其内容。
                        # 你可以使用 bytearray 来存储、修改和操作字节数据。
    for i in range(len(data)):
        key_index=i%key_length
        result.append(data[i]^key[key_index])#异或操作
    return bytes(result)


# 加密数据
encrypted_data = xor_encrypt_decrypt(b"Hello, World!", b"SecretKey")
print("加密后的数据:", encrypted_data)

# 解密数据
decrypted_data = xor_encrypt_decrypt(encrypted_data, b"SecretKey")
print("解密后的数据:", decrypted_data.decode())

