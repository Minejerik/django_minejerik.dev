from django.shortcuts import render
from django.http import HttpResponse
from random import choice

titles = [
    "Did you know these titles change? Reload the page for another!",
    "hello from flask", "0% javascript", "now w/ less color!", "tf is django",
    "this is a title", "we do a little", "huh", "no more flask"
]

quotes = [
    "We do a little programming",
    "Javascript is a plague on earth",
    "Did you ever think about the fact that earth is the only planet people have died on, and it has javascript?",
    "Covid will last 2 weeks (2020)",
    "these change btw",
    "python is the javascript of programming languages",  # <-- quote
    "me when i deploy this website but forget a major feature",
    "are you still here?",
    "it's not a bug, it's an undocumented feature",
    "i concur",
    "how did they compile the first compiler?",
    "",
    "<a href='https://github.com/Minejerik/minejerik.dev'>SOURCE</a>",
]

# Create your views here.

def index(request):
    context = {
        "ran_title": choice(titles),
        "ran_quote": choice(quotes)
    }
    return render(request, "base/index.html", context)