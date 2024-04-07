from django.contrib import admin
from django.utils.text import slugify
from unidecode import unidecode

from .models import (Course, Lecture, Test,
                     LearningProgress, CourseMaterial, CertificationProcess, Grade, Question, Answer)


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    actions = ['regenerate_slug']

    def regenerate_slug(self, request, queryset):
        for course in queryset:
            course.slug = slugify(unidecode(course.title))
            course.save()

    regenerate_slug.short_description = "Перегенерировать слаги"


admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture)
admin.site.register(Test)
admin.site.register(LearningProgress)
admin.site.register(CourseMaterial)
admin.site.register(CertificationProcess)
admin.site.register(Grade)
admin.site.register(Question)
admin.site.register(Answer)
