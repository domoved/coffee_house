from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def set_course_not_started(context, course, progress):
    course_not_started = all(prog.course.title != course.title for prog in progress)
    context['course_not_started'] = course_not_started
    return ''
