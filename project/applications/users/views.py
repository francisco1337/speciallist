from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView,
    UpdateView
)

from django.views.generic.edit import (
    FormView
)

from applications.specialist.models import Meeting

from .forms import (
    ProfileForm,
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    VerificationForm
)
#
from .models import User
# 
from .functions import code_generator


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'
    

    def form_valid(self, form):
        # generamos el codigo
        codigo = code_generator()
        #

        usuario = User.objects.create_user(
            form.cleaned_data['names'].upper(),
            form.cleaned_data['lastnames'].upper(),
            form.cleaned_data['email'].lower(),
            form.cleaned_data['password1'],
            codregistro=codigo
        )
        # # enviar el codigo al email del user
        # asunto = 'Confrimacion de email'
        # mensaje = 'Codigo de verificacion: ' + codigo
        # email_remitente = 'neunapp.cursos@gmail.com'
        # #
        # send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        # redirigir a pantalla de valdiacion

        # return HttpResponseRedirect(
        #     reverse(
        #         'users_app:user-verification',
        #         kwargs={'pk': usuario.id}
        #     )
        # )

        return HttpResponseRedirect(
            reverse('users_app:user-login')
        )



class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        

        user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        #
        User.objects.filter(
            id=self.kwargs['pk']
        ).update(
            is_active=True
        )
        return super(CodeVerificationView, self).form_valid(form)

class ProfileView(UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users_app:user-profile')
    model = User

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["citas"] = Meeting.objects.filter(user=self.request.user).order_by("-date","-time")

        # for cita in context["citas"]:
        #     print(cita.__dict__.keys())
        return context

    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        print("Objecto")

        return self.request.user

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


