from django import template

register = template.Library()


@register.filter
def check_user_type(context, *args, **kwargs):
    import pdb; pdb.set_trace()
    return False
