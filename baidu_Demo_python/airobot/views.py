from django.shortcuts import render
from .models import Post
from . import templates
from .api import get_ernie_response
from erniebot.client import ErnieClient

def get_ernie_response(prompt):
    ernie_client = ErnieClient(api_key="your_api_key_here")
    response = ernie_client.generate_text(
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        top_p=0.9,
        num_return_sequences=1
    )
    return response.generated_text[0]
def home(request):
    return render(request, 'home.html')




def index(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        response = get_ernie_response(prompt)
        return render(request, "ernie/index.html", {"response": response})
    return render(request, "ernie/index.html")