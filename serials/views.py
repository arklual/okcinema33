from django.shortcuts import render, get_object_or_404
from serials.models import Serial, Seriya
from marks.models import SerialVoter
from marks.forms import BallForm
from lxml import etree
from urllib import request as rqs

# Create your views here.
def serial(request, id=None):
    form = BallForm
    serial = get_object_or_404(Serial, id=id)
    kp_rait = 0
    imdb_rait = 0
    if not serial.kp_id is None:
        kp_url = "https://rating.kinopoisk.ru/"+serial.kp_id+".xml"
        try:
            f_xml = rqs.urlopen(kp_url)
            xml = f_xml.read()
            xml_root = etree.fromstring(xml)
            for elem in xml_root.getchildren():
                if not elem.text:
                    text = "None"
                else:
                    text = elem.text
                if(elem.tag == "kp_rating"):
                    kp_rait = float(elem.text)
                if(elem.tag == "imdb_rating"):
                    imdb_rait = float(elem.text)
        except:
            pass
    context = {
        "notSerIsMarked": not SerialVoter.objects.filter(serial_id=id, user_id=request.user.id).exists(),
        "s": serial,
        "range": range(serial.count_sesonov),
        "form": form,
    }
    kp_exist = False
    imdb_exist = False
    context['kp_rait'] = kp_rait
    context['imdb_rait'] = imdb_rait
    if(not kp_rait == 0):
        kp_exist = True
    if(not imdb_rait == 0):
        imdb_exist = True
    context['kp_exist'] = kp_exist
    context['imdb_exist'] = imdb_exist
    context['sers'] = serial.seriya_set.all().filter()
    return render(request, "partial/single_serial.html", context) 
