from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import SellerProfile
from stores.forms import ProductForm, StoreForm
from .models import *
from django.contrib import messages

# Create your views here.
@login_required
def seller_panel_view(request):
    seller_profile = SellerProfile.objects.filter(user=request.user).first()

    if not seller_profile:
        return redirect('customer')
    # When a ForeignKey is set up so that one Seller can have multiple stores, 
    # you can retrieve all the stores for a given seller using Seller.store_set.all()
    stores = seller_profile.store_set.all()

    return render(request, 'seller_panel.html', {
        'seller_profile': seller_profile,
        'stores': stores
    })


@login_required
def create_store_view(request):
    seller_profile = SellerProfile.objects.filter(
        user=request.user
    ).first()

    if not seller_profile:
        messages.error(request, 'You must become a seller first.')
        return redirect('customer')
    if request.method == 'POST':
        form = StoreForm(request.POST) 
        if form.is_valid():
            name= form.cleaned_data['name']
            description= form.cleaned_data['description']
            owner = SellerProfile.objects.get(user=request.user)
            Store.objects.create(name=name,description=description,owner=owner)
            messages.success(request, f'store {name} has created successfully')
            return redirect('seller_panel')
        else:
            messages.error(request, 'fill the fields correctly.')
    else:
        # create an empty form 
        form= StoreForm()         
    return render(request, 'create_store.html', {'form':form})

@login_required
def create_Product_view(request,store_id):
    seller_profile = SellerProfile.objects.filter(
        user=request.user
    ).first()

    store = get_object_or_404(
        Store,
        id=store_id,
        owner=seller_profile
    )

    if not seller_profile:
        messages.error(request, 'You must become a seller first.')
        return redirect('customer')
    if request.method == 'POST':
        # send request.FILES in addition to request.POST
        form = ProductForm(request.POST,request.FILES) 
        if form.is_valid():
            name= form.cleaned_data['name']
            description= form.cleaned_data['description']
            price= form.cleaned_data['price']
            image= form.cleaned_data['image']
            stock = form.cleaned_data['stock']
            seller_profile = SellerProfile.objects.get(user=request.user)
            store = Store.objects.get(
            id=store_id,
            owner=seller_profile
            )

            Product.objects.create(
                name=name,
                description=description,
                price=price,
                image=image,
                stock=stock,
                store=store)
            messages.success(request, f'product {name} has created successfully')
            return redirect('store_detail', store_id=store.id)
        else:
            messages.error(request, 'fill the fields correctly.')
    else:
        # create an empty form 
        form= ProductForm()         
    return render(request, 'create_product.html', {'form':form})

@login_required
def edit_product_view(request, store_id, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        store_id=store_id,
        store__owner__user=request.user
    )

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.image = form.cleaned_data['image']
            product.stock = form.cleaned_data['stock']

            product.save()

            messages.success(
                request,
                f'Product {product.name} updated successfully!'
            )
            return redirect('store_detail', store_id=store_id)

        else:
            messages.error(request, 'Please fill the fields correctly.')

    else:
        form = ProductForm(instance=product)

    return render(request, 'create_product.html', {
        'form': form,
        'product': product,
        'title': 'Edit Product'
    })

@login_required
def store_detail_view(request,store_id):       
    store = Store.objects.get(id=store_id)
    
#     This means that each product is connected to one store.

# The stoer ForeignKey is stored in the Product table, not in the Store table.

# But what if we want to get all products of a specific store?

# Django automatically creates a reverse relationship for us.

# We can access all products of a store using:

# store.product_set.all()
    products = store.product_set.all()
    return render(request, 'store_detail.html', {
        'store': store,
        'products': products
    })


def stores_view(request):
    stores = Store.objects.all()
    return render(request, 'stores.html', {
        'stores': stores,
    })

def home_view(request):
    products = Product.objects.order_by('-created_at')
    return render(request, 'home.html', {
        'products': products,
    })