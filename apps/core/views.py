from django.shortcuts import render

# def home(request):

#     sliders = Slider.objects.filter(active=True)

#     categories = Category.objects.filter(is_active=True)

#     featured_products = Product.objects.filter(
#         is_featured=True
#     )[:8]

#     trending_products = Product.objects.filter(
#         is_trending=True
#     )[:8]

#     best_sellers = Product.objects.filter(
#         is_best_seller=True
#     )[:8]

#     banners = Banner.objects.filter(active=True)

#     blogs = BlogPost.objects.all()[:3]

#     context = {
#         "sliders": sliders,
#         "categories": categories,
#         "featured_products": featured_products,
#         "trending_products": trending_products,
#         "best_sellers": best_sellers,
#         "banners": banners,
#         "blogs": blogs
#     }

#     return render(request, "landing/home.html", context)

def about(request):

    return render(request, "core/about.html")


def contact(request):

    return render(request, "core/contact.html")