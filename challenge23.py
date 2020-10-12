# challenge 23
# Function renameimages() takes a list of filenames in the directory and path of the directory, and renames .jpg files


import os


def renameimages(filelist, path):

    count = 1

    for file in filelist:
        extension = file.split(".")[-1].lower()
        if extension != "jpg":
            continue
        newfile = str(count) + file[0].upper() + file[1:]
        
        src = os.path.join(path,file)
        dst = os.path.join(path,newfile)

        os.rename(src,dst)

        count+=1


def main():
    path = os.getcwd()
    files= ["aaa (1).jpg","aaa .txt","aaa (2).jpg","aaa (3).jpg","aaa (4).jpg","aaa (5).jpg","aaa (6).jpg","aaa (7).jpg"]

    renameimages(files,path)

if __name__ == "__main__":
    main()
