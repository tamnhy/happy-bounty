import os, shutil
os.makedirs("/output", exist_ok=True)
# try multiple names
for name in ["happy.jpg", "12.jpg", "happy.png", "image.jpg"]:
    if os.path.exists(name):
        shutil.copy(name, "/output/image.png")
        break
