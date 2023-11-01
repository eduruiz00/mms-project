from mmdetection.demo.image_demo import main_v2 as detect_img
import json
import os

def get_labels_above_threshold(file_path, classes_string, threshold=0.3):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    labels = data['labels']
    scores = data['scores']
    classes = classes_string.split(' . ')
    
    labels_above_threshold = [classes[label] for label, score in zip(labels, scores) if score > threshold]
    
    return labels_above_threshold

def detect_ingredients(image, ingredients):
    config_path = "mmdetection/configs/grounding_dino/grounding_dino_swin-b_pretrain_mixeddata.py"

    model_path = "mmdetection/weights/groundingdino_swinb_cogcoor_mmdet-55949c9c.pth"
    detect_img(image, config_path, model_path, ingredients)

    base_name = os.path.splitext(os.path.basename(image))[0]

    if os.path.exists(f"output/preds/{base_name}.json"):
        res = get_labels_above_threshold(f"output/preds/{base_name}.json", ingredients)
        return set(res)
