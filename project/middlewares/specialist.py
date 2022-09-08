from applications.specialist.models import Specialist


class Specialist_user_information:
    def __init__(self, get_response):
        print("Francisco mid init")

        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        print("Francisco mid call")
        return response


    def is_specialist(self, request, response):
        print("FRANCISCO mid is specialist")
        return response