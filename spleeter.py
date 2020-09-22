# spleeter separate -i 1.mp3 -p spleeter:2stems -o output

import os
import shutil

#人声背景声分离
# out_path = "output_normal/"
# if not os.path.exists(out_path):
#     os.mkdir(out_path)
# dirs_list = os.listdir(out_path)
# for root, dirs, files in os.walk("normal/"):
#     # count = 0
#     for file in files:
#         file_name = file.split('.')[0]
#         if file_name in dirs_list:
#             print(file_name + "存在")
#             # count = count +1
#         else:
#             audio_name = root + file
#             str = "spleeter separate -i " + audio_name + " -p spleeter:2stems -o " + out_path
#             val = os.system(str)
#
# dirs_list = os.listdir("output_robot/")
# for root, dirs, files in os.walk("robot/"):
#     for file in files:
#         file_name = file.split('.')[0]
#         if file_name in dirs_list:
#             print(file_name + "存在")
#         else:
#             audio_name = root + file
#             str = "spleeter separate -i " + audio_name + " -p spleeter:2stems -o output_robot"
#             val = os.system(str)

# val = os.system("spleeter separate -i 1.mp3 -p spleeter:2stems -o output")
# print(val)

# import spleeter

# spleeter separate -i normal/226337.wav -p spleeter:2stems -o output

#找出分离之后的人声
if not os.path.exists("output_temp_copy"):
    os.makedirs("output_temp_copy")
for root, dirs, files in os.walk("output_temp/"):
    for dir in dirs:
        path = root + dir
        for root1, dirs1, files1 in os.walk(path + "/"):
            for file1 in files1:
                if file1 == "vocals.wav":
                    input_file = path + "/" + file1
                    output_file = "output_temp_copy/" + dir + "_deal.wav"
                    shutil.copy(input_file, output_file)
print("deno")

# if not os.path.exists("output_normal_copy"):
#     os.makedirs("output_normal_copy")
# for root, dirs, files in os.walk("output_normal/"):
#     for dir in dirs:
#         path = root + dir
#         for root1, dirs1, files1 in os.walk(path + "/"):
#             for file1 in files1:
#                 if file1 == "vocals.wav":
#                     input_file = path + "/" + file1
#                     output_file = "output_normal_copy/" + dir + "_deal.wav"
#                     shutil.copy(input_file, output_file)
# print("deno")

# if not os.path.exists("output_robot_copy"):
#     os.makedirs("output_robot_copy")
# for root, dirs, files in os.walk("output_robot/"):
#     for dir in dirs:
#         path = root + dir
#         for root1, dirs1, files1 in os.walk(path + "/"):
#             for file1 in files1:
#                 if file1 == "vocals.wav":
#                     input_file = path + "/" + file1
#                     output_file = "output_robot_copy/" + dir + "_deal.wav"
#                     shutil.copy(input_file, output_file)
# print("deno")
