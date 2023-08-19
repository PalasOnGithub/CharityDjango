from random import choices
from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
import os


# Create your models here.
def get_file_path(obj, fname):
    return os.path.join(
        'Picture',
        obj.stu_name,
        obj.stu_lastname,
        fname,
)


class StudentRegisteration(models.Model):
    GENDER_CHOICES = (
        ('H', 'سالم'),
        ('M', 'دارای معلولیت'),
    )

    HOUSE_CHOICES = (
        ('R', 'اجاره'),
        ('P', 'شخصی'),
        ('E', 'سایر'),
    )

    PARENT_choice = (
        (1 , 'پدر'),
        (2 , "مادر"),
        (3 , 'پدربزرگ'),
        (4 , 'مادر بزرگ'),
        (5 , 'سایرین')
    )

    STUDENT_choice = (
        (0 , 'ابتدایی یا متوسطه اول'),
        (1 , 'ریاضی'),
        (2 , 'تجربی'),
        (3 , 'علوم انسانی'), 
        (4 , 'فنی و دانش'), 
        (5 , 'دانشگاه'),

    )

    LOC_choice =(
        (0 , 'شهرستان'),
        (1 , 'منطقه یک'),
        (2 , 'منطقه دو'),
        (3 , 'منطقه سه'),
        (4 , 'منطقه چهار'), 
        (5 , 'منطقه پنج'),
        (6 , 'منطقه شش'),
        (7 , 'منطقه هفت'),
        (8 , 'دانشگاه')
    )

    Gender_choice = (
        (1 , 'مذکر'),
        (2 , 'مونث'),
    )

    stu_pic = models.ImageField(upload_to =get_file_path, verbose_name="عکس دانش اموز")
    objects = jmodels.jManager()
    stu_name = models.CharField(max_length=32 , verbose_name="نام دانش اموز" , null=True , blank=True)
    stu_lastname = models.CharField(max_length=64 , verbose_name="نام خانوادگی" , null=True , blank=True)
    stu_fathername = models.CharField(max_length=32 , verbose_name="نام پدر دانش اموز" , null=True , blank=True)
    stu_birthdate = jmodels.jDateField(verbose_name="تاریخ تولد دانش اموز" , null=True , blank=True)
    stu_joindate = jmodels.jDateField(verbose_name='تاریخ پیوستن' , null=True , blank=True)
    stu_sex = models.IntegerField(choices=Gender_choice , null=True , blank = True , verbose_name = 'جنسیت')
    stu_par = models.IntegerField(choices=PARENT_choice , null=True , blank = True , verbose_name = "سرپرست")
    stu_pos = models.IntegerField(choices=LOC_choice , null=True , blank = True , verbose_name ='منطق اموزش و پرورش')
    stu_major = models.IntegerField(choices=STUDENT_choice , null=True , blank = True , verbose_name ='رشته تحصیلی')
    stu_nationalcode = models.IntegerField(max_length=10 ,verbose_name="کد ملی دانش اموز" , null=True , blank=True)
    stu_intshenas = models.CharField(max_length=3 ,verbose_name="شماره شناسنامه دانش اموز" , null=True , blank=True)
    stu_placerio = models.CharField(max_length=64 , verbose_name="محل صدور شناسنامه" , null=True , blank=True)
    stu_placerig = models.CharField(max_length=12 , verbose_name="شماره سریال شناسنامه" , null=True , blank=True)
    stu_level = models.IntegerField(max_length=2, verbose_name="پایه تحصیلی" , null=True , blank=True)
    stu_avrage = models.CharField(max_length=5 , verbose_name="معدل دانش اموز" , null=True , blank=True)
    stu_status = models.CharField(max_length=1, choices=GENDER_CHOICES , verbose_name="وضعیت جسمی دانش اموز" , null=True , blank=True)
    stu_dirschool = models.CharField(max_length=64 , verbose_name="محل تحصیل" , null=True , blank=True)
    stu_schoolcode = models.IntegerField(verbose_name="کد مدرسه" , null=True , blank=True)
    stu_lastlevel = models.IntegerField(max_length=2, verbose_name="پایه تحصیلی قبلی" , null=True , blank=True)
    stu_lastschool = models.CharField(max_length=64 , verbose_name="نام مدرسه قبلی" , null=True , blank=True)
    stu_lastavrage = models.CharField(max_length=5 , verbose_name="معدل دانش اموز سال قبل" , null=True , blank=True)
    stu_lastlowcourse = RichTextField(verbose_name = "دروس ضعیف سال گذشته" , null=True , blank=True)
    par_fullname = models.CharField(max_length=86 , verbose_name = "نام و نام خانوادگی سرپرست" , null=True , blank=True)
    par_courselevel = models.CharField(max_length=32 , verbose_name= "تحصیلات سرپرست" , null=True , blank=True)
    par_birthdate = jmodels.jDateField(verbose_name="تاریخ تولد سرپرست" , null=True , blank=True)
    par_job = models.CharField(max_length=32 , verbose_name="شغل سرپرست" , null=True , blank=True)
    par_jobloc = models.CharField(max_length=128 , verbose_name="محل کار" , null=True , blank=True)
    par_jobnum = models.IntegerField(verbose_name="شماره تلفن محل کار" , null=True , blank=True)
    fam_loc = models.CharField(max_length=256 , verbose_name="ادرس منزل" , null=True , blank=True)
    fam_staticnum = models.IntegerField(verbose_name = "تلفن ثابت" , null=True , blank=True)
    fam_dynamicnum = models.IntegerField(verbose_name="تلفن همراه" , null=True , blank=True)
    fam_locstatus = models.CharField(max_length=1, choices=HOUSE_CHOICES , verbose_name="وضعیت مسکن خانواده" , null=True , blank=True)
    fam_locdesc = models.TextField(verbose_name="نوضیحات مربوط به مسکن" , null=True , blank=True)
    fam_numofiters = RichTextField(verbose_name = "تعداد افراد خانواده" , null=True , blank=True)
    from_user = models.ForeignKey(User , blank = True , null= True, on_delete=models.CASCADE, verbose_name="از دانش اموز")



    def __str__(self):
        return f"{self.stu_name} - {self.stu_lastname}"

    class Meta:
        verbose_name = "فرم ثبت نام دانش اموز"
        verbose_name_plural = "فرم ثبت نام دانش اموزان"


