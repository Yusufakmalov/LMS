from django.shortcuts import render, redirect
from django.http import Http404

from .models import CustomUser, RoleName

def users_list(request):
    users = CustomUser.objects.filter(role__name=RoleName.STUDENT)
    return render(request, 'account/users-list.html', {'users': users})


def user_detail(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'account/view-profile.html', {'user': user})



def user_delete(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('account:users_list')
    raise Http404("User not found")