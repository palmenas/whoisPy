#!/usr/bin/env python

import os
import random
import re
import sys
import subprocess
import time

from ipwhois import IPWhois
import pprint

def main():
    # Check if the result file exist then deletes
    if os.path.isfile('./result.txt'): os.remove('./result.txt')

    # Number of args. The second is the file which the script will iterate
    if len(sys.argv) >= 2:

        # Calculate the percentage
        totalLines = 1
        currLine = 1

        with open(sys.argv[1]) as fh:
            for line in fh:
                totalLines += 1
        print('Iterating through {}, checking {} IP addresses...'.format(sys.argv[1], totalLines))

        with open(sys.argv[1]) as fh:
            for line in fh:
                with open('./result.txt', 'a') as fw:
                    perctFile = 100
                    ip = re.sub('\n', '', line)
                    print("Analysis:{}. {}% remaining".format(ip, perctFile))
                    try:
                        obj = IPWhois(ip).lookup_rdap()
                        perctFile = 100 - (currLine*100) / totalLines
                        currLine += 1
                        fw.write(pprint.pformat(obj))

                    except Exception as e:
                        print("Could not lookup IP {0}: {1}".format(ip, e))
                        with open('error.txt', 'a') as flError:
                            flError.write("Could not lookup IP {0}: {1}\n".format(ip, e))
                    
                    # Wait for next query
                    sleepTime = random.randint(1,10)
                    time.sleep(sleepTime)

    else:
        print 'Usage: ./check_ips <file-ip.txt>'
        sys.exit()

if __name__ == '__main__':
    main()
