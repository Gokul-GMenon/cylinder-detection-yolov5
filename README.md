# How to use
This is a yolov5 model trained on cylinder data which is used to detect gas cylinders from top view images and videos

- Clone the yolov5 repository from [here](https://github.com/ultralytics/yolov5). 
- After cloning, clone [this](https://github.com/Gokul-GMenon/cylinder-detection-yolov5/) repository and copy the yolov5 folder into the same directory. Then run the [detect_cylinder.py](https://github.com/Gokul-GMenon/cylinder-detection-yolov5/blob/main/detect_cylinder.py) file (As of now, on a windows machine) like:
```
python detect_cylinder.py --src [NAME OF SOURCE FILE] --dest [NAME OF DESTINATION FILE]
```
