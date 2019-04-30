'''
The Problem:
-----------------------------------------------------------------------------------
A directory at Digital Domain might contain hundreds or even thousands of image files. Doing
an "ls" in this directory will produce a difficult to handle listing of all these files.
For example, here is an ls of a small directory.
> ls
elem.info sd_fx29.0112.rgb sd_fx29.0125.rgb sd_fx29.0137.rgb
sd_fx29.0101.rgb sd_fx29.0113.rgb sd_fx29.0126.rgb sd_fx29.0138.rgb
sd_fx29.0102.rgb sd_fx29.0114.rgb sd_fx29.0127.rgb sd_fx29.0139.rgb
sd_fx29.0103.rgb sd_fx29.0115.rgb sd_fx29.0128.rgb sd_fx29.0140.rgb
sd_fx29.0104.rgb sd_fx29.0116.rgb sd_fx29.0129.rgb sd_fx29.0141.rgb
sd_fx29.0105.rgb sd_fx29.0117.rgb sd_fx29.0130.rgb sd_fx29.0142.rgb
sd_fx29.0106.rgb sd_fx29.0118.rgb sd_fx29.0131.rgb sd_fx29.0143.rgb
sd_fx29.0107.rgb sd_fx29.0119.rgb sd_fx29.0132.rgb sd_fx29.0144.rgb
sd_fx29.0108.rgb sd_fx29.0120.rgb sd_fx29.0133.rgb sd_fx29.0145.rgb
sd_fx29.0109.rgb sd_fx29.0121.rgb sd_fx29.0134.rgb sd_fx29.0146.rgb
sd_fx29.0110.rgb sd_fx29.0123.rgb sd_fx29.0135.rgb sd_fx29.0147.rgb
sd_fx29.0111.rgb sd_fx29.0124.rgb sd_fx29.0136.rgb strange.xml
Did you notice that the file sd_fx29.0122.rgb was missing? Neither did I!
What we'd rather have is a listing that looks like this:
> lss
1 elem.info
46 sd_fx29.%04d.rgb 101-121 123-147
1 strange.xml
It requires a bit of familiarity with C style printf formatting on the
user's part, but once they get used to it, it's great!
The Assignment:
-----------------------------------------------------------------------------------
Implement the "lss" command twice - once in C++ and once in Python, if you are comfortable
with both.
The command needs to accept one optional argument: a path to the directory or file, similar to
the "ls" command.
Make it as general as possible. The goal is to find sequences of files that can be concatenated
together. Please don't rely on specific characters as delimiters since we can't control how artists
name their files. And don't assume anything about the zero-padding.
Beware, we will try your command on some tricky directories, like:
alpha.txt
file01_0040.rgb
file01_0041.rgb
file01_0042.rgb
file01_0043.rgb
file02_0044.rgb
file02_0045.rgb
file02_0046.rgb
file02_0047.rgb
file1.03.rgb
file2.03.rgb
file3.03.rgb
file4.03.rgb
file.info.03.rgb
It should produce:
> lss
1 alpha.txt
4 file01_%04d.rgb 40-43
4 file02_%04d.rgb 44-47
4 file%d.03.rgb 1-4
1 file.info.03.rgb
'''

import os
import re
from more_itertools import consecutive_groups
from pprint import pprint

data_folder = "data"

# 1. Group by length

def group_by_length(lst):
    '''
    This function returns a dictionary where key is the length and
    value is a list of file names that have same length
    '''
    length_to_file_dict = {}
    for each in lst:
        length = len(each)
        if length in length_to_file_dict:
            length_to_file_dict[length].append(each)
        else:
            length_to_file_dict[length] = [each]
    return length_to_file_dict


# 2. Apply regex and find number patterns

def group_by_number_pattern(lst):
    pattern_to_file_dict = {}
    for each in lst:
        pattern = re.findall("([0-9]+)",each)
        len_of_pattern = len(pattern)
        if len_of_pattern in pattern_to_file_dict:
            pattern_to_file_dict[len_of_pattern].append(each)
        else:
            pattern_to_file_dict[len_of_pattern] = [each]
    return pattern_to_file_dict

def group_by_number_pattern_and_length(lst):
    pattern_to_file_dict = {}
    for each in lst:
        pattern = re.findall("([0-9]+)",each)
        len_of_str = len(each)
        len_of_pattern = len(pattern)
        dict_key = str(len_of_pattern) +"_"+ str(len_of_str)
        if dict_key in pattern_to_file_dict:
            pattern_to_file_dict[dict_key].append(re.split("([0-9]+)",each) )
        else:
            pattern_to_file_dict[dict_key] = [re.split("([0-9]+)",each) ]
    return pattern_to_file_dict

def split_by_number_pattern(pattern_dict):
    res_dict = {}
    for key,value in pattern_dict.items():
        res_dict[key] = [re.split("([0-9]+)",each) for each in value]
    return res_dict

def sort_from_right(lst):
    pass

def print_to_console(lst):
    '''
    lst should be in the following format
    lst should consist of list
    each list should have the following
    at index 0 - count
    at index 1 - file format
    at index 2 -  string which indicates start and end of series
    '''
    for each in sorted(lst,lambda x: x[1]):
        print(each[0],each[1],each[2])

def group_by_hash(lst):
    res_dict = {}
    for each in lst:
        hash_value = hash(tuple(re.split("[0-9]+",each)))
        if hash_value in res_dict:
            res_dict[hash_value].append(re.split("([0-9]+)",each))
        else:
            res_dict[hash_value] = [re.split("([0-9]+)",each)]
    return res_dict

def combine_values(lst):
    fin_lst = []
    res = []
    for each in zip(*lst):
        fin_lst.append(set(each))
    for each in fin_lst:
        if len(each)>1:
            int_lst = [int(i) for i in each]
            temp_lst = []
            for each_lst in [list(group) for group in consecutive_groups(sorted(int_lst))]:
                if len(each_lst)==1:
                    temp_lst.append(str(each_lst[0]))
                else:
                    temp_lst.append(str(each_lst[0]) + "-" + str(each_lst[-1]))
            res.append("\t".join(temp_lst))
                
        else:
            res.append(each)
    return res

# Use [list(group) for group in consecutive_groups(sorted(z))] , consecutive_groups is imported from more_itertools

# Go from right to left .. find extension.. group them.. then find next sub extension and group them.. keep doing that till 
# we reach start of the string?

# use sorted with key as regex output of digits pattern


# Current output: 
# 1866123909547272289 [{'alpha.txt'}]
# 8211676718420172478 [{'elem.info'}]
# 873150919273017500 [{'file.info.'}, {'03'}, {'.rgb'}]
# 7688575126262578364 [{'file'}, '1-2', {'_'}, '40-47', {'.rgb'}]
# -247798305264179467 [{'file'}, '1-4', {'.'}, {'03'}, {'.rgb'}]
# 6496405249312978273 [{'sd_fx'}, {'29'}, {'.'}, '101-121\t123-147', {'.rgb'}]
# 1522664490650659231 [{'strange.xml'}]


if __name__ == "__main__":
    lst = os.listdir("data/")
    # temp1 = group_by_length(lst)
    # new_dict = {}
    # for key,value in temp1.items():
    #     new_dict[key] = group_by_number_pattern(value)
    new_dict = group_by_number_pattern_and_length(lst)
    pprint(new_dict)