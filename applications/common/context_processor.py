from applications.common.utilities import get_current_application_name


def set_template_variables(request):
    current_application_name = get_current_application_name(request)

    return {
        'CURRENT_APPLICATION_NAME': current_application_name,
    }
