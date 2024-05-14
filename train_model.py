from datetime import datetime
from ultralytics import YOLO

# Load the YOLOv8 model
#model = YOLO('yolov8n.pt')
pretrained_model = YOLO('models/best.pt')

# Obtiene la fecha y hora actual
actual_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Ruta de salida del mejor modelo
output = f'models/trains/{actual_time}.pt'

# TRAINING
results = pretrained_model.train(data='/home/rama811/repos/pytorch-dev-template/ball_detection/dataset/soccerNet/data.yaml',
                                 epochs=10, patience=10, project=output)
