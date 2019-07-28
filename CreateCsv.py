import shutil, os

src = "E:\\ImageProcessing\\Training Data\\Images"

file = open("E:\\ImageProcessing\\Training Data\\dataset.csv", "w")

headers = "filepath,angle,class\n"
file.write(headers)

for filename in os.listdir(src):
    filepath = src + "\\" + filename
    classname = filename.split("_", 2)[0]
    angle = filename.split("_", 2)[1]

    data = filepath + "," + angle + "," + classname + "\n"
    file.write(data)

    print(filepath)

file.close()