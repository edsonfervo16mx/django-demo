from django import template

from courses.models import Course

from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag()
def last_course():
    """Obtiene el ultimo curso puesto en la libreria"""
    return Course.objects.latest('created_at')


@register.filter('time_estimate')
def time_estimate(word_count):
    # Determina el numero de minutos que le toma terminar el curso
    minutes = round(word_count/2)
    return minutes


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    # Convertir texto en formato html
    html = markdown.markdown(markdown_text)
    return mark_safe(html)
