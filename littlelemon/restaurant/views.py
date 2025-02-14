# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menuitems = Menu.objects.all()
    menu_dict = {'menu': menuitems}
    return render(request, 'menu.html', menu_dict)

def menu_item(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        item = Menu.objects.get(id=num)
        return render(request, 'menu_item.html', {'item': item})