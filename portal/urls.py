from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListScholarships.as_view(), name='list_schloarships'),
    path('profileupdate', views.UpdateProfile.as_view(), name='profile_update'),
    path('organisation', views.ShowOrganistionSchloarship.as_view(),
         name='organisation_home'),
    path('editorganisation', views.EditOrganisation.as_view(),
         name='edit_organisation'),
    path('newscholarship', views.NewScholarship.as_view(), name='new_schloarship'),
    path('deletescholarship/<int:sid>/',
         views.DeleteScholarship.as_view(), name='delete_schloarship'),
]
