import sys
import os

foldername = str(sys.argv[1])                 # args variable from .bat
path = os.environ.get('ProjectsPath')         # get projects directory to the env vars
token = os.environ.get('gt')                  # get GitHub token from the env vars
_dir = path + '/' + foldername

# Check if the folder exists
if os.path.exists(_dir):
    os.system(f'code {_dir}') # Open in VS Code
else:
    print(f"The folder '{_dir}' does not exist.")