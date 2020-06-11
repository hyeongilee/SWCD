#!/usr/bin/python

import sys, getopt
from dv import AedatFile
import scipy.io as sio
import numpy as np
import imageio

class Struct:
    pass

def main(argv):
    inputfile = ''
    outputfile = ''
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg    

    data = {'aedat': out}

    with AedatFile(inputfile) as f:
        
        fps = 30.0
        dt = 1/(fps/1000.0)
        I = np.zeros((240,320))
        prev_time = 0
        initial_time = 1588242864305911 #modify the value
        for e in f['events']:
            time = (e.timestamp - initial_time)//1000
            time = int(time//dt)
            x = e.x
            y = e.y
            if(prev_time != time):
                imageio.imwrite('images/'+str(prev_time)+'.png', I)
                I = np.zeros((240,320))
            I[y][x] = 255.0
            prev_time = time
            
    out.data.polarity.numEvents = len(out.data.polarity.x)
    sio.savemat(outputfile, data)
    
if __name__ == "__main__":
   main(sys.argv[1:])
