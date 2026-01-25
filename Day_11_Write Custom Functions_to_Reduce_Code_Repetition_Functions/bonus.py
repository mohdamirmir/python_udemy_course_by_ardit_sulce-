from optparse import Values
from pathlib import Path
import os

os.chdir(Path(__file__).parent)
Path("data").mkdir(exist_ok=True)
Path("data/temp.txt").touch(exist_ok=True)

def get_average():
    with open("data/temp.txt", "r") as file:
        data = file.readlines()
    
    values = data[1:]

    values = [float(i) for i in values]

    average_local = sum(values)/len(values)

    return average_local


average = get_average()
print(average)
