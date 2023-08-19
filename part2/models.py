from django.urls import reverse
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
import os
import random 
import uuid

# Create your models here.
def get_file_path(obj, fname):
    return os.path.join(
        'Picture',
        obj.name,
        obj.from_user.username,
        fname,
)

def get_file_kio(obj, fname):
    return os.path.join(
        'Picture',
        obj.name,
        obj.stu_lastname,
        fname,
)


def genrate_random_code():
    man = str(random.randint(1000000000, 9999999999)) 
    return man

class Studentprofolio(models.Model):
    GENDER_CHOICES = (
        ('H', 'سالم'),
        ('M', 'دارای معلولیت'),
    )

    HOUSE_CHOICES = (
        ('R', 'اجاره'),
        ('P', 'شخصی'),
        ('E', 'سایر'),
    )

    STU_STATUS = (
        ('A' , 'تایید شده'),
        ('W' , 'در انتظار بررسی'),
        ('R' , 'رد شده'),
    )

    stu_pic = models.ImageField(upload_to =get_file_kio, verbose_name="عکس دانش اموز")
    objects = jmodels.jManager()
    stu_name = models.CharField(max_length=32 , verbose_name="نام دانش اموز")
    stu_lastname = models.CharField(max_length=64 , verbose_name="نام خانوادگی")
    stu_fathername = models.CharField(max_length=32 , verbose_name="نام پدر دانش اموز")
    stu_birthdate = jmodels.jDateField(verbose_name="تاریخ تولد دانش اموز")
    stu_nationalcode = models.IntegerField(max_length=10 ,verbose_name="کد ملی دانش اموز")
    stu_intshenas = models.CharField(max_length=3 ,verbose_name="شماره شناسنامه دانش اموز")
    stu_placerhi = models.CharField(max_length=64 , verbose_name="محل صدور شناسنامه")
    stu_placerig = models.CharField(max_length=12 , verbose_name="شماره سریال شناسنامه")
    stu_status = models.CharField(max_length=1, choices=GENDER_CHOICES , verbose_name="وضعیت جسمی دانش اموز")
    stu_dirschool = models.CharField(max_length=64 , verbose_name="محل تحصیل")
    par_fullname = models.CharField(max_length=86 , verbose_name = "نام و نام خانوادگی سرپرست")
    par_courselevel = models.CharField(max_length=32 , verbose_name= "تحصیلات سرپرست")
    par_birthdate = jmodels.jDateField(verbose_name="تاریخ تولد سرپرست")
    par_job = models.CharField(max_length=32 , verbose_name="شغل سرپرست")
    par_jobloc = models.CharField(max_length=128 , verbose_name="محل کار")
    par_jobnum = models.IntegerField(verbose_name="شماره تلفن محل کار")
    fam_loc = models.CharField(max_length=256 , verbose_name="ادرس منزل")
    fam_staticnum = models.IntegerField(verbose_name = "تلفن ثابت")
    fam_dynamicnum = models.IntegerField(verbose_name="تلفن همراه")
    fam_locstatus = models.CharField(max_length=1, choices=HOUSE_CHOICES , verbose_name="وضعیت مسکن خانواده")
    stu_unicode = models.CharField(max_length=11 , unique=True, verbose_name="کد بورسیه" )
    from_user = models.ForeignKey(User , on_delete=models.CASCADE, verbose_name="از دانش اموز")
    reg_status = models.CharField(max_length=1, choices= STU_STATUS, verbose_name="وضعیت پرونده" , default='W')

    def __str__(self):
        return f"{self.stu_name} - {self.stu_lastname}"

    class Meta:
        verbose_name = "پرونده دانش اموز"
        verbose_name_plural = "پرونده دانش اموزان"


