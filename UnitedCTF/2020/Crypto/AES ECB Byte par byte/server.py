from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

flag = 'FLAG-1234567aaaaaaaaaaaaa65'

key = Random.get_random_bytes(16)
aes = AES.new(key, AES.MODE_ECB)

while True:
    print("""ECB Crypto Menu
1. Encrypt flag
2. Encrypt flag (hex name)
3. Exit
""")
    choice = input("> Your choice: ").strip()

    if choice not in "123" or choice == "":
        print("Invalid choice.")
        continue

    if choice == "1":
        name = input("> Please enter your name: ").encode()
    
    if choice == "2":
        name = bytes.fromhex(input("> Please enter your name (hex format): "))

    if choice == "3":
        print("Goodbye!")
        break
    
    data = name + flag.encode()
    print('Encrypting', pad(data, 16))
    print(f"Result: {aes.encrypt(pad(data, 16)).hex()}")
