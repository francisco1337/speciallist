from django import forms


from applications.specialist.models import Clinic, Meeting, Specialist

class MeetForm(forms.ModelForm):
    

    def __init__(self, slug, *args, **kwargs):
        self.id_user = slug
        print("MeetForm")
        print(slug)
        self.clinic = slug
        
        super(MeetForm, self).__init__(*args, **kwargs)

    

    
    class  Meta:
        model = Meeting
        fields = ('__all__')
        exclude = (
            'specialist',
            'user'   
        )
        labels = {
            'topic': 'Asunto',
            'clinic': 'Clinica',
        }

        widgets = { 
            'topic':forms.Select(
                    attrs={
                        'placeholder' : 'Asunto',
                        'class':'controled'
                    }
                ),
            'clinic':forms.Select(
                    attrs={
                        'placeholder' : 'Asunto',
                        'class':'controled',
                        'readonly': 'readonly'
                    }
                ),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'date':forms.DateInput(
                    attrs={
                        'placeholder' : 'Fecha',
                        'type' : 'date',
                        'class':'controled'
                    }
                ),
            
        }


class SpecialistInfoForm(forms.ModelForm):
    
    class  Meta:
        model = Specialist
        fields = ('__all__')
        exclude = (
            'specialist',
            'user'   
        )
        labels = {
            'topic': 'Asunto',
            'clinic': 'Clinica',
        }

        widgets = { 
            'topic':forms.Select(
                    attrs={
                        'placeholder' : 'Asunto',
                        'class':'controled'
                    }
                ),
            'clinic':forms.Select(
                    attrs={
                        'placeholder' : 'Asunto',
                        'class':'controled'
                    }
                ),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'date':forms.DateInput(
                    attrs={
                        'placeholder' : 'Fecha',
                        'type' : 'date',
                        'class':'controled'
                    }
                ),
            
        }

class ClinicForm(forms.ModelForm):
    
    class  Meta:
        model = Clinic
        fields = ('__all__')
        exclude = (
            'specialist',
            'country',
            'map_iframe'   
        )
        # labels = {
        #     'topic': 'Asunto',
        #     'clinic': 'Clinica',
        # }

        # widgets = { 
        #     'topic':forms.Select(
        #             attrs={
        #                 'placeholder' : 'Asunto',
        #                 'class':'controled'
        #             }
        #         ),
        #     'clinic':forms.Select(
        #             attrs={
        #                 'placeholder' : 'Asunto',
        #                 'class':'controled'
        #             }
        #         ),
        #     'time': forms.TimeInput(attrs={'type': 'time'}),
        #     'date':forms.DateInput(
        #             attrs={
        #                 'placeholder' : 'Fecha',
        #                 'type' : 'date',
        #                 'class':'controled'
        #             }
        #         ),
            
        # }

class SpecialistCreateForm(forms.ModelForm):

    
    
    class  Meta:
        model = Specialist
        fields = ('__all__')
        exclude = (
            'specialist',
            'user'   
        )
        labels = {
            'topic': 'Asunto',
            'clinic': 'Clinica',
        }

        widgets = { 
            'topic':forms.Select(
                    attrs={
                        'placeholder' : 'Asunto',
                        'class':'controled'
                    }
                ),
            'clinic':forms.Select(
                    attrs={
                        'placeholder' : 'Asunto',
                        'class':'controled'
                    }
                ),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'date':forms.DateInput(
                    attrs={
                        'placeholder' : 'Fecha',
                        'type' : 'date',
                        'class':'controled'
                    }
                ),
            
        }

