import os


path = os.getcwd()
print(path)

data_folder = os.path.join(path, "data")

if not os.path.exists(data_folder):
    os.mkdir(data_folder)

file_path = os.path.join(data_folder, "registro.txt")

if not os.path.exists(file_path):
    file = open(file_path, "w")
    file.write("Name, Age\n")
    file.close()

