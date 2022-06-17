from django.urls import path
from . import views

app_name = 'market'
urlpatterns = [
  path('market/', views.market, name='market'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
  
]


urlpatterns += [
  path('update_item/', views.update_item, name='update_item'),
  path('process_order/', views.process_order, name='process_order'),

]

urlpatterns += [
  path('login/', views.login_user, name='login'),
]

