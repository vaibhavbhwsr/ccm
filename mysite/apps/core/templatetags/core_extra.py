from django import template

register = template.Library()


@register.filter
def get_cases_counts(client, user):
    return user.lawyer_cases.filter(client=client).count()


@register.filter
def get_client_total_bill(client, user):
    rate = user.user_info.billing_rate
    return user.lawyer_cases.filter(client=client).count() * rate if rate else 0
