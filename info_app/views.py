from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
from django.urls import reverse_lazy,reverse
from django.views.generic import (View,TemplateView,ListView,DetailView,FormView)
from django.core.mail import send_mail
from random import randint

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class view_joblist_index(ListView):
    context_object_name = 'job_list_index'
    model = models.model_job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_id = models.model_testimonial.objects.all().order_by("-id")[0]
        # max_id = models.model_testimonial.objects.all().aggregate(max_id=max("id"))['max_id']
        while True:
            pk = randint(0, max_id.pk)
            testimonial = models.model_testimonial.objects.filter(pk=pk).first()
            if testimonial:
                context['testimonial'] = testimonial
                return context

    template_name = 'index.html'


class view_testimonial_index(ListView):
    context_object_name = 'testimonial_list_index'
    model = models.model_testimonial
    template_name = 'index.html'

class view_about(ListView):
    context_object_name = 'testimonial_list_about'
    model = models.model_testimonial
    template_name = 'info_app/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobnumber = models.model_jobnum.objects.filter(pk=1).first()
        context['jobnumber'] = jobnumber
        return context

class view_testimonial(ListView):
    context_object_name = 'testimonial_details'
    model = models.model_testimonial
    template_name = 'info_app/testimonials.html'

def view_contact(request):
    if request.method == 'POST':
        form = forms.form_contact(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            sender_subject = form.cleaned_data['subject']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail(sender_subject, message, sender_email, ['koopaconn@gmail.com'],fail_silently=False,)
            form = 'Thanks for contacting us!'
            return render(request, 'info_app/thanks.html', {'form': form})
    else:
        form = forms.form_contact()

    return render(request, 'info_app/contact.html', {'form': form})

class view_thanks(TemplateView):
    template_name = 'thanks.html'

class view_joblist(ListView):
    context_object_name = 'job_list'
    model = models.model_job
    template_name = 'info_app/job_list.html'

class view_jobdetails(DetailView):
    context_object_name = 'job_details'
    model = models.model_job
    template_name = 'info_app/job_detail.html'
