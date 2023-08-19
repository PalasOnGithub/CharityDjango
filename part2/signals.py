from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import*
from part1.models import StudentRegisteration
from django.contrib.auth.models import User


@receiver(post_save, sender=StudentRegisteration)
def create_profile(sender, instance, created, **kwargs):
    if created:
        genrate_ins_unicode = str(instance.stu_joindate.year)[2:] + str(instance.stu_sex) + str(instance.stu_birthdate.year)[2:] + str(instance.stu_par)
            
        if instance.stu_status == 'H':
            genrate_ins_unicode += str(1)
        else:
            genrate_ins_unicode += str(2)

            #genrate_ins_unicode += str(instance.stu_level)
            #genrate_ins_unicode += str(instance.stu_major)
            #genrate_ins_unicode += str(instance.stu_pos)

        Studentprofolio.objects.get_or_create(
            stu_pic = instance.stu_pic,
            stu_name = instance.stu_name,
            stu_lastname = instance.stu_lastname,
            stu_fathername = instance.stu_fathername,
            stu_birthdate = instance.stu_birthdate,
            stu_nationalcode = instance.stu_nationalcode,
            stu_intshenas = instance.stu_intshenas,
            stu_placerhi = instance.stu_placerio,
            stu_placerig = instance.stu_placerig,
            stu_status = instance.stu_status,
            stu_dirschool = instance.stu_dirschool,
            par_fullname = instance.par_fullname,
            par_courselevel =instance.par_courselevel,
            par_birthdate = instance.par_birthdate,
            par_job = instance.par_job,
            par_jobloc = instance.par_jobloc,
            par_jobnum = instance.par_jobnum,
            fam_loc = instance.fam_loc,
            fam_staticnum = instance.fam_staticnum,
            fam_dynamicnum = instance.fam_dynamicnum,
            fam_locstatus = instance.fam_locstatus,
            stu_unicode = genrate_ins_unicode,
            from_user = instance.from_user
            )


