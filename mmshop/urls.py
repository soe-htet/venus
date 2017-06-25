from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mmshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^$', 'products.views.all', name='home'),
    url(r'^s/$', 'products.views.search', name='search'),
    url(r'^products/$', 'products.views.all', name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),

    url(r'^cart/$', 'Carts.views.view', name='cart'),
    url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
    url(r'^cart/(?P<id>\d+)/$', 'Carts.views.remove_cart', name='remove_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'Carts.views.update_cart', name='update_cart'),

    url(r'^ajax/dismiss_marketing_message/$', 'marketing.views.dismiss_marketing_message', name='dismiss_marketing_message'),
    url(r'^ajax/email_signup/$', 'marketing.views.email_signup', name='ajax_email_signup'),
    url(r'^ajax/add_user_address/$', 'accounts.views.add_user_address', name='ajax_add_user_address'),

    url(r'^orders/$', 'orders.views.user_orders', name='user_orders'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),
)

# if settings.DEBUG:
# 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)