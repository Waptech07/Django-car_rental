from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Car, Categories, Rental
from django.contrib.auth.models import auth, User
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
    cars = Car.objects.all()[:4]
    return render(request, 'index.html', {'cars': cars})

def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:

            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already exists")
                return redirect("register")
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already Registered")
                return redirect("register")
            
            else:
                user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password,
                )

                user.save()
                
                return redirect("login")
            
        else:
            messages.info(request, "Password does not match")
            return redirect("register")

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)

            return redirect("/")
        else:

            messages.info(request, "Invalid Credential")
            return redirect("login")
    else:
        return render(request, "login.html")

def logout(request):

    auth.logout(request)
    return redirect("/login")

@login_required(login_url="login")
def car_list(request):
    cars = Car.objects.all()
    audi_cars = Categories.AudiCar.objects.all()
    bmw_cars = Categories.BmwCar.objects.all()
    mercedes_cars = Categories.MercedesCar.objects.all()
    toyota_cars = Categories.ToyotaCar.objects.all()

    context = {
        'cars' : cars,
        'audi_cars' : audi_cars,
        'bmw_cars' : bmw_cars,
        'mercedes_cars' : mercedes_cars,
        'toyota_cars' : toyota_cars     
    }
    return render(request, 'car_list.html', context)

@login_required(login_url="login")
def rent_car(request):
    if request.method == 'POST':
        car_id = request.POST['car']
        rental_date = request.POST['rental_date']
        return_date = request.POST['return_date']

        try:
            car = Car.objects.get(id=car_id)

            # Check if the car is available for the selected dates
            existing_rentals = Rental.objects.filter(car=car)
            for rental in existing_rentals:
                if rental_date <= rental.return_date and return_date >= rental.rental_date:
                    messages.error(request, 'Car is not available for the selected dates.')
                    return redirect('rent_car')

            # Create a new rental record
            rental = Rental(car=car, customer=request.user, rental_date=rental_date, return_date=return_date)
            rental.save()

            messages.success(request, 'Car rented successfully.')
            return redirect('return_car')
        except Car.DoesNotExist:
            messages.error(request, 'Car not found.')
    
    cars = Car.objects.all()
    return render(request, 'rent_car.html', {'cars': cars})

@login_required(login_url="login")
def return_car(request):
    if request.method == 'POST':
        rental_id = request.POST['rental']
        return_date = request.POST['return_date']

        try:
            rental = Rental.objects.get(id=rental_id)

            # Ensure that the return date is not before the rental date
            if return_date < str(rental.rental_date):
                messages.error(request, 'Return date cannot be before the rental date.')
                return redirect('return_car')

            # Update the return date in the rental record
            rental.return_date = return_date
            rental.save()

            messages.success(request, 'Car returned successfully.')
            return redirect('car_list')
        except Rental.DoesNotExist:
            messages.error(request, 'Rental record not found.')

    rentals = Rental.objects.all()
    return render(request, 'return_car.html', {'rentals': rentals})

def guest_user(request):
    
    # Get all books which are not issued to user
    cars = Car.objects.all()[:4]

    return render(request, 'guest_user.html', {'cars': cars,})

@login_required(login_url="login")
def rent_history(request):

    my_items = Rental.objects.filter(customer_id=request.user)

    paginator = Paginator(my_items, 10)

    page_number = request.GET.get("page")
    show_data_final = paginator.get_page(page_number)

    return render(request, 'rent_history.html', {'rentals': show_data_final})

@login_required(login_url="login")
def user_profile(request):
    profile = User.objects.all()

    return render(request, 'user_profile.html', {'profile' : profile})

@login_required(login_url="login")
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('edit_profile')

    else:

        return render(request, 'edit_profile.html')

@login_required(login_url="login")
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST["confirm_new_password"]

         # Verify old password
        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
        elif new_password != confirm_new_password:
            messages.error(request, 'New passwords do not match.')
        else:
            # Change the password
            request.user.set_password(new_password)
            request.user.save()

            # Update the user's session to prevent them from being logged out
            update_session_auth_hash(request, request.user)

            messages.success(request, 'Your password has been changed successfully.')
            return redirect('change_password')

    
    return render(request, "change_password.html")