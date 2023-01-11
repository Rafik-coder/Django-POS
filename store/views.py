from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse

from .models import Employee, Products
from django.http import HttpResponseRedirect, JsonResponse
from django import forms

import json
from django.core.files.storage import default_storage


# Create your views here.


# def index(request):


def login(request):
    # admin = User.objects.all()
    username = ''
    password = ''
    user_id = ''
    response = {
        'status': "fail",
        'message': ''
    }
    employee = Employee.objects.all()

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        for em in employee:

            if username == em.name and password == em.password:
                response['status'] = 'success'
                return HttpResponseRedirect(reverse("store:pos"))

            elif username == '' and password == '':
                response['message'] = "Please Enter Both Username and Password"
                return HttpResponseRedirect(reverse("store:login"))

            else:
                response['message'] = "Invalid Username or Password"
                return HttpResponseRedirect(reverse("store:login"))

    context = {
        'employee': employee,
        'request': request,
        'msg': response['message'],
        'user_id': user_id
    }

    return render(request, 'store/index.html', context)


def pos(request):
    search = ''

    products_json = []

    selected = []

    with default_storage.open("store/static/store/selected/selected.json", "r") as f:
        data = json.load(f)

    for n in data:
        for p in data[n]:
            selected.append(p)

    # print(selected)
    # for p in selected:
    #     print(p['name'])

    try:
        if request.POST:
            search = request.POST.get('search')

            with default_storage.open("store/static/store/products/products.json", "r") as f:
                data = json.load(f)

                data = {}


            with default_storage.open("store/static/store/products/products.json", "w") as f:
                json.dump(data, f)

            try:
                products_names = Products.objects.filter(name__icontains=search)

                for product in products_names:

                    print(product.category_id)

                    with default_storage.open("store/static/store/products/products.json", "r") as f:
                        data = json.load(f)

                        data[product.name] = {
                            "name": str(product.name),
                            "price": float(product.price),
                            "stock": int(product.stock),
                            "category_id": str(product.category_id),
                        },


                        with default_storage.open("store/static/store/products/products.json", "w") as f:
                            json.dump(data, f)



                print(products_json)

                # else:
                #     for product in products_names:
                #         products_json.append(product)

                # return JsonResponse({"products": products_json})

            except Products.DoesNotExist:
                print('Hey')

            with default_storage.open("store/static/store/products/products.json", "r") as f:
                data = json.load(f)

            print(data)

            for p in data:
                # print("")
                print(data[p])
                # print("")
                for l in range(len(data[p])):
                    print(l)
                    products_json.append(p[l])

            # print(products_json)
            # for p in products_json:
            #     print(p['name'])

            context = {
                'products': products_json,
                # 'search': search,
                # 'selected': selected,
            }

            return JsonResponse(context)

        else:
            products = Products.objects.all()

            for product in products:
                products_json.append(product)

            context = {
                'products': products_json,
                # 'search': search,
                'selected': selected,
            }

            return render(request, 'store/pos.html', context)

    except UnboundLocalError:
        print('leave')


def selected_json(p_name, p_price, p_qnt, stock):

    with default_storage.open("store/static/store/selected/selected.json", "r") as f:
        data = json.load(f)

    data[p_name] = {
        'name': p_name,
        'price': p_price,
        'qnt': int(p_qnt),
        'stock': int(stock),
    },

    with default_storage.open("store/static/store/selected/selected.json", "w") as f:
        json.dump(data, f)


def delete_selected_json(p_name):
    with default_storage.open("store/static/store/selected/selected.json", "r") as f:
        data = json.load(f)

    data.pop(p_name)

    with default_storage.open("store/static/store/selected/selected.json", 'w') as file:
        json.dump(data, file)


def deleted(request):
    selected_products = []
    if request.method == "POST":
        product = request.POST.get("p_name")

        print(product)

        delete_selected_json(product)

    with default_storage.open("store/static/store/selected/selected.json", "r") as f:
        data = json.load(f)

    for n in data:
        for p in data[n]:
            selected_products.append(p)

    return JsonResponse({'products': selected_products})


def selected(request):

    selected_products = []

    if request.method == "POST":
        product = request.POST.get("p_name")
        qnt = request.POST.get("p_qnt")
        product_d = Products.objects.get(name__exact=product)
        price = product_d.price * int(qnt)
        stock = product_d.stock

        if int(qnt) > stock or int(qnt) < 0:
            print("hey")

        else:
            selected_json(product, price, qnt, stock)

        print("success")
        print(int(qnt) * price)

    with default_storage.open("store/static/store/selected/selected.json", "r") as f:
        data = json.load(f)

    for n in data:
        for p in data[n]:
            selected_products.append(p)

    return JsonResponse({'products': selected_products})

