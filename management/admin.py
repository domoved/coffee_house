from django.contrib import admin
from .models import LearningProgress, Document, CourseMaterial, CertificationProcess, Grade

admin.site.register(LearningProgress)
admin.site.register(Document)
admin.site.register(CourseMaterial)
admin.site.register(CertificationProcess)
admin.site.register(Grade)