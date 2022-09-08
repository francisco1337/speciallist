from datetime import datetime

from django.db.models.query import QuerySet
from django.forms import BaseForm, ModelChoiceField
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView,FormView, ListView, UpdateView
from django.http.response import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage

from applications.specialist.forms import ClinicForm, MeetForm, SpecialistCreateForm, SpecialistInfoForm


from applications.specialist.models import Clinic, Meeting, Meeting_topic, Schedule, Specialism, Specialist
from applications.users.models import Country, State

# Create your views here.

class SearchSpecialistView(TemplateView):
    template_name = "specialist/search.html"
    
    def get_context_data(self, **kwargs):
        context = super(SearchSpecialistView, self).get_context_data(**kwargs)
        context["specialisms"] = Specialism.objects.all()
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        city = request.POST.get("city")
        specialism = request.POST.get("specialism")
        url = reverse("specialist_app:search_specialist_results")+f"?city={city}&specialism={specialism}"
        print(url)

        return HttpResponseRedirect(url)

class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


class SearchSpecialistResultsView(ListView):
    template_name = "specialist/search_results.html"
    model = Clinic
    context_object_name = "Clinics"  
    paginate_by = 5 
    paginator_class = MyPaginator   



    def get_context_data(self, **kwargs):
        city = self.request.GET.get("city")
        specialism = self.request.GET.get("specialism")

        # FILTRO DEL ESTADO Y LAS CLINICAS CON ESTE ESTADO EN EL PAIS
        country = Country.objects.filter(country="México")
        print('country: ',country)
        country_id = country.values()[0].get("id") if(country.values()) else None
        print('country_id: ',country_id)
        state = State.objects.filter(country_id=country_id,state=city )
        print('state: ',state)
        #FILTRO DE LOS ESPECIALISTAS CON LA ESPECIALIDAD SELECCIONADA
        specialism = Specialism.objects.filter(specialism=specialism)
        print('specialism: ',specialism)
        specialism_id = specialism.values()[0].get("id")
        print('specialism_id: ',specialism_id)
        specialist = Specialist.objects.filter(specialism=specialism_id)
        print('specialist: ',specialist)
        clinics = Clinic.objects.filter(specialist__in = specialist, state__in = state)#, country__in = country #country_id__in=country,state_id__in=state, specialist_id__in = specialist
        print(f"Clinic.objects.filter(country_id__in={country},state_id__in={state}, specialist_id__in = {specialist})")
        print('clinics: ',clinics)
        # clinics = Clinic.objects.all()
        # print("-------------------------------------------------------")
        # print(clinics)


        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        
        paginator = self.paginator_class(clinics, self.paginate_by)
        
        clinics = paginator.page(page)
        
        context['Clinics'] = clinics
        
       

        return context


# # CORREGIR EL METODO
    # def get_context_object_name(self, object_list):
    #     city = self.request.GET.get("city")
    #     specialism = self.request.GET.get("specialism")

    #     # FILTRO DEL ESTADO Y LAS CLINICAS CON ESTE ESTADO EN EL PAIS
    #     country = Country.objects.filter(country="México")
    #     country_id = country.values()[0].get("id") if(country.values()) else None
    #     state = State.objects.filter(country_id=country_id,state=city )

    #     #FILTRO DE LOS ESPECIALISTAS CON LA ESPECIALIDAD SELECCIONADA
    #     specialism = Specialism.objects.filter(specialism=specialism)
    #     specialism_id = specialism.values()[0].get("id")
    #     specialist = Specialist.objects.filter(specialism=specialism_id)

    #     # """Get the name of the item to be used in the context."""
    #     clinicas = Clinic.objects.filter(country_id__in=country,state_id__in=state, specialist_id__in = specialist).select_related()
    #     self.get_queryset=clinicas
        
    #     if self.context_object_name:
    #         return self.context_object_name
    #     elif hasattr(object_list, 'model'):
    #         return '%s_list' % object_list.model._meta.model_name
    #     else:
    #         return None
    
    # def paginate_queryset(self, queryset, page_size):
    #     """Paginate the queryset, if needed."""
    #     paginator = self.get_paginator(
    #         queryset, page_size, orphans=self.get_paginate_orphans(),
    #         allow_empty_first_page=self.get_allow_empty())
    #     page_kwarg = self.page_kwarg
    #     page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
    #     try:
    #         page_number = int(page)
    #     except ValueError:
    #         if page == 'last':
    #             page_number = paginator.num_pages
    #         else:
    #             raise Http404(_('Page is not “last”, nor can it be converted to an int.'))
    #     try:
    #         page = paginator.page(page_number)
    #         return (paginator, page, page.object_list, page.has_other_pages())
    #     except InvalidPage as e:
    #         raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
    #             'page_number': page_number,
    #             'message': str(e)
    #         })

