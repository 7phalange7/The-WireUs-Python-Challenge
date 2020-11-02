# challenge 47

import os


def find_files(home):
    fname = []
    for root, d_names, f_names in os.walk(home):
        for f in f_names:
            fname.append(os.path.join(root, f))

    for i in fname:
        print(i)


def main():

    curr_dir = os.getcwd()
    find_files(curr_dir)



if __name__ == "__main__":
    main()
