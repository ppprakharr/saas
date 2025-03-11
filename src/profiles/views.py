from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()

@login_required
def profile_view(request,username=None):
    user = get_object_or_404(User,username=username)
    owner = request.user
    context={
        'profile': user,
        'owner':owner
    }
    return render(request, 'profiles/details.html',context)

@login_required
def profile_list_view(request):
    users = User.objects.filter(is_active=True)
    owner=request.user
    context={
        'users':users,
        'owner':owner
    }
    return render(request,'profiles/list.html',context)



# Create your views here.
