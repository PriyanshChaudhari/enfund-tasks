from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')  # Redirect to a dashboard or home page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
