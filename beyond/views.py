from django.shortcuts import render, get_object_or_404, redirect
from beyond.cart import Cart
from beyond.models import Picture, Category, Order


def home(request):
    pictures = Picture.objects.all()
    context = dict(pictures=pictures)
    return render(request, 'beyond/home.html', context)


def about(request):
    return render(request, 'beyond/about.html')


def show_picture(request, picture_id):
    picture = get_object_or_404(Picture, id=picture_id)
    images = picture.images.all()
    in_cart = picture.in_cart(request)
    categories = Category.objects.all()
    picture_category = ",".join(str(category) for category in picture.categories.all())
    context = dict(picture=picture, images=images, in_cart=in_cart, categories=categories,
                   picture_category=picture_category)
    return render(request, 'beyond/picture.html', context)


def pictures(request, category_id=None):
    if category_id is None:
        pictures = Picture.objects.all()
    else:
        category_id = int(category_id)
        pictures = Picture.objects.filter(categories__id=category_id)
    in_cart = []
    for picture in pictures:
        in_cart.append(picture.in_cart(request))
    categories = Category.objects.all()
    context = dict(pictures=pictures, categories=categories, category_id=category_id, in_cart=in_cart)
    return render(request, 'beyond/pictures.html', context)


def cart(request):
    print request.session['color']
    cart = Cart(request)
    items_ids = ",".join(str(item.product.id) for item in cart.item_list)
    context = dict(cart=cart, items_ids=items_ids)
    return render(request, 'beyond/cart.html', context)


def add_to_cart(request, picture_id):
    cart = Cart(request)
    if int(picture_id) == 1:
        request.session['color'] = 'red'
    else:
        request.session['color'] = 'blue'
    cart.add(Picture.objects.get(id=picture_id))
    cart.save(request)
    return redirect('cart')


def delete_from_cart(request, picture_id):
    cart = Cart(request)
    cart.remove(picture_id)
    cart.save(request)
    return redirect('cart')


def update_cart(request):
    return render(request, 'beyond/cart.html', None)


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    cart.save(request)
    return redirect('cart')


def make_order(request):
    # order = Order(name=request.GET['ni'],email=request.GET['em'], )
    # for id in request.GET['ps'].split(','):

    return redirect('pictures')
