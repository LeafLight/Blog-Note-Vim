#notevim_utils.py
########################################
#import
import json
import sys
import getopt
import os
import time
from os.path import expanduser
########################################
#utils_func
# get the note dir of the name defined by '-n'
# 'BlogDir' is reserved for the blog Directory of Hexo
def GetTheDir(filename=None):
    #skip the first arg. : the name of this script
    with open("/".join(__file__.split("/")[:-1])+"/notevimFileDir.json", 'r') as f:
        DirDict = json.load(f)
    return DirDict[filename]
# list all the note and their dirs
def ListTheNote():
    with open("/".join(__file__.split("/")[:-1])+"/notevimFileDir.json", 'r') as f:
        DirDict = json.load(f)
        print("All of the notes and their directories:")
        print("________________________________________")
        for key,value in DirDict.items():
            print(key,value)
# replace ~ in filePath because python don't use it as home dir in default
def ReplaceTildeInDir(filePath):
    if filePath[0] == '~':
        filePath = filePath.replace('~',expanduser("~"))
    return filePath
# get the file name of the note by splitting the file path
def get_filename(filePath):
    return filePath.split('/')[-1]
# convert time stamp into time in format defined by time.asctime()
def TimeStampToTime(timestamp):
    return time.asctime(time.localtime(timestamp))
# get the modification time of the file referred
def get_ModifyTime(filePath, convert=False):
    mtime = os.path.getmtime(ReplaceTildeInDir(filePath))
    if convert :
        mtime = TimeStampToTime(mtime)
    return mtime
# get the corresponding blog path of the note by spliting and catenating
def get_BlogDir(filePath):
    return GetTheDir("BlogDir")+get_filename(filePath)
    #list the names of the code
########################################
#main
argv = sys.argv[1:]
try:
    #short options mode
    opts, args = getopt.getopt(argv,'n::lc:u:')
except:
    print('Error: Invalid option(s), from notevim_utils.py')

for opt,val in opts:
    if opt in ['-n']:
        #name of the note
        filename = val
        #get the directory of the note and edit it
        os.system('vim %s'%(GetTheDir(filename))) 
    if opt in ['-l']:
        #list the names of the note
        ListTheNote()
    if opt in ['-c']:
        #copy the note into Blog dir
        filename = val
        cmd = 'cp %s %s'%(GetTheDir(filename), get_BlogDir(GetTheDir(filename))) 
        os.system('cp %s %s'%(GetTheDir(filename), get_BlogDir(GetTheDir(filename))))
        print("command(s) executed:")
        print("________________________________________")
        print(cmd)
    if opt in ['-u']:
        #update the specifc file(rm the old one and cp the new one)
        filename = val
        filePath = GetTheDir(filename)
        #get two modification time stamps respectively
        raw_file_mtime = get_ModifyTime(filePath, convert=True)
        gbs_file_mtime = get_ModifyTime(get_BlogDir(filePath), convert=True)
        print("raw file modification time: ",raw_file_mtime)
        print("blg file modification time: ",gbs_file_mtime)
        print("________________________________________")
        print("Update the old one?[Y/n]")
        while True:
            Yn = input()
            if (Yn == 'y')|(Yn == 'Y'):
                if raw_file_mtime<gbs_file_mtime:
                    os.system('rm %s'%(filePath))
                    os.system('cp %s %s'%(get_BlogDir(GetTheDir(filename)), GetTheDir(filename)))
                    break
                else:
                    os.system('rm %s'%(get_BlogDir(filePath)))
                    os.system('cp %s %s'%(GetTheDir(filename), get_BlogDir(GetTheDir(filename))))
                    break

            elif (Yn == 'n')|(Yn =='N'):
                break
            else:
                print("Invalid input,Try again...[Y/n]")

                

