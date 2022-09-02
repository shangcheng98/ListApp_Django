from django.shortcuts import render
from .models import ListItem
from .models import user

# Create your views here.
def mylist(req):
    if req.method == 'POST':
        print('received Data : ' , req.POST['task'])
        ListItem.objects.create(context =  req.POST['task'])
    
    all_items = ListItem.objects.all()
    return render(req, 'list.html',{'all_items':all_items})


def signUp(req):
    if req.method =="POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user().name = username
        user().password = password
        user().save()

    return render(req,"login.html")