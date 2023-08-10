import re
from typing import Any
from django.http import HttpResponse

def validate_fields(*args: Any):
    return all(arg.strip() != '' for arg in args)

def verify_password(request: HttpResponse, password: str):

    if not len(password) > 6:
        return False
    
    if not re.search('[A-Z]', password):
        return False
    
    if not re.search('[a-z]', password):
        return False
    
    if not re.search('[0-9]', password):
        return False
    
    if not re.search('[@, &]', password):
        return False

    return True

