# PythonBatchFeb2026
A repository with all the classes material for becoming a python developer

Install 

    git for windows

    vs code

    python
        microsoft store -- python3 (version)


git clone https://github.com/Navya416/PythonBatchFeb2026.git

first time you need to pass the credentials, when running

## Git Commands

To clone a repository (not needed in codespace, needed for local development):

    git clone https://github.com/Navya416/PythonBatchFeb2026.git

To list the local branches:

    git branch

To create a branch:

    git checkout -b class01

To see the latest local changes:

    git status

To check/verify the modified content in existing file,

    git diff 

To stage the changes:

    git add <filename>

To commit the changes:

    git commit -m "commit message"

To push the changes,

    git push origin <sourceBRanch>

    class01 -> main
    ex: git push origin class01

# Daily
To check the branch is clean,

    git status 

To checkout to the main branch

    git checkout main 

To get the latest changes

    git pull origin main 

To create new branch

    git checkout -b <NEW BRANCH NAME>

# Virtual Environment

    Isolated environment 

why needed
    - same system, multiple projects
        - different python versions 
        - same python verison, but differenet module versions

How to create Virtual Environment 
    - Virtualenv
    - venv
    - pipenv
    - poetry 
    - uv

1) Using Virtualenv
    
    Install
        pip install virtualenv
    
    create virtual environment
        python -m virtualenv .venv
    
    activate virtual environment
        linux
            source .venv/bin/activate

        windows
            .venv/script/activate

2) Using Poetry
    pip install -U pip poetry

    python -m poetry config virtualenvs.create true
    python -m poetry config virtualenvs.in-project true
    python -m poetry config installer.parallel true
    python -m poetry config installer.max-workers 5
    
    python -m poetry init
    #python -m poetry shell
    python -m poetry install --no-root

    python -m poetry env info   
    venvpath/python/Scripts/activate

    pip install poetry
    poetry add pandas        

# Course Completed

    00. Dev Setup
    Installing IDE/Editor
    Installing Python and local setup
    Github access, creating project

        git commands
    markdown syntax
    daily activity and usage

    01.Introduction
        Importance of Python
        Two versions of Python (2.x & 3.x)

    