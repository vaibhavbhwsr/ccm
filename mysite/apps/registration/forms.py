from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registration.models import UserInfo


class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(widget=forms.RadioSelect, choices=UserInfo.USER_TYPE)

    class Meta:
        model = User
        fields = ['user_type', 'username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email', 'password2': 'Confirm Password'}

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user_info = UserInfo.objects.create(user=user, user_type=self.cleaned_data.get('user_type'))
        user_info.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    image = forms.ImageField()
    phone_num = forms.CharField()
    billing_rate = forms.IntegerField()
    speciality = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'image', 'phone_num',
            'billing_rate', 'speciality'
        ]

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.user_info.image = self.cleaned_data.get('image')
        user.user_info.phone_num = self.cleaned_data.get('phone_num')
        user.user_info.billing_rate = self.cleaned_data.get('billing_rate')
        user.user_info.speciality = self.cleaned_data.get('speciality')
        user.user_info.save()
        return user
