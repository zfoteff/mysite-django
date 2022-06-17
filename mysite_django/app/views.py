from datetime import datetime
from django.http import JsonResponse

def index(req):
    return JsonResponse(data={'Response': 'Hello, World!', 'Time': datetime.now()})
