import argparse
import os
import csv
import cv2
import numpy as np
import matplotlib.pyplot as plt

from image_diff import getDiffImage

class ImageDiffWithCsv:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path_0', required=True)
        arg_parser.add_argument('--target_col_0', type=int, default=0)
        arg_parser.add_argument('--read_csv_path_1', required=True)
        arg_parser.add_argument('--target_col_1', type=int, default=0)
        arg_parser.add_argument('--write_dir_path')
        arg_parser.add_argument('--write_image_path', default='../save/sorted.png')
        return arg_parser

    def getFileList(self, csv_path, target_col):
        root_dir_path = os.path.dirname(csv_path)
        with open(csv_path, 'r') as file_list_csv:
            file_path_list = list(csv.reader(file_list_csv))
            file_path_list = list(zip(*file_path_list))[target_col]
            file_path_list = [os.path.join(root_dir_path, file_path) for file_path in file_path_list]
        return file_path_list

    def showImages(self, img_list_list, indicies, h, w):
        num_shown = h * w
        h = 3 * h

        scale = 3
        plt.figure(figsize=(scale * h, scale * w))

        for counter, index in enumerate(indicies):
            if counter + 1 > num_shown:
                break            
            subplot_index = 3 * w * (counter // w) + (counter % w) + 1

            plt.subplot(h, w, subplot_index, xlabel="x_" + str(counter + 1))
            plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)
            plt.imshow(img_list_list[index][0])

            plt.subplot(h, w, subplot_index + w, xlabel="y_" + str(counter + 1))
            plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)
            plt.imshow(img_list_list[index][1])

            plt.subplot(h, w, subplot_index + 2 * w, xlabel="diff_" + str(counter + 1))
            plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)
            plt.imshow(img_list_list[index][2])
        plt.tight_layout()
        plt.savefig(self.args.write_image_path)
        plt.show()

    def exec(self):
        file_path_list_0 = self.getFileList(self.args.read_csv_path_0, self.args.target_col_0)
        file_path_list_1 = self.getFileList(self.args.read_csv_path_1, self.args.target_col_1)

        if os.path.exists(self.args.write_dir_path) == False:
            os.makedirs(self.args.write_dir_path)
        img_list_list = []
        diff_value_list = []

        for file_path_0, file_path_1 in zip(file_path_list_0, file_path_list_1):
            ## open
            img_0 = cv2.imread(file_path_0)
            img_0 = cv2.cvtColor(img_0, cv2.COLOR_BGR2RGB)
            img_1 = cv2.imread(file_path_1)
            img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
            ## resize
            height, width, _ = img_0.shape
            if img_1.shape[0] < height:
                height = img_1.shape[0]
            if img_1.shape[1] < width:
                width = img_1.shape[1]
            img_0 = cv2.resize(img_0, (width, height))
            img_1 = cv2.resize(img_1, (width, height))
            ## diff
            diff_img = getDiffImage(img_0, img_1)
            diff_value = diff_img.mean()
            ## save
            diff_img_name = os.path.basename(file_path_0).split('.')[0] + "_diff.png"
            write_path = os.path.join(self.args.write_dir_path, diff_img_name)
            cv2.imwrite(write_path, diff_img)
            print("Save:", write_path)
            ## append
            img_list_list.append([img_0, img_1, diff_img])
            diff_value_list.append(diff_value)
        sorted_indicies = np.argsort(diff_value_list)
        self.showImages(img_list_list, sorted_indicies, 2, 10)


if __name__ == '__main__':
    image_diff_with_csv = ImageDiffWithCsv()
    image_diff_with_csv.exec()