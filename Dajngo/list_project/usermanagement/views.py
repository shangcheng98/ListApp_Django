from django.shortcuts import render

# Create your views here.

def signIn(req):
    print('sign in ')
    return render(req,"signin.html")