import os
import sys
from glob import glob
from pathlib import Path

def search(channel):

    paths = Path(os.getcwd()).glob('**/*.pro',)
    for path in paths:
        with open(path,'r') as file:
            content = file.read()
            if (channel in content):
                print(path)

search(sys.argv[1])
