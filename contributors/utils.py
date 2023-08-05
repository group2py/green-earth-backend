from typing import Any

def validate_fields(*args: Any):
    return all(arg.strip() != '' for arg in args)


