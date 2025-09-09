import threading

from counters.views import increment_counter, service_counter
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import LoginForm


def index(request, *args, **kwargs):
    if request.method == "GET":
        host = request.META.get("HTTP_HOST", "")
        if host in settings.SUB_DEV:
            return render(request, "ecr/base_link_tree.html")
        elif host in settings.PROD_ECR:
            return render(request, "ecr/base_link_tree.html")
        elif host in settings.PROD_IPROF:
            return render(request, "iprof/base_link_tree.html")
        else:
            referer = (
                request.GET.get("ref") or request.META.get("HTTP_REFERER")
            ) or "HTTP"
            ctx = {"referer": referer}
            return redirect(reverse("core:about"))
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            service_counter(request, user=form.get_user())
            try:
                login(request, form.get_user())
                response = render(request, "development/index.html")
                response["HX-Redirect"] = "/app/"
                return response
            except Exception as e:
                print(e)
                form.add_error(
                    "username",
                    "algo deu errado, contacte o suporte",
                )

        return render(request, "development/form_login.html", {"form": form})


def _context_get(request):
    thread = threading.Thread(target=increment_counter, args=(request,))
    thread.start()
    return render(request, "core/login_no_pass.html")
