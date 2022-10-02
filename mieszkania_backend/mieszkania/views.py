# external
from .helpers.classes import CustomGenericAPI
from rest_framework.response import Response
# models
from mieszkania.models import Apartment, PriceRecord
# serializers
from mieszkania.serializers import ApartmentSerializer

class ApartmentGenericAPI(CustomGenericAPI):
    queryset = Apartment.objects
    serializer_class = ApartmentSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            prices = PriceRecord.objects.filter(apartment_id=pk)
            data = [price for price in prices.values()]
            return Response(data)
        return self.list(request, pk, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

    def patch(self, request, pk, *args, **kwargs):
        return self.partial_update(request, pk)