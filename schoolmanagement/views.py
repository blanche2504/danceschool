from django.shortcuts import get_object_or_404, render

from schoolmanagement.models import School

__all__ = [
    "dettaglio_scuola",
    "lista_scuole",
]


def lista_scuole(request):
    scuole = School.objects.all()
    return render(
        request,
        "schoolmanagement/school_list.html",
        {"object_list": scuole},
    )


def dettaglio_scuola(request, pk):
    scuola = get_object_or_404(School, pk=pk)
    return render(
        request,
        "schoolmanagement/school_detail.html",
        {"object": scuola},
    )
