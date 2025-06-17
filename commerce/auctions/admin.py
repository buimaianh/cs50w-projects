from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Listings, Bid, Comment, Watchlist, Category

# Register your models here.
admin.site.register(User, UserAdmin)
# admin.site.register(Listings)
# admin.site.register(Bid)
# admin.site.register(Comment)
# admin.site.register(Watchlist)
# admin.site.register(Category)

@admin.register(Listings)
class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'starting_bid', 'image_url', 'category', 'created_at', 'updated_at', 'is_active', 'seller')

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'buyer', 'bid_amount', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'comment_user', 'content', 'created_at')

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'listing')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

