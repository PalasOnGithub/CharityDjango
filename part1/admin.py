from django.contrib import admin
from .models import*
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


class BarAdmin(admin.ModelAdmin):
    list_filter = (
        ('stu_birthdate', JDateFieldListFilter),
    )


admin.site.register(StudentRegisteration, BarAdmin)

class NixAdmin(admin.ModelAdmin):
    list_filter = (
        ('par_birthdate', JDateFieldListFilter),
        ('hus_birthdate', JDateFieldListFilter),
        ('hus_deaddate', JDateFieldListFilter),
        ('hus_cutdate', JDateFieldListFilter),

    )

admin.site.register(ParentsRegisteration, NixAdmin)

admin.site.register(HomeBack)