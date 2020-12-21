import os
import glob
from shutil import copyfile

all_list =list(glob.iglob('/home/judah/Desktop/cropped_full_ct/ncp/**/*.*',recursive = True))

for x in all_list:
    path = x[:-9]
    sml_list =list(glob.iglob(path+'**/*.*',recursive = True))
    nums = []
    for z in sml_list:
        num = z[-8:-4]
        num = int(num)
        nums.append(num)
    flag = sum(nums)//len(nums)
    flag = str(flag)
    while len(flag) < 4:
        flag = '0'+flag
    flag = path+'/'+flag+'.jpg'
    if not os.path.exists(path.replace('cropped_full_ct','Flagship')):
        os.makedirs(path.replace('cropped_full_ct','Flagship'))
    try:
        copyfile(flag,flag.replace('cropped_full_ct','Flagship'))
    except:
        print(flag)
     
