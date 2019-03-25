import os
import sys

digits = [str(i) for i in range(10)]

# def Rename(args):
def Rename(args='./'):
    files = os.listdir(args)

    for File in files:
        if len(File.split(".")) > 2:
            continue
        file_name, file_type = File.split(".")
        if file_type == "py" and file_name[0] in digits and "_" in file_name:
            # print(file_name)
            file_num = file_name.split('_')[0]
            file_num = str(int(file_num)) 
            if len(file_name.split('_')) > 1:
                a = str(file_num) + '.' + ''.join(file_name.split('_')[1:]) + '.py'
                print(File+'-->'+a)
                os.rename(args+File,args+a)

Rename()