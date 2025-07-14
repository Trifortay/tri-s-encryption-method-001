import hashlib
import time
import os

pythonpath = os.path.dirname(os.path.abspath(__file__))
os.chdir(pythonpath)
os.makedirs()

dictionarysize= {
    1:"1m",     2:"2m",     3:"4m",
    4:"8m",     5:"16m",    6:"32m",
    7:"64m",    8:"128m",   9:"256m",
    10:"512m", 11:"1024m", 12:"2048m"}

def encrypt(key):
    pass

def decrypt(key):
    pass

print("Make sure you want the folder that you wanna Encrypt or Decrypt is in this folder where this Python script is.\nAlso make sure if you used this before, the folder this program creates is empty.")
time.sleep(1)
action1="\0"

while True:
    while action1 != "e" and action1 != "d":
        action1=input("Encrypt or Decrypt? (e/d): ").lower()
    if action1 == "e":
        print("This will encrypt everything ")
        encrypt()
    
    

