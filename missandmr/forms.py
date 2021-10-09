from django import forms
from django.forms import ModelForm

class ContactForm(forms.Form):
    fullName = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

class ContestantForm(forms.Form):
    name = forms.CharField()
    picture = forms.ImageField()
    # contestantsCode = forms.CharField(widget = forms.HiddenInput())
    gender =  forms.CharField(widget=forms.Select(choices=[
      ('male', 'Male'),
      ('female', 'Female')
    ]))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    proofOfPayment = forms.ImageField()



# def generateContestantCode(self):
#     mylist = []
#     mylist=[random.randint(1, 6) for w in range(6)]
#     result = ''.join(str(e) for e in mylist)
#     return result

# return ''.join(str(e) for e in [random.randint(1, 6) for w in range(6)])

    # if request.method == "POST":
    #     form = GeeksForm(request.POST, request.FILES)
    #     if form.is_valid():