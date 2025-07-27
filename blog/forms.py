from django import forms
from .models import Blog

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'preview', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

    def clean(self):
        cleaned_data = super().clean()
        text = f"{cleaned_data.get('title', '')} {cleaned_data.get('content', '')}".lower()
        for word in FORBIDDEN_WORDS:
            if word in text:
                raise forms.ValidationError(f"Запрещено использовать слово «{word}» в заголовке или содержании.")
        return cleaned_data
