from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import contestant, youtubelink, contact
from .forms import ContactForm, ContestantForm
import random

# Create your views here.
def index(request):
    youtubeLink = youtubelink.objects.all()
    getContestants = contestant.objects.all()
    return render(request, 'thabisaView/index.html', {'videos': youtubeLink, 'contestant': getContestants})

def contestantsView(request):
    if request.method == 'POST':
        form = ContestantForm(request.POST, request.FILES)
        contestantModel = contestant()
        if form.is_valid():
            contestantModel.name = form.cleaned_data['name']
            contestantModel.picture = form.cleaned_data['picture']
            contestantModel.contestantsCode = ''.join(str(e) for e in [random.randint(1, 9) for w in range(6)])
            contestantModel.description = form.cleaned_data['description']
            contestantModel.proofOfPayment = form.cleaned_data['proofOfPayment']
            contestantModel.save()
            return HttpResponse("<script>alert('You have sucessfully submitted this form.'); location.replace('/')</script>")
        else:
            return HttpResponse("<script>alert('There is an error, please try again later.')</script>")

    form = ContestantForm()
    return render(request, 'thabisaView/contestants.html', {'form': form})


def contactsView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        contactModel = contact()
        if form.is_valid():
            contactModel.fullName = form.cleaned_data['fullName']
            contactModel.email = form.cleaned_data['email']
            contactModel.message = form.cleaned_data['message']
            contactModel.save()
            return HttpResponse("<script>alert('You have sucessfully submitted this form.'); location.replace('/')</script>")
        else:
            return HttpResponse("<script>alert('There is an error, please try again later.')</script>")

    form = ContactForm()
    return render(request, 'thabisaView/contact.html', {'form': form})

def aboutView(request):
    return render(request, 'thabisaView/about.html', {})
