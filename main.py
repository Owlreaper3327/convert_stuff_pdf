"""Simple console script to convert images into pdf"""
#First, we define our imports
import os
import img2pdf
import pandas as pd



#Here we'll define functions

def extract_imgs(path_to):
    """This function will perform a search in the dir you pass in the params"""
    
    imgs = []
    
    for piname in os.listdir(path_to):
        #For compatibility reasons, this code only accepts 4 formats
        if not (piname.endswith(".jpg") or piname.endswith(".png") or piname.endswith(".jpeg") or piname.endswith(".webp")):
            continue

        path = os.path.join(path_to, piname)

        if os.path.isdir(path):
            continue

        imgs.append(path)
    
    imgs.sort()
    
    return imgs

def convert_pdf(path_to, final_name, imgs):
    """This function will perform the pdf conversion and give a decent name"""

    name_f = final_name + ".pdf"

    path = os.path.join(path_to, name_f)

    cont = 0

    with open(path, "wb") as final_pdf:
        final_pdf.write(img2pdf.convert(imgs))

    print("\a")



#Here we'll define the main logic of the program

objdir = "" #variable for image's dir path
final_name = "" #defines the final name of the resultant pdf
imgs = [] #Stores the images in dir
queue = [] #queue of paths
progress = 0 #progress

while(True):
    try:
        objdir = input("Introduce the complete path to your pictures folder: ")

        if not (os.path.exists(objdir)):
            raise OSError("Path included doesn't exist")

        if not (os.path.isdir(objdir)):
            raise OSError("Wrong input, must be a folder")
        
        final_name = input("Introduce the name to your resultant file: ")

        queue.append((final_name, objdir))

    except OSError:
        print("Path you included is not valid")
        continue
    else:
        val = input("Do you want to add more files? (s/n)\n")

        if val.lower() == "s":
            continue
        else:
            break

for name, dir in queue:
    imgs = extract_imgs(dir)
    convert_pdf(dir, name, imgs)
    print("\a")
    progress += 1
    print(f"Actual progress {progress}/{len(queue)}")
    print(f"{(progress/len(queue)) * 100:.2f}% completed")

print("\a")
print("\a")
print("FINISHED!")


#Here we'll clean up