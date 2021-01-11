from django import forms


class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name')
    last_name = forms.CharField()
    email = forms.EmailField(help_text="Please enter your email!", )
    address = forms.CharField(required= False, )
    Technology = forms.CharField(initial= "Django", disabled= True, )
    age = forms.IntegerField()
    password = forms.CharField(widget= forms.PasswordInput)
    re_password = forms.CharField(help_text= "Re-enter your password", widget= forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError("password is too short!")
        return password
