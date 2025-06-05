from image_db_service import get_images_in_time_range
from yolo_service import detect_objects_in_images


def orchestrate_services(start_time, end_time, target_classes):
    images_with_time = get_images_in_time_range(start_time, end_time)
    print(f"[MCP] Retrieved {len(images_with_time)} image(s) in range")
    result_images = detect_objects_in_images(images_with_time, target_classes)
    return result_images
