from django import template

register = template.Library()


@register.filter
def get_cases_counts(client, user):
    return user.lawyer_cases.filter(client=client).count()


@register.filter
def get_client_total_bill(client, user):
    return user.lawyer_cases.filter(client=client).count() * user.user_info.billing_rate
