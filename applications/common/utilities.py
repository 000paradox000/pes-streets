def get_current_application_name(request):
    try:
        app_name = request.resolver_match.namespace

        if app_name is None or app_name == '':
            app_name = "home"
    except Exception as e:
        app_name = "home"

    return app_name

