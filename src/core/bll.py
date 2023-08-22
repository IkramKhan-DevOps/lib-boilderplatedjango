from .models import Application


def get_or_create_application():
    applications = Application.objects.all()
    return applications[0] if applications else Application.objects.create()
