from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm


def registration_view(request):
    context = {}

    if request.POST:
        print("DEBUG:  registration_view:POST")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            __submit_registration_form(request, form)
            return redirect("home")
        else:
            context["registration_form"] = form

    else:
        print("DEBUG:  registration_view:GET")
        form = RegistrationForm()
        context = __show_registration_form(form)
        return render(request, "account/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


#############################################################################
def __submit_registration_form(request, form):
    form.save()
    email = form.cleaned_data.get("email")
    raw_password = form.cleaned_data.get("password1")
    print(email)
    print(raw_password)
    account = authenticate(email=email, password=raw_password)
    print(account)
    login(request, account)


def __show_registration_form(form):
    context = {"registration_form": form}
    return context
