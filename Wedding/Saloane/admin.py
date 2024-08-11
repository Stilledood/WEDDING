from django.contrib import admin
from .models import BallRoom
from .models import Anunt
from .forms import AnuntForm
from .models import AttributeSalon, AttributeCoafor, AttributeCatering, AttributeFotograf, AttributeValet, \
    AttributeSalonImage
from .forms import AttributeSalonForm, AttributeCoaforForm, AttributeCateringForm, AttributeFotografForm, \
    AttributeValetForm, AttributeSalonImageFormSet

admin.site.register(BallRoom)


class AnuntAdmin(admin.ModelAdmin):
    form = AnuntForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Anunt, AnuntAdmin)


class AttributeSalonImageInline(admin.TabularInline):
    model = AttributeSalonImage
    formset = AttributeSalonImageFormSet
    extra = 1  # Number of forms to show


class AttributeSalonAdmin(admin.ModelAdmin):
    form = AttributeSalonForm
    inlines = [AttributeSalonImageInline]
    list_display = ('id_anunt', 'min_guests', 'max_guests', 'type_events')
    list_filter = ('id_anunt',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set the user_id during the first save.
            obj.user_id = request.user
        super().save_model(request, obj, form, change)


admin.site.register(AttributeSalon, AttributeSalonAdmin)


class AttributeCoaforAdmin(admin.ModelAdmin):
    form = AttributeCoaforForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(AttributeCoafor, AttributeCoaforAdmin)


class AttributeCateringAdmin(admin.ModelAdmin):
    form = AttributeCateringForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(AttributeCatering, AttributeCateringAdmin)


class AttributeFotografAdmin(admin.ModelAdmin):
    form = AttributeFotografForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(AttributeFotograf, AttributeFotografAdmin)


class AttributeValetAdmin(admin.ModelAdmin):
    form = AttributeValetForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(AttributeValet, AttributeValetAdmin)
