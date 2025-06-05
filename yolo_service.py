from ultralytics import YOLO

model = YOLO("yolov8n.pt")

CLASS_LABELS = {
    2: "car",
    5: "bus",
    7: "truck",
    3: "motorbike"
}

NAME_TO_CLASS_ID = {v: k for k, v in CLASS_LABELS.items()}


def detect_objects_in_images(image_time_list, target_classes):
    result = []
    class_ids = [NAME_TO_CLASS_ID[name] for name in target_classes if name in NAME_TO_CLASS_ID]

    for img_path, timestamp in image_time_list:
        results = model(img_path)
        detected_classes = set()
        for r in results:
            for cls in r.boxes.cls:
                cls_id = int(cls)
                if cls_id in class_ids:
                    detected_classes.add(CLASS_LABELS[cls_id])
        if detected_classes:
            result.append({
                "image": img_path,
                "time": timestamp,
                "detected_classes": list(detected_classes)
            })
    return result