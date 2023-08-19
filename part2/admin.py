from django.contrib import admin
from .models import*
from django_jalali.admin.filters import JDateFieldListFilter
from .models import Track
# Register your models here.
class BarAdmin(admin.ModelAdmin):
    list_filter = (
        ('stu_birthdate', JDateFieldListFilter),
    )


admin.site.register(ReportStudent, BarAdmin)
admin.site.register(Track)
admin.site.register(EropStudent)


class NixAdmin(admin.ModelAdmin):
    list_filter = (
        ('par_birthdate', JDateFieldListFilter),
        ('stu_birthdate', JDateFieldListFilter),
    )

admin.site.register(Studentprofolio, NixAdmin)

class ioxAdmin(admin.ModelAdmin):
    list_filter = (
        ('create_at', JDateFieldListFilter),
    )

admin.site.register(Blog, ioxAdmin)

class xeoAdmin(admin.ModelAdmin):
    list_filter = (
        ('create_at', JDateFieldListFilter),
    )

admin.site.register(EventCategory, xeoAdmin)
