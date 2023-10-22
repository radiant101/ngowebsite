from django import forms
from home.models import Report

class TextReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['text', 'location', 'ngo']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'ngo': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(TextReportForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Report Text'
        self.fields['location'].label = 'Location'
        self.fields['ngo'].label = 'Select NGO'
        

class ImageReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['image', 'location', 'ngo']
        widgets = {
            'image': forms.ClearableFileInput(),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'ngo': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(ImageReportForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = 'Upload Image'
        self.fields['location'].label = 'Location'
        self.fields['ngo'].label = 'Select NGO'