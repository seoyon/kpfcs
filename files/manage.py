from files.models import *
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), "attach/")

def upload(f):
    new_name = ""
    for char in f.name:
        if char == " " or char == ",":
            new_name += "_"
        else:
            new_name += char
    File(
        name = new_name,
        path = BASE_DIR + new_name
    ).save()
    with open(BASE_DIR + new_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def delete(f_id):
    f = File.objects.get(id = f_id)
    os.remove(f.path)
    f.delete()
