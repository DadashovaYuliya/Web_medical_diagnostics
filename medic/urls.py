from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from medic.apps import MedicConfig
from medic.views import (AboutPageView, AppointmentCreateView, ContactsTemplateView, HomePageView, ServiceDetailView,
                         ServiceListView, view_results)

app_name = MedicConfig.name


urlpatterns = [
    path("services/", ServiceListView.as_view(), name="services_list"),
    path("services/<int:pk>/", ServiceDetailView.as_view(), name="services_detail"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("", HomePageView.as_view(), name="main"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("appointments/", AppointmentCreateView.as_view(), name="appointments"),
    path("results/", view_results, name="view_results"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
