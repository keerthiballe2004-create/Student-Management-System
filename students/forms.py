
from django import forms
from django.core.validators import RegexValidator
from .models import Student


class StudentForm(forms.ModelForm):

    phone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message='Enter a valid 10-digit Indian mobile number.'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter phone number'
        })
    )

    email = forms.EmailField(
        error_messages={
            'invalid': 'Please enter a valid email address.'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email address'
        })
    )

    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name'
            }),

            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course'
            }),

            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address',
                'rows': 3
            }),

            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

            'certificate': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
