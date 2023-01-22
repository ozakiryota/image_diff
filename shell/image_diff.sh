#!/bin/bash

original_pwd=$(pwd)
exec_pwd=$(cd $(dirname $0); pwd)

cd $exec_pwd

python3 $exec_pwd/../pyscr/image_diff_with_csv.py \
    --read_csv_path_0 $HOME/dataset/airsim/tmp/file_list.csv \
    --target_col_0 0 \
    --read_csv_path_1 $HOME/dataset/airsim/tmp/blur_resynthesized/file_list.csv \
    --target_col_1 0 \
    --flag_use_feature \
    --write_dir_path $HOME/dataset/airsim/tmp/diff

cd $original_pwd
