from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


key = get_random_bytes(16)

flag = open('flag.txt','rb').read().strip()

def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return ct_bytes, cipher.iv

def decrypt_data(data, iv):
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.decrypt(bytes.fromhex(data))
    return unpad(ct, AES.block_size)

print("Hey, you look like a smart pirate, can you use CBC bit flipping to get the flag?")
msg = b"pirates=0"
print(f"Current Auth Message is: {msg.decode('utf-8')}")
ct_bytes, iv = encrypt_data(msg)
enc = iv.hex() + ct_bytes.hex()

print(f"Encrypted auth message: {enc}")
enc_msg = input("Give me Encrypted msg in hex: ")
try:
    final_dec_msg = decrypt_data(enc_msg, iv)

    if b"pirates=1" in final_dec_msg:
        print('Yarr\' you got it, now for a reward.')
        print(flag)
        exit()
    else:
        print(final_dec_msg)
        print('Nope, try again.')
        exit()
except Exception as e:
    print(e)
    print('Something went wrong and we had to throw it all overboard, bye.')