class ParentsRegisteration(models.Model):
    STATUS_CHOICES = (
        ('L', 'زندگی با همسر'),
        ('D', 'فوت همسر'),
        ('C', 'جدا از همسر'),
    )

    HOUSE_CHOICES = (
        ('R', 'اجاره'),
        ('P', 'شخصی'),
        ('E', 'سایر'),
    )

    objects = jmodels.jManager()

    par_fullname = models.CharField(max_length=128 , null=True , blank=True, verbose_name="نام و نام خانوادگی")
    par_fathername = models.CharField(max_length=32 , null=True , blank=True, verbose_name="نام پدر")
    par_natcode = models.IntegerField(null=True , blank=True , verbose_name="کد ملی")
    par_profilio = models.CharField(max_length=32,  verbose_name="شناسنامه" , null=True , blank=True)
    par_birthdate = jmodels.jDateField(verbose_name="تاریخ تولد", null= True, blank= True)
    par_job = models.CharField(max_length=128, verbose_name="شاغل در" , null=True , blank=True)
    par_reward = models.TextField(max_length=128, verbose_name="سنوات خدمات", null=True , blank=True)
    par_numjob = models.CharField(max_length=254, verbose_name="تلفن و ادرس محل کار", null=True , blank=True)
    hus_fullname = models.CharField(max_length=128 , null=True , blank=True, verbose_name="نام و نام خانوادگی همسر")
    hus_fathername = models.CharField(max_length=32 , null=True , blank=True, verbose_name="نام پدر")
    hus_natcode = models.IntegerField(null=True , blank=True , verbose_name="کد ملی")
    hus_profilio = models.CharField(max_length=64, verbose_name="شناسنامه" , null=True , blank=True)
    hus_birthdate = jmodels.jDateField(verbose_name="تاریخ تولد", null= True, blank= True)
    hus_job = models.CharField(max_length=256, verbose_name="شاغل در" , null=True , blank=True)
    hus_reward = models.TextField(verbose_name="سنوات خدمات", null=True , blank=True)
    hus_numjob = models.CharField(max_length=254, verbose_name="تلفن و ادرس محل کار", null=True , blank=True)
    par_status = models.CharField(max_length=1, choices=STATUS_CHOICES , verbose_name="وضعیت تاهل")
    hus_deaddate = jmodels.jDateField(verbose_name="تاریخ فوت", null= True, blank= True)
    hus_descdead = models.CharField(max_length=256 , null=True , blank=True , verbose_name='علت فوت')
    hus_cutdate = jmodels.jDateField(verbose_name="تاریخ جدایی", null= True, blank= True)
    hus_desccut = models.CharField(max_length=256 , null=True , blank=True , verbose_name='علت جدایی')
    fam_numofiters = RichTextField(verbose_name = "تعداد افراد خانواده")
    fam_deschealth = RichTextField(verbose_name = "وضعیت جسمی و روحی خانواده")
    fam_locstatus = models.CharField(max_length=1, choices=HOUSE_CHOICES , verbose_name="وضعیت مسکن خانواده")
    fam_poomon = RichTextField(verbose_name = "وضعیت درامد خانواده")

    def __str__(self):
        return f"{self.par_fullname} - {self.par_natcode}"

    class Meta:
        verbose_name = "فرم مربوط به سرپرست خانواده"
        verbose_name_plural ="فرم مربوط به سرپرستان خانواده"


class HomeBack(models.Model):
    name = models.TextField(verbose_name="نام")
    picture = models.ImageField(upload_to= 'Picture/Home_main_image/',null=True, blank=True , verbose_name="عکس")
    num_page = models.IntegerField(null=True , blank=True , verbose_name="شماره عکس")

    class Meta:
        verbose_name = "عکس پس زمینه سایت"
        verbose_name_plural ="عکس های پس زمینه سایت"