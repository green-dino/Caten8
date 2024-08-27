from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

def landing_page(request):
    return render(request, 'meow/landing_page.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'meow/user_list.html', {'users': users})

def trouble_ticket_list(request):
    # Add logic to retrieve and display trouble tickets
    return render(request, 'meow/trouble_ticket_list.html')

def user_detail(request, user_id):
    user = get_object_or_404(User, UserId=user_id)
    return render(request, 'meow/user_detail.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'meow/create_user.html', {'form': form})