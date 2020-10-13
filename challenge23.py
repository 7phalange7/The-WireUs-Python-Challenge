# challenge 23

import os


def renameimages(filelist, path):

    count =1

    for c,file in enumerate(os.listdir(path)):

        if file in filelist:
            continue
        extension=file.split(".")[-1].lower()
        if extension != "jpg":
            continue

        newfile=str(count) + file[0].upper() + file[1:]

        src=os.path.join(path, file)
        dst=os.path.join(path, newfile)

        os.rename(src, dst)

        count += 1


def main():
    path=os.getcwd()
    files=["aaa (1).jpg", "aaa (2).jpg"]  # files not to be renamed

    renameimages(files, path)

if __name__ == "__main__":
    main()
