from django.shortcuts import render
from account.models import Account

def home_screen_view(request):
    headers = request.headers
    content = {}
    """
    list_of_values = []
    list_of_values.append("Frist entry")
    list_of_values.append("Frist second")
    list_of_values.append("Frist thirt")
    list_of_values.append("Frist four")
    list_of_values.append("Frist five")
    content['list_of_values'] = list_of_values
    questions = Question.objects.all()
    content['questions'] = questions
    """
    accounts = Account.objects.all()
    content['accounts'] = accounts

    return render(request, "personal/home.html",content)
