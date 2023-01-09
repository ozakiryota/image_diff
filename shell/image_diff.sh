#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/image_diff_with_csv.py \
    --read_csv_path_0 $HOME/dataset/airsim/sample_data/file_list.csv \
    --target_col_0 0 \
    --read_csv_path_1 $HOME/dataset/airsim/sample_data/file_list.csv \
    --target_col_1 1 \
    --write_dir_path $HOME/dataset/airsim/sample_data/diff
