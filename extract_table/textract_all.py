#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os
import time
import glob
import sys
import textract_python_table_parser as tptp

'''
    File name: testract_all.py
    Author: Shaoyu Liu
    Date created: 12/08/2021
    Python Version: 3.9
'''
#change to the directory
#cd /Users/apple/Desktop/research_fellow_documents/process_illinois/

def get_direc(direc):
    """get the lists of all files under the directory"""
    path = os.path.join(direc, direc+'png', '*png')
    direc_list = glob.glob(path)

    return direc_list
    

def main(direc):
    direc_list = get_direc(direc)
    
    for file in direc_list:
        file_code = file.split('/')[-1].split('.')[0]
        
        table_csv = tptp.get_table_csv_results(file)

        direc_new = direc + 'csv'

        output_file = '{}/{}/{}.csv'.format(direc, direc_new, file_code)

        with open(output_file, "wt") as fout:
            fout.write(table_csv)

        print('output file saved: ', output_file)

if __name__ == "__main__":
    direc = sys.argv[1]
    main(direc)
