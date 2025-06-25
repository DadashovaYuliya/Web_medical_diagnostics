from django.contrib import admin

from medic.models import Appointment, DiagnosticResult, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = (
        "name",
        "description",
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "patient",
        "service",
        "date_time",
    )
    list_filter = ("date_time",)
    search_fields = ("service",)


@admin.register(DiagnosticResult)
class DiagnosticResultAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "appointment",
        "result",
        "result_date",
    )
    list_filter = ("result_date",)
    search_fields = ("appointment",)
