from django import template

register = template.Library()

@register.inclusion_tag
def selected(p_id=''):
    from pos.store.models import Products
    try:
        product = Products.objects.get(name__exact=p_id)
        print(product)

    except Products.DoesNotExist:
        print("value error")
