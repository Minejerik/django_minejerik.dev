from django.shortcuts import render
import os
import markdown
import functools
from django.http import HttpResponse, Http404

BLOG_PATH = "blog/blog"

#@functools
def get_blog_post(blog_post):
    """
    Gets the data for a blog post.
    EX: 
        ```
        get_blog_post('1.md')
        returns content
        ```
    EX of using wrong
        ```
        get_blog_post('1.py')
        raises Http404
        ```
    """

    # Defines base dictonary for blog post
    # Will be modified later on and returned
    bp = {
        "id":"",
        "title":"",
        "source":"",
        "date":"",
        "content":"",
        "read_time":0
    }

    # If the blog post is not in the blog path will raise 404
    # Helps prevent directory traversal
    if blog_post not in os.listdir(BLOG_PATH):
        raise Http404

    # Reads the file, sets data to content
    with open(f"{BLOG_PATH}/{blog_post}", "r") as f:
        data = f.read()

    # splits the data into array at newlines
    split_data = data.splitlines()
    
    # sets all the attributes for the blog post
    bp["id"] = blog_post.replace(".md","")
    bp['title'] = split_data[0].replace('TITLE:',"")
    bp['source'] = split_data[1].replace('SOURCE:',"")
    bp['date'] = split_data[2].replace('DATE:',"")
    content = "\n".join(split_data[3:])
    bp['content'] = markdown.markdown(content)
    bp['read_time'] = len(data.split()) // 150

    return bp


def get_all_post_data():
    """
    Returns array of all blog posts.
    """
    toreturn = []
    for id in reversed(sorted(os.listdir(BLOG_PATH))):
        toreturn.append(get_blog_post(id))

    return toreturn


# Create your views here.
def index(request):
    blog_data = get_all_post_data()
    context = {
        "posts":blog_data
    }
    return render(request, "blog/blog.html", context)


def blog_post(request, blog_id):
    post_data = get_blog_post(str(blog_id)+".md")
    context = {
        "post":post_data
    }
    return render(request, "blog/blog_post.html", context)