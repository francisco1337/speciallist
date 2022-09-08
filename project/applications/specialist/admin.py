from django.contrib import admin
from .models import Clinic,Title,Specialist,Specialism,Availability,Meeting,Meeting_topic,Schedule

# Register your models here.


admin.site.register(Clinic)
admin.site.register(Title)
admin.site.register(Specialist)
admin.site.register(Specialism)
admin.site.register(Schedule)
admin.site.register(Availability)
admin.site.register(Meeting)
admin.site.register(Meeting_topic)




