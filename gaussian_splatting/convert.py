import os
import logging
from argparse import ArgumentParser
import shutil


#定义一个命令行参数解释器
parser = ArgumentParser("Colmap converter")
parser.add_argument("--no_gpu", action='store_true') #是否使用GPU，动作为True
parser.add_argument("--skip_matching", action='store_true') #是否跳过匹配步骤，动作为True
parser.add_argument("--source_path", "-s", required=True, type=str) #源路径，必须参数，指添加的源文件路径
parser.add_argument("--camera", default="OPENCV", type=str) #相机模型，默认为空
parser.add_argument("--colmap_executable", default="", type=str) #Colmap执行路径，默认为空
parser.add_argument("--resize", action="store_true") #是否图像缩放，动作为True
parser.add_argument("--magick_executable", default="", type=str) #magick执行路径，默认为空
#解析命令行参数
args = parser.parse_args()

#根据用户输入的参数，确定了调用COLMAP和Magick的命令，以及是否使用GPU。
colmap_command = '"{}"'.format(args.colmap_executable) if len(args.colmap_executable) > 0 else "colmap"
magick_command = '"{}"'.format(args.magick_executable) if len(args.magick_executable) > 0 else "magick"
use_gpu = 1 if not args.no_gpu else 0

#如果没有选择跳过匹配步骤，那么进行匹配（调用COLMAP的命令）
if not args.skip_matching:
    os.makedirs(args.source_path + "/distorted/sparse", exist_ok=True)

    ## 特征提取
    feat_extracton_cmd = colmap_command + " feature_extractor "\
        "--database_path " + args.source_path + "/distorted/database.db \
        --image_path " + args.source_path + "/input \
        --ImageReader.camera_model " + args.camera + " \
        --ImageReader.single_camera 1 \
        --SiftExtraction.use_gpu " + str(use_gpu)
    exit_code = os.system(feat_extracton_cmd)
    if exit_code != 0:
        logging.error(f"Feature extraction failed with code {exit_code}. Exiting.")
        exit(exit_code)

    ## 特征匹配
    feat_matching_cmd = colmap_command + " exhaustive_matcher \
        --database_path " + args.source_path + "/distorted/database.db \
        --SiftMatching.use_gpu " + str(use_gpu)
    exit_code = os.system(feat_matching_cmd)
    if exit_code != 0:
        logging.error(f"Feature matching failed with code {exit_code}. Exiting.")
        exit(exit_code)

    ## 困束调整
    mapper_cmd = (colmap_command + " mapper \
        --database_path " + args.source_path + "/distorted/database.db \
        --image_path "  + args.source_path + "/input \
        --output_path "  + args.source_path + "/distorted/sparse \
        --Mapper.ba_global_function_tolerance=0.000001")
    exit_code = os.system(mapper_cmd)
    if exit_code != 0:
        logging.error(f"Mapper failed with code {exit_code}. Exiting.")
        exit(exit_code)

#进行图像去畸变步骤，然后将sparse目录下的文件移动到sparse/0目录下

img_undist_cmd = (colmap_command + " image_undistorter \
    --image_path " + args.source_path + "/input \
    --input_path " + args.source_path + "/distorted/sparse/0 \
    --output_path " + args.source_path + "\
    --output_type COLMAP")
exit_code = os.system(img_undist_cmd)
if exit_code != 0:
    logging.error(f"Mapper failed with code {exit_code}. Exiting.")
    exit(exit_code)

files = os.listdir(args.source_path + "/sparse")
os.makedirs(args.source_path + "/sparse/0", exist_ok=True)

for file in files:
    if file == '0':
        continue
    source_file = os.path.join(args.source_path, "sparse", file)
    destination_file = os.path.join(args.source_path, "sparse", "0", file)
    shutil.move(source_file, destination_file)


#如果用户选择了图像缩放，那么进行图像的缩放，使用Magick的mogrify命令，将图像缩放到原来的50%、25%和12.5%
if(args.resize):
    print("Copying and resizing...")

    os.makedirs(args.source_path + "/images_2", exist_ok=True)
    os.makedirs(args.source_path + "/images_4", exist_ok=True)
    os.makedirs(args.source_path + "/images_8", exist_ok=True)
    # Get the list of files in the source directory
    files = os.listdir(args.source_path + "/images")
    # Copy each file from the source directory to the destination directory
    for file in files:
        source_file = os.path.join(args.source_path, "images", file)

        destination_file = os.path.join(args.source_path, "images_2", file)
        shutil.copy2(source_file, destination_file)
        exit_code = os.system(magick_command + " mogrify -resize 50% " + destination_file)
        if exit_code != 0:
            logging.error(f"50% resize failed with code {exit_code}. Exiting.")
            exit(exit_code)

        destination_file = os.path.join(args.source_path, "images_4", file)
        shutil.copy2(source_file, destination_file)
        exit_code = os.system(magick_command + " mogrify -resize 25% " + destination_file)
        if exit_code != 0:
            logging.error(f"25% resize failed with code {exit_code}. Exiting.")
            exit(exit_code)

        destination_file = os.path.join(args.source_path, "images_8", file)
        shutil.copy2(source_file, destination_file)
        exit_code = os.system(magick_command + " mogrify -resize 12.5% " + destination_file)
        if exit_code != 0:
            logging.error(f"12.5% resize failed with code {exit_code}. Exiting.")
            exit(exit_code)

print("Done.")