class SpecialistInfo(DetailView):

    template_name = "specialist/info.html"
    model = Specialist

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})
        print("---------------------------")
        print(obj)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        specialist = context.get('object')
        context['clinics'] = Clinic.objects.filter(specialist = specialist)
        print(context['clinics'])
        

        return context


class SpecialistInfoEdit(UpdateView):

    template_name = "specialist/info_edit.html"
    form_class = SpecialistInfoForm
    model = Specialist

    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        specialist_profile = super().get_object()
        

        if request.user != specialist_profile.user:
            return HttpResponseRedirect(reverse('specialist_app:search_specialist'))

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        print("get_object")
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})

        print(type(obj))
        return obj

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        specialist = Specialist.objects.filter(user=self.request.user).values()[0].get('slug')
        print(specialist)
        return reverse('specialist_app:info_specialist', kwargs={'slug': specialist}) 

   
  

class SpecialistMeeting(FormView):
    template_name = "specialist/meet.html"
    form_class = MeetForm
    success_url = '.'

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            print("-------------------------")
            slug = self.kwargs.get("slug")
            specialist = Specialist.objects.filter(slug=slug)[0]
            
            clinics:dict = Clinic.objects.filter(specialist=specialist).values('id','clinic')
            print(clinics)
            clinic_choices =[]
            for clinic in clinics:
                clinic_choices.append(((clinic.get('id')),(clinic.get('clinic'))))
            clinic_choices = tuple(clinic_choices)

            topics:dict = Meeting_topic.objects.filter(specialist=specialist).values('id','topic')
            print(topics)
            topic_choices =[]
            for topic in topics:
                topic_choices.append(((topic.get('id')),(topic.get('topic'))))
            topic_choices = tuple(topic_choices)

            form_class = self.get_form_class()
            form_class.base_fields["clinic"].choices = clinic_choices
            form_class.base_fields["topic"].choices = topic_choices

            
        return form_class(**self.get_form_kwargs())

    def get_form_kwargs(self):
        kwargs = super(SpecialistMeeting, self).get_form_kwargs()
        kwargs.update({
            'slug': self.kwargs['slug'],
        })
        choices = (('1','1'),('2','2'))
        kwargs['initial']={'clinic': choices }
        print("----------------ANALISISS")
        print(kwargs)
        return kwargs

    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user

    def form_valid(self, form):
        
        
        # Next, try looking up by primary key.
        slug = self.kwargs.get('slug')  
        
        try:
            # Get the single item from the filtered queryset
            obj:Specialist = Specialist.objects.filter(slug=slug)[0]
            print(obj)
        except Exception as e:
            raise Http404(("No %(verbose_name)s found matching the query") %
                        {'verbose_name': str(e)})

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        print(obj)
        self.object.specialist = obj

        self.object.save()
        # self.get_success_url()
        return HttpResponseRedirect(reverse("specialist_app:user_dates", kwargs={"user":self.object.user}))


