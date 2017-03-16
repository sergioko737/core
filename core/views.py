from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Person
from .forms import PersonForm

# Create your views here.
def reg_form(request): #view of registration form
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('core/reg_success.html', {})
    else:
        form = PersonForm()
    return render(request, 'core/reg_form.html', {'form': form})

def reg_success(request): #view after successful form submission
    return render(request, 'core/reg_success.html', {})
