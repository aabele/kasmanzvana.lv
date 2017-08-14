# from django.template.loader import render_to_string
from django import template

register = template.Library()


@register.simple_tag
def breadcrumbs(number):

    return ""
    # phone = phones.database.Phone(number)
    # categories = phone.get_categories()[:-1]
    #
    # context_data = []
    # aggregated = []
    #
    # for cat in categories:
    #     aggregated.append(cat)
    #     context_data.append(("".join(aggregated), cat))
    #
    # return render_to_string("breadcrumbs.html", {
    #     "categories": context_data,
    #     "number": number
    # })


@register.filter(name='is_phone')
def is_phone(value):
    pass
    # phone = phones.database.Phone(value)
    # return phone.has_data()


@register.filter(name='is_category')
def is_category(value):
    pass
    # category = phones.database.Category(value)
    # return category.has_data()
