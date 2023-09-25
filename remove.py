import sys
import os
import shutil
from github import Github

foldername = str(sys.argv[1])                 # args variable from .bat
path = os.environ.get('ProjectsPath')         # get projects directory to the env vars
token = os.environ.get('gt')                  # get GitHub token from the env vars
_dir = path + '/' + foldername

ghub = Github(token)
user = ghub.get_user()
login = user.login

# Check if the repository already exists
existing_repo = None
try:
    existing_repo = user.get_repo(foldername)
except Exception as e:
    pass

# If the repository exists, delete it
if existing_repo:
    existing_repo.delete()
    print(f'{foldername} repository on GitHub deleted.')
else:
    print(f"{foldername} is not a repository on GitHub")

try:
    # Check if the local folder exists and delete it
    if os.path.exists(_dir):
        try:
            # Use the os module's rmtree function to delete the directory and its contents
            shutil.rmtree(_dir)
            print(f"Directory '{_dir}' and its contents have been deleted.")
        except FileNotFoundError:
            print(f"Folder '{_dir}' does not exist.")
    else:
        print(f"The directory '{_dir}' does not exist.")
except OSError as e:
    print(f"Error: {e}")
    print("Please remove Residual files manually. Use 'pj open' to open the Projects folder")
except Exception as e:
    print(f"An error occurred: {e}")