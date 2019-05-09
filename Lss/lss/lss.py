import os
import re
import sys
from more_itertools import consecutive_groups
from itertools import tee, chain
from collections import defaultdict
import argparse
import time

split_func = lambda x: [re.split("([0-9]+)", each) for each in x]


def hash_(values):
    temp_lst = []
    for each_value in values:
        if each_value.isdigit():
            if each_value.startswith("0"):
                temp_lst.append("0")
        else:
            temp_lst.append(each_value)
    return hash(tuple(temp_lst))


# @timeit
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
        grouped_dict[hash_(each)].append(each)

    return grouped_dict


def pairwise(iterable):
    '''
    Takes a iterable object as input and returns a iterable of two items at a time
    if input is a iterable named s with value as [s0,s1,s2,s3,s4]
    output is ((s0,s1), (s1,s2), (s2, s3),(s3,s4))

    '''
    lst1, lst2 = tee(iterable)
    next(lst2, None)
    return zip(lst1, lst2)


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
            digits_length = len(each[0])
            # Forming file pattern
            file_pattern += "%{0}{1}d".format(
                0 if pad else '', digits_length if digits_length > 1 else '')
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


# @timeit
def parse_for_patterns(pattern_wise_dict):
    '''
    This function takes a dictionary and parses it to separate patterns in
    each of the value and then passes each of these separated values to
    combine values function.
    '''
    for value in pattern_wise_dict.values():
        split_index = []
        if len(value) <= 1:
            print_pattern(["1", "".join(value[0]), ""])
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


def read_file_paths(location):
    if os.path.isdir(location):
        return os.listdir(location)
    else:
        print(
            "Invalid path - {0}\nPlease input a valid and existing directory path"
            .format(location))
        return []


def print_pattern(file_pattern_lst):
    '''
    This function takes a list and prints it to console in the following format
    Number_of_files    File Pattern    Series.
    '''
    print("\t".join([
        str(i) if not isinstance(i, list) else "".join(chain.from_iterable(i))
        for i in file_pattern_lst
    ]))


def lss(path, file_lst):
    print("\n>lss output for {0}\n".format(path))
    try:
        parsed_file_paths_lst = split_func(file_lst)
        hash_dict = group_by_hash(parsed_file_paths_lst)
        parse_for_patterns(hash_dict)
    except:
        print("Unable to parse for patterns")
    finally:
        print('-' * 50 + "\n")


def parse_input_args(paths, option=1):
    if option == 1:
        lss("Combined output", [
            each_file for each_path in paths
            for each_file in read_file_paths(each_path)
        ])
    else:
        for each_path in paths:
            lss(each_path, read_file_paths(each_path))


def interactive_input(paths):
    if paths:
        if len(paths) == 1:
            lss(paths[0], read_file_paths(paths[0]))
        else:
            flag = True

            while (flag):
                print(
                    "You have given multiple inputs. Please choose one of the following options"
                )
                print("1. Combined output")
                print("2. Individual outputs")
                try:
                    input_option = int(input())
                except Exception:
                    print("Invalid input, please choose again")
                    continue
                if input_option in [1, 2]:
                    flag = False
                    parse_input_args(paths, option=input_option)
                    break
                else:
                    print("Invalid input, please choose again")
    else:
        lss("Current Location", read_file_paths("."))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="command line arguments parser for lss command")
    parser.add_argument("path",
                        metavar='p',
                        type=str,
                        nargs='*',
                        help='path of the directory')
    args = parser.parse_args()
    interactive_input(args.path)
