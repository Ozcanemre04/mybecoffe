
from datetime import datetime


from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout
from mybecoffeApp.models import  recettes,presence, users
from .forms import  recettesForm, registerForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
   if request.user.is_authenticated:
      return redirect('/recettes/')
   return render(request,'mybecoffeApp/home.html')




#register
def create_user(request):
   if request.user.is_authenticated:
      return redirect('/recettes/')
   form=registerForm()
   if request.method == 'POST':
      form=registerForm(request.POST)
      if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         messages.success(request,'account was created for '+ user)
         return redirect('/login/')
      else:
         messages.success(request,'password too short or username already used')   
   context={'form':form}
   return render(request,'mybecoffeApp/register.html',context)



#login
def index_login(request):
  if request.user.is_authenticated:
    return redirect('/recettes/')
  if request.method =='POST':
     username=request.POST.get('username')
     password=request.POST.get('password')
     user=authenticate(request,username=username,password=password)

     if user is not None:
       login(request,user)
       return redirect('/recettes/')
   
     else:
      messages.success(request,'error wrong password or username')

  return render(request,'mybecoffeApp/login.html')

#logout
def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='login')
#all recettes 
def index_recettes(request):
   now =datetime.now().strftime('%H:%M')
   today_date=datetime.now().strftime('%Y-%m-%d')
   recette = recettes.objects.all().order_by('date')
   h1=datetime.now().strftime('07:00')
   h2=datetime.now().strftime('15:00')
   
   userr=request.user
   presences=presence.objects.filter(user_id= userr ,date=today_date)
   
   
      
   return render(request, 'mybecoffeApp/index.html',context={"recettes":recette,"now":now,'h1':h1,"presences":presences,"h2":h2,'today':today_date})

#post arrival_time
@login_required(login_url='login')
def create_arrival(request):
    if request.method == "POST":
        now = datetime.now()
        presences = presence.objects.filter(user_id=request.user, date=now)
        if not presences:
            presence.objects.create(user_id=request.user,date=now,arrival_time=now).save()
        else:
            return redirect("home")
        messages.success(request, " arrival_time succesfully reported." )

        return redirect("/recettes/")
#post depart_time
@login_required(login_url='login')
def update_depart(request):
    if request.method == "POST":
        now = datetime.now()
        presences = presence.objects.get(user_id=request.user, date=now)
        if presences:
            presences.depart_time = now
            presences.save()
            messages.info(request, "Depart_time succesfully reported.")
        return redirect("/recettes/") 


@login_required(login_url='login')
#post recettes
def create_recettes(request):
   form=recettesForm()
   if request.method == 'POST':
      form=recettesForm(request.POST)
      if form.is_valid():
         form.instance.user_id = request.user
         form.save()
         return redirect('/recettes/')
      else:
         messages.success(request,'date already picked or date is not valid')   
   context={'form':form}
   return render(request,'mybecoffeApp/postrecettes.html',context)


#get presences
@login_required(login_url='login')
def index_presences(request):
   presences = presence.objects.all().order_by('date')
   return render(request,'mybecoffeApp/all_users_presences.html',context={'presences':presences})

#update recettes
@login_required(login_url='login')
def update_recettes(request,pk):
  recettess=recettes
  try:
   
    userr=request.user
    recettess=recettes.objects.get(id=pk)
    form=recettesForm(instance=recettess)
  
    if request.method == 'POST':
      form=recettesForm(request.POST,instance=recettess)
      if form.is_valid():
         if not userr.chef:
          form.instance.user_id = request.user
          form.save()
          return redirect('/recettes/')
         else:
            form.save()
            return redirect('/recettes/')

      else:
         messages.success(request,'date already picked or date is not valid')
  except ObjectDoesNotExist:
      return redirect('/recettes/')
         
  context={'form':form,"recettess":recettess}
  return render(request,'mybecoffeApp/patch_recette.html',context)


#delete recette
@login_required(login_url='login')
def destroy_recettes(request,pk):
   recettess=recettes.objects.get(id=pk)
   if request.method == 'POST':
      recettess.delete()
      return redirect('/recettes/')
   return render(request,'mybecoffeApp/index.html')


  #get profile   
@login_required(login_url='login')
def index_profile(request,pk):
  try: 
    userr=users.objects.get(id=pk)
    form=registerForm(instance=userr)

    if request.method =='POST':
      form=registerForm(request.POST,instance=userr)
      if form.is_valid():
         form.instance.user_id = request.user
         form.save()
         return redirect('/recettes/')
      else:
         messages.success(request,'password too short or username already used') 
  except ObjectDoesNotExist:
      return redirect('/recettes/')        
  return render(request,'mybecoffeApp/profile.html',context={'form':form,'userr':userr})


#all users
@login_required(login_url='login')
def index_users(request):
   
   userss=users.objects.filter(chef=False)
   return render(request,'mybecoffeApp/all_users.html',context={'userss':userss})

