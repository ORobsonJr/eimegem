from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from converter import converter
from rest_framework.response import Response

# Create your views here.
class PAGE(TemplateView):
    template_name = 'index.html'


#REST api
@api_view(['POST'])
def convert_image(request):
    """Convert image to text"""

    image_data = request.data
    #Content of image in base64

    file_location = converter.create_file(image_data)
    data_processed = converter.img_to_str(file_location)
    if type(data_processed) is dict:
        if data_processed.get('erro') is None:
            return Response(
                {"data": str(converter.img_to_str(file_location))}
                ) 
    
        return Response({"erro": data_processed}, status=500)
    
    return Response({'data': data_processed})


