from django.shortcuts import render, redirect
from accounts.forms import UserLoginForm, UserRegisterForm
from accounts.models import CustomerProfile, SellerProfile
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def user_register_view(request):
    if request.method == 'POST':
        # UserRegisterForm is a form that we defined previously in the form file
        form = UserRegisterForm(request.POST)   
        # all the data that is sent by post will be saved in the form 
        if form.is_valid():
        # when we use a model in our form(going to complete database with column based on form)
            user = form.save()
            # Objects.create() exists on all Django models. It creates a new row in the database table for that model
            # , just like creating a new instance of User or CustomerProfile and saving it to the database.
            CustomerProfile.objects.create(user=user)
            login(request,user)
            messages.success(request, f'user {user.first_name} has successfully registered')
            return redirect('home')  
        # or return redirect(reverse('home'))
        else:
            messages.error(request, f'there was an error in registeration')
    else:
        form= UserRegisterForm()
    return render(request,'registration/signup.html',{'form':form})   

def user_login_view(request):
    if request.method == 'POST':
        # UserLoginForm is a form that we defined previously in the form file
        form = UserLoginForm(request,data=request.POST)   
        # all the data that is sent by post will be saved in the form 
        # form.is_valid() check both field validation as well as if user exist with these user and pass
        if form.is_valid():
            # اون کاربری که با شماره تلفن و رمز عبور درست وارد شده رو به من بده
            #  get user comes from AuthenticationForm
            user= form.get_user()
            login(request,user)
            messages.success(request, f'user {user.first_name} has successfully entered')
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid phone number or password.')
    else:
        form= UserLoginForm()
    return render(request,'registration/login.html',{'form':form})        
    
def user_logout_view(request):
    messages.info(request, f'successfully loged out')
    logout(request)
    return redirect('home')    


@login_required
def customer_view(request):
    customerProfile = get_object_or_404(
        CustomerProfile,
        user=request.user
    )

    # if user is not seller none will be returned
    sellerProfile =  SellerProfile.objects.filter(
        user=request.user
    ).first()

    return render(request, 'customer_panel.html', {
        'customer': customerProfile,
        'seller_profile' : sellerProfile
    })

@login_required
def become_seller_view(request):
    SellerProfile.objects.get_or_create(user=request.user)
    return redirect ('seller_panel')


