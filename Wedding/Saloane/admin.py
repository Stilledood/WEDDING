from django.contrib import admin
from .models import BallRoom
from .models import Anunt
from .forms import AnuntForm
from .models import AttributeSalon
from .forms import AttributeSalonForm

admin.site.register(BallRoom)


class AnuntAdmin(admin.ModelAdmin):
    form = AnuntForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Anunt, AnuntAdmin)


class AttributeSalonAdmin(admin.ModelAdmin):
    form = AttributeSalonForm

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set the user_id during the first save.
            obj.user_id = request.user
        super().save_model(request, obj, form, change)

admin.site.register(AttributeSalon, AttributeSalonAdmin)
