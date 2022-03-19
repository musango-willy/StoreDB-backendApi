from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('groups', views.CategoryGroupView.as_view()),
    path('category', views.CategoryView.as_view()),
    path('store', views.ProductsView.as_view()),
    path('products', views.Sale_ProductView.as_view()),
    path('inventories', views.InventoriesView.as_view()),
    path('get_item/<str:pk>', views.search_items),
    path('invent', views.inventoriesView),
    path('group_relations', views.category_relview),
    path('post_products', views.products_post),
    path('cat_products', views.category_rel_view.as_view()),

    
]

