import os

path = os.getcwd()

print("Files in this directory:")

for file in os.listdir(path):
    print(file)