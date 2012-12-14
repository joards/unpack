import subprocess
import os

cwd = os.getcwd()
files = os.listdir(cwd)
newcwd = os.path.join(cwd, "unpacked")

#check if unpackfolder exist
if not os.path.isdir(newcwd):
    os.mkdir(newcwd)
os.chdir(newcwd) #set unpackfolder as current working directory

#unpacks all files ending with .rar to the unpacked folder in the scripts folder
#takes directory and filelist to iterate through
def iterdir(currentdir, filelist):
    for filename in filelist:
        f = os.path.join(currentdir, filename)
        if f.endswith(".rar"):
            subprocess.call(['unrar', 'x', f])
        elif os.path.isdir(f):
            iterdir(f, os.listdir(f))


iterdir(cwd, files)

