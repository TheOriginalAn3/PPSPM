import sys
import os

# Get sys-env-vars
path = os.environ.get('ProjectsPath')         # get projects directory to the env vars
token = os.environ.get('gt')                  # get GitHub token from the env vars
    
# Check if any argument has been passed to python
try:
    foldername = str(sys.argv[1])                 # args variable from .bat
    _dir = path + '/' + foldername
    
    # Check if the folder exists
    if os.path.exists(_dir):
        os.system(f'start {_dir}') # Use the 'start' command to open the --Project Specific-- folder in File Explorer (Windows-specific)
    else:
        print(f"The folder '{_dir}' does not exist.")
except Exception as e:
    os.system(f'start {path}') # Use the 'start' command to open the Projects folder in File Explorer (Windows-specific)