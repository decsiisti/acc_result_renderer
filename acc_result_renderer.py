#!/usr/bin/env python3

import sys, getopt
import os.path
import json
from acc_result import AccResult
from tabulate import tabulate

def main(argv):
    inputfile = ""
    opts, args = getopt.getopt(argv, "hi:", ["input="])
    for opt, arg in opts:
        if opt == "-h":
            print('acc_result_renderer.py -i <input file>')
            sys.exit()
        elif (opt in ("-i", "--input")):
            inputfile = arg

    if not os.path.isfile(inputfile):
        print('input file not specified')
        sys.exit()
        
    with open(inputfile, 'r') as file:
        jsonstring = json.loads(file.read())
        result = AccResult.from_dict(jsonstring)
        print(tabulate(result.getResultTable(), headers = ["No.", "Driver", "Car"]))
    
if __name__ == "__main__":
    main(sys.argv[1:])