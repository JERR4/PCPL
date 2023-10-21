import json
import sys
import gen_random
from print_result import print_result
from cm_timer import cm_timer_1
from field import field

path = r'D:\BMSTU\PS-CS\3 sem\Labs\Lab3\lab_python_fp\data_light.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return field(data, 'job-name')

"""
@print_result
def f2(arg):
    raise NotImplemented


@print_result
def f3(arg):
    raise NotImplemented


@print_result
def f4(arg):
    raise NotImplemented
"""

if __name__ == '__main__':
    with cm_timer_1():
        #f4(f3(f2(f1(data))))
        f1(data)
