# Установка библиотек
!pip install ultralytics

from google.colab import drive
drive.mount('/content/drive')

from ultralytics import YOLO

model = YOLO('yolo11n.pt')  
result = model.train(
    data='/content/drive/MyDrive/dataset/data.yaml',  
    epochs=30,
    imgsz=640,
    batch=4,
    project='runs/yolov11_train',
    name='experiment1'
)
