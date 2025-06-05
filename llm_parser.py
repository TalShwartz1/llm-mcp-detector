import re

CLASSES = ["car", "bus", "truck", "motorbike"]


def parse_mission(mission_text):
    """Extracts start/end time and target object classes from the mission."""
    time_matches = re.findall(r'(\d{1,2}:\d{2})', mission_text)
    classes = [cls for cls in CLASSES if cls in mission_text.lower()]
    if len(time_matches) >= 2:
        start, end = time_matches[0], time_matches[1]
        return start, end, classes
    raise ValueError("Could not parse time range from mission.")

