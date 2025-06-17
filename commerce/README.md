## Project: Commerce

This is an online auction site built with Django as part of Harvard's **CS50 Web Programming with Python and JavaScript** course.

Users can create listings, place bids, comment, add items to a watchlist, and browse by categories.

---

### Features

- **Models**
  - `Listings`: Represents an auction item (title, description, starting bid, image URL, category, active status, seller, created at)
  - `Bid`: Represents a user's bid for a listing.
  - `Comment`: Represents a comment made on a listing.
  - Uses Django’s built-in `User` model for authentication.

---

- **User Functionality**

  - #### Create Listing ####
    - Users can create a new listing with:
      - Title
      - Description
      - Starting bid
      - (Optional) Image URL
      - (Optional) Category
    - Listings are active by default and visible to all users.
    - Created date is auto saved by Django

#### 📋 Active Listings Page
- Home page shows **all currently active listings**.
- Each listing shows:
  - Title
  - Description
  - Current Price (latest/highest bid or starting price)
  - Image (if provided)

#### 📄 Listing Page
- Clicking a listing shows full details.
- Logged-in users can:
  - ➕ Add/Remove the listing from **Watchlist**
  - 💬 Post **comments**
  - 💸 Place **bids**
    - Bids must be ≥ starting price and > any existing bids
    - Invalid bids show an error message
  - 🏁 **Close the auction** (only by the listing creator)
    - When closed, the highest bidder is declared the winner
    - Winner will see a message that they’ve won

#### 👁️ Watchlist
- Logged-in users can view their Watchlist.
- Lists all saved listings with links back to their pages.

#### 🧩 Categories
- A dedicated page shows all listing categories.
- Clicking a category shows all **active listings** under that category.

---

## 🔐 Django Admin
- Site admins can manage:
  - Listings
  - Bids
  - Comments
- All CRUD actions are supported via Django admin panel.

---

## 🛠️ Technologies
- Python 3
- Django 4.x+
- SQLite (default)
- HTML + CSS + Django templates

---

## 📁 Folder Structure (Simplified)

