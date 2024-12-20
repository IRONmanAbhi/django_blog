from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def registration(request):
    if(request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!, Your are now able to login")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if(request.method == 'POST'):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if(u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile Info successfully updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'profile': profile,
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)