from django import forms
from django_select2 import forms as select2forms

from .models import RegistroPagosModel, RegistroCreditos, EstatusCredito, RegistroPagosModelManual
from applications.dashboard.models import SimuladorPrueba
from applications.users.models import RegistroCreditosModel


class NumeroContratoSelect2Widget(select2forms.Select2Widget):
    def label_from_instance(self, obj):
        return obj.numero_contrato


class RegistroPagosForm(forms.ModelForm):

    simulador = forms.CharField(
        required=True,
        label='Numero de contrato:',
        widget=forms.TextInput(
            attrs={
                'id': 'id_simulador',
                'class': 'form-control mb-2',
                'placeholder': 'Ingrese el número de contrato',
            }
        ),




    )

    monto_pagado = forms.DecimalField(

        label='Monto a pagar: ',
        required=False,
        widget=forms.widgets.NumberInput(
            attrs={
                'id': 'id_monto_total_registro',
                'class': 'form-control mb-2',
                'placeholder': 'ingrese la cantidad...',

            }
        )
    )

    comprobante_pago = forms.FileField(
        label="Comprobante de Pago: ",
        required=False,
        widget=forms.ClearableFileInput(
            attrs={

                'class': 'form-control mb-2',
                'placeholder': 'ingresa el archivo...',
                'type': 'file',

            }
        ),

    )

    class Meta:
        model = RegistroPagosModel
        fields = ['simulador', 'monto_pagado', 'comprobante_pago']

    # def clean_simulador_manual(self):
    #     data = self.cleaned_data['simulador']
    #     try:
    #         # Busca un simulador con el número de contrato ingresado manualmente
    #         simulador = SimuladorPrueba.objects.get(numero_contrato=data)
    #     except SimuladorPrueba.DoesNotExist:
    #         raise forms.ValidationError(
    #             "El número de contrato ingresado no es válido.")
    #     return simulador

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.simulador = self.cleaned_data['simulador']
    #     if commit:
    #         instance.save()
    #     return instance


class RegistroPagosFormManual(forms.ModelForm):

    simulador = forms.ModelChoiceField(
        queryset=RegistroCreditosModel.objects.all(),
        label='Numero de contrato:',
        empty_label='Seleccionar',
        widget=NumeroContratoSelect2Widget(
            attrs={
                'id': 'id_simulador',
                'class': 'form-control mb-2'
            }
        )


    )

    monto_pagado = forms.DecimalField(

        label='Monto a pagar: ',
        required=False,
        widget=forms.widgets.NumberInput(
            attrs={
                'id': 'id_monto_total_registro',
                'class': 'form-control mb-2',
                'placeholder': 'ingrese la cantidad...',

            }
        )
    )

    comprobante_pago = forms.FileField(
        label="Comprobante de Pago: ",
        required=False,
        widget=forms.ClearableFileInput(
            attrs={

                'class': 'form-control mb-2',
                'placeholder': 'ingresa el archivo...',
                'type': 'file',

            }
        ),

    )

    class Meta:
        model = RegistroPagosModelManual
        fields = ['simulador', 'monto_pagado', 'comprobante_pago']
