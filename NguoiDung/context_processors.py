def username(request):
    return {
        'session_username': request.session.get('user_username')
    }