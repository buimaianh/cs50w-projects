from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Listings(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    starting_bid = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, max_length=100, blank=True, null=True, on_delete=models.SET_NULL, related_name='listings')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='auctions')

    def __str__(self):
        return self.title
    
    def get_current_bid(self):
        bids = self.bids.all()
        if bids:
            return max(bid.bid_amount for bid in bids)
        return self.starting_bid
    
class Bid(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='bids')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bids')
    bid_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.username} - {self.bid_amount} on {self.listing.title}"
    
class Comment(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='comments')
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment_user.username} commented on "{self.listing.title}": \"{self.content[:20]}...\"'

class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watchlist')
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='watchlist')

    def __str__(self):
        return f"{self.user.username} watching {self.listing.title}"
    
