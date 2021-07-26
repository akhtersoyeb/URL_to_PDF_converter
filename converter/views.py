from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from django.views.generic import View, FormView
from django.core.files.base import ContentFile
import requests
import convertapi
from .forms import UrlForm
convertapi.api_secret = 'your-convertapi-secret-key-here'


class WebToPdfConverterView(FormView):
    form_class = UrlForm
    template_name = 'converter/webToPdfConverter.html'

    def form_valid(self, form):
        try : 
            url = form.cleaned_data['url']
            result = convertapi.convert('pdf', { 'Url': url }, from_format = 'web')
            r = requests.get(result.file.url)
            converted_file = ContentFile(r.content)
            return FileResponse(converted_file)
        except : 
            return HttpResponse("Something Went Wrong!, refresh the page")


#  convertapi.api_secret = '<YOUR SECRET HERE>'
#  convertapi.convert('pdf', {
    #  'Url': 'https://github.com/akhtersoyeb/Noob-Django-Ecommerce/blob/main/products/views.py'
#  }, from_format = 'web').save_files('/path/to/dir')
