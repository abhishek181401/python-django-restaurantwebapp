import logging

from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Owner,ContactNumber,UserQuery,Recipe,TeamMember
from .validation import form_validation

logger = logging.getLogger('django')


#Create your views here.
def index(request):
    recipes = Recipe.objects.all()[:3]
    recipe_types = Recipe.objects.values_list('type', flat=True).distinct()
    q= request.GET.get('q')
    if q:
        recipes = Recipe.objects.filter(type=q)[:3]
    context = { 
        'recipes':recipes,
        'recipe_types':recipe_types,
    }

    return render(request,'core/index.html',context)

def contact_us(request):
    owner = Owner.objects.all()
    contact_nums = ContactNumber.objects.all()
    try:    
        if request.method == "POST":
            firstname,lastname,service,email,phone,message = form_validation(request)
            UserQuery.objects.create(firstname=firstname,lastname=lastname,service=service,email=email,phone_number=phone,message=message)
            return redirect('contact_us')
        context ={
            "owner":owner,
            'contact_nums':contact_nums,
        }
        return render(request,"core/contact_us.html",context)
    
    except Exception as exc:
        logger.error(str(exc),exc_info=True)
        return render(request,"core/contact_us.html")



def about_us(request):
    teammembers = TeamMember.objects.all()

    # Set the number of team members per page
    items_per_page = 3

    # Create a paginator object
    paginator = Paginator(teammembers, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page', 1)

    try:
        # Get the current page's team members
        current_teammembers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        current_teammembers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page
        current_teammembers = paginator.page(paginator.num_pages)

    context = {
        'teammembers': current_teammembers,
    }

    return render(request, "core/about_us.html", context)


def allergy_advice(request):
    return render(request,'core/allergyadvice.html')

def our_services(request):
    return render(request,'core/our_services.html')

def our_menu(request):
    recipes = Recipe.objects.all()
    print(recipes)
    context={
        "recipes":recipes,
    }
    return render(request,'core/our_menu.html',context)
