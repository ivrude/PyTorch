from ultralytics import YOLO
model = YOLO('prepared/yolov8n-cls.pt')
result = model.train(data="prepared", epochs=10, imgsz=180)