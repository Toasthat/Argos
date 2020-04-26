import numpy as np
import sys.argv
from tomlkit import parse
class Routine(object):
    def __init__(self,feed_config=None,gray_frame=False):
        if feed_config=None:
            self.feed=cv2.VideoCapture(0)
        self.frame=self.feed.read()
        #adding options for specific cameras later


def load_config(toml_file, table):
    with open(toml_file, "r") as f:
        data = f.read()
        config = parse(data)
        print(config)
    return config[table]

if __name__=="__main__":
    #configure task
    config = load_config(toml,argv[0])
    #TODO wrap the configuration in try catch blocks    
