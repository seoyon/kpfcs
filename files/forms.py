from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import os

from files.models import *

class UploadForm(forms.Form):
    file = forms.FileField(label = 'File to upload')
    
    def clean_file(self):
	filename = self.cleaned_data['file'].name
	#fname_list = filename.split("/")
	#filename = fname_list[len(fname_list)-1]
        filename = filename.replace(" ","_").replace(",","_")
	try:	
	    File.objects.get(name=filename)
	    #print "The file already exists."
	    return form.ValidationError("Same filename exists!")
	except ObjectDoesNotExist:
	    return self.cleaned_data['file']
	
