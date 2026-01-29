from django.shortcuts import render

from products.models import Product


def home(request):
    todays_deal_products = Product.objects.filter(tags__tag_name="Today's Deal")
    return render(request, "home.html", {
        "todays_deal_products": todays_deal_products
    })

def about_us(request):
    return render(request, "about_us.html")