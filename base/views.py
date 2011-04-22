# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from findtutor.base.models import TutorProfile
from findtutor.base.forms import *
import glob
import os

def start_page(request):
    tutor_list = TutorProfile.objects.all()
    loc_form = SearchLocationForm(auto_id=True)
    sub_form = SearchSubjectForm(auto_id=True)
    pics = []
    for x in glob.glob('/home/hansolo81/projects/findtutor/sitemedia/images/*.jpg'):
        pics.append(os.path.basename(x))
    return render_to_response('base/index.html', {'tutor_list': tutor_list, 'loc_form': loc_form, 'sub_form': sub_form, 'pics': pics})
