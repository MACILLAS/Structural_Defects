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

#### Dataset Cross-Validation

```
yolo task=detect mode=val model=./results/QuakeCity_baseline/detect/trainn/weights/best.pt data=./datasets/Zhang-1/data.yaml
```

* QuakeCity (train) ==> Zhang (test)
    * yolo_nano
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 
                   all        289        664      0.456     0.0628     0.0519     0.0289
       corrosion-rebar        289        255          1          0          0          0
                 crack        289        195     0.0473     0.0154    0.00447    0.00213
              spalling        289        214       0.32      0.173      0.151     0.0845
    ```
    * yolo_medium
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 
                   all        289        664      0.501       0.11     0.0946     0.0409
       corrosion-rebar        289        255          1          0          0          0
                 crack        289        195        0.1      0.041     0.0107    0.00315
              spalling        289        214      0.403       0.29      0.273       0.12
    ```
    * yolo_xl
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 
                   all        289        664      0.493     0.0869     0.0661     0.0316
       corrosion-rebar        289        255          1          0          0          0
                 crack        289        195     0.0717      0.041    0.00863    0.00246
              spalling        289        214      0.406       0.22       0.19     0.0923
    ```


* Zhang (train) ==> QuakeCity (test)
    * yolo_nano
    ```
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 61/61 [01:03<00:00,  1.04s/it]
                   all        962      76803     0.0716     0.0389     0.0497     0.0226
       corrosion-rebar        962        848   0.000113    0.00472   5.77e-05   1.73e-05
                 crack        962      49759     0.0934    0.00474     0.0514     0.0265
              spalling        962      26196      0.121      0.107     0.0977     0.0413
    ```
    * yolo_medium
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 61/61 [04:22<00:00,  4.30s/it]
                   all        962      76803     0.0585     0.0606     0.0477     0.0188
       corrosion-rebar        962        848   0.000287     0.0212   0.000149   4.96e-05
                 crack        962      49759     0.0702     0.0117     0.0403     0.0196
              spalling        962      26196      0.105      0.149      0.103     0.0369
    ```
    * yolo_xl
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        962      76803     0.0576      0.069     0.0469     0.0181
       corrosion-rebar        962        848   0.000499      0.033   0.000263   7.03e-05
                 crack        962      49759     0.0749     0.0153      0.043     0.0199
              spalling        962      26196     0.0975      0.159     0.0975     0.0344
    ```

* CODEBRIM (train) ==> S2DS (test)
    * yolo_nano
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        122        892      0.223       0.11     0.0744     0.0261
       corrosion-rebar        122        320      0.255    0.00937     0.0252    0.00678
                 crack        122        191      0.175      0.173     0.0851      0.027
         efflorescence        122        165      0.213     0.0545     0.0379     0.0141
              spalling        122        216      0.249      0.204       0.15     0.0566
    ```
    * yolo_m
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████
                   all        122        892      0.175      0.137     0.0923     0.0324
       corrosion-rebar        122        320      0.175     0.0156     0.0421     0.0139
                 crack        122        191      0.121      0.236        0.1     0.0309
         efflorescence        122        165       0.14     0.0606      0.047      0.018
              spalling        122        216      0.263      0.236       0.18     0.0667
    ```
    * yolo_xl
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 8/8 [01:18<00:00,  9.77s/it]
                   all        122        892      0.251      0.141     0.0934     0.0373
       corrosion-rebar        122        320      0.419     0.0219       0.05      0.015
                 crack        122        191      0.163      0.251      0.115     0.0408
         efflorescence        122        165      0.124     0.0485      0.028     0.0103
              spalling        122        216      0.298      0.241      0.181     0.0831
    ```

* S2DS (train) ==> CODEBRIM (test)
    * yolo_n
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 14/14 [00:12<00:00,  1.10it/s]
                   all        213       1106      0.102      0.112      0.047     0.0171
       corrosion-rebar        213         61     0.0131      0.115      0.016    0.00705
                 crack        213        559      0.118     0.0751     0.0357     0.0148
         efflorescence        213        104     0.0356     0.0192    0.00983    0.00577
              spalling        213        382       0.24      0.241      0.126     0.0409
    ```
    * yolo_m
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 14/14 [00:57<00:00,  4.09s/it]
                   all        213       1106      0.103      0.124     0.0432     0.0163
       corrosion-rebar        213         61      0.017       0.18     0.0196    0.00521
                 crack        213        559     0.0912     0.0537       0.03     0.0143
         efflorescence        213        104      0.134     0.0769     0.0341     0.0141
              spalling        213        382      0.168      0.183      0.089     0.0318
    ```
    * yolo_xl
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 14/14 [02:18<00:00,  9.89s/it]
                   all        213       1106     0.0811      0.108     0.0385     0.0148
       corrosion-rebar        213         61    0.00973      0.115     0.0124    0.00308
                 crack        213        559     0.0703     0.0662     0.0271     0.0123
         efflorescence        213        104     0.0852     0.0481     0.0133    0.00629
              spalling        213        382      0.159      0.202      0.101     0.0376
    ```

* S2DS (train) ==> Zhang (test)
    * yolo_n
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 19/19 [00:
                   all        289        664      0.202       0.24      0.152     0.0728
       corrosion-rebar        289        255      0.241      0.267      0.141     0.0537
                 crack        289        195       0.11     0.0667     0.0598     0.0202
              spalling        289        214      0.256      0.388      0.255      0.145
    ```
    * yolo_m
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 19/19 [00:
                   all        289        664      0.257       0.29      0.195      0.101
       corrosion-rebar        289        255      0.237       0.31      0.176     0.0644
                 crack        289        195      0.231      0.102      0.107     0.0358
              spalling        289        214      0.303      0.458      0.302      0.204
    ```
    * yolo_x
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 19/19 [00:
                   all        289        664      0.249      0.284      0.199       0.12
       corrosion-rebar        289        255      0.244      0.282      0.147     0.0582
                 crack        289        195      0.192      0.108     0.0849     0.0329
              spalling        289        214      0.312      0.463      0.366      0.268
    ```

* Zhang (train) ==> S2DS (test)
    * train_n
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 8/8 [00:01
                   all        122        892      0.241      0.111     0.0953     0.0472
       corrosion-rebar        122        320       0.39      0.153      0.135     0.0645
                 crack        122        191      0.211     0.0838     0.0668     0.0309
         efflorescence        122        165          0          0          0          0
              spalling        122        216      0.364      0.208       0.18     0.0933
    ```
    * train_m
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 8/8 [00:03
                   all        122        892      0.219       0.12      0.111     0.0621
       corrosion-rebar        122        320      0.335      0.163      0.146     0.0714
                 crack        122        191      0.165     0.0995     0.0749     0.0403
         efflorescence        122        165          0          0          0          0
              spalling        122        216      0.376      0.218      0.225      0.137
    ```
    * train_x
    ```
                     Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 8/8 [00:05
                   all        122        892      0.309      0.122      0.117     0.0627
       corrosion-rebar        122        320      0.418      0.155      0.158     0.0723
                 crack        122        191      0.389      0.126      0.104     0.0485
         efflorescence        122        165          0          0          0          0
              spalling        122        216       0.43      0.208      0.205       0.13
    ```

    