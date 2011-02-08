from django import template

from articles.models import Category

register = template.Library()

@register.inclusion_tag("include/category-block-list.html")
def get_category_list():
    categories = Category.objects.all()

    data = {
        "categories": categories,
    }

    return data