class ReportStudent(models.Model):
    name = models.CharField(max_length=128 , verbose_name='نام')
    objects = jmodels.jManager()
    from_user = models.ForeignKey(User , on_delete=models.CASCADE, verbose_name="از دانش اموز")
    pic = models.ImageField(upload_to = get_file_path , verbose_name="عکس کارنامه")
    stu_birthdate = jmodels.jDateField(verbose_name="تاریخ تحویل کارنامه")
    stu_report = models.ForeignKey(Studentprofolio , on_delete=models.CASCADE, verbose_name = "پیوند به پرونده")

    def __str__(self):
        return f"{self.name} - {self.from_user.username}"

    class Meta:
        verbose_name = "کارنامه دانش اموز"
        verbose_name_plural = "کارنامه دانش اموزان"


class EventCategory(models.Model):
    name = models.CharField(max_length=128 , verbose_name="عنوان دسته بندی")
    objects = jmodels.jManager()
    create_at = jmodels.jDateField(verbose_name="تاریخ انتشار")
    picture = models.ImageField(upload_to='Picture/Event_pictures/%Y/%m/%d/', max_length=150 , verbose_name="عکس")
    
    def __str__(self):
        return self.name 


    class Meta:
        verbose_name = "دسته بندی خبر"
        verbose_name_plural = "دسته بندی های خبر"



class Blog(models.Model):
    iox_cet = models.ForeignKey(EventCategory , on_delete=models.CASCADE , verbose_name="دسته بندی خبر")
    name = models.CharField(max_length=50, null=True, blank=True , verbose_name="نام خبر یا موضوع")
    short_desc = models.TextField( null=True, blank=True , verbose_name='کوتاه شده عنوان' )
    location_Event = models.TextField(null = True , blank = True , verbose_name="محل خبر")
    desc_first = models.TextField( null=True, blank=True , verbose_name="نوضیحات")
    picture = models.ImageField(upload_to= 'Picture/Event_pictures/%Y/%m/%d/',null=True, blank=True , verbose_name="عکس خبر")
    end_desc = models.TextField(null = True, blank= True , verbose_name="توضیحات نهایی")
    video = models.FileField(upload_to = 'Audios/%Y/%m/%d/', null=True , blank = True , verbose_name="فیلم یا ویدیو از موضوع")
    objects = jmodels.jManager()
    create_at = jmodels.jDateField(verbose_name="تاریخ انتشار")
    fiknole = models.UUIDField("فیلد شناسایی" , default=uuid.uuid4(), unique=True)


    def __str__(self):
        return self.name

    def get_exact_url(self):
        return reverse('detailpage', args=[self.fiknole])

    class Meta:
        verbose_name = "خبر یا گفت و گو"
        verbose_name_plural = "اخبار یا گفت و گو ها"

class Track(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True , verbose_name = 'اسم ' )
    desc = models.TextField(null=True, blank=True , verbose_name = ' توضیحات')
    picture = models.ImageField(upload_to= 'Picture/Track_pictures/%Y/%m/%d/',null=True, blank=True , verbose_name = 'عکس ')
    track_audio = models.FileField(upload_to = 'Audios/%Y/%m/%d/', null=True, blank=True , verbose_name = 'قایل اهنگ')
    track_audio_remix = models.FileField(upload_to = 'Audios/Remixes/%Y/%m/%d/' , null = True , blank = True , verbose_name = 'ریمیکس اهنگ')
    Time = models.CharField(max_length = 10, null=True ,blank=True , verbose_name = "مدت اهنگ")
    create_on = models.DateTimeField(auto_now_add=True, null=True, blank=True , verbose_name = 'تاریخ انتشار')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اهنگ'
        verbose_name_plural = 'اهنگ ها'

class EropStudent(models.Model):
    come_from = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="درخواست کننده")
    reason = models.TextField(null=True , blank=True , verbose_name= 'توضیحات')
    
    def __str__(self):
        return self.come_from.username

    class Meta:
        verbose_name = 'گزارش'
        verbose_name_plural = 'گزارش ها'