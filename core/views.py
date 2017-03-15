from django.shortcuts import render

# Create your views here.
def reg_form(request):
    return render(request, 'core/reg_form.html', {})
