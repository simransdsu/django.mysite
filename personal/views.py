from django.shortcuts import render


# Create your views here.
from account.models import Account


def home_screen_view(request):
    accounts = Account.object.all()

    context = {"accounts": accounts}
    return render(request, "personal/home.html", context)
