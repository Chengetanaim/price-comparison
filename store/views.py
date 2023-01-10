from django.shortcuts import render
from .models import Product, Category, Website
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# from .adding import process
#
# process()


def index(request):
    categories = Category.objects.all()
    laptop = Category.objects.get(name='Laptops')
    laptop_list_random = laptop.products.order_by('?')
    laptop_list_random2 = laptop.products.order_by('?')
    laptop_list_random3 = laptop.products.order_by('?')
    headphone = Category.objects.get(name='Headphones')

    headphone_list_random4 = headphone.products.order_by('?')
    headphone_list_random5 = headphone.products.order_by('?')
    headphone_list_random6 = headphone.products.order_by('?')

    paginator_random = Paginator(laptop_list_random, 1)
    paginator_random2 = Paginator(laptop_list_random2, 1)
    paginator_random3 = Paginator(laptop_list_random3, 1)

    paginator_random4 = Paginator(headphone_list_random4, 1)
    paginator_random5 = Paginator(headphone_list_random5, 1)
    paginator_random6 = Paginator(headphone_list_random6, 1)
    page = request.GET.get('page')
    try:
        laptops_random = paginator_random.page(page)
        laptops_random2 = paginator_random2.page(page)
        laptops_random3 = paginator_random3.page(page)

        headphones_random4 = paginator_random4.page(page)
        headphones_random5 = paginator_random5.page(page)
        headphones_random6 = paginator_random6.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        laptops_random = paginator_random.page(1)
        laptops_random2 = paginator_random2.page(1)
        laptops_random3 = paginator_random3.page(1)

        headphones_random4 = paginator_random4.page(1)
        headphones_random5 = paginator_random5.page(1)
        headphones_random6 = paginator_random6.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        laptops_random = paginator_random.page(paginator_random.num_pages)
        laptops_random2 = paginator_random2.page(paginator_random2.num_pages)
        laptops_random3 = paginator_random3.page(paginator_random3.num_pages)

        headphones_random4 = paginator_random4.page(paginator_random4.num_pages)
        headphones_random5 = paginator_random5.page(paginator_random5.num_pages)
        headphones_random6 = paginator_random6.page(paginator_random6.num_pages)

    context = {'laptops_random': laptops_random,
               'laptops_random2': laptops_random2,
               'laptops_random3': laptops_random3,
               'headphones_random4': headphones_random4,
               'headphones_random5': headphones_random5,
               'headphones_random6': headphones_random6,
               'categories': categories}
    return render(request, 'store/index.html', context)


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    categories = Category.objects.all()
    product_list = category.products.order_by('-id')
    product_list_random = category.products.order_by('?')
    product_list_random2 = category.products.order_by('?')
    paginator = Paginator(product_list, 3)
    paginator_random = Paginator(product_list_random, 3)
    paginator_random2 = Paginator(product_list_random2, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
        products_random = paginator_random.page(page)
        products_random2 = paginator_random2.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
        products_random = paginator_random.page(1)
        products_random2 = paginator_random2.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
        products_random = paginator_random.page(paginator.num_pages)
        products_random2 = paginator_random2.page(paginator.num_pages)

    context = {'category': category,
               'products': products,
               'categories': categories,
               'products_random': products_random,
               'products_random2': products_random2
               }
    return render(request, 'store/category.html', context)


def website(request, website_id):
    website = Website.objects.get(id=website_id)
    categories = Category.objects.all()
    product_list = website.products.order_by('-id')
    product_list_random = website.products.order_by('?')
    product_list_random2 = website.products.order_by('?')
    paginator = Paginator(product_list, 3)
    paginator_random = Paginator(product_list_random, 3)
    paginator_random2 = Paginator(product_list_random2, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
        products_random = paginator_random.page(page)
        products_random2 = paginator_random2.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
        products_random = paginator_random.page(1)
        products_random2 = paginator_random2.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
        products_random = paginator_random.page(paginator.num_pages)
        products_random2 = paginator_random2.page(paginator.num_pages)

    context = {'category': category,
               'products': products,
               'categories': categories,
               'products_random': products_random,
               'products_random2': products_random2,
               'website': website,
               }
    return render(request, 'store/website.html', context)


def about_us(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'store/about_us.html', context)


class SearchResultsView(ListView):
    model = Product
    template_name = 'store/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
        Q(name__icontains=query) | Q(category__name__icontains=query) | Q(website__name__icontains=query) | Q(price__icontains=query)
        )
        return object_list


