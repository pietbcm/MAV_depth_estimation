# Configurations & Hyperparameters for model training
import torch

config = {
    # Model training configurations
    "device": "cuda" if torch.cuda.is_available() else "cpu",
    "epochs": 1,
    "batch_size": 1, # For test, use a smaller batch size
    "train_val_split": 0.8,
    "learning_rate": 0.001,
    "weight_decay": 0.0001,
    "num_workers": 1, # Number of CPU workers for data loading, small for test
    "ssim_weight": 0.8,
    
    # Model configurations
    "input_channels": 1, # Only use RGB as input
    "output_channels": 1,
    "input_type_uint8": True,
    
    # Data 
    'image_path': 'data/original_image',
    'depth_path': 'data/depth_map',
    "image_mode": "L", # "RGB" or "L" (grayscale)

    # Model paths
    "logging_on": True,
    "save_model_path": "models",
    "save_log_path": "logs/logger",
    "save_event_path": "logs/events",
}