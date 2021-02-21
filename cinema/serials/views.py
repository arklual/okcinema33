from django.shortcuts import render, get_object_or_404
from serials.models import Serial, Seriya
from marks.models import SerialVoter
from marks.forms import BallForm

# Create your views here.
def serial(request, id=None):
    form = BallForm
    serial = get_object_or_404(Serial, id=id)
    context = {
        "notSerIsMarked": not SerialVoter.objects.filter(serial_id=id, user_id=request.user.id).exists(),
        "s": serial,
        "range": range(serial.count_sesonov),
        "form": form,
    }
    context['sers'] = serial.seriya_set.all().filter()
    return render(request, "partial/single_serial.html", context)