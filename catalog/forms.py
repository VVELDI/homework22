# catalog/forms.py
from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')
        all_text = f"{name} {description}".lower()

        for word in FORBIDDEN_WORDS:
            if word in all_text:
                raise forms.ValidationError(f"Использование слова «{word}» запрещено.")
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price
