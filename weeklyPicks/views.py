from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .models import Pick, User
# Create your views here.
def index(request):
    context = {
		"picks": Pick.objects.all(),
        "users": User.objects.all(),
	}
    return render(request, "weeklypicks/index.html", context)

def user(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        "users": user,   
    }
    return render(request, "weeklypicks/index.html", context) 

def pick(request, pick_id):
    try:
        pick = Pick.objects.get(pk=pick_id)
    except Pick.DoesNotExist:
        raise Http404("Pick does not exist.")
    context = {
        "pick": pick,
        "users": User.objects.all(),
        #"no users": User.objects.exclude(picks=pick).all() 
    }
    return render(request, "weeklypicks/pick.html", context)


def login(request):
    #username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(request, username=username, password=password)
    #if user is not None:
    #    login(request, user)
    return render(request, "weeklypicks/login.html")


def addPick(request, pick_id):
    try:
        user_id = int(response.POST["users"])
        user = User.objects.get(pk=user_id)
        pick = Pick.objects.get(pk=pick_id)
    except KeyError: 
        return render(request, "picks/error.html", {"message": "No user selected."})
    except User.DoesNotExist:
        return render(request, "picks/error.html", {"message": "No picks"})
    except Pick.DoesNotExist:
        return render(request, "picks/error.html", {"message": "No picks"})
    
    user.picks.add(pick)
    return HttpResponseRedirect(reverse("pick", argd=(pick_id,)))