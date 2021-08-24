from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from cowsay.forms import AddCowsayForm
from cowsay.models import Cowsay

from django.urls import reverse
from subprocess import check_output

# Create your views here.
def Cowsay_view(request):
    cowlist = ""
    if request.method == 'POST':
        form = AddCowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Cowsay.objects.create(
                cowsay_str=data["cowsay_str"]
            )
            cowlist = check_output(['cowsay', data["cowsay_str"]]).decode()
    form = AddCowsayForm()
    return render(request, 'index.html' ,{"form": form, 'blue': cowlist})


def History_view(request):
    cowsay_list = Cowsay.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {'cowsay_list': cowsay_list})
