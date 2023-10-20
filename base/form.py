from django.forms import ModelForm
from .models import room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
