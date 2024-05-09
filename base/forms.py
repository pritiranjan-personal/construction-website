from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'message']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        #     'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Message'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs = {'class': 'form-control', 'placeholder': 'Name'}
        self.fields["email"].widget.attrs = {'class': 'form-control', 'placeholder': 'Email'}
        self.fields["phone"].widget.attrs = {'class': 'form-control', 'placeholder': 'Phone'}
        self.fields["message"].widget.attrs = {'class': 'form-control', 'rows': 10, 'placeholder': 'Message'}

    


