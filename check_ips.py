#!/usr/bin/python

import os
import time
import subprocess
import re

def main():
    os.remove('./result.txt')
    with open('./ips1.txt') as fh:
        for line in fh:
            with open('./result.txt', 'a') as fw:
                line = re.sub('\n', '', line)
                fw.write('Analysis of %s' % line)
                print line
                result = subprocess.call(['whois', line])
                fw.write(result)
                # fw.write('End of Analysis')
                # time.sleep(3)

if __name__ == '__main__':
    main()
