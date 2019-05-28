import os
import sys

# make a list of repositories where we have to get the git log history
# we should made this step dynamic by giving the repository names as input to the script

repo_list=["server","mgateway","html5","toolkit"]

# check for the existency of directory
# make an empty list to store the json data from each directory

out_put=[]

for i in repo_list:
  os.chdir(os.path.dirname(sys.argv[0]))
  os.chdir("path/i")  # /home/usr/GIT_MIGRATION/server or we could automate this by searching the path by directory name
  report=os.popen('<command>').read()
  out_put.append(report)
print(out_put)

# make sure that this out_put is in json format
# we should customize the output using inputs that are passed by the user

# change the json format into excel format
# make the directory with the name of date_report_ondot
# email notification



=============================================
os.chdir('c:\\gfg_dir') 
  
# varify the path using getcwd() 
cwd = os.getcwd() 
  
# print the current directory 
print("Current working directory is:", cwd)
==============================================
os.chdir(os.path.dirname(sys.argv[0]))
==============================================
# cronr job format
* * * * * /home/udi/foo/bar.py
==============================================
#This will change your current working directory to so that opening relative paths will work:

import os
os.chdir("/home/udi/foo")
#However, you asked how to change into whatever directory your Python script is located, even if you don't know what directory that will be when you're writing your script. To do this, you can use the os.path functions:

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
#This takes the filename of your script, converts it to an absolute path, then extracts the directory of that path, then changes into that directory.
=================================================
