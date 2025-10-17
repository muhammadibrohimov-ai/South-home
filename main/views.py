from django.shortcuts import render
from .models import Home, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


@login_required()
def home_page_view(request):

    home = Home.objects.all()

    homes = Home.objects.all()

    if request.method == 'GET':
        data = request.GET

        keyword = data.get('keyword')
        city = data.get('city')
        status = data.get('status')
        price_min = data.get('price_min')
        price_max = data.get('price_max')
        size_min = data.get('size_min')
        size_max = data.get('size_max')
        bathrooms = data.get('bathrooms')
        garages = data.get('garages')

        if keyword:
            homes = homes.filter(Q(name__icontains=keyword) | Q(desc__icontains=keyword))

        if city:
            homes = homes.filter(city__iexact=city)

        if status:
            homes = homes.filter(status__iexact=status)

        if price_min and price_max:
            homes = homes.filter(price__gte=price_min, price__lte=price_max)

        if size_min and size_max:
            homes = homes.filter(size__gte=size_min, size__lte=size_max)

        if bathrooms:
            bathrooms = int(bathrooms)
            if bathrooms < 5:
                homes = homes.filter(num_of_bathrooms=bathrooms)
            else:
                homes = homes.filter(num_of_bathrooms__gte=5)

        if garages:
            garages = int(garages)
            if garages < 5:
                homes = homes.filter(num_of_garages=garages)
            else:
                homes = homes.filter(num_of_garages__gte=5)

    return render(request, 'index.html', {'homes': homes, 'categories':Category.objects.all()})

@login_required()
def blog(request):
    
    return render(request=request, template_name='blog.html', context={"homes" : Home.objects.all()})


@login_required()
def single_blog(request):
    
    return render(request=request, template_name='single-blog.html', context={"homes" : Home.objects.all()})


@login_required()
def contact(request):
    
    return render(request=request, template_name='contact.html')


@login_required()
def about(request):
    
    return render(request=request, template_name='about-us.html', context={"homes" : Home.objects.all()})


@login_required()
def listings(request):
    
    return render(request=request, template_name='listings.html', context={"homes" : Home.objects.all()})