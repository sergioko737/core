from django.shortcuts import render
from django.utils import timezone
from .models import Person
from .forms import PersonForm

# Create your views here.
def reg_form(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return render(request, 'core/reg_form.html', {'form': form})
    else:
        form = PersonForm()
    return render(request, 'core/reg_form.html', {'form': form})
