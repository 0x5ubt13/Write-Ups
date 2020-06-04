#!/usr/env/python3

key1 = "5dcec311ab1a88ff66b69ef46d4aba1aee814fe00a4342055c146533"
key1xor3 = "9a13ea39f27a12000e083a860f1bd26e4a126e68965cc48bee3fa11b"
key2xor3xor5 = "557ce6335808f3b812ce31c7230ddea9fb32bbaeaf8f0d4a540b4f05"
key1xor4xor5 = "7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb"
key3xor4 = "996e59a867c171397fc8342b5f9a61d90bda51403ff6326303cb865a"
keyallxored = "306d34c5b6dda0f53c7a0f5a2ce4596cfea5ecb676169dd7d5931139"

keys = [key1, key1xor3, key2xor3xor5, key1xor4xor5, key3xor4, keyallxored]

print('raw keys:\n',keys)

keys2 = []
for key in keys:
    keys2.append(int(key,16))

print('converted keys:\n',keys2)

key1 = keys2[0]
key1xor3 = keys2[1]
key2xor3xor5 = keys2[2]
key1xor4xor5 = keys2[3]
key3xor4 = keys2[4]
keyallxored = keys2[5]

print("Key 1 =", key1)
key3 = key1^key1xor3
print("Key 3 =", key3)
key4 = key3^key3xor4
print("Key 4 =", key4)
key5 = ((key1^key4)^key1xor4xor5)
print("Key 5 =", key5)
key2 = (key2xor3xor5^(key3^key5))
print("Key 2 =", key2)
flag = (keyallxored^(key1^key2^key3^key4^key5))
print("flag = ", flag)

flaghex = hex(flag) #0x666c61677b6e30745f7430305f683472445f6830703366756c6c797d
flagascii = bytes.fromhex('666c61677b6e30745f7430305f683472445f6830703366756c6c797d').decode('utf-8')
print(flagascii)
