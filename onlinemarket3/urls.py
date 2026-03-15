from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('apps.landing.urls')),

    path('accounts/', include('apps.accounts.urls')),
    path('core/', include('apps.core.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('cart/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
    path('payments/', include('apps.payments.urls')),
    path('shipping/', include('apps.shipping.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('coupons/', include('apps.coupons.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('finance/', include('apps.accounts_finance.urls')),
    path('reports/', include('apps.reports.urls')),
    path('blog/', include('apps.blog.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)