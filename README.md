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

# class00
    00. Dev Setup
    Installing IDE/Editor
    Installing Python and local setup
    Github access, creating project


# class01

        git commands
    markdown syntax
    daily activity and usage

    01.Introduction
        Importance of Python
        Two versions of Python (2.x & 3.x)

# class02
       
    PEP 8 Guidelines (https://peps.python.org/pep-0008/)
    Shebang line
    Indendation Issue and best practices
    built-in functions
    print function
    Script mode vs interactive mode
    Jupyter notebook usage
    Ascii and Unicode characters


# class03

    Comment Operator
    keywords and Identifiers
    Line continuation and statement separator operators

    02.Basics
        Arithmetic operations
            +, -, , /, //, %, *
            divmod() function
            compound opertions

    Assignments:

        1) try to the sum of digits in a integer number, using divmod()
        2) If a clock has revolved for 32 times, and is half way, how many days completed

# class04-1

        Practical Problem solving
        working with complex numbers
        abs() function
        Operator precedence in Arithmetic operations

    Assignments:

        1) savings Bank 
        2) Bank loan
            simple interest 
            compund interest
        3) convert from hex to oct , and vice versa
        4) feet to cms conversion    

# class05

    String operations
    Usage of single, double and triple quotes
    len() function
    Indexing and Slicing Strings

# class06

    string attributes
    String formatting: old & new styles, f-strings
    bytearray() and byte() strings
    unicode strings

# class07

    string attributes
    String formatting: old & new styles, f-strings
    bytearray() and byte() strings
    unicode strings

# class08
    
    String formatting: old & new styles, f-strings
    unicode strings

# class09

     bytearray() and byte() strings
    Usage of help
    Usage of pydoc

    03.Language Components
        Relational Operations
        Logical Operations
    
# class10

        Boolean Operations
    Bitwise Operations
    Identity Operations
        Dual Memory management Strategy
    range() function
    Conditional Operations

# class11

        Structural Pattern Matching
    Loops: for & while, break, continue, pass, sys.exit
    # Assignment: Try these break, continue, pass, on a for loop example

# class12

        Walrus Operator

04.Exception Handling
    Exceptions Hierarchy
    Different types of errors, error vs exception and exception groups
    Handling single and multiple exceptions
    raising exceptions
    asserts
    traceback
    exception Groups
    warnings

# class13

    05.Debugging
    Importance of logical errors
    Debugging with pydevd
    Debugging with pdb, ipdb
    breakpoint() function
    PYTHONBREAKPOINT environment variable usage
    post analyses of executed script

# class14

    06.Collections
    Lists

# class15

    Copy Problem - shallow copy vs deepcopy
    Tuples & namedtuples
    Immutability & unpacking
    Sets
        attributes, operations

# class16

        fronzensets
    Dictionaries
        zip() function
        workaround for switch case
    Comprehensions
    Working with Iterables - sum(), max(), min()