from django import template
from products.models import Category
from django.utils.http import urlencode


register = template.Library()


@register.simple_tag
def tags_categories():
    return Category.objects.filter(id__lt=11)

@register.simple_tag
def cat():
    return Category.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
# @register.simple_tag(takes_context=True)
# def change_params(context, **kwargs):
#     query = context['request'].GET.dict()
#     query.update(kwargs)
    
#     return urlencode(query)

