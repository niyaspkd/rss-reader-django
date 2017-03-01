from django.shortcuts import render
import feedparser
from .forms import RssForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):

 
 if request.method == "POST":
 	form = RssForm(request.POST)	
 	
 	if form.is_valid():
 		data = form.cleaned_data['link']
 		d = feedparser.parse(data)
		
    		
   	return render(request, 'home.html', {'d' : d })

 else :

 	form = RssForm()
 	return render(request, "home.html" , {'form' : form }) 			