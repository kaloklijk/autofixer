''' 
This project is for automatically fixing bugs and automatically making your code beautiful. It is still not completed
lots of samples of bugs are required to complete this program.
----------------------------------------------------------------------------------------------------------------------
usage:
python codefixer.py [filename]
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
    def __init__(self):
        # skeleton for the class for fixing bugs
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

        


    def conanfix(line):
        '''
        add back : in the end of line if needed
        '''
        if line[-2] != ":":
            line = line[:-1] + ":" + line[-1:]
        return line

    def indentation(line, degree):
        '''
        for doing indentation automaticallly for degree times
        '''
        for i in np.arange(degree):
            line = "    "+line
        return line

    def iffix(line):
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

    def forfix(line):
        '''
        automatically fixing bugs in for statement
        '''

        line = fix.conanfix(line)
        # 
        # return
        return line

    def typefix(line):
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
    def linefixer(line):
        ''' 
        automatically fix bugs in your program
        '''
        global indent
        global dedent
        global preline_indent
        dedent = 0
        # parameters
        line_indent = (len(line) - len(line.lstrip()))/4
        length = len(line)
        # indentation comparison
        indentdiff = preline_indent-line_indent
        if indentdiff > 0:
            indent -= indentdiff
        preline_indent = line_indent
        # dedent everything for easily bug fixing
        line = line.lstrip()
        # { # } operator for not fixing the line
        if "#" in line:
            return line
        # if, while statement fixing
        if "if" in line or "while" in line:
            indent += 1
            dedent += 1
            line = fix.iffix(line)
        # for statement fixing
        if "for" in line:
            indent += 1
            dedent += 1
            line = fix.forfix(line)
        # automatic indentation
        line = fix.indentation(line, indent-dedent)
        # return the fixed line of code
        print([indent, dedent])
        
        return line


    # driver code
    def codefixer(file):
        '''
        automatically fix bugs in the program
        '''
        new_lines = []
        with open(file, "r") as f:
            f.seek(0)
            lines = f.readlines()
            for line in lines:
                new_lines.append(fix.linefixer(line))
        with open(file, "w+") as f:
            f.writelines(new_lines)

        # execute the current file after fixing the code
        exec(open(file).read())


def codefixer(file):
    fix.codefixer(file)


if __name__ == '__main__':
    try:
        if sys.argv[1] == "self":
            codefixer(__file__)
        else:
            filename = sys.argv[1]
            codefixer(filename)
    except:
        print("file name required")

