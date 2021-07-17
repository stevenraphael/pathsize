# Pathsize

Pathsize is a tool that displays the sizes of subdirectories and files in a given path.

## Installation

Clone the repository:
```
git clone https://github.com/stevenraphael/pathsize
```
Install the project:
```
pip install pathsize/
```


To get the sizes of all subdirectories and files contained in a path ```$PATH```, type:
```
pathsize $PATH
```
This will show up to 1000 of the largest items in the path. 
To change the number of items shown, use the ```--top``` option, followed by a number.
To only show sizes of subdirectories and not files, use the ```--nofiles``` option.