class ClinicInfo(DetailView):

    template_name = "specialist/clinic.html"
    model = Clinic

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        print(context.keys())


        format = '%Y-%m-%d %H:%M %p'
        format24 = '%H:%M'
        format12 = '%I:%M %p'


        clinic=self.kwargs.get("pk")
        specialist = Specialist.objects.filter(user=self.request.user).first()
        print(specialist)
        print(clinic)
        schedule = Schedule.objects.filter(specialist=specialist, clinic=clinic).first()
        timetemp = datetime.strftime( datetime.strptime(schedule.lunes.get('monday_start'), format24), format12)
        print(timetemp)
        schedule.lunes["monday_start"] = datetime.strftime( datetime.strptime(schedule.lunes.get('monday_start'), format24), format12)
        schedule.lunes["monday_end"] = datetime.strftime( datetime.strptime(schedule.lunes.get('monday_end'), format24), format12)
        schedule.martes["tuesday_start"] = datetime.strftime( datetime.strptime(schedule.martes.get('tuesday_start'), format24), format12)
        schedule.martes["tuesday_end"] = datetime.strftime( datetime.strptime(schedule.martes.get('tuesday_end'), format24), format12)
        schedule.miercoles["wednesday_start"] = datetime.strftime( datetime.strptime(schedule.miercoles.get('wednesday_start'), format24), format12)
        schedule.miercoles["wednesday_end"] = datetime.strftime( datetime.strptime(schedule.miercoles.get('wednesday_end'), format24), format12)
        schedule.jueves["thursday_start"] = datetime.strftime( datetime.strptime(schedule.jueves.get('thursday_start'), format24), format12)
        schedule.jueves["thursday_end"] = datetime.strftime( datetime.strptime(schedule.jueves.get('thursday_end'), format24), format12)
        schedule.viernes["friday_start"] = datetime.strftime( datetime.strptime(schedule.viernes.get('friday_start'), format24), format12)
        schedule.viernes["friday_end"] = datetime.strftime( datetime.strptime(schedule.viernes.get('friday_end'), format24), format12)
        schedule.sabado["saturday_start"] = datetime.strftime( datetime.strptime(schedule.sabado.get('saturday_start'), format24), format12)
        schedule.sabado["saturday_end"] = datetime.strftime( datetime.strptime(schedule.sabado.get('saturday_end'), format24), format12)
        schedule.domingo["sunday_start"] = datetime.strftime( datetime.strptime(schedule.domingo.get('sunday_start'), format24), format12)
        schedule.domingo["sunday_end"] = datetime.strftime( datetime.strptime(schedule.domingo.get('sunday_end'), format24), format12)

        print(schedule.lunes)
        context["schedule"]= schedule

        return context

    # def get_object(self, queryset=None):
    #     """
    #     Return the object the view is displaying.
    #     Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
    #     Subclasses can override this to return any object.
    #     """
    #     # Use a custom queryset if provided; this is required for subclasses
    #     # like DateDetailView
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #     # Next, try looking up by primary key.
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     slug = self.kwargs.get(self.slug_url_kwarg)
    #     if pk is not None:
    #         queryset = queryset.filter(pk=pk)
    #     # Next, try looking up by slug.
    #     if slug is not None and (pk is None or self.query_pk_and_slug):
    #         slug_field = self.get_slug_field()
    #         queryset = queryset.filter(**{slug_field: slug})
    #     # If none of those are defined, it's an error.
    #     if pk is None and slug is None:
    #         raise AttributeError(
    #             "Generic detail view %s must be called with either an object "
    #             "pk or a slug in the URLconf." % self.__class__.__name__
    #         )
    #     try:
    #         # Get the single item from the filtered queryset
    #         obj = queryset.get()
    #     except queryset.model.DoesNotExist:
    #         raise Http404(_("No %(verbose_name)s found matching the query") %
    #                     {'verbose_name': queryset.model._meta.verbose_name})

    #     print(type(obj))
    #     return obj

