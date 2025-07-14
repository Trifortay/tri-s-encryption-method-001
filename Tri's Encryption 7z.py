import hashlib
import random
import time
import os

pythonpath = os.path.dirname(os.path.abspath(__file__)) # Grabs this python script location
os.chdir(pythonpath)                                    # Changes current terminal to the python script
os.makedirs("input",exist_ok=True)
os.makedirs("output",exist_ok=True) 


dictionarysize= {
    1:"1m",     2:"2m",     3:"4m",
    4:"8m",     5:"16m",    6:"32m",
    7:"64m",    8:"128m",   9:"256m",
    10:"512m", 11:"1024m", 12:"2048m"}

dsize_display=" 1: 1MB (Very low compression but very fast)\n 2: 2MB\n 3: 4MB\n 4: 8MB\n 5: 16MB\n 6: 32MB\n 7: 64MB (Good balance between compression ratio and speed)\n 8: 128MB\n 9: 256MB (Use if you want very strong compression)\n10: 512MB\n11: 1GB (Overkill usually. Requires a lot of RAM.)\n12: 2GB (VERY OVERKILL! Requires an absurd amount of RAM.)"

#print(dsize_display)

def hashing(newkey):
    newkey=newkey.encode('utf-8')
    start_time=time.perf_counter_ns()
    for x in range(1000000):
        newkey=hashlib.sha3_512(newkey).digest()
        if (x+1) % 50000 == 0:
            print(f"\rSHA 512 Hash {x+1:7}/1000000 finished @ {(x+1)/(time.perf_counter_ns()-start_time)*1e9:9.2f} hashes per second",end="",flush=True)
    
    start_time=time.perf_counter_ns()
    for x in range(1000000):
        newkey=hashlib.sha3_256(newkey).digest()
        if (x+1) % 50000 == 0:
            print(f"\rSHA 256 Hash {x+1:7}/1000000 finished @ {(x+1)/(time.perf_counter_ns()-start_time)*1e9:9.2f} hashes per second.",end="",flush=True)
    
    print()
    return newkey.hex()

def encrypt(dsize,masterkey):
    pass

def decrypt(masterkey):
    pass

print("Make sure you want the folder that you wanna Encrypt or Decrypt is in the input folder where this Python script is.\nAlso make sure if you used this before, the folders are empty.")
time.sleep(1)
action1="\0"
enckey="\0"
masterkey="\0"
salt=format(random.randint(0,4294967295),'08x')


while True:
    while action1 != "e" and action1 != "d":
        action1=input("Encrypt or Decrypt? (e/d): ").lower()
    if action1 == "e":
        print("This will Encrypt everything in the directory [input/].")
        print("Input Dictionary size for LZMA2.")
        print(dsize_display)
        dsize = 0
        while  dsize < 1 or dsize > 12:
            try:
                dsize=int(input("\nDictionary Size (Input 1-12): "))
            except ValueError:
                continue
        
        enckey=input("Now enter a password: ")
        newkey="".join([enckey,salt])
        masterkey=hashing(newkey)
        print(masterkey)
        
        #print(newkey)
        encrypt(dsize,masterkey)
        break
    elif action1 == "d":
        print("This will Decrypt everything in the directory [output/].")
    

