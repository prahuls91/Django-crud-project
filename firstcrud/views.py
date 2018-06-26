from django.shortcuts import render
from .import forms

# Create your views here.

def index(request):

#    return HttpResponse("Hie")
  #  my_dict = {'insert_me': "Hello I am from views.py file"}
    return render(request, 'blogpost /index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method=="POST":
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("Validation sucess")
            print("Name:" + form.cleaned_data['name'])
            print("Email:" + form.cleaned_data['email'])
            print("Text info:" + form.cleaned_data['text'])
    return render(request,'blogpost/form_page.html',{'form': form})