from typing import Any
from PIL import Image

def validate_fields(*args: Any):
    return all(arg.strip() != '' for arg in args)

def check_image(file):
    try:
        img = Image.open(file)
        valid_formats = ('JPEG', 'PNG', 'SVG')
        if img.format not in valid_formats:
            return False
        return True
    except Exception as e:
        return False