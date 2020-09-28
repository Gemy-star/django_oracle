from django.shortcuts import render
from .models import get_resYear


def get_home(request):
    resyear = get_resYear()
    context = {
        "resyears": resyear
    }
    return render(request, 'db_orcale/home.html', context)


