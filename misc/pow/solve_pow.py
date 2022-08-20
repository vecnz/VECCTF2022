import hashlib, time, sys


chall = bytes.fromhex(sys.argv[2]) #bytes.fromhex('88888')

prefix = sys.argv[1] #'4063853ede9ed227871a1967c0ae36cceea2c1b3b72d8d8aae6de1b7b92d15aa'

'''
def is_valid(digest):
    return digest[:difficulty] == chall
'''

def is_valid(digest):
    '''
    Converts to a byte array and checks if the last bytes are equal to the challenge.
    '''

    byte_view = bytes.fromhex(digest)
    hashed_bytes = hashlib.sha256(byte_view).digest()
    return hashed_bytes.endswith(chall)

start_time = time.time()
i = 0
while True:
    i += 1

    #Removes 0x from the beginning of the string
    hex_i = hex(i)[2:]

    #Makes sure that the length of hex_i is multiple of 2
    if len(hex_i) % 2 != 0:
        hex_i = '0' + hex_i

    s = prefix + hex_i

    if is_valid(s):
        print(s)
        print(i)
        break

print("Took: " + str(time.time() - start_time))

print(s + " + " + hex_i)
print("hashes to")
print(hashlib.sha256(bytes.fromhex(s)).hexdigest())