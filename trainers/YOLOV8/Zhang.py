import os
import ultralytics
from ultralytics import YOLO
from roboflow import Roboflow

HOME = os.getcwd()
print(HOME)

ultralytics.checks()

rf = Roboflow(api_key="YOUR API KEY")
os.chdir('./datasets')
project = rf.workspace("cvisslab").project("zhang-3seb8")
dataset = project.version(1).download("yolov8")