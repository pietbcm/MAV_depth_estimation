# Configurations & Hyperparameters for model training
import torch

config = {
    # Model training configurations
    "device": "cuda" if torch.cuda.is_available() else "cpu",
    "epochs": 100,
    "batch_size": 8, # For test, use a smaller batch size
    "train_val_split": 0.8,
    "learning_rate": 0.001,
    "weight_decay": 0.0001,
    "num_workers": 1, # Number of CPU workers for data loading, small for test
    "patience": 5, # Early stopping patience
    
    # Data 
    'h5_path': 'data/h5',
    'raw_path': 'data/raw_image',
    'image_path': 'data/original_image',
    'depth_path': 'data/depth_matrix',
    'uyvy_path': 'data/uyvy',
    "yuv_path": "data/yuv",
    'image_width': 240,
    'image_height': 520,
    "image_mode": "YUV", # "RGB" or "L" (grayscale) or "UYVY" or "YUV"
    "input_type_uint8": False,
    "cam_hor_FOV": 100,
    
    # Model configurations
    "input_channels": 3, # 3 for RGB, 1 for grayscale, 1 for uyuv(1*H*2W), 3 for yuv
    "output_channels": 16, # Output depth vector length

    # Model paths
    "logging_on": True,
    "save_model_path": "models",
    "save_log_path": "logs/logger",
    "save_event_path": "logs/events",
}