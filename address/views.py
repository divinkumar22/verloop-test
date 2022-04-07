from rest_framework.views import APIView
from rest_framework.response import Response
from address.googlemap import get_coordinates
from address.negotiation import CustomContentNegotiation

class AddressDetailsView(APIView):
    """
    Returns details about Address
    """
    content_negotiation_class = CustomContentNegotiation
    queryset = None 
    def get(self,request,format=None):
        try:
            address = request.data['address']
            data = get_coordinates(address)
            return Response(data)
        except:
            return Response({"data":"Please Enter Address/other error"})