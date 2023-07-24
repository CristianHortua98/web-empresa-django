from .models import Link

def ctx_dict(request):
    ctx = {}
    ctx['links'] = Link.objects.all()
    return ctx