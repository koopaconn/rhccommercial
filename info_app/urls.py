from django.urls import path
from info_app import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'info_app'

urlpatterns = [
    path('about/',views.view_about.as_view(),name='about'),
    # path('testimonials/',views.view_testimonial.as_view(),name='testimonials'),
    path('contact/',views.view_contact,name='contact'),
    path('contact/thanks',views.view_thanks.as_view(),name='thanks'),
    path('portfolio/',views.view_joblist.as_view(),name='joblist'),
    path('portfolio/<int:pk>/',views.view_jobdetails.as_view(),name='jobdetails'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
