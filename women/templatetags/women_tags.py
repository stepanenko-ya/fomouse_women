from django import template
# from women.models import Women, Category
from women.models import *


register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)




@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None):
    if sort:
        cats = Category.objects.all().order_by(sort)
    else:
        cats = Category.objects.all()
    return {'cats': cats}


