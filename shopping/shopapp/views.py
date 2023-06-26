from django.shortcuts import get_object_or_404, render,HttpResponse
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def allProdCat(req,c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category,slug= c_slug)
        products_list = Product.objects.all().filter(category= c_page,available = True)
    else :
        products_list = Product.objects.all().filter(available = True)
    paginator = Paginator(products_list,6)
    try:
        page = int(req.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(req,"category.html",{'category': c_page, 'products': products})

def proDetail(req,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug = c_slug, slug = product_slug)
    except Exception as e:
        raise e
    return render(req,'product.html',{'product': product })