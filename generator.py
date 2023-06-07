import os
import argparse
from extractFunc import ExtractFuncs

def gen(config_list, save_to, max_lines):
    e = ExtractFuncs()
    gen_num = 0
    while True:
        gen_num += 1
        if gen_num >= 300:
            print('Config and max lines are hard to fit, please change config or max lines!')
            exit(0)
        cmd = f"csmith {' '.join(config_list)} --output {save_to}"
        os.system(cmd)
        if max_lines is None:
            break
        funcs, funcsname = e.getFuncs(save_to)
        is_pass = True
        for name in funcsname:
            if 'func' not in name:
                continue
            i = funcsname.index(name)
            func = funcs[i]
            tmp = func.splitlines()
            for i in tmp:
                if not i.strip():
                    tmp.remove(i)
            length = len(tmp)
            if length > max_lines:
                is_pass = False
                break

        if is_pass:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=1, help="number of programs generated")
    parser.add_argument('-o', '--output', default='./out', help='path to save results')
    parser.add_argument('-l', '--max-lines', help='max line number of function generated')

    args = parser.parse_args()

    with open('config', 'r') as f:
        config = [i.strip() for i in f.readlines()]
    assert config, "Read config failed."
    
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    for i in range(int(args.number)):
        gen(config, f'{args.output}/{i}.c', int(args.max_lines))
        print(f'Done: {args.output}/{i}.c')
