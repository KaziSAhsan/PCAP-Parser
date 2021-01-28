#!/usr/bin/env python3
##-----------------------------------------------------------------
##Program Name  - md5parser.py
##Program Dir   - Desktop/KaziAhsan
##Date          - 01/18/2021
##Programmer    - Kazi Ahsan
##Description   - Identify malware from pcap by matching hashe
##-----------------------------------------------------------------

import sys
#import hashlib
#import os

import pandas as pd
from pandas import DataFrame
import datetime
from datetime import date
import csv


def main():
    # Create a list of malware that can be found
    mal_file = {'531828e91ced7be99b989c0a64e50f56':'trojan', 
                '5e976d618a95ba3e41c77f1a5c8f1a6e':'arp', 
                'd0c2102f36e51bc5872ccbdd0e9e7d31':'wannacry1',
                '7b3baa7d6bb3720f369219789e38d6ab':'Flash Exploit',
                '1e34fdebbf655cebea78b45e43520ddf':'Java Exploit',
                '120d87d02ad7e7e8eec5654f9022d75c':'Malware',
                '5071534ded881ff35afe89934ce25b02':'Trojan'
               }

    # This dictionary will store the values if there's a malware match found
    match = {}
    
    # args will extract the filename from bash script
    args = sys.argv[1]
    # Check to ensure the program is reading the correct filename
    print("\nFile name is: "+ args)

    f        = open(args, "r")
    f1       = f.read()

    time     = date.today()
    Hash     = []
    Malware  = []


    # Loop through the mal_file dictionary and check the keys
    # against the pcap file and identify matches if there's any
    for key, value in mal_file.items():
        if key in f1:
            match[value] = key
            Hash.append(key)
            Malware.append(value)
 
    # Create a DataFrame and input all the data into it
    data = pd.DataFrame({'Date': time, 'FileName': args, 'Hash': Hash, 'Malware': Malware})

    # If there are malware found, then print out that the file
    # is infected and also print the hash and the malware name
    # if no matches found, then print out that no malware found
    if match != {}:
        print("\n\033[31m Your File is infected -- Please see the table below: ""\033[0:36m \n")# .format(match))
        print(data.to_string(justify='center', index=False))
    else:
        print("\n\033[01;33m Your File does not match any known malware")

    # Append the data to a csv file for further analysis
    with open(r'/media/sf_Shared/FromPython.csv', 'a', newline='') as f:
        data.to_csv(f, header=False, index=False)

if __name__ == "__main__":
    main()



