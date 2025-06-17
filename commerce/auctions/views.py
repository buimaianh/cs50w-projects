from django.shortcuts import render
from auctions.models import Listings, Bid, Comment, Watchlist, Category
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'auctions/login.html', {'error': 'Invalid username or password'})
    return render(request, 'auctions/login.html')

def logout_view(request):
    logout(request)
    return redirect("login")

def index(request):
    listings = Listings.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'auctions/index.html', {'listings': listings})

def create_new_listing(request):
    if not request.user.is_authenticated:
        error = "You must be logged in to create a new listing."
        return render(request, 'auctions/create_listing.html', {'error': error})

    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        starting_bid = int(request.POST.get('starting_bid', 0))
        image_url = request.POST.get('image_url', '')
        category_name = request.POST.get('category', '')
        category = Category.objects.filter(name=category_name).first()

        listing = Listings(
            title=title,
            description=description,
            starting_bid=starting_bid,
            image_url=image_url,
            category=category,
            seller=request.user
        )
        listing.save()
        return redirect('index')
    
    categories = Category.objects.all()
    if not categories:
        categories = ['No categories available']
    return render(request, 'auctions/create_listing.html', {'categories': categories})

def listing_detail(request, listing_id):
    listing = Listings.objects.get(id=listing_id)
    listing_comments = listing.comments.all().order_by('-created_at')
    return render(request, 'auctions/listing_detail.html', {
        'listing': listing,
        'comments': listing_comments
        })

def add_to_watchlist(request, listing_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to add items to your watchlist.", extra_tags="watchlist_message")
            return redirect('listing_detail', listing_id=listing_id)
        
        listing = Listings.objects.get(id=listing_id)
        watchlist_entry, created = Watchlist.objects.get_or_create(
            user=request.user,
            listing=listing
        )
        if created:
            messages.success(request, f"{listing.title} has been added to your watchlist.", extra_tags="watchlist_message")
        else:
            messages.info(request, f"{listing.title} existed.", extra_tags="watchlist_message")
        return redirect('listing_detail', listing_id=listing_id)
    
def place_bid(request, listing_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to place a bid.", extra_tags="place_bid_message")
            return redirect('listing_detail', listing_id=listing_id)
        
        listing = Listings.objects.get(id=listing_id)
        bid_amount = int(request.POST.get('bid_amount'))
        current_bid = listing.get_current_bid()

        buyer = request.user
        seller = listing.seller
        if buyer == seller:
            messages.error(request, "You cannot place a bid on your own listing.", extra_tags="place_bid_message")
            return redirect('listing_detail', listing_id=listing_id)

        if bid_amount <= current_bid:
            messages.error(request, "Your bid must be higher than the current bid.", extra_tags="place_bid_message")
            return redirect('listing_detail', listing_id=listing_id)
        
        placed_bid = Bid(
            listing=listing,
            buyer=request.user,
            bid_amount=bid_amount
        )
        placed_bid.save()
        messages.success(request, f"Your bid of {bid_amount} has been placed on {listing.title}.", extra_tags="place_bid_message")
        return redirect('listing_detail', listing_id=listing_id)

def close_listing(request, listing_id):
    if request.method == 'POST':
        # if not request.user.is_authenticated:
        #     messages.error(request, "You must be logged in to close a listing.", extra_tags="close_listing_message")
        #     return redirect('listing_detail', listing_id=listing_id)
        
        # if listing.seller != request.user:
        #     messages.error(request, "You can only close your own listings.", extra_tags="close_listing_message")
        #     return redirect('listing_detail', listing_id=listing_id)
        
        listing = Listings.objects.get(id=listing_id)
        listing.is_active = False
        listing.save()
        messages.success(request, f"{listing.title} has been closed.", extra_tags="close_listing_message")
        return redirect('listing_detail', listing_id=listing_id)
    
def add_comment(request, listing_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to add a comment.", extra_tags="add_comment_message")
            return redirect('listing_detail', listing_id=listing_id)
        
        listing = Listings.objects.get(id=listing_id)
        comment = request.POST.get('comment')
        if not comment:
            messages.error(request, "Comment cannot be empty.", extra_tags="add_comment_message")
            return redirect('listing_detail', listing_id=listing_id)
        
        new_comment = Comment(
            listing=listing,
            comment_user=request.user,
            content=comment
        )
        new_comment.save()
        messages.success(request, "Your comment has been added.", extra_tags="add_comment_message")
        return redirect('listing_detail', listing_id=listing_id)
    
def list_watchlist(request):
    if not request.user.is_authenticated:
        error = "You must be logged in to view your watchlist."
        return render(request, 'auctions/watchlist.html', {'error': error})
    
    user = request.user
    watchlist_items = user.watchlist.all()
    print(watchlist_items)
    return render(request, 'auctions/watchlist.html', {
        'watchlist_items': watchlist_items
        })
def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'auctions/categories.html', {'categories': categories})

def listings_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    listings = Listings.objects.filter(category=category).order_by('-created_at')
    return render(request, 'auctions/listings_by_category.html', {
        'category': category,
        'listings': listings
    })
    

