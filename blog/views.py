from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


def starting_page(request):
    """Pàgina principal: mostra els 3 posts més recents."""
    latest_posts = Post.objects.order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    """Llistat de tots els posts ordenats per data descendent."""
    all_posts = Post.objects.order_by("-date")
    return render(request, "blog/post_list.html", {"posts": all_posts})


def post_detail(request, slug):
    """Detall d'un post. Retorna 404 si el slug no existeix."""
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})


def authors(request):
    """Llistat de tots els autors registrats."""
    all_authors = Author.objects.all()
    return render(request, "blog/authors_list.html", {"authors": all_authors})


def author_detail(request, author_id):
    """Detall d'un autor i els seus posts. Retorna 404 si l'id no existeix."""
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "blog/author_detail.html", {"author": author})


def tags(request):
    """Llistat de totes les etiquetes disponibles."""
    all_tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", {"tags": all_tags})


def tag_posts(request, tag_id):
    """Posts que contenen una etiqueta concreta. Retorna 404 si l'etiqueta no existeix."""
    tag = get_object_or_404(Tag, pk=tag_id)
    tagged_posts = tag.post_set.order_by("-date")
    return render(request, "blog/tag_post.html", {"tag": tag, "posts": tagged_posts})
