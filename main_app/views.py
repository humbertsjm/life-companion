from typing import Any

from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        return super().get_context_data(**kwargs)