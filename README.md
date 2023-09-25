### Install: 
```bash
cd [Path to where you want to save the .bat and python scripts]
Then add that same path to your System- or User- Variables as a path under "Path"

git clone "https://github.com/TheOriginalAn3/PPSPM"

cd ProjectInitializationAutomation
pip install PyGithub

now you can use the 'pj' command in your terminal
```

### Usage:
```ps1
To create a repo and folder type in 'pj create <name of your folder/project>'
To remove/delete a repo and folder type in 'pj remove <name of your folder/project>'
To resume(open) work on a project type in 'pj open <name of your folder/project>'
To open a folder type in 'pj open <name of your folder/project>'
To open the Projects folder saved as a Sys-Var type 'pj open'
```

### Env Vars:
```ps1
ProjectsPath=[Path to Projects folder]
gt = [Your GitHub Token]
```
