from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    pid = models.CharField(unique=True, max_length=12, verbose_name="PID")
    email = models.EmailField(null=True, verbose_name="Email")
    phone = models.CharField(null=True, max_length=11)
    homeaddress = models.CharField(null=True, max_length=140, verbose_name="Home Address")
    localaddress = models.CharField(null=True, max_length=140, verbose_name="Local Address")
    instate = models.NullBooleanField(null=True, verbose_name="In-state")
    grade = models.IntegerField(unique=False, null=True, max_length=3)
    finalexam = models.IntegerField(unique=False, null=True, max_length=4, verbose_name="Final Exam")
    degree = models.CharField(null=True, max_length=50)
    major = models.CharField(max_length=20)
    #imageurl = models.ImageField(max_length=100)
    iep = models.NullBooleanField(null=True, verbose_name="IEP")    
    comments = models.TextField()
    
    class Meta(object):
        ordering = ('pid', 'name')

    def __unicode__(self):
        return U'%s %s' %(self.name, self.pid)

class Course(models.Model):
    name = models.CharField(unique=True, max_length=50)
    callnumber = models.CharField(unique=False, max_length=4)
    instructor = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    term = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)
    date = models.DateField()
    
    class Meta(object):
        verbose_name_plural = "Courses"
        ordering = ('-date', 'name')
        
    def __unicode__(self):
        return U'%s | %s' %(self.callnumber, self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Course, self).save(*args, **kwargs)