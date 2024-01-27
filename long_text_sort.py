import numpy as np
import pandas as pd

path = 'long_text_ta.txt'


def sort_save(idx):
    global tmp
    tmp.sort(key=lambda x: x[1])
    save_path = 'long_text_tb_{}.txt'.format(idx)
    with open(save_path, 'a') as writer:
        tmp = map(lambda x: ','.join(map(str, x)) + '\n', tmp)
        writer.writelines(tmp)
        writer.write('\n')


with open(path) as reader:
    tmp = []
    cnt = 0
    for idx, d in enumerate(reader.readlines()):
        item = list(map(int, d.strip().split(',')))
        tmp.append(item)
        if (idx + 1) % 10 == 0:
            if cnt % 2 == 0:
                sort_save(1)
            else:
                sort_save(2)
            tmp = []
            cnt += 1