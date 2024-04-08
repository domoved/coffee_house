from django.contrib import admin
from django.utils.text import slugify
from unidecode import unidecode

from .models import (Course, Lecture, Test,
                     LearningProgress, CourseMaterial, CertificationProcess, Grade, Question, Answer)


class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('test_slug',)
    actions = ['regenerate_slug']

    def regenerate_slug(self, request, queryset):
        for test in queryset:
            test.test_slug = slugify(unidecode(test.title))
            test.save()

    regenerate_slug.short_description = "Перегенерировать слаги"


class LectureAdmin(admin.ModelAdmin):
    readonly_fields = ('lecture_slug',)
    actions = ['regenerate_slug']

    def regenerate_slug(self, request, queryset):
        for lecture in queryset:
            lecture.course_slug = slugify(unidecode(lecture.title))
            lecture.save()

    regenerate_slug.short_description = "Перегенерировать слаги"


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('course_slug',)
    actions = ['regenerate_slug']

    def regenerate_slug(self, request, queryset):
        for course in queryset:
            course.course_slug = slugify(unidecode(course.title))
            course.save()

    regenerate_slug.short_description = "Перегенерировать слаги"


admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(LearningProgress)
admin.site.register(CourseMaterial)
admin.site.register(CertificationProcess)
admin.site.register(Grade)
admin.site.register(Question)
admin.site.register(Answer)
