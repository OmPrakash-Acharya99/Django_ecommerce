from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from store.forms import customUserForm
def register(request):
    form = customUserForm()
    if request.method == 'POST':
        form = customUserForm(request.POST)
        if  form.is_valid():
            form.save()
            messages.success(request,'Register Successful ! , Login to Continue')
            return redirect('/login')
    context = {'form':form}
    return render(request,"store/auth/register.html",context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect('/')
    else:
        
        if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = name , password = password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in successfully.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or pasword")
                return redirect('/login')
       
    return render(request,'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
        return redirect('/')
            
            
