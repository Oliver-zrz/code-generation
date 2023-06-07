import shutil
import os
from extractFunc import ExtractFuncs

PATH = '/home/data/caoy/data'
MOVETO = '/home/data/caoy/more_than_40_data'

e = ExtractFuncs()
files = os.listdir(PATH)
for f in files:
    fp = os.path.join(PATH, f)
    funcs, funcsname = e.getFuncs(fp)
    length = 0
    if 'func_1' in funcsname:
        i = funcsname.index('func_1')
        func = funcs[i]
        tmp = func.splitlines()
        for i in tmp:
            if not i.strip():
                tmp.remove(i)
        length = len(tmp)

    if length > 40:
        move_to = os.path.join(MOVETO, f)
        shutil.move(fp, move_to)
    
    print(f'Done: {fp}')