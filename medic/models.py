from django.db import models

from users.models import User


class Service(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="medic/image", verbose_name="Изображение", blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пациент", related_name="appointments")
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name="Услуга", related_name="services")
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.email} - {self.service.name} at {self.date_time}"


class DiagnosticResult(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="result")
    result = models.TextField()
    result_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Результат для: {self.appointment}"
