from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    """Autor d'un post del blog."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        """Retorna el nom complet de l'autor."""
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    """Etiqueta per classificar posts."""

    caption = models.CharField(max_length=50)

    def __str__(self):
        """Retorna el nom de l'etiqueta."""
        return self.caption


class Post(models.Model):
    """Article del blog amb títol, contingut, imatge i metadades."""

    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    excerpt = models.TextField(max_length=500)
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    # un autor pot tenir molts posts, però un post té un sol autor
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        """Retorna el títol del post."""
        return self.title

    class Meta:
        ordering = ["-date"]
