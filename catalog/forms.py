from django import forms
from .models import Product, Category


FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise forms.ValidationError(f"Слово «{word}» запрещено в названии.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise forms.ValidationError(f"Слово «{word}» запрещено в описании.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price
