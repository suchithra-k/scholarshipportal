from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from .forms import StudentSignUpForm
from .user_constants import UserConstant
from .models import Role, Organisation


@login_required
def process_login(request):
    user_role = request.user.profile.role.role_id
    if user_role == UserConstant.ROLE_ADMIN:
        return redirect('admin:index')
    if user_role == UserConstant.ROLE_STUDENT:
        return redirect('list_schloarships')
    if user_role == UserConstant.ROLE_ORGANISATION_ADMIN:
        return redirect('organisation_home')
    return HttpResponse("Hello, world. <a href='/logout'>logout</a> ") 


def register_user(request):
    user_role = request.GET.get('user_role')
    user_role = user_role if user_role == 'organisation' else 'student'

    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.date_of_birth = form.cleaned_data.get('birth_date')
            user.profile.gender = form.cleaned_data.get('gender')
            user_role = form.cleaned_data.get('user_role')
            if user_role == 'organisation':
                user.profile.role = Role.objects.get(pk=UserConstant.ROLE_ORGANISATION_ADMIN)
                Organisation(user=user).save()
            user.save()
            messages.success(
                request, 'Welcome %s! Your account has been created! You are now able to log in' % user.username)
            return redirect('login')
    else:
        form = StudentSignUpForm()
        form.fields["user_role"].initial = user_role

    return render(request, "registration/signup.html", {'form': form, 'user_role': user_role})
