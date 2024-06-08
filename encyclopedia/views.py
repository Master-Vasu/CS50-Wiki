from django.shortcuts import render
from markdown2 import Markdown
from random import choice
from django.http import HttpResponse

from . import util


def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def entry(request, title):
    content = convert_md_to_html(title)
    if content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content,
        })
    

def search(request):
    if request.method == "POST":
        entry_search = request.POST["q"]
        content = convert_md_to_html(entry_search)
        if content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": content,
            })
        else:
            all_entries = util.list_entries()
            recommendation = []
            for entry in all_entries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "entries": recommendation
            })


def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry with this title already exists in the encyclopedia!"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content,
            })
        

def edit(request):
    if request.method == "POST":
        title = request.POST["entry_title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content,
        })
    

def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content,
        })
    

def random(request):
    entries = util.list_entries()
    title = choice(entries)
    content = convert_md_to_html(title)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content,
    })
    