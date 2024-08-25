from django.shortcuts import render
from .models import Post
from . import templates
from .api import get_ernie_response

def home(request):
    return render(request, 'home.html')




def index(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        response = get_ernie_response(prompt)
        return render(request, "ernie/index.html", {"response": response})
    return render(request, "ernie/index.html")