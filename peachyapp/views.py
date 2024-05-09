from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from . models import Profile
from . forms import ChangePasswordForm, UpdateUserForm

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'User has been Updated!!')
            return redirect("home")
        return render(request, "auth/update_user.html", {"user_form":user_form})
    else:
        messages.success(request, "You must be logged in to access the page!!")
        return redirect("home")




def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user 
        # Is form filled out?
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success, "Your Password Has Been Updated, Please Log In Again.."
                return redirect('user_login')
            else:
                
                for error in list(form.errors.values()):
                    messages.error(request, error)  #This helps for django errors
                    return redirect('update_password')

        else:
            form = ChangePasswordForm(current_user)
            return render(request, "auth/update_password.html", {"form":form})
        
    else:
        messages.success(request, 'You must be logged in to view page')
        return redirect('home')


def birthdays(request):
    return render(request, 'products/birthdays.html', {})

def events(request):
    return render(request, 'products/events.html', {})

def home(request):
    return render(request, 'index.html', {})




def user_logout(request):
    logout(request)
    messages.success(request, 'You are now logged out!')
    return redirect('home')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        capital_username = username.capitalize()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {capital_username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password!')
    return render(request, 'auth/login.html', {})



def register(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # other details
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # phone = request.POST['phone']
        # city = request.POST['city']
        # country = request.POST['country']
        # gender = request.POST['gender']
        # nationality = request.POST['nationality']
        # group = request.POST['group']

        # user_details = Profile(first_name=first_name, last_name=last_name, email=email, phone=phone, city=city, country=country, nationality=nationality, gender=gender, group=group)
        # user_details.save()
        

        # Chech if passwords match
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email already exists')
                    return redirect('register')
                else:
                    # Looks good
                    capitalize_username = username.capitalize()
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    # profile = Profile.objects.create(user=user, phone=phone, city=city, gender=gender, nationality=nationality, country=country)
                    # profile.save()
                    # Login after registration
                    auth.login(request, user)
                    messages.success(request, f'Welcome {capitalize_username} to the PeachyBoys!')
                    # return redirect('index')
                    user.save()
                    return redirect('home')
        else:
            messages.warning(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'auth/register.html', {})