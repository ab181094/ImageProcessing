import shutil, os

src = "E:\\ImageProcessing\\BRODATZ Training"
dst = "E:\\ImageProcessing\\Training Data\\Images"

# shutil.copy(src, dst, follow_symlinks=True)

for filename in os.listdir(src):
    newdir = src + "\\" + filename
    for file in os.listdir(newdir):
        image = newdir + "\\" + file
        shutil.copy(image, dst, follow_symlinks=True)
