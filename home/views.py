from django.shortcuts import render,redirect
from django.contrib import messages
from home.forms import ContactForm
from home.models import Aboutus, Chef, ContactMessage
from product.models import Product, Category, Images, Comment
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)

def home(request):
    category = Category.objects.all()
    product_latest = Product.objects.all().order_by('?')[:5]
    context = {
        'category':category,
        'product_latest':product_latest,
    }
    return render(request, 'index1.html', context)

def product_details(request, id, slug):
    product = Product.objects.get(pk=id)
    category = Category.objects.all().order_by('id')
    product_all = Product.objects.all().order_by('?')
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id,)
    context = {
        'product': product,
        'product_all': product_all,
        'images':images,
        'category': category,
        'comments': comments,
    }
    return render(request, 'product_details.html', context)

def category_product(request,id, slug):
    category = Category.objects.all()
    product_latest = Product.objects.all().order_by('-id')[:8]
    # catdata = Category.objects.get(pk=1)
    products = Product.objects.filter(category_id=id)
    paginator = Paginator(products, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        # 'catdata': catdata,
        'products': products,
        'product_latest' : product_latest,

    }
    return render(request, 'menu.html', context)


def aboutus(request):
    aboutus = Aboutus.objects.all()
    chef = Chef.objects.all()
    context = {
        'aboutus':aboutus,
        'chef':chef,
    }
    return render(request, 'about_us.html', context)

def contactus(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.phone = form.cleaned_data['phone']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi! Rahmat")
            return redirect('home')
    form = ContactForm
    context = {'form': form}
    return render(request,'contact.html', context)