from django.forms import ModelForm, DateField, DateInput
from .models import CustomUser


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['birthday'] = DateField(
            label='birthday',
        )

    class Meta:
        verbose_name = 'User'
        model = CustomUser
        fields = (
            'username',
            'birthday',
            'random_number'
        )
        widgets = {'birthday': DateInput(attrs={'class': 'datepicker'})}

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
