import sys
import glob
import os
import cv2
import shutil
import numpy as np
from mask_to_bb import mask_to_bbox, plot_bbox

DATASET_DIR = '/home/zaid/datasets/defect_segment/s2ds'
OUTPUT_DIR = '/home/zaid/datasets/defect_segment/s2ds_out'

# white: cracks
# red: spalling
# yellow: corrosion
# blue: efflorescence

def main(dataset_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'check'), exist_ok=True)

    train = sorted(glob.glob(os.path.join(dataset_dir, "train", "*")))
    test = sorted(glob.glob(os.path.join(dataset_dir, "test", "*")))
    val = sorted(glob.glob(os.path.join(dataset_dir, "val", "*")))
    images = train + test + val
    n = len(images)

    for i,img in enumerate(images):
        if '_lab' in img:
            continue        

        print(f"Processing image {i} of {n}", end='\r')

        img_name = img.split('/')[-1]
        shutil.copy(img, os.path.join(output_dir, 'images', img_name))
        
        mask = cv2.imread(img.replace('.png', '_lab.png'), cv2.IMREAD_COLOR)
        mask_crack = cv2.inRange(mask, np.array([255, 255, 255]), np.array([255, 255, 255]))
        mask_spall = cv2.inRange(mask, np.array([0, 0, 255]), np.array([0, 0, 255]))
        mask_eff = cv2.inRange(mask, np.array([255, 255, 0]), np.array([255, 255, 0]))
        mask_corr = cv2.inRange(mask, np.array([0, 255, 255]), np.array([0, 255, 255]))        

        label_cracks = mask_to_bbox(mask_crack)
        label_spall = mask_to_bbox(mask_spall)
        label_eff = mask_to_bbox(mask_eff)
        label_corr = mask_to_bbox(mask_corr)

        with open(os.path.join(output_dir, 'labels', img_name.replace('.png', '.txt')), 'w') as f:
            for label in label_cracks:
                f.write('0 ' + ' '.join([str(x) for x in label]) + '\n')
            for label in label_spall:
                f.write('1 ' + ' '.join([str(x) for x in label]) + '\n')
            for label in label_corr:
                f.write('2 ' + ' '.join([str(x) for x in label]) + '\n')
            for label in label_eff:
                f.write('3 ' + ' '.join([str(x) for x in label]) + '\n')

        img_check = plot_bbox(cv2.imread(img, cv2.IMREAD_COLOR), label_cracks, (255, 255, 255))
        img_check = plot_bbox(img_check, label_spall, (0, 0, 255))
        img_check = plot_bbox(img_check, label_corr, (0, 255, 255))
        img_check = plot_bbox(img_check, label_eff, (255, 255, 0))

        cv2.imwrite(os.path.join(output_dir, 'check', img_name.replace('.png', '_check.png')), img_check)
    

if __name__ == "__main__":
    main(DATASET_DIR, OUTPUT_DIR)