from django.contrib import admin

from .models import UserProfile, Document


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('document_type',)


admin.site.register(UserProfile)
admin.site.register(Document, DocumentAdmin)