from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from converter import converter
from rest_framework.response import Response
from converter import learn_words

# Create your views here.
class PAGE(TemplateView):
    template_name = 'index.html'

class Refresh(TemplateView):
    template_name = 'learn_words.html'


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
def refresh_learn_ai(request):
    """
    Run learn_words file
    """

    try:
        learn_words.main()
        return Response(status=200)
    
    except Exception as e:
        return Response({'exception': str(e)}, status=500)

