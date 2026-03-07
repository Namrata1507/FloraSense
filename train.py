# train.py
# Script to train YOLOv8 model for weed detection

from ultralytics import YOLO
import torch

def main():

    # Check if GPU is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    # Load pretrained YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Start training
    model.train(
        data="data.yaml",     # dataset configuration file
        epochs=50,            # number of training cycles
        imgsz=640,            # image size
        batch=16,             # batch size
        device=device,        # CPU or GPU
        project="runs/detect",
        name="florasense_train",
        workers=4,
        patience=20
    )

    # Validate the trained model
    model.val()

    print("Training completed successfully!")

if __name__ == "__main__":
    main()