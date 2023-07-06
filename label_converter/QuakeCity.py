import os
import numpy as np
import cv2
from skimage.measure import label, regionprops, find_contours
from skimage.morphology import dilation, closing

""" Creating a directory """


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


""" Convert a mask to border image """


def mask_to_border(mask):
    h, w = mask.shape
    border = np.zeros((h, w))

    contours = find_contours(mask)
    for contour in contours:
        for c in contour:
            x = int(c[0])
            y = int(c[1])
            border[x][y] = 255

    return border


""" Mask to bounding boxes """


def mask_to_bbox(mask):
    bboxes = []

    mask = mask_to_border(mask)
    lbl = label(mask)
    props = regionprops(lbl)
    for prop in props:
        x1 = prop.bbox[1]
        y1 = prop.bbox[0]

        x2 = prop.bbox[3]
        y2 = prop.bbox[2]

        bboxes.append([x1, y1, x2, y2])

    return bboxes


def parse_mask(mask):
    mask = np.expand_dims(mask, axis=-1)
    mask = np.concatenate([mask, mask, mask], axis=-1)
    return mask


def remove_small_boxes(bboxes, min_size = 50):
    temp = bboxes
    for bbox in bboxes:
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        if width < min_size or height < min_size:
            temp.remove(bbox)
    return temp

def write_outfile(bboxes, classification, outfile):
    for bbox in bboxes:
        xmin, ymin, xmax, ymax = bbox[0], bbox[1], bbox[2], bbox[3]
        width, height = int(xmax - xmin), int(ymax - ymin)
        x_centre, y_centre = xmin + width, ymin + height

        # Convert to Percentile
        x_centre, y_centre, width, height = x_centre / w, y_centre / h, width / w, height / h

        outfile.write(str(classification)+ " " + str(x_centre) + " " + str(y_centre) + " " + str(width) + " " + str(height) + "\n")


if __name__ == "__main__":
    """ Load the dataset """
    DATA_DIR = r'F:\Accumulated_Defect_Segmentation\UH_QuakeCity\QuakeCity\label'
    IMG_DIR = r'F:\Accumulated_Defect_Segmentation\UH_QuakeCity\QuakeCity\image'

    """ Create dir """
    create_dir(os.path.join(DATA_DIR, "YOLO_annotations"))

    files = os.scandir(os.path.join(DATA_DIR, "crack"))
    for file in files:

        print("Processing "+file.name)

        name = file.name.split(".")[0]

        # Output File
        outfile = open(os.path.join(DATA_DIR, "YOLO_annotations", name+".txt"), "w")

        """ Read image and mask """
        image = cv2.imread(os.path.join(IMG_DIR, file.name), cv2.IMREAD_COLOR)
        h, w, _ = image.shape

        crack_mask = cv2.imread(os.path.join(DATA_DIR, "crack", file.name), cv2.IMREAD_GRAYSCALE)
        rebar_mask = cv2.imread(os.path.join(DATA_DIR, "rebar", file.name), cv2.IMREAD_GRAYSCALE)
        spall_mask = cv2.imread(os.path.join(DATA_DIR, "spall", file.name), cv2.IMREAD_GRAYSCALE)

        """ Detecting Bounding Boxes """
        crack_mask = closing(dilation(dilation(dilation(dilation(dilation(closing(closing(crack_mask))))))))
        crack_bboxes = mask_to_bbox(crack_mask)
        rebar_mask = closing(dilation(dilation(dilation(dilation(dilation(closing(closing(rebar_mask))))))))
        rebar_bboxes = mask_to_bbox(rebar_mask)
        spall_mask = closing(dilation(dilation(dilation(dilation(dilation(closing(closing(spall_mask))))))))
        spall_bboxes = mask_to_bbox(spall_mask)

        """ Remove Too Small Boxes """
        crack_bboxes = remove_small_boxes(crack_bboxes)
        rebar_bboxes = remove_small_boxes(rebar_bboxes)
        spall_bboxes = remove_small_boxes(spall_bboxes)

        """ Write to File """
        write_outfile(crack_bboxes, 0, outfile)
        write_outfile(rebar_bboxes, 2, outfile)
        write_outfile(spall_bboxes, 1, outfile)

        """
        for bbox in crack_bboxes:
            # [top left, bottom right]
            image = cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)
        for bbox in rebar_bboxes:
            image = cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        for bbox in spall_bboxes:
            image = cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 255), 2)

        cv2.imshow("Test", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        """

        outfile.close()

files.close()
