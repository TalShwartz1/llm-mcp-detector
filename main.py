import unittest
from llm_parser import parse_mission
from image_db_service import get_images_in_time_range
from mcp_orchestrator import orchestrate_services


class TestLLMMCPPipeline(unittest.TestCase):

    def test_image_db_service(self):
        images = get_images_in_time_range("11:00", "11:05")
        image_names = [img for img, t in images]
        self.assertIn("image1.jpg", image_names)
        self.assertIn("image2.jpg", image_names)
        self.assertIn("image3.jpg", image_names)


if __name__ == '__main__':
    mission_text = "detect all buses and cars in images between 11:00 and 11:05"
    start, end, target_classes = parse_mission(mission_text)

    results = orchestrate_services(start, end, target_classes)

    print("Detection Results:")
    for item in results:
        print(f"Image: {item['image']}, Time: {item['time']}, Detected: {item['detected_classes']}")
