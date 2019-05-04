
import os
import re
from more_itertools import consecutive_groups
from pprint import pprint
import json
from itertools import chain, tee

data_folder = "data"


def group_by_hash(lst):
    res_dict = {}
    for each in lst:
        hash_value = hash(tuple(re.split("[0-9]+", each)))
        if hash_value in res_dict:
            res_dict[hash_value].append(each)
        else:
            res_dict[hash_value] = [each]
    return res_dict


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def check_pattern(str1, str2):
    str_split1 = re.split("([0-9]+)", str1)[::-1]
    str_split2 = re.split("([0-9]+)", str2)[::-1]
    counter = 0
    for i, j in zip(*[str_split1, str_split2]):
        if i != j:
            counter += 1
        if counter >= 2:
            return False
    return True


def parse_simple_pattern(lst):
    global global_lst
    temp_str = ""
    pattern = ""
    count = 1
    for each in lst:
        if isinstance(each, list):
            int_lst = [int(i) for i in each]
            group_lst = [
                list(group) for group in consecutive_groups(sorted(int_lst))
            ]
            pattern = ",".join(
                str(i) if len(i) == 1 else str(i[0]) + "-" + str(i[-1])
                for i in group_lst)
            pad = True if each[0].startswith("0") else False
            temp_str += f"%{0 if pad else ''}{len(each[0]) if len(each[0])>1 else ''}d"
            count = len(int_lst)
        else:
            temp_str += each

    global_lst.append([temp_str, pattern, count])


def print_patterns(lst):
    for each in lst:
        if each[1]:
            print(each[2], each[0], each[1])
        else:
            print(1, each[0])


def parse_for_patterns(pattern_wise_dict):
    for key, value in pattern_wise_dict.items():
        split_index = []
        if len(value) <= 1:
            global_lst.append([value[0], None])
            continue
        for index, (i, j) in enumerate(pairwise(value)):
            if check_pattern(i, j):
                pass
            else:
                split_index.append(index + 1)
        if not split_index or split_index[0] != 0:
            split_index.insert(0, 0)
        split_index.append(len(value))
        for i, j in pairwise(split_index):
            combine_values(value[i:j])


def combine_values(lst):
    split_lst = [re.split("([0-9]+)", each) for each in lst]
    fin_lst = []
    for each in zip(*split_lst):
        val = list(set(each))
        fin_lst.append(val[0] if len(val) == 1 else val)
    parse_simple_pattern(fin_lst)


if __name__ == "__main__":
    lst = os.listdir("data/")

    global_lst = []
    new_dict = group_by_hash(lst)
    parse_for_patterns(new_dict)
    print_patterns(global_lst)
