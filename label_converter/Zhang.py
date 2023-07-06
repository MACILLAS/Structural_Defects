import sys
import glob
import os
import cv2
import shutil
import numpy as np
from mask_to_bb import mask_to_bbox, plot_bbox

DATASET_DIR = '/home/zaid/datasets/defect_segment/zhang_defect_segmentation'
OUTPUT_DIR = '/home/zaid/datasets/defect_segment/zhang_defect_segmentation_out'


def main(dataset_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'check'), exist_ok=True)

    images = sorted(glob.glob(os.path.join(dataset_dir, "images", "*")))
    n = len(images)

    for i,img in enumerate(images):
        if '_lab' in img:
            continue        

        print(f"Processing image {i} of {n}", end='\r')

        img_name = img.split('/')[-1]
        shutil.copy(img, os.path.join(output_dir, 'images', img_name))

        img_id  = img_name.split('.')[0]                
                
        f_crack = os.path.join(dataset_dir, 'masks', img_id+'crack'+'.jpg')
        f_spall = os.path.join(dataset_dir, 'masks', img_id+'spall'+'.jpg')
        f_corr = os.path.join(dataset_dir, 'masks', img_id+'rebar'+'.jpg')
        
        if not os.path.exists(f_crack):
            label_cracks = []
        else:
            mask_crack = cv2.imread(f_crack, cv2.IMREAD_GRAYSCALE)
            label_cracks = mask_to_bbox(mask_crack)

        if not os.path.exists(f_spall):
            label_spall = []
        else:
            mask_spall = cv2.imread(f_spall, cv2.IMREAD_GRAYSCALE)
            label_spall = mask_to_bbox(mask_spall)
        
        if not os.path.exists(f_corr):
            label_corr = []
        else:
            mask_corr  = cv2.imread(f_corr, cv2.IMREAD_GRAYSCALE)
            label_corr = mask_to_bbox(mask_corr)

        with open(os.path.join(output_dir, 'labels', img_id + '.txt'), 'w') as f:
            for label in label_cracks:
                f.write('0 ' + ' '.join([str(x) for x in label]) + '\n')
            for label in label_spall:
                f.write('1 ' + ' '.join([str(x) for x in label]) + '\n')
            for label in label_corr:
                f.write('2 ' + ' '.join([str(x) for x in label]) + '\n')


        img_check = plot_bbox(cv2.imread(img, cv2.IMREAD_COLOR), label_cracks, (255, 255, 255))
        img_check = plot_bbox(img_check, label_spall, (0, 0, 255))
        img_check = plot_bbox(img_check, label_corr, (0, 255, 255))

        cv2.imwrite(os.path.join(output_dir, 'check', img_name.replace('.png', '_check.png')), img_check)
    

if __name__ == "__main__":
    main(DATASET_DIR, OUTPUT_DIR)