from django.contrib import admin
from info_app.models import model_job,model_jobpic,model_testimonial,model_jobnum

# Register your models here.
admin.site.register(model_job)
admin.site.register(model_jobpic)
admin.site.register(model_testimonial)
admin.site.register(model_jobnum)
