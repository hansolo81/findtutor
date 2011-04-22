from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
       return '%s' % self.name

class StateAdmin(admin.ModelAdmin):
    pass

class District(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State)

    def __str__(self):
        return '%s, %s' % (self.name, self.state)

class DistrictAdmin(admin.ModelAdmin):
    pass

class Location(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District)

    def __str__(self):
        return '%s, %s' % (self.name, self.district)

class LocationAdmin(admin.ModelAdmin):
    pass

class Level(models.Model):
    name = models.CharField(max_length=20)
    grade_name = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % self.name

class LevelAdmin(admin.ModelAdmin):
    pass

class Sublevel(models.Model):
    name = models.IntegerField()
    level = models.ForeignKey(Level)

    def __str__(self):
        return '%s %s %s' % (self.level, self.level.grade_name, self.name)

class SublevelAdmin(admin.ModelAdmin):
    pass

class Subject(models.Model):
    name = models.CharField(max_length=100)
    sublevel = models.ForeignKey(Sublevel)

    def __str__(self):
        return '%s : %s'% (self.name, self.sublevel)

class SubjectAdmin(admin.ModelAdmin):
    pass

class TutorProfile(models.Model):
    user = models.ForeignKey(User)
    dob = models.DateField('Date of birth', null=True)
    location = models.ForeignKey(Location, null=True)
    subjects_on_offer = models.ManyToManyField(Subject)

    def __str__(self):
        return "%s" % self.user.get_full_name()

def create_tutor_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = TutorProfile.objects.get_or_create(user=instance)

post_save.connect(create_tutor_profile, sender=User)

class TutorProfileAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Location, LocationAdmin)
#admin.site.register(District, DistrictAdmin)
#admin.site.register(State, StateAdmin)
#admin.site.register(Subject, SubjectAdmin)
#admin.site.register(TutorProfile, TutorProfileAdmin)
#admin.site.register(Level, LevelAdmin)
#admin.site.register(Sublevel, SublevelAdmin)

