
https://docs.python.org/3/

we will be using few modules
- csv module ()
- glob module
- shutil module


glob - u need to run the script from operator import getitem
from python_udemy_course_by_ardit_sulce.Day_15_Built_in_Tools__VersionControl_Standard_Modules_Git.e2 import data
from the folder where the script resides

csv.reader() - this function returns and iterator which needs to be converted to a list

using json data

import json

json.load() - json string to python datastructure



[
    { 
        "question_test": "What are Dolphins?",
        "alternatives": ["Amphibians", "Fish", "Mammals", "Birds"],
        "correct_answer": 3
    },
    { 
        "question_test": "What occupies most of the Earth's Surface?",
        "alternatives": ["Land", "Water"],
        "correct_answer": 2
    }

]


#installin git

brew install git 

adding git to the repo..
git init

to check satus
git status

add files to tracking
git add . 

commit chnages 
git commit -m "initial commit"


git remote add origin <REPO_URL>

git push


git checkout vs git reset

git checkout changes branches
eg. git checkout -b features

git reset moves head, 

git reset --soft HEAD~1
Removes commit
Keeps changes staged
Safe for fixing commit messages

when to use: “I want to redo my last commit”


git reset HEAD~1

Removes commit
Keeps changes unstaged
when to use: “Undo commit but keep my code”


git reset --hard HEAD~1
Removes commit
Deletes changes permanently ❌

when to use: “I want to nuke everything and go back”

newer git prefers 
git switch #for changing branches