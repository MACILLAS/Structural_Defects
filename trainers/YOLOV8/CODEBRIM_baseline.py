import os
import ultralytics
from ultralytics import YOLO
from roboflow import Roboflow

HOME = os.getcwd()
print(HOME)

ultralytics.checks()

rf = Roboflow(api_key="YOUR API KEY")
os.chdir('./datasets')
project = rf.workspace("cvisslab").project("codebrim-poidd")
dataset = project.version(2155).download("yolov8")

# run for training
#yolo task=detect mode=train model=yolov8s.pt data=./dataset/data.yaml epochs=25 imgsz=1024