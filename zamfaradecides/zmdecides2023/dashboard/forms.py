from django import forms

from .models import User, Agent

class UserForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    widget = {
        'password': forms.PasswordInput(),
    }
    
    def clean_email(self, *args, **kwargs):
        formUser = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if User.objects.filter(username=formUser).exists():
                raise forms.ValidationError(
                    "The given email is already registered")
        else:  # Update
            dbUser = self.Meta.model.objects.get(
                id=self.instance.pk).username.lower()
            if dbUser != formUser:  # There has been changes
                if User.objects.filter(username=formUser).exists():
                    raise forms.ValidationError(
                        "The given email is already registered")
        return formUser

    def clean_password(self):
        FormPassword = self.cleaned_data.get("password", None)
        if self.instance.pk is not None:
            if not FormPassword:
                # return None
                return self.instance.password

        return FormPassword
    
    
    class Meta:
        model = User
        fields = '__all__'
        

class AgentForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    widget = {
        'password': forms.PasswordInput(),
    }
    
    def clean_email(self, *args, **kwargs):
        formUser = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if User.objects.filter(username=formUser).exists():
                raise forms.ValidationError(
                    "The given email is already registered")
        else:  # Update
            dbUser = self.Meta.model.objects.get(
                id=self.instance.pk).username.lower()
            if dbUser != formUser:  # There has been changes
                if User.objects.filter(username=formUser).exists():
                    raise forms.ValidationError(
                        "The given email is already registered")
        return formUser

    def clean_password(self):
        FormPassword = self.cleaned_data.get("password", None)
        if self.instance.pk is not None:
            if not FormPassword:
                # return None
                return self.instance.password

        return FormPassword
    
    
    class Meta:
        model = Agent
        fields = ['username', 'passwords']
