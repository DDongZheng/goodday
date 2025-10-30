from django.contrib import admin

# Register your models here.

from .models import Goodthing

@admin.register(Goodthing)
class GoodthingAdmin(admin.ModelAdmin):
    list_display = ["id","content","likes_count","not_good_count","created_at"]
    list_filter = ['created_at']
    search_fields = ['content']
    readonly_fields = ['created_at', 'updated_at']
