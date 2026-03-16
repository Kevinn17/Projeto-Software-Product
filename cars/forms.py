from django import forms 
from cars.models import Marca, Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor < 20000:
            self.add_error('valor','Valor mínimo permitido: R$20.000')
        return valor 
    
    def clean_fabricado_em(self):
        fabricado_em = self.cleaned_data.get('fabricado_em')
        if fabricado_em < 2000:
            self.add_error('fabricado_em', 'Ano mínimo permitido: 2000')
        return fabricado_em
