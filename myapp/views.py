from django.shortcuts import render
from myapp.forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

def thanks(request):
    return render(request,"myapp/thanks.html")


def index(request):
    name=''
    email=''
    comment=''


    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        message=form.cleaned_data.get("message")

        subject= "A Visitor's Comment"


        comment= name + " with the email, " + email + ", sent the following message:\n\n" + message;
        send_mail(subject, comment, 'bennyhinnotieno@gmail.com', [email])

        return thanks(request)

    else:
        return render(request, "myapp/index.html",{"form":form})
