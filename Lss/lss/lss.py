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




# Go from right to left .. find extension.. group them.. then find next sub extension and group them.. keep doing that till 
# we reach start of the string?
if __name__ == "__main__":
    lst = os.listdir("data/")
    temp1 = group_by_length(lst)
    new_dict = {}
    for key,value in temp1.items():
        new_dict[key] = group_by_number_pattern(value)
    pprint(new_dict)