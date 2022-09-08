#
from django.urls import path

from . import views

app_name = "specialist_app"

urlpatterns = [
    path(
        'search/', 
        views.SearchSpecialistView.as_view(),
        name='search_specialist',
    ),
    path(
        'search/results/', 
        views.SearchSpecialistResultsView.as_view(),
        name='search_specialist_results',
    ),
    path(
        '<slug>/', 
        views.SpecialistInfo.as_view(),
        name='info_specialist',
    ),
    path(
        '<slug>/edit/', 
        views.SpecialistInfoEdit.as_view(),
        name='info_specialist_edit',
    ),
    path(
        '<slug>/meeting/', 
        views.SpecialistMeeting.as_view(),
        name='specialist_meeting',
    ),
    path(
        'clinic/<pk>/', 
        views.ClinicInfo.as_view(),
        name='specialist_clinic',
    ),
    path(
        'clinic/<pk>/edit/', 
        views.ClinicInfoEdit.as_view(),
        name='specialist_clinic_edit',
    ),
    # path(
    #     'clinic/<pk>/edit/schedule/', 
    #     views.clinic_schedule,
    #     name='specialist_clinic_edit_clinic_schedule',
    # ),
    path(
        'specialist/register/', 
        views.SpecialistRegister,
        name='specialist_register',
    ),
    path(
        'user/<user>/dates',
        views.Dates.as_view(),
        name="user_dates"
    ),
    path(
        'specialist/dates',
        views.SpecialistDates.as_view(),
        name="specialist_dates"
    )
]