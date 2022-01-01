from django.contrib import admin


from .models import *

admin.site.register(Employee)
admin.site.register(Disease)
admin.site.register(Drug)
admin.site.register(Symptom)
admin.site.register(Covid)
admin.site.register(ChronicDisease)
admin.site.register(TimeTable)
# admin.site.register(Prescription)
admin.site.register(ContactedPersons)
admin.site.register(EduCovidStat)
admin.site.register(MostCommonDisease)
admin.site.register(MostCommonDiseaseEmp)
admin.site.register(CityCommonDisease)
admin.site.register(BiontechCovidEmp)
admin.site.register(SinovacCovidEmp)





