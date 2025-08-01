## Project: Wiki

This is a Wikipedia-like encyclopedia web app built with Django as part of Harvard's **CS50 Web Programming with Python and JavaScript** course.

Users can browse, search, and read articles written in Markdown. They can also create, edit, and save new pages. A random page feature are included for easier navigation.

### Features

- **Entry Page**
   - Visit `/wiki/TITLE` to view an encyclopedia entry.
   - If the entry exists, it is rendered as HTML (converted from Markdown).
   - If the entry does **not** exist, a custom error page is shown.

- **Index Page**
   - Lists all encyclopedia entries.
   - Each entry name is a clickable link that navigates to the corresponding entry page.

- **Search**
   - Users can search for encyclopedia entries using the sidebar search box.
   - Exact match → Redirect to the entry page.
   - Partial match → Show a list of all entries containing the query as a substring.

- **Create New Page**
   - Users can create new encyclopedia entries with a title and Markdown content.
   - Duplicate titles are **not allowed** — a proper error message is displayed if attempted.
   - On successful creation, the user is redirected to the new entry’s page.

- **Edit Page**
   - Each entry page includes an “Edit” link.
   - Users can update the Markdown content using a pre-filled textarea.
   - On save, changes are written to disk and the user is redirected to the updated entry page.

- **Random Page**
   - Users can click "Random Page" to be redirected to a random encyclopedia entry.

- **Markdown to HTML**
   - All entry content is written in Markdown and converted to HTML when displayed.
   - The app uses [`markdown2`](https://github.com/trentm/python-markdown2) for the conversion.

### Technologies
   - Python 3
   - Django
   - Markdown2 (`pip install markdown2`)

### Folder Structure (Simplified)
   ```text
   wiki/
   ├── encyclopedia/
   │ ├── templates/
   │ │ └── encyclopedia/
   │ ├── util.py
   │ └── views.py
   ├── entries/ # Markdown files for each entry stored here
   ├── wiki/
   │ └── settings.py
   ├── manage.py
   └── README.md
   ```

### How to Run
   1. Install dependencies:
   
      ```bash
      pip install django markdown2
      ```
   
   2. Run the server:
   
      ```bash
      python manage.py runserver
      ```
   
   3. Access the app at http://127.0.0.1:8000/



