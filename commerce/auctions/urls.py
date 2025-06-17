from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auctions/categories/<int:category_id>/', views.listings_by_category, name='listings_by_category'),
    path('auctions/categories/list/', views.list_categories, name='list_categories'),
    path('auctions/watchlist/list/', views.list_watchlist, name='list_watchlist'),
    path('auctions/comment/<int:listing_id>/', views.add_comment, name='add_comment'),
    path('auctions/close_listing/<int:listing_id>/', views.close_listing, name='close_listing'),
    path('auctions/place_bid/<int:listing_id>/', views.place_bid, name='place_bid'),
    path('auctions/watchlist/<int:listing_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('auctions/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('auctions/create/', views.create_new_listing, name='create_new_listing'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]