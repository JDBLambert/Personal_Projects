# github.com/JDBLambert
# 4/16/2021
# A file generator/obfiscator meant to produce several random dummy files or to hide a specific file among several other files.
# Not very good if the other party knows what they are doing.
# But the average person will hopefully be confused as to why these files won't open and appear broken.

# Requirements:
# wordList.txt

import random
random.seed()
import os

# configs
filesCount = 5000
createTextNames = True      # False means a random string of numbers will be used.
createTextContent = True    # False means a random string of numbers will be used.
lowerFileSize = 2**4        # Only changes the amount of words/numbers that are used and not the file's actual size.
upperFileSize = 2**14       # Only changes the amount of words/numbers that are used and not the file's actual size.

# Toggle this if you just want a bunch of dummy files.
usingSpecialFile = True
fileName = "special file.txt"

with open('wordList.txt') as wordList:
    words = wordList.read().splitlines()

if not os.path.exists("files"):
    os.mkdir("files")

def generateNames(size):
    if(createTextNames):
        length = random.randrange(1, 4)
        name = random.choice(words)
        for i in range(length):
            name = name + " " + random.choice(words)
            if(bool(random.getrandbits(1))):
                break
        if(size < 10**3):
            name += ".txt"
        elif(size<10**5):
            name += ".pdf"
        elif(size < 10**7):
            name += ".png"
        elif (size < 10**9):
            name += ".mp4"
        else:
            name += ".zip"
    else:
        name = str(random.randint(10**6, 10**12))
    return name


def generateFile(specialFile = False):
    size = random.randrange(lowerFileSize, upperFileSize)
    print(size)
    name = generateNames(size)
    print(name)
    with open("files/" + name, "w") as f:
        if(specialFile):
            with open(fileName) as file2hide:
                f.write(file2hide.read())
                print("^special file")
        else:
            for i in range(size):
                if(createTextContent):
                    f.write(random.choice(words)+" ")
                    if(bool(random.getrandbits(1))):
                        f.write("\n")
                    elif(bool(random.getrandbits(1))):
                        f.write(",")
                else:
                    f.write(str(random.randint(1, 2**32)))


if __name__ == "__main__":
    # decide when the file will be swapped
    file2hideIndex = random.randrange(1, filesCount-1)
    for i in range(filesCount):
        if(usingSpecialFile and i == file2hideIndex):
            generateFile(True)
        else:
            generateFile()
