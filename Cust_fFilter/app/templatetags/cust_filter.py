from django import template

register = template.Library()
@register.filter(name='tn')
def tru(value,n):
    result = value[0:n]
    return result
@register.filter(name='c_and_c')
def cut_and_add(value,arg):
    result = value[:9]+str(arg)
    return result

