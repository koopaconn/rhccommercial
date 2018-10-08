from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy,reverse
from django.views.generic import (View,TemplateView,ListView,DetailView)

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class view_joblist_index(ListView):
    context_object_name = 'job_list_index'
    model = models.model_job
    template_name = 'index.html'

class view_testimonial_index(ListView):
    context_object_name = 'testimonial_list_index'
    model = models.model_testimonial
    template_name = 'index.html'
    
class view_about(TemplateView):
    template_name = 'info_app/about.html'

class view_testimonial(TemplateView):
    context_object_name = 'testimonial_details'
    model = models.model_testimonial
    template_name = 'info_app/testimonials.html'

class view_contact(TemplateView):
    template_name = 'info_app/contact.html'

class view_joblist(ListView):
    context_object_name = 'job_list'
    model = models.model_job
    template_name = 'info_app/job_list.html'

class view_jobdetails(DetailView):
    context_object_name = 'job_details'
    model = models.model_job
    template_name = 'info_app/job_detail.html'
