from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import User
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method == "GET":
        return render(request, 'news/index.html')
    return HttpResponse("Error")
