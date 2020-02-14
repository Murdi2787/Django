from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Manufacturer, Collection, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    manufacturer = None
    manufacturers = Manufacturer.objects.all()
    collection = None
    collections = Collection.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                      'manufacturer': manufacturer,
                      'manufacturers': manufacturers,
                      'collection': collection,
                      'collections': collections,
                  })


def product_list_manufacturer(request, manufacturer_slug=None):
    manufacturer = None
    manufacturers = Manufacturer.objects.all()
    products = Product.objects.filter(available=True)
    if manufacturer_slug:
        manufacturer = get_object_or_404(Manufacturer, slug=manufacturer_slug)
        products = products.filter(manufacturer=manufacturer)
    return render(request,
                  'shop/product/list.html',
                  {
                      'manufacturer': manufacturer,
                      'manufacturers': manufacturers,
                      'products': products
                  })


def product_list_collection(request, collection_slug=None):
    collection = None
    collections = Collection.objects.all()
    products = Product.objects.filter(available=True)
    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = products.filter(collection=collection)
    return render(request,
                  'shop/product/list.html',
                  {
                      'collection': collection,
                      'collections': collections,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
