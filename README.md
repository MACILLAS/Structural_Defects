# Structural Defect Detection Datasets
Prepared for academic credit: MSCI623 S2023

## Motivation
Vision-based visual inspections are a promising approach to reduce the labour costs
of a vital process to ensure high level of service and safety of public infrastructure.

In vision-based visual inspections, researcher will typically be expected to create their own datasets.
This is inefficient use of the researcher's time and without a benchmark, it is difficult to evaluate the 
performance of models and disincentives development of civil tailored models.

Another benefit of accumulating large datasets is to mitigate biases from any single dataset.
This can greatly increase model generalization and thus realworld applicability.  

In this work the authors will accumulate several defect detection datasets.
The authors will explore generalizability through zero-shot cross-validation.
And propose mitigation techniques to incorporate your own data. 

## Acknowledgement 
Thank you to those researchers that have graciously allowed us to use their datasets as a starting point.
We ask that if this work has been useful to you please also cite our data contributors.

## Data Preparation

We will convert all formats to YOLO format see: https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/#11-create-datasetyaml

YOLO Format:
One *.txt file per image (if no object in image, no *.txt file is required).
* One row per object
* Each row is class x_centre y_center width height format
* Box coordinates must be in normalized xywh format (from 0 - 1). If your boxes are in pixels, divide x_center and width by image width, and y_center and height by image height.
* Class numbers are zero-indexed (start from 0)

Directories

./datasets/images/train/datasource_0.jpg
./datasets/labels/train/datasource_0.txt

See structuraldamage.yaml for class definitions.

Due to incosistencies in the Zhang Dataset (i.e., rebar class should be 'spalling' with rebar labelled) authors relabelled
the relavant sections on Roboflow. 

You can find these datasets on Roboflow Universe at:

### CODEBRIM Bounding Box:
https://universe.roboflow.com/cvisslab/codebrim-poidd/dataset/2155

### Zhang Bounding Box:
https://universe.roboflow.com/cvisslab/zhang-3seb8/dataset/1

### QuakeCity Bounding Box:
https://universe.roboflow.com/cvisslab/quakecity/dataset/1

### S2DS
https://universe.roboflow.com/cvisslab/s2ds/dataset/1