from applications.specialist.models import Clinic, Specialist

def specialist_user_information(request):
   specialist =  False
   specialistInfo = None
   specialistClinic = None
   clinic = False
   if request.user.is_authenticated:
      specialist = Specialist.objects.filter(user = request.user).exists()
      if specialist:
         specialistInfo = Specialist.objects.filter(user = request.user)[0]
         clinic = Clinic.objects.filter(specialist = specialistInfo).exists()
         if clinic:
            specialistClinic = Clinic.objects.filter(specialist = specialistInfo).values()[0]
            specialistInfo = Specialist.objects.filter(user = request.user).values()[0]
   return {
      'is_espacialist':specialist,
      'specialistInfo':specialistInfo,
      'is_spaialistClinic': clinic,
      'specialistClinic':specialistClinic
      } 