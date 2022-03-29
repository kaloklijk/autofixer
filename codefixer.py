''' 
This project is for automatically fixing bugs and automatically making your code beautiful. It is still not completed
lots of samples of bugs are required to complete this program.
----------------------------------------------------------------------------------------------------------------------
usage:

import codefixer / from code fixer import *
## code fixing
codefixer.fix.codefixer()
.. your code ..
or 
try:
    .. your code ..
except:
codefixer.fix.codefixer()
'''

# import dependencies
import numpy as np
import os
import sys
# import icecream for debugger
#from icecream import ic
# import threading for multi-processing bug fixing
from threading import Thread
# global variables
dedent = 0
indent = 0
preline_indent = 0
# functions
class bugs:
    '''
    class for storing different types of bugs
    '''
    # skeleton for bugs storage, maybe useful in the future
    def __init__(self, buglist):
        self.buglist = buglist
    
    def add_bug(self,bug):
        self.buglist.append(bug)

class fix(bugs):
    '''
    this class is for fixing bugs
    '''
    def __init__(self, count = 0):
        # skeleton for the class for fixing bugs
        self.count = count
        pass

    def add_fixer(codelist):
        '''
        add a list of code to this class for fixing bugs
        '''
        with open("codefixer.py", "a+") as f:
            f.seek(60)
            f.write("\n")
            f.writelines(codelist)
            f.write("\n")

        


    def conanfix(self, line):
        '''
        add back : in the end of line if needed
        '''
        if line[-1] != ":":
            line = line + ":"
        return line

    def indentation(self, line, degree = 0):
        '''
        for doing indentation automaticallly for degree times
        '''
        for i in np.arange(degree):
            line = "    "+line
        return line

    def iffix(self, line):
        '''
        fixing bugs in if/while statements
        '''
        index = line.find("if")
        # single equals in if comparison
        index_eq = line.find("=")
        if (index_eq > index) and (line[index_eq-1] != "<" and line[index_eq-1] != ">") and (line[index_eq+1] != "=" and line[index_eq-1] != "="):
            line = line[:index_eq]+"="+line[index_eq:]
        # missing conan {:}
        line = fix.conanfix(line)
        # 
        # return 
        return line

    def forfix(self, line):
        '''
        automatically fixing bugs in for statement
        '''

        line = fix.conanfix(line)
        # 
        # return
        return line

    def typefix(self, line):
        '''
        automatically delete the type added in your code
        '''
        # removing all the type indicator
        if line.find("string") == 0:
            line = line[6:]
            line = line.lstrip()
        if line.find("int") == 0:
            line = line[3:]
            line = line.lstrip()
        if line.find("bool") == 0:
            line = line[4:]
            line = line.lstrip()
        if line.find("double") == 0:
            line = line[6:]
            line = line.lstrip()
        if line.find("float") == 0:
            line = line[5:]
            line = line.lstrip()
        # dictionary , missing
        if line[-1] != ":" and ":" in line:
            if line[-1] != ",":
                line = line + ","
        return line 



    ## fixing the bugs in a single line of code
    def linefixer(self, line):
        ''' 
        automatically fix bugs in your program
        '''
        global indent
        global dedent
        global preline_indent
        dedent = 0
        # parameters
        line_indent = (len(line) - len(line.lstrip()))//4
        length = len(line)
        # indentation comparison
        while preline_indent > line_indent:
            indent = indent - 1
            preline_indent = preline_indent - 1
        # dedent everything for easily bug fixing
        line = line.lstrip()
        # { # } operator for not fixing the line
        if "#" in line:
            return line
        # if, while statement fixing
        if "if" in line or "while" in line:
            indent = indent + 1
            dedent = 1
            self.iffix(line)
        # for statement fixing
        if "for" in line:
            indent = indent + 1
            dedent = 1
            self.forfix(line)

        #

        # automatic indentation
        self.indentation(line, indent-dedent)
        # return the fixed line of code
        return line


    # driver code
    def codefixer():
        '''
        automatically fix bugs in the program
        '''
        new_lines = []
        with open(__file__, "r") as f:
            f.seek(0)
            lines = f.readlines()
            for line in lines:
                new_lines.append(fix.linefixer(line)+"\n")
        with open(__file__, "w+") as f:
            f.writelines(new_lines)

        # execute the current file after fixing the code
        print(exec(__file__).read())




