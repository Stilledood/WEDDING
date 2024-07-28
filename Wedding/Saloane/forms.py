from django import forms
from .models import Anunt
from .models import AttributeSalon


class AnuntForm(forms.ModelForm):
    class Meta:
        model = Anunt
        fields = '__all__'  # Or list specific fields


class AttributeSalonForm(forms.ModelForm):
    type_events = forms.MultipleChoiceField(
        choices=[
            ('NUNTA', 'Nunta'),
            ('BOTEZ', 'Botez'),
            ('CORPORATE', 'Corporate'),
            ('ALTELE', 'Altele')
        ],
        widget=forms.CheckboxSelectMultiple,
    )

    facilities = forms.MultipleChoiceField(
        choices=[
                ('Aer Conditionat', 'Aer Conditionat'),
                ('Sistem de sonorizare', 'Sistem de sonorizare'),
                ('Lumini arhitecturale', 'Lumini arhitecturale'),
                ('Iluminat profesional', 'Iluminat profesional'),
                ('Ring de dans', 'Ring de dans'),
                ('Scenă pentru formație/muzicieni', 'Scenă pentru formație/muzicieni'),
                ('Decoratiuni incluse', 'Decoratiuni incluse'),
                ('Baie Separata', 'Baie Separata'),
                ('Prezidiu', 'Prezidiu'),
                ('Decor mese', 'Decor mese'),
                ('Wifi', 'Wifi'),
                ('Decor scaune', 'Decor scaune'),
                ('Meniuri pentru meese', 'Meniuri pentru mese'),
                ('Vedere panoramica', 'Vedere panoramica'),
                ('Proximitea centrului orasului', 'Proximitatea centrului orasului'),
                ('Foto corner', 'Foto corner'),
                ('Casuta de dar', 'Casuta de dar'),
                ('Locatie pe lac', 'Locatie pe lac'),
                ('Vedere la lac', 'Vedere la lac'),
                ('Locatie in padure', 'Locatie in padure'),
                ('Event planner', 'Event planner'),
                ('Stativ cu lista invitatilor', 'Stativ cu lista invitatilor'),
                ('Numere pentru mese', 'Numere pentru mese'),
                ('Loc de relaxare', 'Loc de relaxare '),
        ],
        widget=forms.CheckboxSelectMultiple,
    )

    catering = forms.MultipleChoiceField(
        choices=[
            ('Bucatarie proprie', 'Bucatarie proprie'),
            ('Servicii de catering incluse sau opționale', 'Servicii de catering incluse sau opționale'),
            ('Meniuri speciale', 'Meniuri speciale'),
            ('Degustare meniu', 'Degustare meniu'),
            ('Serviciul ospatarilor gratuit', 'Serviciul ospatarilor gratuit'),
            ('Candy Bar', 'Candy Bar'),
            ('Shot Bar', 'Shot Bar'),
            ('Fruit Bar', 'Fruit Bar'),
            ('Cocktail Bar', 'Cocktail Bar'),
            ('Obiceiuri', 'Obiceiuri'),
            ('Open bar', 'Open bar'),
            ('All inclusive', 'All inclusive'),
            ('Cofetarie/Patiserie', 'Cofetarie/Patiserie ')
        ],
        widget=forms.CheckboxSelectMultiple,
    )


    zona_exterior = forms.MultipleChoiceField(
        choices=[
            ('Loc pentru fumat', 'Loc pentru fumat'),
            ('Terasa acoperita', 'Terasa acoperita'),
            ('Terasa descoperita', 'Terasa descoperita'),
            ('Piscina', 'Piscina'),
            ('Foisor evenimente', 'Foisor evenimente'),
            ('Zona foto', 'Zona foto'),
            ('Fantana arteziana', 'Fantana arteziana'),
            ('Loc de joaca', 'Loc de joaca'),
            ('Gradina amenajata pentru cereemonie', 'Gradina amenajata pentru ceremonie')
        ],
        widget=forms.CheckboxSelectMultiple,
    )

    parking = forms.MultipleChoiceField(
        choices=[
            ('Parcare gratuita', 'Parcare gratuita'),
            ('Parcare platita', 'Parcare platita'),
            ('Supreaveghere video', 'Supraveghere video'),
            ('Parcare iluminata', 'Parcare iluminata')
        ],
        widget=forms.CheckboxSelectMultiple,
    )

    saftey = forms.MultipleChoiceField(
        choices=[
            ('Alarma incendiu', 'Alarma incendiu'),
            ('Detectoare de fum', 'Detectoare de fum'),
            ('Acces ambulanta', 'Acces ambulanta'),
            ('Supreaveghere video', 'Supraveghere video'),
            ('Extinctoare', 'Extinctoare'),
            ('Serviciu de paza', 'Serviciu de paza'),
            ('Kit de prim ajutor', 'Kit de prim ajutor')
        ],
        widget=forms.CheckboxSelectMultiple,
    )


def clean(self):
    cleaned_data = super().clean()
    for field in ['type_events', 'facilities', 'catering', 'zona_exterior', 'parking', 'saftey']:
        cleaned_data[field] = ','.join(cleaned_data.get(field, []))
    return cleaned_data


class Meta:
    model = AttributeSalon
    fields = '__all__'