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
import cStringIO,operator

def indent(rows, hasHeader=False, headerChar='-', delim=' | ', justify='left',
           separateRows=False, prefix='', postfix='', wrapfunc=lambda x:x):
    """Indents a table by column.
       - rows: A sequence of sequences of items, one sequence per row.
       - hasHeader: True if the first row consists of the columns' names.
       - headerChar: Character to be used for the row separator line
         (if hasHeader==True or separateRows==True).
       - delim: The column delimiter.
       - justify: Determines how are data justified in their column. 
         Valid values are 'left','right' and 'center'.
       - separateRows: True if rows are to be separated by a line
         of 'headerChar's.
       - prefix: A string prepended to each printed row.
       - postfix: A string appended to each printed row.
       - wrapfunc: A function f(text) for wrapping text; each element in
         the table is first wrapped by this function."""
    # closure for breaking logical rows to physical, using wrapfunc
    def rowWrapper(row):
        newRows = [wrapfunc(item).split('\n') for item in row]
        return [[substr or '' for substr in item] for item in map(None,*newRows)]
    # break each logical row into one or more physical ones
    logicalRows = [rowWrapper(row) for row in rows]
    # columns of physical rows
    columns = map(None,*reduce(operator.add,logicalRows))
    # get the maximum of each column by the string length of its items
    maxWidths = [max([len(str(item)) for item in column]) for column in columns]
    rowSeparator = headerChar * (len(prefix) + len(postfix) + sum(maxWidths) + \
                                 len(delim)*(len(maxWidths)-1))
    # select the appropriate justify method
    justify = {'center':str.center, 'right':str.rjust, 'left':str.ljust}[justify.lower()]
    output=cStringIO.StringIO()
    if separateRows: print >> output, rowSeparator
    for physicalRows in logicalRows:
        for row in physicalRows:
            print >> output, \
                prefix \
                + delim.join([justify(str(item),width) for (item,width) in zip(row,maxWidths)]) \
                + postfix
        if separateRows or hasHeader: print >> output, rowSeparator; hasHeader=False
    return output.getvalue()

# written by Mike Brown
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/148061
def wrap_onspace(text, width):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).
    """
    return reduce(lambda line, word, width=width: '%s%s%s' %
                  (line,
                   ' \n'[(len(line[line.rfind('\n')+1:])
                         + len(word.split('\n',1)[0]
                              ) >= width)],
                   word),
                  text.split(' ')
                 )

import re
def wrap_onspace_strict(text, width):
    """Similar to wrap_onspace, but enforces the width constraint:
       words longer than width are split."""
    wordRegex = re.compile(r'\S{'+str(width)+r',}')
    return wrap_onspace(wordRegex.sub(lambda m: wrap_always(m.group(),width),text),width)

import math
def wrap_always(text, width):
    """A simple word-wrap function that wraps text on exactly width characters.
       It doesn't split the text in words."""
    return '\n'.join([ text[width*i:width*(i+1)] \
                       for i in xrange(int(math.ceil(1.*len(text)/width))) ])
    
