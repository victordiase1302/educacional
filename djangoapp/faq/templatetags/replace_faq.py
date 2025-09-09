from django import template

register = template.Library()


@register.filter(name="paragraph_replace")
def paragraph_replace(text):
    return text.replace(";", '</li><li class="pb-2">')
