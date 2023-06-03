from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from converter import converter
from converter.text_handling import utils as utils_converter
from rest_framework.response import Response

# Create your views here.
class PAGE(TemplateView):
    template_name = 'index.html'


#REST api
@api_view(['POST'])
def convert_image(request):
    """Convert image to text"""

    image_data = request.data
    #Content of file in base64
    converter_object = converter.ConvertObject() 

    file_location = converter_object.create_file(image_data)
    data_processed = converter_object.img_to_str(file_location)
    if type(data_processed) is dict:
        if data_processed.get('erro') is None:
            return Response(
                {"data": str(converter.img_to_str(file_location))}
                ) 
    
        return Response({"erro": data_processed}, status=500)
    
    return Response({'data': data_processed})

@api_view(['POST'])
def text_correction(request):
    """
    Receive a text and correct them
    """

    try:
        text = request.data
        result = utils_converter.correct_by_gpt(text['data'])
        return Response({"data": result})
    
    except Exception as e:
        return Response({'erro': str(e)}, status=500)