if __name__ == '__main__':
    labels = ('First Name', 'Last Name', 'Age', 'Position')
    data = \
    '''John,Smith,24,Software Engineer
       Mary,Brohowski,23,Sales Manager
       Aristidis,Papageorgopoulos,28,Senior Reseacher'''
    rows = [row.strip().split(',')  for row in data.splitlines()]

    print 'Without wrapping function\n'
    print indent([labels]+rows, hasHeader=True)
    # test indent with different wrapping functions
    width = 10
    for wrapper in (wrap_always,wrap_onspace,wrap_onspace_strict):
        print 'Wrapping function: %s(x,width=%d)\n' % (wrapper.__name__,width)
        print indent([labels]+rows, hasHeader=True, separateRows=True,
                     prefix='| ', postfix=' |',
                     wrapfunc=lambda x: wrapper(x,width))
    
    # output:
    #
    #Without wrapping function
    #
    #First Name | Last Name        | Age | Position         
    #-------------------------------------------------------
    #John       | Smith            | 24  | Software Engineer
    #Mary       | Brohowski        | 23  | Sales Manager    
    #Aristidis  | Papageorgopoulos | 28  | Senior Reseacher 
    #
    #Wrapping function: wrap_always(x,width=10)
    #
    #----------------------------------------------
    #| First Name | Last Name  | Age | Position   |
    #----------------------------------------------
    #| John       | Smith      | 24  | Software E |
    #|            |            |     | ngineer    |
    #----------------------------------------------
    #| Mary       | Brohowski  | 23  | Sales Mana |
    #|            |            |     | ger        |
    #----------------------------------------------
    #| Aristidis  | Papageorgo | 28  | Senior Res |
    #|            | poulos     |     | eacher     |
    #----------------------------------------------
    #
    #Wrapping function: wrap_onspace(x,width=10)
    #
    #---------------------------------------------------
    #| First Name | Last Name        | Age | Position  |
    #---------------------------------------------------
    #| John       | Smith            | 24  | Software  |
    #|            |                  |     | Engineer  |
    #---------------------------------------------------
    #| Mary       | Brohowski        | 23  | Sales     |
    #|            |                  |     | Manager   |
    #---------------------------------------------------
    #| Aristidis  | Papageorgopoulos | 28  | Senior    |
    #|            |                  |     | Reseacher |
    #---------------------------------------------------
    #
    #Wrapping function: wrap_onspace_strict(x,width=10)
    #
    #---------------------------------------------
    #| First Name | Last Name  | Age | Position  |
    #---------------------------------------------
    #| John       | Smith      | 24  | Software  |
    #|            |            |     | Engineer  |
    #---------------------------------------------
    #| Mary       | Brohowski  | 23  | Sales     |
    #|            |            |     | Manager   |
    #---------------------------------------------
    #| Aristidis  | Papageorgo | 28  | Senior    |
    #|            | poulos     |     | Reseacher |
    #---------------------------------------------
    ===================================================
    import os
 
def main():
    
    # Create directory
    dirName = 'tempDir'
    
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")        
    
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")
    
    dirName = 'tempDir2/temp2/temp'
    
    # Create target directory & all intermediate directories if don't exists
    try:
        os.makedirs(dirName)    
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")  
        
    
    # Create target directory & all intermediate directories if don't exists
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")    
        
    
if __name__ == '__main__':
    main()
    =================================
    # printing the file paths
import sys
import os
import inspect

print "Python " + sys.version
print

print __file__                                        # main.py
print sys.argv[0]                                     # main.py
print inspect.stack()[0][1]                           # lib/bar.py
print sys.path[0]                                     # C:\filepaths
print

print os.path.realpath(__file__)                      # C:\filepaths\main.py
print os.path.abspath(__file__)                       # C:\filepaths\main.py
print os.path.basename(__file__)                      # main.py
print os.path.basename(os.path.realpath(sys.argv[0])) # main.py
print

print sys.path[0]                                     # C:\filepaths
print os.path.abspath(os.path.split(sys.argv[0])[0])  # C:\filepaths
print os.path.dirname(os.path.abspath(__file__))      # C:\filepaths
print os.path.dirname(os.path.realpath(sys.argv[0]))  # C:\filepaths
print os.path.dirname(__file__)                       # (empty string)
print

print inspect.getfile(inspect.currentframe())         # lib/bar.py

print os.path.abspath(inspect.getfile(inspect.currentframe())) # C:\filepaths\lib\bar.py
print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # C:\filepaths\lib
print

print os.path.abspath(inspect.stack()[0][1])          # C:\filepaths\lib\bar.py
print os.path.dirname(os.path.abspath(inspect.stack()[0][1]))  # C:\filepaths\lib
