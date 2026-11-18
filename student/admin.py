from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'branch')  # Shows these 3 columns
    search_fields = ('name', 'roll_no')           # Adds a search box at the top
    list_filter = ('branch',)                     # Adds a filter sidebar on the right

admin.site.register(Student, StudentAdmin)

admin.site.site_header = "Student Management System"
admin.site.site_title = "Student Admin Portal"


# Register your models here.
