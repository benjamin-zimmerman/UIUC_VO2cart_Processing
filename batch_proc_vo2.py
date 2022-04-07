import proc_gxt_vo2 as gxt
import os


path = "E://PEA//data//Temp_VO2"
dir_list = os.listdir(path)
csv_file = 'E://PEA//data//Temp_VO2//gxt_vo2_data.csv'

interval = 2


for xl_file in dir_list:
    print(os.path.join(path, xl_file))
    df = gxt.minbyminVO2(os.path.join(path, xl_file))
    downsampled_vo2 = gxt.downsample_minbyminVO2(df, interval)
    downsampled_vo2.T.iloc[[1]].to_csv(csv_file, mode = 'a', header = False, index = False)

#TODO:
# get a column of subjects
# append subjects to first column of csv file