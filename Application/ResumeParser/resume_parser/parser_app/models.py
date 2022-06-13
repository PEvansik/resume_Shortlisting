from django.db import models
from django import forms
from django.forms import ClearableFileInput

# for deleting media files after record is deleted
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Resume(models.Model):
    # check         = models.CharField('Manual Check',max_length=255, null=True, blank=True)
    resume        = models.FileField('Upload Resumes', upload_to='resumes/')
    name          = models.CharField('Name', max_length=255, null=True, blank=True)
    email         = models.CharField('Email', max_length=255, null=True, blank=True)
    mobile_number = models.CharField('Mobile Number',  max_length=255, null=True, blank=True)
    education     = models.CharField('Education', max_length=255, null=True, blank=True)
    skills        = models.CharField('Skills', max_length=1000, null=True, blank=True)
    company_name  = models.CharField('Company Name', max_length=1000, null=True, blank=True)
    college_name  = models.CharField('College Name', max_length=1000, null=True, blank=True)
    years  = models.CharField('Total experience in years', max_length=1000, null=True, blank=True)
    # date_string   =models.CharField("experience",max_length=255, null=True, blank=True)
    designation   = models.CharField('Designation', max_length=1000, null=True, blank=True)
    experience    = models.CharField('Experience', max_length=1000, null=True, blank=True)
    uploaded_on   = models.DateTimeField('Uploaded On', auto_now_add=True)
    
    # relvant_experience=models.CharField('Relevant Experinece', max_length=1000, null=True, blank=True)
    
class UploadResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume']
        widgets = {
            'resume': ClearableFileInput(attrs={'multiple': True}),
        }
class feedback(models.Model):
    resumeId = models.CharField(max_length=255,blank=True)
    RightExperience = models.CharField( max_length=255,blank=True)
    RightSkills = models.CharField(max_length=255,blank=True)
    

    def __str__(self):
        return self.RightExperience
# delete the resume files associated with each object or record
@receiver(post_delete, sender=Resume)
def submission_delete(sender, instance, **kwargs):
    instance.resume.delete(False)

ai=["python","sql"]