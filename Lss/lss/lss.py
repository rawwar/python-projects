import os
import re
import sys
from more_itertools import consecutive_groups
from pprint import pprint
from itertools import tee
from collections import defaultdict

data_folder = "data"


def group_by_hash(file_list):
    '''
    This function takes a list and groups elements
    based on a hash and returns a dictionary.

    Parameters:
        file_list: list of all file names
    Returns:
        grouped_dict: A dictionary where key is a hash and value is a
                      list of file names with similar pattern
    '''
    grouped_dict = defaultdict(lambda: [])
    for each in file_list:
        hash_value = hash(tuple(re.split("[0-9]+", each)))
        grouped_dict[hash_value].append(re.split("([0-9]+)", each))

    return grouped_dict


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def check_pattern(file1, file2):
    '''
    This function takes two lists, compares them and False True if
    two functions differ at more than two places else it returns True
    '''
    counter = 0
    for i, j in zip(*[file1[::-1], file2[::-1]]):
        if i != j:
            counter += 1
        if counter >= 2:
            return False
    return True


def parse_simple_pattern(lst):
    '''
    This function takes a list of similar file patterns,
    parses them and  passes them to print_pattern
    '''
    sequence = ""
    file_pattern = ""
    count = 1
    for each in lst:
        if isinstance(each, list):
            int_lst = [int(i) for i in each]
            group_lst = [
                list(group) for group in consecutive_groups(sorted(int_lst))
            ]
            # makes a sequence separated by comma
            sequence = ",".join(
                str(i) if len(i) == 1 else str(i[0]) + "-" + str(i[-1])
                for i in group_lst)
            # To check if the numbers are zero padded
            pad = True if each[0].startswith("0") else False
            temp = len(each[0])
            # Forming file pattern
            file_pattern += f"%{0 if pad else ''}{temp if temp>1 else ''}d"
            count = len(int_lst)
        else:
            file_pattern += each
    print_pattern([count, file_pattern, sequence])


def combine_values(lst):
    '''
    This function takes a list of file patterns and combines
    them to be parsable by parse_simple_pattern function.
    '''
    fin_lst = []
    for each in zip(*lst):
        val = list(set(each))
        fin_lst.append(val[0] if len(val) == 1 else val)
    parse_simple_pattern(fin_lst)


def parse_for_patterns(pattern_wise_dict):
    '''
    This function takes a dictionary and parses it to separate patterns in
    each of the value and then passes each of these separated values to
    combine values function.
    '''
    for value in pattern_wise_dict.values():
        split_index = []
        if len(value) <= 1:
            print_pattern([value[0][0], None])
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


def print_pattern(file_pattern_lst):
    '''
    This function takes a list and prints it to console in the following format
    Number_of_files    File Pattern    Series.
    '''
    if file_pattern_lst[1]:
        print(file_pattern_lst[0], file_pattern_lst[1], file_pattern_lst[2])
    else:
        print(1, file_pattern_lst[0])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        file_lst = os.listdir(".")
    else:
        file_lst = os.listdir(sys.argv[1])
    hash_dict= group_by_hash(file_lst)
    parse_for_patterns(hash_dict)
