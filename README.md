# Detect gas cylinders in conveyor belts  :revolving_hearts:  :revolving_hearts:
- This model can be used to track moving gas cylinders in a conveyor belt.
- It was built as part of a solution of a problem statement
- It uses the yolov5 model to detect the cylinders. The model was trained using a custom dataset and the wieghts were obtained.
- __A custom detect.py file has been done based on the detect.py on the yolov5 repo. After one clones the repo, replace that file with this file. This will enable each instance of detection of the file (an image or a video) to be stored on a given destination folder along with a text file that gives infromation about the detected cylinders.__

## Dataset Used
- The dataset of cylinders was provided as part of a problem statement.
- This dataset was then labelled and augmented in Roboflow.
- Find the link of the dataset [here](https://drive.google.com/drive/folders/1pxKVh_Av9P_3Zs_CCRbgjixkqefQVjP9?usp=sharing).

# How to use
This is a yolov5 model trained on cylinder data which is used to detect gas cylinders from top view images and videos

- Clone the yolov5 repository from [here](https://github.com/ultralytics/yolov5). 
- After cloning, clone [this](https://github.com/Gokul-GMenon/cylinder-detection-yolov5/) repository, copy the yolov5 folder into the same directory. Then run the [detect_cylinder.py](https://github.com/Gokul-GMenon/cylinder-detection-yolov5/blob/main/detect_cylinder.py) file (As of now, on a windows machine) like:
```
python detect_cylinder.py --src [NAME OF SOURCE FILE] --dest [NAME OF DESTINATION FILE]
```
