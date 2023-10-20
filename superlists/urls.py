from django.contrib import admin
from django.urls import include, path
from lists import views as list_views
from lists import urls as list_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('', list_views.home_page, name='home'),
    path('lists/', include(list_urls)),
    path('accounts/', include(accounts_urls)),
    path("admin/", admin.site.urls),
]
