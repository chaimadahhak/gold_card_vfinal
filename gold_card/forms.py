from django import forms

class ImageProcessingForm(forms.Form):
    image = forms.ImageField()
    extracted_text = forms.CharField(widget=forms.Textarea, required=False)
