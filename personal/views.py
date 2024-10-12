import os
import json
from django.conf import settings
from django.http import Http404
from django.shortcuts import render


# Create your views here.
def personal(request):
    
    context = {
        "first_name": "David",
        "last_name": "Schmid",
    }
    return render(request, "personal.html", context)