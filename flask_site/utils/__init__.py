import os

cur_dir = os.getcwd()
parrent_dir = os.path.abspath(os.path.join(cur_dir, os.pardir))

import sys
sys.path.append(parrent_dir)
