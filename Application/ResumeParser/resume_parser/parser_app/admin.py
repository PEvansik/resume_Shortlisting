from django.contrib import admin
from .models import Resume,feedback

admin.site.register(feedback)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass