
import os
import shutil
import sys


script_head_name = sys.argv[0].rsplit('.py')[0]
if os.path.exists(script_head_name):
    shutil.rmtree('./{0}'.format(script_head_name))
os.mkdir('./{0}'.format(script_head_name))
