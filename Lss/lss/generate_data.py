import os

data = '''elem.info sd_fx29.0112.rgb sd_fx29.0125.rgb sd_fx29.0137.rgb
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
test6_file.01033.txt
test6_file.01034.txt
test6_file.01035.txt
test6_file.01040.txt
test6_file.01041.txt
test6_file.01042.txt
test6_file.1033.txt
test6_file.1034.txt
test6_file.1035.txt
test6_file.1040.txt
test6_file.1041.txt
test6_file.1042.txt
test6_file.1066.txt
test6_file.1067.txt
'''
# sd29_fx.rgb.0112
# sd29_fx.rgb.0113
# sd29_fx.rgb.0114
# sd29_fx.rgb.0115
# sd29_fx.rgb.0116
# file01_0040.rgb
# file01_0041.rgb
# file01_0042.rgb
# file01_0043.rgb
# file02_0044.rgb
# file02_0045.rgb
# file02_0046.rgb
# file02_0047.rgb
# mile02_0044.rgb
# mile02_0045.rgb
# mile02_0046.rgb
# mile02_0047.rgb
# file01_0040_01.rgb
# file01_0041_01.rgb
# file01_0042_01.rgb
# file01_0043_01.rgb
# file02_0044_01.rgb
# file02_0045_01.rgb
# file02_0046_01.rgb
# file02_0047_01.rgb
# mile02_0044_01.rgb
# mile02_0045_01.rgb
# mile02_0046_01.rgb
# mile02_0046_01_asd_05.rgb
# mile02_0046_01_asd_06.rgb
# mile02_0046_01_asd_07.rgb
# mile02_0046_01_asd_08.rgb
# mile02_0046_01_asd1_09.rgb
# mile02_0046_01_asd1_10.rgb
# mile01_0047_01_asd_05.rgb
# mile01_0047_01_asd_06.rgb
# mile01_0047_01_asd_07.rgb
# mile01_0047_01_asd_08.rgb
# mile01_0047_01_asd1_09.rgb
# mile01_0047_01_asd1_10.rgb
# mile02_0048_01_asd_05.rgb
# mile02_0048_01_asd_06.rgb
# mile02_0048_01_asd_07.rgb
# mile02_0048_01_asd_08.rgb
# mile02_0048_01_asd1_09.rgb
# mile02_0048_01_asd1_10.rgb
# mile02_0049_01_asd_05.rgb
# mile02_0049_01_asd_06.rgb
# mile02_0049_01_asd_07.rgb
# mile02_0049_01_asd_08.rgb
# mile02_0049_01_asd1_09.rgb
# mile02_0049_01_asd1_10.rgb
# mile02_0050_01_asd_05.rgb
# mile02_0050_01_asd_06.rgb
# mile02_0050_01_asd_07.rgb
# mile02_0050_01_asd_08.rgb
# mile02_0050_01_asd1_09.rgb
# mile02_0046_01_asd1_10.rgb
# mile02_0047_01.rgb
# mile02_0047_02.rgb
# mile02_0047_03.rgb
# mile02_0047_04.rgb
# mile02_0047_05.rgb
# mile02_0047_06.rgb
# file1.03.rgb
# file2.03.rgb
# file3.03.rgb
# file4.03.rgb
# file.info.03.rgb
# '''

if not os.path.exists("data"):
    os.mkdir("data")
for each in data.replace("\n"," ").split():
    open(os.path.join("data",each),'w').close()

