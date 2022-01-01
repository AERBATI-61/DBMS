from django.contrib import admin
from django import urls
from django.urls import path
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", base, name="index"),

    path('employee/', EmployeeList.as_view(), name="employee-list"),
    path("create-employee/", CreateEmployee.as_view(), name="create-employee"),
    path("employee-update/<str:pk>/", UpdateEmployee.as_view(), name="update-employee"),
    path("employee-delete/<str:pk>/", DeleteEmployee.as_view(), name="delete-employee"),

    path("disease-list", DiseaseList.as_view(), name="disease-list"),
    path("disease-create", CreateDisease.as_view(), name="disease-create"),
    path("diseases/<str:pk>/", UpdateDisease.as_view(), name="desease-update"),
    path("disease-delete/<str:pk>/", DeleteDisease.as_view(), name="disease-delete"),

    path("covid-list", CovidList.as_view(), name="covid-list"),
    path("covid-create", CreateCovid.as_view(), name="covid-create"),
    path("covid-update/<int:pk>/", UpdateCovid.as_view(), name="covid-update"),
    path("covid-delete/<int:pk>/", DeleteCovid.as_view(), name="covid-delete"),

    path("timetable-list", TimeTableList.as_view(), name="timetable-list"),
    path("timetable-create", CreateTimeTable.as_view(), name="timetable-create"),
    path("timetime-update/<int:pk>/", UpdateTimeTable.as_view(), name="timetime-update"),
    path("timetable-delete/<int:pk>/", DeleteTimeTable.as_view(), name="timetable-delete"),

    path('egitim-covid-durumu/', edu_covid_stat, name="egitim-covid-durumu"),

    path('most-common-disease/', most_common_diseases, name="most-common-disease"),
    path('most-common-used-drugs/', most_common_used_drugs, name="most-common-used-drugs"),
    path("most-common-covid-symptoms/", most_common_covid_symptoms, name="most-common-covid-symptoms"),
    path("most-contacted-persons/", most_contacted_persons, name="most-contacted-persons"),
    path("most-freq-ill-emps-covid/", most_freq_ill_emps_covid, name="most-freq-ill-emps-covid"),

    path('city-common-disease/', city_common_diseases, name="city-common-disease"),
    path("blood-group-covid-stat/", blood_group_covid_stat, name="blood-group-covid-stat"),
    path("working-hours-covid-stat/", working_hours_covid_stat, name="working-hours-covid-stat"),

    path("weekends-workers-covid-report/", weekends_workers_covid_report, name="weekends-workers-covid-report"),


    path("vac-vs-non-vac/", vac_non_vac_ratio, name="vac-vs-non-vac"),
    path("non-vaccinated-covid-in-one-year/", non_vaccinated_emp_dis_pres, name="non-vaccinated-emp-dis-pres"),



    path("biontech-vs-sinovac/", biontech_sinovac_comp, name="biontech-vs-sinovac"),
    path("loginUser/", loginUser, name="loginUser"),
    path("logoutUser/", logoutUser, name="logoutUser"),










]
