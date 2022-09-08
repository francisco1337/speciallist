from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class':'controled'
            }
        )
    )
    password2 = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class':'controled'
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'names',
            'lastnames',
            'email',
        )

        labels = {
            'names': '',
            'lastnames':'',
            'email':'',
        }

        widgets = { 
            'names':forms.TextInput(
                    attrs={
                        'placeholder' : 'Nombres',
                        'class':'controled'
                    }
                ),
            'lastnames':forms.TextInput(
                    attrs={
                        'placeholder' : 'Apellidos',
                        'class':'controled'
                    }
                ),
            'email':forms.TextInput(
                    attrs={
                        'placeholder' : 'Correo Electronico',
                        'class':'controled'
                    }
                ),
        }
        # help_texts = {
        #     'names': 'Some useful help text.',
        # }
        # error_messages = {
        #     'names': {
        #         'max_length': "This writer's name is too long.",
        #     },
        # }
        
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')
            self.add_error('password1', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Correo Electronico',
                'class':'controled'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña',
                'class':'controled'
            }
        )
    )

    def clean(self):
        print(1)
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        print(email, password)

        if not authenticate(username=email, password=password):
            raise forms.ValidationError({'email':'Correo o Contraseña incorrectos'})
        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )


class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)


    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']

        if len(codigo) == 6:
            # verificamos si el codigo y el id de usuario son validos:
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('el codigo es incorrecto')
        else:
            raise forms.ValidationError('el codigo es incorrecto')


class ProfileForm(forms.ModelForm):
    
    class  Meta:
        model = User
        fields = ('__all__')
        exclude = (
            'password',
            'last_login',
            'is_active',
            'is_staff',
            'codregistro',
            'facebook',
            'google',
            'is_superuser',
            'groups',
            'user_permissions'
        )


