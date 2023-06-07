import sys

import os

def gen(config_list, save_to):
    cmd = f"csmith {' '.join(config_list)} --output {save_to}"
    os.system(cmd)


if __name__ == "__main__":
    with open('config', 'r') as f:
        config = [i.strip() for i in f.readlines()]
    assert config, "Read config failed."
    save_to_dir = '/home/data/caoy/data'
    # gen(config, 'test.c')
    for i in range(100000):
        gen(config, f'{save_to_dir}/{i}.c')
        print(f'Done: {save_to_dir}/{i}.c')
