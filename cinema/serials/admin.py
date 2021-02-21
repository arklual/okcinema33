from django.contrib import admin
from .models import Serial, Seriya

class SeriyaInline(admin.TabularInline):
    model = Seriya
    fk_name = "serial"
@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith", )
    inlines = [
        SeriyaInline,
    ]