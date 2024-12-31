from django.http import JsonResponse

class AuthMiddleware:
    """
    自定义身份验证中间件，用于检查每个请求的 X-Auth-Token。
    """
    def __init__(self, get_response):
        # get_response 是下一个中间件或视图的回调函数
        self.get_response = get_response

    def __call__(self, request):
        # 在请求到达视图之前，检查请求头中是否有 X-Auth-Token
        auth_token = request.headers.get('X-Auth-Token')

        if not auth_token or auth_token != "my_secret_token":
            # 如果没有提供正确的令牌，则拒绝访问
            return JsonResponse({"error": "Unauthorized"}, status=403)

        # 如果验证通过，继续处理请求
        response = self.get_response(request)
        return response
