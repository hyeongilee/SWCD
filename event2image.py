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
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('aedat4tomat.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('aedat4tomat.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is "', inputfile)
    print('Output file is "', outputfile)
    

    data = {'aedat': out}

    with AedatFile(inputfile) as f:

        # loop through the "events" stream
        fps = 30.0
        dt = 1/(fps/1000.0)
        #initial = f['events']
        I = np.zeros((240,320))
        prev_time = 0
        initial_time = 1588242864305911
        for e in f['events']:
            #print(e.timestamp)
            time = (e.timestamp - initial_time)//1000
            #print(time)
            time = int(time//dt)
            x = e.x
            y = e.y
            if(prev_time != time):
                imageio.imwrite('images/'+str(prev_time)+'.png', I)
                I = np.zeros((240,320))
            I[y][x] = 255.0
            prev_time = time
            
        
    #Add counts
    out.data.polarity.numEvents = len(out.data.polarity.x)
    #out.data.imu6.numEvents = len(out.data.imu6.accelX)
    sio.savemat(outputfile, data)
    
if __name__ == "__main__":
   main(sys.argv[1:])
