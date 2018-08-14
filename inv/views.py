from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Inv
#from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.        	
def inv_list(request):
    invs = Inv.objects.filter(loginInRDP__lte=timezone.now()).order_by('loginInRDP')
    return render(request, 'inv/inv_list.html', {'invs': invs})

def inv_detail(request):
    iii = 3

def inv_import_login(request):
    i = 3
    