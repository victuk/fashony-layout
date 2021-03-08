from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import contestant, youtubelink, contact
from .forms import ContactForm

# Create your views here.
def index(request):
    youtubeLink = youtubelink.objects.all()
    getContestants = contestant.objects.all()
    return render(request, 'thabisaView/index.html', {'videos': youtubeLink, 'contestant': getContestants})

def contestantsView(request):
    return render(request, 'thabisaView/contestants.html', {})


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
