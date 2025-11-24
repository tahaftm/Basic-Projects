import os
import shutil
source = r"C:/Users/DELL/Desktop/machine learning/CodeAlpha intership challenges/source"
destination = r"C:/Users/DELL/Desktop/machine learning/CodeAlpha intership challenges/destination"
for i in os.listdir(source):
    # print(i)
    if i.lower().endswith(".pdf"):
        shutil.move(os.path.join(source, i), os.path.join(destination,i))