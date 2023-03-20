class ExampleMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("****************----------------------------------------------------------------------------------------------------------------------------------------------------******************")
        print('Middleware called')
        user = request.user
        print('USER-EMAIL:', user)
        print('USER-ID:', user.id)

        response = self.get_response(request)
        user_name=request.META.get('USER')
        print('USER-NAME', user_name)

        request_id = request.META.get('X-Request-ID')
        print('REQUEST-ID', request_id)

        print("****************----------------------------------------------------------------------------------------------------------------------------------------------------******************")

        return response