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

## Running Instructions

#### Run Docker Container

``` bash
docker run --shm-size 15gb -it -v ./results:/projects/results msci623yolov8:latest
```

#### Run Training

``` bash 
yolo task=detect mode=train model=yolov8s.pt data=./datasets/CODEBRIM-2155/data.yaml epochs=50 imgsz=1024 batch=-1 patience=10 device=0 plots=True
```

#### Results

* CODEBRIM_baseline (model=yolov8x.pt)

```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        213       1106      0.451      0.329      0.295      0.144
       corrosion-rebar        213         61      0.334      0.262       0.18     0.0735
                 crack        213        559       0.44      0.252      0.264      0.113
         efflorescence        213        104      0.442       0.25      0.215      0.108
              spalling        213        382      0.587      0.552      0.521      0.281
```

* CODEBRIM_baseline (model=yolov8l.pt)
```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        213       1106      0.426      0.386      0.308      0.151
       corrosion-rebar        213         61      0.387      0.361      0.264      0.131
                 crack        213        559      0.343      0.342      0.255      0.106
         efflorescence        213        104      0.425       0.25       0.18     0.0931
              spalling        213        382      0.549      0.592      0.533      0.274
```

* CODEBRIM_baseline (model=yolov8m.pt)

```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        213       1106      0.391      0.365      0.305      0.148
       corrosion-rebar        213         61      0.333      0.377       0.24       0.12
                 crack        213        559      0.353      0.293      0.242        0.1
         efflorescence        213        104      0.403       0.24      0.222     0.0974
              spalling        213        382      0.477       0.55      0.515      0.274

```

* CODEBRIM_baseline(model=yolov8n.pt)
```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        213       1106      0.298      0.336      0.241      0.108
       corrosion-rebar        213         61      0.229      0.258      0.128     0.0539
                 crack        213        559      0.307      0.324       0.23      0.093
         efflorescence        213        104      0.236      0.212      0.149      0.062
              spalling        213        382       0.42      0.552      0.458      0.223
```

* Zhang_baseline (model=yolov8n.pt)

```
                   all        289        664      0.688      0.653      0.683      0.428
       corrosion-rebar        289        255      0.611      0.547      0.557      0.253
                 crack        289        195      0.663      0.616      0.654      0.373
              spalling        289        214      0.789      0.794      0.836      0.657
```

* Zhang_baseline (model=yolov8m.pt) (train 2)

```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        289        664      0.716      0.697      0.724      0.492
       corrosion-rebar        289        255      0.608      0.631      0.609      0.318
                 crack        289        195      0.727      0.605      0.682      0.426
              spalling        289        214      0.813      0.855      0.882      0.732
```

* Zhang_baseline (model=yolov8x.pt) (train 3)

```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        289        664      0.723      0.718      0.732      0.502
       corrosion-rebar        289        255       0.61      0.626      0.593      0.304
                 crack        289        195      0.739      0.672      0.721      0.477
              spalling        289        214      0.821      0.854      0.881      0.724
```


* S2DS_baseline (model=yolov8n.pt)

```
                   all        289        664      0.688      0.653      0.683      0.428
       corrosion-rebar        289        255      0.611      0.547      0.557      0.253
                 crack        289        195      0.663      0.616      0.654      0.373
              spalling        289        214      0.789      0.794      0.836      0.657

```

* S2DS_baseline (model=yolov8m.pt)
```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        122        892      0.578      0.395      0.422      0.254
       corrosion-rebar        122        320      0.594      0.494      0.524      0.313
                 crack        122        191      0.432      0.382      0.315      0.171
         efflorescence        122        165      0.668      0.279      0.363      0.204
              spalling        122        216      0.618      0.426      0.488      0.329

```

* S2DS_baseline (model=yolov8x.pt)
```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|████████
                   all        122        892      0.512      0.415      0.413       0.25
       corrosion-rebar        122        320      0.574      0.455      0.458      0.284
                 crack        122        191      0.411      0.482      0.365      0.208
         efflorescence        122        165      0.525      0.261      0.337      0.192
              spalling        122        216      0.538      0.463      0.494      0.317
```

* QuakeCity_baseline (model=yolov8n.pt) (train 3)

```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        289        664      0.723      0.718      0.732      0.502
       corrosion-rebar        289        255       0.61      0.626      0.593      0.304
                 crack        289        195      0.739      0.672      0.721      0.477
              spalling        289        214      0.821      0.854      0.881      0.724
```

* QuakeCity_baseline (model=yolov8m.pt) (train 9)

```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|████████
                   all        962      76803      0.512      0.422      0.419      0.298
       corrosion-rebar        962        848      0.471      0.192      0.232      0.122
                 crack        962      49759      0.508      0.401      0.401      0.279
              spalling        962      26196      0.558      0.672      0.624      0.493
```

* QuakeCity_baseline (model=yolov8x.pt) (train 10)

```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|████████
                   all        962      76803      0.505      0.475      0.458       0.33
       corrosion-rebar        962        848       0.45      0.273      0.295      0.154
                 crack        962      49759       0.51      0.448      0.435      0.314
              spalling        962      26196      0.556      0.703      0.643       0.52

```