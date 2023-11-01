from django.db import models
from django.urls import reverse


class Films(models.Model):
    films = models.CharField(
        max_length=255, null=True,
        verbose_name='Film name'
    )

    def __str__(self):
        return self.films


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_slug': self.slug})


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Article text')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d",
                              verbose_name='Photo')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 verbose_name='Category')
    films = models.ManyToManyField(Films, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug_name': self.slug})

    class Meta:
        ordering = ['title', 'id']
