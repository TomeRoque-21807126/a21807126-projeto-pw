from django import template

register = template.Library()

@register.filter
def format_weather_id(value):
    return f"{int(value):02}"