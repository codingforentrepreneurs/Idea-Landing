from django.conf import settings


def hiit_project_name(request):
    project = getattr(request, 'project_name', None)
    context = {}
    if project is None:
        project_name = getattr(settings, "PROJECT_NAME", "Hiit Startup")
        request.project_name = project_name
        hiit_project_name =   project_name

        context = {
            "hiit_project_name": hiit_project_name,
        }
    return context