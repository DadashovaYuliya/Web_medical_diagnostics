from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView

from medic.forms import AppointmentForm
from medic.models import Appointment, Service


class HomePageView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"

    def post(self, request, *args, **kwargs):

        if self.request.method == "POST":
            name = self.request.POST.get("name")
            phone = self.request.POST.get("phone")
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено. Ответ будет направлен по номеру: {phone}.")
        return render(request, "contacts.html")


class ServiceListView(ListView):
    model = Service
    template_name = "services_list.html"
    context_object_name = "services"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "services_detail.html"
    context_object_name = "service"


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "appointments.html"
    success_url = reverse_lazy("medic:view_results")

    def form_valid(self, form):
        form.instance.patient = self.request.user
        return super().form_valid(form)


def view_results(request):
    user = request.user
    appointments = user.appointments.all().order_by("-date_time")
    appointments_with_results = request.user.appointments.filter(result__isnull=False).select_related("result")
    return render(
        request,
        "view_results.html",
        {
            "appointments_with_results": appointments_with_results,
            "appointments": appointments,
        },
    )
