from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def set_course_not_started(context, course, progress):
    course_not_started = True
    for prog in progress:
        if course.title == prog.course.title:
            course_not_started = False
            break
    context['course_not_started'] = course_not_started
    return ''
