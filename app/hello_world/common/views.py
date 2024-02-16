from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from common.stress_test import perform_stress_test
import logging

logger = logging.getLogger("")


class IndexView(TemplateView):
    template_name = "index.html"


def stress_test_view(request, stress_level: int):
    logger.info(f"Starting to perform a stress test of {2*100}MB memory load.")
    perform_stress_test(stress_level)
    return HttpResponse("<h1>Performing the stress test.</h1>")
