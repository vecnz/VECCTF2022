import secrets, os, time, threading
import pow

difficulty = 6
hexdigest_size = 32

user_challenge = pow.Pow(hexdigest_size, difficulty, secrets.token_hex().encode())
user_challenge.create_challenge()

print(f"Arrh, solve me challenge such that sha256({user_challenge.hash} + suffix) ends with {user_challenge.chall}")
user_suffix = input("Your suffix: ")

if len(user_suffix) % 2 != 0:
    print("suffix must contain an even amount of characters")
    exit(1)

if not user_challenge.check_solution(user_suffix):
    print('Wrong suffix')

print('Correct suffix')
os.system('/spidermonkey_build/mozilla-unified/obj-normal-x86_64-pc-linux-gnu/dist/bin/js')

def call_js():
    os.system('/spidermonkey_build/mozilla-unified/obj-normal-x86_64-pc-linux-gnu/dist/bin/js')


t = threading.Thread(target=call_js)
t.daemon = True
t.start()

time.sleep(60)