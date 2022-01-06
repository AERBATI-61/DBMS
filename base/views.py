from django.http import HttpResponse
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.

# employee

def base(request):
    return render(request, 'base.html')


class EmployeeList(ListView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'Employee/employee-list.html'


class CreateEmployee(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee-list')
    template_name = 'Employee/employee-form.html'


class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee-list')
    template_name = 'Employee/employee-form.html'


class DeleteEmployee(DeleteView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'Employee/employee-delete.html'
    success_url = reverse_lazy('employee-list')

# disease
class DiseaseList(ListView):
    model = Disease
    context_object_name = 'diseases'
    template_name = 'Desease/desease-list.html'


class CreateDisease(CreateView):
    model = Disease
    fields = '__all__'
    success_url = reverse_lazy('disease-list')
    template_name = 'Desease/desease-form.html'


class UpdateDisease(UpdateView):
    model = Disease
    fields = '__all__'
    success_url = reverse_lazy('disease-list')
    template_name = 'Desease/desease-form.html'


class DeleteDisease(DeleteView):
    model = Disease
    context_object_name = 'disease'
    success_url = reverse_lazy('disease-list')
    template_name = 'Desease/desease-delete.html'


# covid
class CovidList(ListView):
    model = Covid
    context_object_name = 'covid_lists'
    template_name = 'Covid/covid-list.html'


class CreateCovid(CreateView):
    model = Covid
    fields = '__all__'
    success_url = reverse_lazy('covid-list')
    template_name = 'Covid/covid-form.html'


class UpdateCovid(UpdateView):
    model = Covid
    fields = '__all__'
    success_url = reverse_lazy('covid-list')
    template_name = 'Covid/covid-form.html'


class DeleteCovid(DeleteView):
    model = Covid
    context_object_name = 'covid_list'
    success_url = reverse_lazy('covid-list')
    template_name = 'Covid/covid-delete.html'


# time table
class TimeTableList(ListView):
    model = TimeTable
    context_object_name = 'timetables'
    template_name = 'Time Table/timetable-list.html'


class CreateTimeTable(CreateView):
    model = TimeTable
    fields = '__all__'
    success_url = reverse_lazy('timetable-list')
    template_name = 'Time Table/timetable-form.html'


class UpdateTimeTable(UpdateView):
    model = TimeTable
    fields = '__all__'
    success_url = reverse_lazy('timetable-list')
    template_name = 'Time Table/timetable-form.html'


class DeleteTimeTable(DeleteView):
    model = TimeTable
    context_object_name = 'timetable'
    success_url = reverse_lazy('timetable-list')
    template_name = 'Time Table/timetable-delete.html'


# class PrescriptionList(ListView):
#     model = Prescription
#     context_object_name = 'prescriptions'
#     template_name = 'presciption-list.html'


# class CreatePrescription(CreateView):
#     model = Prescription
#     context_object_name = 'prescription'
#     success_url = reverse_lazy('prescriptions')
#     template_name = 'base/prescription-form'


# class SymptomsList(ListView):
#     model = Prescription
#     context_object_name = 'symptoms'
#     template_name = 'base/symptoms-list.html'


# class CreateSymptom(CreateView):
#     model = Symptom
#     context_object_name = 'symptom'
#     success_url = reverse_lazy('symptoms')
#     template_name = 'base/symptom-form'


# class DrugsList(ListView):
#     model = Drug
#     context_object_name = 'drugs'
#     template_name = 'base/drugs-list.html'


# class CreateDrug(CreateView):
#     model = Drug
#     context_object_name = 'drug'
#     success_url = reverse_lazy('drugs')
#     template_name = 'base/drug-form'


# class ChronicDiseaseList(ListView):
#     model = ChronicDisease
#     context_object_name = 'chronic_diseases'
#     template_name = 'base/chronic-disease-list.html'


# class CreateChronicDisease(CreateView):
#     model = ChronicDisease
#     context_object_name = 'chronic_disease'
#     success_url = reverse_lazy('chronic-diseases')
#     template_name = 'base/chronic-disease-form'


def edu_covid_stat(request):
    groups = EduCovidStat.objects.all()
    undergra_cnt = 0
    masters_cnt = 0
    doctorate_cnt = 0
    undergra_p = 0
    masters_p = 0
    doctorate_p = 0
    total = 0
    for group in groups:
        if group.level_of_education == "doctorate":
            doctorate_cnt = group.mycount
        if group.level_of_education == "masters":
            masters_cnt = group.mycount
        if group.level_of_education == "undergraduate":
            undergra_cnt = group.mycount

    total = undergra_cnt + masters_cnt + doctorate_cnt
    doctorate_p = (doctorate_cnt * 100) / total
    masters_p = (masters_cnt * 100) / total
    undergra_p = (undergra_cnt * 100) / total

    context = {
        'doctorate_p': doctorate_p,
        'masters_p': masters_p,
        'undergra_p': undergra_p,
        'undergra_cnt': undergra_cnt,
        'masters_cnt': masters_cnt,
        'doctorate_cnt': doctorate_cnt,
        'total': total,
        'levels': EduCovidStat.objects.all()

    }

    return render(request, 'Egitim/egitim-covid-durumu.html', context)


def most_common_diseases(request):
    diseases = MostCommonDisease.objects.all()
    # max_cnt1 = 0
    # max_cnt2 = 0
    # max_cnt3 = 0
    # for group in diseases:
    #     if group.disease_count >= max_cnt1 or (group.disease_count >= max_cnt2):
    #         max_cnt3 = max_cnt2
    #         if group.disease_count >= max_cnt1:
    #             max_cnt2 = max_cnt1
    #             max_cnt1 = group.disease_count
    #         elif group.disease_count >= max_cnt2:
    #             max_cnt2 = group.disease_count
    # selected_d = []
    # for group in diseases:
    #     if group.disease_count == max_cnt1 or group.disease_count == max_cnt2 or group.disease_count == max_cnt3:
    #         selected_d.append(group)
    employees = MostCommonDiseaseEmp.objects.all()

    context = {
        'selected_d': diseases,
        'employees': employees
    }

    return render(request, 'Most/most-common-disease.html', context)


def city_common_diseases(request):
    common_diseases = CityCommonDisease.objects.all()
    city = ''
    city_name = []
    pre_city = ''
    cnt = 0
    selected_d = []
    for disease in common_diseases:
        pre_city = city
        city = disease.city
        if city not in city_name:
            city_name.append(city)
            if pre_city != city:
                for disease in common_diseases:
                    if city == disease.city and cnt < 4:
                        selected_d.append(disease)
                        cnt += 1

            cnt = 0
    context = {
        'selected_d': selected_d,
        'city_common_diseases': CityCommonDisease.objects.all()
    }
    return render(request, 'city_common_diseases.html', context)




def blood_group_covid_stat(request):
    emp_groups = BloodGroupCovidFreq.objects.all()
    context = {
        'emp_groups': emp_groups
    }
    return render(request, 'blood-group-covid-stat.html', context)







def most_common_used_drugs(request):
    context = {
        "most_common_used_drugs": MostCommonlyUsedDrug.objects.all(),
        "most_common_used_drugs_users": MostCommonlyUsedDrugsUser.objects.all()
    }
    return render(request, 'Most/most_common_used_drugs.html', context)


def vac_non_vac_ratio(request):
    vaccinated_cnt = 0
    non_vaccinated_cnt = 0
    total = 0
    covid_emps = Covid.objects.all()
    for emp in covid_emps:
        if(emp.vaccinated == True):
            vaccinated_cnt += 1
        else:
            non_vaccinated_cnt += 1
    total = vaccinated_cnt + non_vaccinated_cnt
    if total != 0:
        vaccinated_per = (vaccinated_cnt/total) * 100
        non_vaccinated_per = (non_vaccinated_cnt/total) * 100
    context = {
        "vaccinated_cnt": vaccinated_cnt,
        "non_vaccinated_cnt": non_vaccinated_cnt,
        "vaccinated_per": vaccinated_per,
        "non_vaccinated_per": non_vaccinated_per,
        "total": total
    }
    return render(request, "vac-vs-non-vac.html", context)





def working_hours_covid_stat(request):
    emp_groups = CovidEmpWorkingHoursStat.objects.all()
    context = {
        'emp_groups': emp_groups
    }
    return render(request, "Work/working-hours-covid-stat.html" , context)


def most_common_covid_symptoms(request):
    symptoms = MostCommonCovidSymptom.objects.all()
    context = {
        'symptoms': symptoms
    }
    return render(request, "Most/most-common-covid-symptoms.html", context)





def most_contacted_persons(request):
    emps = MostContactedPerson.objects.all()
    context = {
        'emps': emps
    }
    return render(request, "Most/most-contacted-persons.html", context)





def biontech_sinovac_comp(request):
    biontech = BiontechCovidEmp.objects.all()
    sinovac = SinovacCovidEmp.objects.all()
    biontech_rate = 0
    biontech_total_time = 0
    biontech_num_of_emps = 0

    sinovac_rate = 0
    sinovac_total_time = 0
    sinovac_num_of_emps = 0

    for emp in biontech:
        if emp.total_time is not None:
            biontech_total_time += emp.total_time
            biontech_num_of_emps += emp.num_of_emps

    for emp in sinovac:
        if emp.total_time is not None:
            sinovac_total_time += emp.total_time
            sinovac_num_of_emps += emp.num_of_emps

    biontech_rate = (biontech_total_time/biontech_num_of_emps)
    sinovac_rate = (sinovac_total_time/sinovac_num_of_emps)

    context = {
        'biontech_rate': biontech_rate,
        'sinovac_rate': sinovac_rate
    }
    return render(request, 'biontech-sinovac-covid-emp.html', context)


def weekends_workers_covid_report(request):
    employees = WeekendsWorker.objects.all()
    covid_emps = WeekendsWorkersCovid.objects.all()

    context = {
        'all_emps': employees,
        'covid_emps': covid_emps
    }

    return render(request, "Work/weekends-workers-covid-report.html", context)


def most_freq_ill_emps_covid(request):
    emps = MostFreqillEmp.objects.all()
    covid_emps = MostFreqillEmpsCovid.objects.all()

    context = {
        'emps': emps,
        'covid_emps': covid_emps
    }
    return render(request, "Most/most-freq-ill-emps-covid.html", context)


def non_vaccinated_emp_dis_pres(request):
    emp = NonVaccinatedEmp.objects.all()
    dis_pres = NonVaccinatedEmpDisPre.objects.all()

    context = {
        'emps': emp,
        'dis_pres': dis_pres,
        'covid_emps': Covid.objects.all()
    }
    return render(request, "non-vac-covid-in-one-year.html", context)





















def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "Login/login.html", {
                "error": "bu kullani adi veya sifresi bulunmamaktadir"
            })
    else:
        return render(request, "Login/login.html")



def logoutUser(request):
    logout(request)
    return redirect("index")
