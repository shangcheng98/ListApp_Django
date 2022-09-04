from ast import Delete, If
from turtle import done
from urllib import request
from django.shortcuts import render
from .models import ListItem
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect   
# from .models import user
from django.contrib.auth.models import User

# Create your views here.

 

def mylist(req):
    if req.method == 'POST':
        if req.POST['type'] == 'add':
            print('received Data : ' , req.POST['task'])
            ListItem.objects.create(context =  req.POST['task'])
        elif (req.POST['type'] == 'choose'):
            ListItem.objects.all().update(done = False)
            id_str = req.POST['id']
            id_array = id_str.split(',')
            print('received IDData : ' , id_array)
            
            for i in range(len(id_array)):
               
                ListItem.objects.filter(id=id_array[i]).update(done = True)
                
            print(ListItem.objects.all())

        elif req.POST['type'] =='delete':
            ListItem.objects.filter(done = True).delete() 
    
    all_items = ListItem.objects.all()
     
    return render(req, 'list.html',{'all_items':all_items})

def logins(req):
    if req.method == 'POST':
        Tusername = req.POST.get("username")
        Tpassword = req.POST.get("password")
        newusername = req.POST.get("signUsername")
        newpassword = req.POST.get("signPassword")
        print(Tusername)
        print(newusername)
        if newusername == None:
            user = authenticate(username = Tusername,password = Tpassword)
            if user:
                login(req,user)
                print('okok!!!')
                return redirect('mylist')
            else:
                print('wrong!!!')
                return render(req,'login.html')
        else:
            newusername = req.POST.get("signUsername")
            newpassword = req.POST.get("signPassword")
            cuser = User.objects.create_user(username = newusername,password=newpassword)
            cuser.save()
            print('new user show up')
    return render(req,"login.html")

 