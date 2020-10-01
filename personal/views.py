from django.shortcuts import render


# Create your views here.
from personal.models import Question


def home_screen_view(request):
    context = {
        "some_string": "this is some string that I'm passing to the view",
        "some_number": 45,
        "list_of_values": [
            "First entry",
            "Second entry",
            "Third entry",
            "Fourth entry"
        ]
    }
    return render(request, "personal/home.html", context)

def questions(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, "personal/questions.html", context)
