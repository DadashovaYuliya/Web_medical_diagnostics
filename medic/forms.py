from django.forms import BooleanField, DateTimeInput, ModelForm

from medic.models import Appointment


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class AppointmentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Appointment
        fields = ["service", "date_time"]
        widgets = {
            "date_time": DateTimeInput(attrs={"type": "datetime-local"}),
        }
