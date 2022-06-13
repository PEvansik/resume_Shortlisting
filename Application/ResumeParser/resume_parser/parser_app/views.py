from asyncio.windows_events import NULL
from typing import Counter
from urllib import response
from django.shortcuts import render, redirect
from resume_parser.utils import extract_years
from pyresparser import ResumeParser
from .models import Resume, UploadResumeModelForm, feedback
from django.contrib import messages
from django.conf import settings
from django.db import IntegrityError
from django.http import HttpResponse, FileResponse, Http404
from .models import Resume
import os
import csv
#  extracting date time from experience string

import re
from datetime import datetime
from django.contrib import messages


def homepage(request):


    if request.method == 'POST':
        Resume.objects.all().delete()
        # feedback.objects.all()

        file_form = UploadResumeModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('resume')
        resumes_data = []   
        if file_form.is_valid():
            for file in files:
                try:
                    # saving the file
                    resume = Resume(resume=file)
                    resume.save()
                    jd="python,machine learning"
                    # extracting resume entities
                    parser = ResumeParser(os.path.join(settings.MEDIA_ROOT, resume.resume.name))
                    data = parser.get_extracted_data()
                    resumes_data.append(data)
                    # resume.check              = print('Maual check')
                    resume.name               = data.get('name')
                    resume.email              = data.get('email')
                    resume.mobile_number      = data.get('mobile_number')
                #   calculateing years of experienece
                    # resume.date_string        = data.get('date_string')
                    if data.get('degree') is not None:
                        resume.education      = ', '.join(data.get('degree'))
                    else:
                        resume.education      = None
                    # if not data.get('company_names') :
                    #     messages.warning(request, 'multiple fields is missing in requesting manual checking',Counter)

                    # else:
                    #     resume.company_names      = data.get('company_names')
                    # # if data.get('college_name') is None:
                    # #     messages.warning(request, 'Multiple filed is missing requesting manual checking in  Resume:')

                    # else:
                    #     resume.college_name       = data.get('college_name')
                    resume.designation        = data.get('designation')
                    listofdates="28 june 2019-28 jan 2021"

                    resume.years  = extract_years(listofdates)
                    # resume.years(listofdates=listofdates)
                    # if data.get('years') is not None:
                    #     resume.years     = ', '.join(data.get('years'))
                    # else:
                    #     resume.years     ="Not able to detect dates"
                    # print(resume.years)
                

                    # match_str = re.search(r'\')

                    # resume.relvant_experience=data.get('relevant_experience')
                    if data.get('skills') is not None:
                        resume.skills         = ', '.join(data.get('skills'))

                        
                    else:
                        resume.skills         = None
                    if data.get('experience') is not None:
                        resume.experience     = ', '.join(data.get('experience'))
                    else:
                        resume.experience     = None
                    resume.save()
                except IntegrityError:
                    messages.warning(request, 'Duplicate resume found:', file.name)
                    return redirect('homepage')
            resumes = Resume.objects.all()
            messages.success(request, 'Resumes uploaded!')
            context = {
                'resumes': resumes,
                
            }
        
        return render(request, 'base.html', context)
    else:
        form = UploadResumeModelForm()
    return render(request, 'base.html', {'form': form})
def dCsv(request):
    
    response= HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Resume','Name','Email','mobile number','Education','SKills','Company','College','Designation','Experience','Score'])
    for resume in Resume.objects.all().values_list('resume','name','email','mobile_number','education','skills','company_name','college_name','designation','experience'):
        writer.writerow(resume)
    response['Content-Disposition'] = 'attachment; filename="parsed_data.csv"'
    return(response)