class ClinicInfoEdit(UpdateView):

    template_name = "specialist/clinic_edit.html"
    model = Clinic
    form_class = ClinicForm

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        print(context.keys())

        clinic=self.kwargs.get("pk")
        specialist = Specialist.objects.filter(user=self.request.user).first()
        print(specialist)
        print(clinic)
        schedule = Schedule.objects.filter(specialist=specialist, clinic=clinic).first()
        context["schedule_form"]= schedule

        return context

    def get_form(self, form_class=None):
        print("---------def get_form(self, form_class=None)")
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.form_class
            

        form_class:ClinicForm

        # print(form_class(**self.get_form_kwargs()))  
        return form_class(**self.get_form_kwargs())


    def get_form_kwargs(self) :
        print("-------def get_form_kwargs(self)")
        form_context = super().get_form_kwargs()
        form_context['initial']={
            "francisco":"francisco"
        }
        # print(form_context)
        return form_context

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        specialist = Specialist.objects.filter(user=self.request.user).values()[0].get('id')
        clinic = Clinic.objects.filter(specialist=specialist).values()[0].get('id')
        clinic = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        return reverse('specialist_app:specialist_clinic', kwargs={'pk': clinic})

    def post(self, request: HttpRequest, *args, **kwargs):
        

        clinic=kwargs.get("pk")
        specialist = Specialist.objects.filter(user=request.user)

        if clinic and specialist:
            
            monday_start = request.POST.get("monday_start")
            monday_end = request.POST.get("monday_end")
            tuesday_start = request.POST.get("tuesday_start")
            tuesday_end = request.POST.get("tuesday_end")
            wednesday_start = request.POST.get("wednesday_start")
            wednesday_end = request.POST.get("wednesday_end")
            thursday_start = request.POST.get("thursday_start")
            thursday_end = request.POST.get("thursday_end")
            friday_start = request.POST.get("friday_start")
            friday_end = request.POST.get("friday_end")
            saturday_start = request.POST.get("saturday_start")
            saturday_end = request.POST.get("saturday_end")
            sunday_start = request.POST.get("sunday_start")
            sunday_end = request.POST.get("sunday_end")
            
            schedule, created = Schedule.objects.get_or_create(
                
                    {"specialist":specialist,
                    "clinic":clinic}
                )
            schedule:Schedule

            if schedule:
                schedule.lunes={"monday_start":monday_start,"monday_end":monday_end}
                schedule.martes={"tuesday_start":tuesday_start,"tuesday_end":tuesday_end}
                schedule.miercoles={"wednesday_start":wednesday_start,"wednesday_end":wednesday_end}
                schedule.jueves={"thursday_start":thursday_start,"thursday_end":thursday_end}
                schedule.viernes={"friday_start":friday_start,"friday_end":friday_end}
                schedule.sabado={"saturday_start":saturday_start,"saturday_end":saturday_end}
                schedule.domingo={"sunday_start":sunday_start,"sunday_end":sunday_end}
                
                schedule.save()

        return super().post(request, *args, **kwargs)

# def clinic_schedule(request:HttpRequest):

#     print(request.user)
#     print("----------------------def clinic_schedule(request:HttpRequest):")
#     """Return the URL to redirect to after processing a valid form."""
#     specialist = Specialist.objects.filter(user=request.user).values()[0].get('id')
#     clinic = Clinic.objects.filter(specialist=specialist).values()[0].get('id')
#     raise ("ENTRE")
#     return HttpResponseRedirect( reverse('specialist_app:specialist_clinic', kwargs={'pk': clinic}) )



def SpecialistRegister(request:HttpRequest):
    print(request.user)

    specialist_exist = Specialist.objects.filter(user = request.user).exists()
    if not specialist_exist:
        specialist = Specialist.objects.create(user = request.user)
        specialist.save()
    
    specialist:Specialist = Specialist.objects.filter(user = request.user).get()


    clinic_exist = Clinic.objects.filter(specialist = specialist).exists()
    if not clinic_exist:
        clinic:Clinic = Clinic.objects.create(specialist = specialist)
        clinic.save()
    return HttpResponseRedirect(reverse("specialist_app:info_specialist",kwargs={'slug':specialist.slug}))

class Dates(ListView):
    template_name = "specialist/dates.html"
    model = Meeting
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["dates"] = Meeting.objects.filter(user=self.request.user).order_by("-date","-time")

        # for cita in context["citas"]:
        #     print(cita.__dict__.keys())
        return context

class SpecialistDates(ListView):
    template_name = "specialist/specialist_dates.html"
    model = Meeting
    context_object_name = "dates"

    
    def get_queryset(self):
        queryset = super().get_queryset() 
        queryset:QuerySet
        specialist = Specialist.objects.filter(user=self.request.user)
        print(specialist)
        queryset.filter(specialist=specialist)
        print(queryset)
        return queryset
    
    
    

    


