# Code Generation

## About
[Csmith](https://github.com/csmith-project/csmith) is a random generator of C programs. This is a script to help customize the number of generated programs, the maximum number of lines of the function and the program output location. The `config` file is the options of Csmith, you can customize the options by changing this file.

## Usage

```shell
python generator.py [-h] [-n NUMBER] [-o OUTPUT] [-l MAX_LINES]

options:
  -h,            show this help message and exit
  -n NUMBER,     number of programs generated
  -o OUTPUT,     path to save results
  -l MAX_LINES,  max line number of function generated
```

## Environment
python=3.10
csmith>=2.4
