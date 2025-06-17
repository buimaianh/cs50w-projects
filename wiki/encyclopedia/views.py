from django.shortcuts import render, redirect
from . import util
import markdown2

# Create your views here.
def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request, title):
    content_markdown = util.get_entry(title)
    if content_markdown is None:
        return render(request, "encyclopedia/error.html", {
            "message": f'"{title}" not found.'
        })
    content_html = markdown2.markdown(content_markdown)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content_html
    })

def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()

    search_results = []
    for entry in entries:
        if entry.lower() == query.lower():
            print(f"Exact match found: {entry}")
            return redirect('entry', title=entry)
        elif query.lower() in entry.lower():
            search_results.append(entry)
    if len(search_results) > 0:
        print(f'Partial match found for "{query}"": {search_results}')
        return render(request, "encyclopedia/search_results.html", {
            "query": query,
            "search_results": search_results
        })
        
    return render(request, "encyclopedia/error.html", {
        "message": f'"{query}" not found.'
    })

def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        
        if not title or not content:
            return render(request, "encyclopedia/error.html", {
                "message": "Title and content cannot be empty."
            })
        
        for entry in util.list_entries():
            if title.lower() == entry.lower():
                return render(request, "encyclopedia/error.html", {
                    "message": f'"{title}" already exists.'
                })
    
        util.save_entry(title, content)
        return redirect('entry', title=title)
    
    return render(request, "encyclopedia/new_page.html")

def edit_page(request, entry):
    if request.method == "POST":
        edited_content = request.POST.get("edited_content", "")
        util.save_entry(title=entry, content=edited_content)
        return redirect('entry', title=entry)
    
    content_md = util.get_entry(title=entry)
    return render(request, "encyclopedia/edit.html", {
        "title": entry,
        "content": content_md
    })

def random_page(request):
    import random
    entries = util.list_entries()
    random_entry = random.choice(entries)
    content_markdown = util.get_entry(random_entry)
    content_html = markdown2.markdown(content_markdown)
    return render(request, "encyclopedia/random_page.html", {
        # "entry": random_entry,
        "content": content_html
    })