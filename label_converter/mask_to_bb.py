import os
import numpy as np
import cv2
from glob import glob
from tqdm import tqdm
from skimage.measure import label, regionprops, find_contours

""" Creating a directory """
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

""" Convert a mask to border image """
def mask_to_border(mask):
    h, w = mask.shape
    border = np.zeros((h, w))

    contours = find_contours(mask, 128)
    for contour in contours:
        for c in contour:
            x = int(c[0])
            y = int(c[1])
            border[x][y] = 255

    return border

""" Mask to bounding boxes (yolo) """
def mask_to_bbox(mask):
    bboxes = []
    h, w = mask.shape

    mask = mask_to_border(mask)
    lbl = label(mask)
    props = regionprops(lbl)
    for prop in props:
        x1 = prop.bbox[1] / w
        y1 = prop.bbox[0] / h

        x2 = prop.bbox[3] / w
        y2 = prop.bbox[2] / h

        xc = (x1 + x2) / 2
        yc = (y1 + y2) / 2

        bw = x2 - x1
        bh = y2 - y1

        bboxes.append([xc, yc, bw, bh])

    return bboxes

def plot_bbox(img, bboxes, c):
    img_h, img_w, _ = img.shape
    for bbox in bboxes:
        x = bbox[0] * img_w
        y = bbox[1] * img_h
        w = bbox[2] * img_w
        h = bbox[3] * img_h

        x1 = int(x - w / 2)
        y1 = int(y - h / 2)
        x2 = int(x + w / 2)
        y2 = int(y + h / 2)
        

        cv2.rectangle(img, (x1, y1), (x2, y2), c, 2)

    return img
def parse_mask(mask):
    mask = np.expand_dims(mask, axis=-1)
    mask = np.concatenate([mask, mask, mask], axis=-1)
    return mask

if __name__ == "__main__":
    """ Load the dataset """
    images = sorted(glob(os.path.join("data", "image", "*")))
    masks = sorted(glob(os.path.join("data", "mask", "*")))

    """ Create folder to save images """
    create_dir("results")

    """ Loop over the dataset """
    for x, y in tqdm(zip(images, masks), total=len(images)):
        """ Extract the name """
        name = x.split("/")[-1].split(".")[0]

        """ Read image and mask """
        x = cv2.imread(x, cv2.IMREAD_COLOR)
        y = cv2.imread(y, cv2.IMREAD_GRAYSCALE)

        """ Detecting bounding boxes """
        bboxes = mask_to_bbox(y)

        """ marking bounding box on image """
        for bbox in bboxes:
            x = cv2.rectangle(x, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)

        """ Saving the image """
        cat_image = np.concatenate([x, parse_mask(y)], axis=1)
        cv2.imwrite(f"results/{name}.png", cat_image)