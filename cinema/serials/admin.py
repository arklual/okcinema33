from django.contrib import admin
from .models import Serial, Seriya
from marks.models import SerialRecension

class SeriyaInline(admin.TabularInline):
    model = Seriya
    fk_name = "serial"
class RecensionInline(admin.TabularInline):
    model = SerialRecension
    fk_name = "serial"
@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith", )
    inlines = [
        SeriyaInline,
        RecensionInline,
    ]