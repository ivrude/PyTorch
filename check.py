from ultralytics import YOLO
model = YOLO('runs/classify/train/weights/best.pt')  # load a custom model

# Predict with the model
results = model('5.jpg',)  # predict on an image
if results[0].probs.top1 == 0:
    print("daisy")
elif results[0].probs.top1 == 1:
    print("dandelion")
elif results[0].probs.top1 == 3:
    print("sunflowers")
else:
    print("rose")
