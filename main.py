"""
Usage: 
    main.py <path> [--top=<top>] [--nofiles]

    main.py -h | --help
    
Options:
    -h --help          show this screen             
    --top=<top>        how many of the largest items to show [default: 1000].
    --nofiles          excludes files in the path from being printed.
"""    

import os, sys, docopt


def listsizes(path, top, nofiles):
    """
    Prints the sizes of items (folders/files) directly contained in the given path, sorted from largest to smallest.
    
    Arguments:
    path: a path to the folder that the function works with.
    top: an integer detailing the number of items to be printed (how many of the largest items will be printed).
    nofiles: excludes files in the path from being printed if nofiles is true.
    """
    sizes = []
    # Creates a list of (file/directory, size) pairs
    for f in os.listdir(path):        
        newpath = os.path.join(path, f)
        if os.path.isfile(newpath):
            if not nofiles:
                sizes.append([f, os.path.getsize(newpath)])
        elif not os.path.islink(newpath):
            try:
                sizes.append(['<DIR> ' + f, recursivesize(newpath)])
            except PermissionError:
                print(f'Unable to fully access {f}: Permission denied')
    sizes.sort(key=lambda s: -1 * s[1])
    sizes = sizes[:top]
    alignspacing = max(len(s[0]) for s in sizes) + 5
    MB = 2 ** 20
    KB = 2 ** 10
    for s in sizes:
        if s[1] > MB:
            print(f'{s[0] : <{alignspacing}} {round(s[1] / MB, 2):.2f} MB')
        elif s[1] > KB:
            print(f'{s[0] : <{alignspacing}} {round(s[1] / KB, 2):.2f} KB')
        else:    
            print(f'{s[0] : <{alignspacing}} {s[1]} bytes')


def recursivesize(path='.'):
    """
    Given a path to a folder, gets the cumulative size of the folder, excluding simlinks contained in the folder.
    
    If no path is specified, the path defaults to the current path.
    """    
    total = 0

    for f in os.listdir(path):      
        newpath = os.path.join(path,f)
        if os.path.isfile(newpath):
            total += os.path.getsize(newpath)
        elif not os.path.islink(newpath):
            total += recursivesize(newpath)
    return total

    
def main():
    args = docopt.docopt(__doc__)
    nofiles = args['--nofiles']
    path = args['<path>']
    top = int(args['--top']) if args['--top'] else 1000
    listsizes(path, top, nofiles)
    
if __name__ == '__main__':
    main()
        
        