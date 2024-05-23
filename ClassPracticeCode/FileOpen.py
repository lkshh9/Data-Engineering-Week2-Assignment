import os


f = open("demofile")

print(f.read())

# Read Only Parts of the File
print(f.read(5))

# You can return one line by using the readline() method:
print(f.readline())

for x in f:
    print(x)

# f.close()

f = open("demofile2", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:

f = open("demofile2", "r")
print(f.read())

# f = open("myfile", "x")
os.remove("myfile")

if os.path.exists("myfile"):
    os.remove("myfile")
else:
    print("The file does not exist")
