#/usr/bin/python

import datetime
#import os
import glob2

"""
Then create a script that merges the three text files into a new text file
containing the text of all three files. The filename of the merged text file
should contain the current timestamp down to the millisecond level.
E.g. "2016-06-01-13-57-39-170965.txt".
"""

filename = datetime.datetime.now()
samplefiles = glob2.glob('file*')
#print((filename.strftime("%Y-%m-%d-%H-%M-%S-%f")))

with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'a+') as myoutput:

    for samplefile in samplefiles:
        sf = open(samplefile, 'r')
        #line = sf.read()
        myoutput.write(sf.read() + "\n")
        #print(line)


