## Project: Google Search Clone

This project is a front-end clone of Google Search, built as part of Harvard's **CS50 Web Programming with Python and JavaScript** course. It includes implementations of:

- Google Search
- Google Image Search
- Google Advanced Search

### Features

- **Three Pages**:
  - `index.html`: Standard Google Search
  - `image_search.html`: Google Image Search
  - `advanced_search.html`: Google Advanced Search

- **Navigation**  
  Links in the top-right corner allow easy switching between pages.

- **Search Functionality**:
  - Text input for queries
  - “Google Search” and “I’m Feeling Lucky” buttons
  - Redirects to actual Google search results using query parameters

- **Image Search**  
  Input a query → redirect to real Google Image results

- **Advanced Search**:
  - Includes fields for:
    - All these words
    - This exact word or phrase
    - Any of these words
    - None of these words
    - Numbers ranging from...to...
  - Styled similar to Google’s own UI
  - Submit redirects to Google’s advanced search with correct query strings

- **Styling**
  - Search bar centered and rounded like Google’s
  - “Advanced Search” button styled with blue background and white text
  - Overall CSS closely mimics Google’s design

### Technologies

- HTML
- CSS

### Folder Structure
```text
├── search/
│ ├── index.html
│ ├── image_search.html
│ ├── advanced_search.html
│ └── README.md
```

### How to Run

Just open `index.html` in your browser. No server required.

