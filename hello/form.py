from django import forms
from .models import Friend,Message
from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    age = forms.IntegerField(label='Age')

# class CheckForm(forms.Form):
#     check = forms.BooleanField(label='Check',required=False)

# class checkForms(forms.Form):
#     check = forms.NullBooleanField(label='Check')

class CheckForm(forms.Form):
    data = [
        ('one','item 1'),
        ('two','item 2'),
        ('three','item 3'),
    ]
    choice = forms.MultipleChoiceField(label='radio',choices=data,widget=forms.SelectMultiple(attrs={'size':3}))

class HelloForm(forms.Form):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label='gender',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    age = forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateField(label='birthday',widget=forms.DateInput(attrs={'class':'form-control'}))

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','age','birthday']

class FindForm(forms.Form):
    find = forms.CharField(label='Find',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

class CheckForm(forms.Form):
    str = forms.CharField(label='strings',widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower() != 'yes'):
            raise forms.ValidationError('You must input "yes".')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['friend','title','content']
        widgets = {
            'friend':forms.Select(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),
        }