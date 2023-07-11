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

# run docker
# docker run --shm-size 15gb -it msci623yolov8:test
# run for training
#yolo task=detect mode=train model=yolov8s.pt data=./datasets/CODEBRIM-2155/data.yaml epochs=50 imgsz=1024 batch=-1 patience=10 device=0