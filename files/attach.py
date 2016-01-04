from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import mimetypes
import os
import urllib

from files.models import *

def get_download_response(request, num):
    exact_file=get_object_or_404(File,id = num)
    content = open(exact_file.path, "rb")
    response = HttpResponse(content.read())
    content.close()
    
    type, encoding = mimetypes.guess_type(exact_file.name)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat(exact_file.path).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding
    
    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % exact_file.name.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(exact_file.name.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header
    
    return response
