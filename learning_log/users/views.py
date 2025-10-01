from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registration of a new user"""
    if request.method != 'POST':
        # Display default empty registration form
        form = UserCreationForm
    else:
        # Processing of a completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Logging user and redirection on the main page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display an empty form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
