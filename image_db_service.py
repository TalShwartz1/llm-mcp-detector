def get_images_in_time_range(start_time, end_time):
    """Simulates retrieving images between two times."""
    dummy_images = [
        ("image1.jpg", "11:00"),
        ("image2.jpg", "11:03"),
        ("image3.jpg", "11:04")
    ]
    return [(img, t) for img, t in dummy_images if start_time <= t <= end_time]

