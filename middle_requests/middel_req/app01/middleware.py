import logging
from django.http import JsonResponse
class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 记录请求信息
        # logging.info(f"Request Path: {request.path} | Method: {request.method}")

        # 调用下一个中间件或者视图
        response = self.get_response(request)

        # 返回响应
        return response

    # 如果需要处理请求，可以在此方法中修改请求
    def process_request(self, request):
        logging.info(f"Processing request at {request.path}")
class ResponseHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 获取视图的响应
        response = self.get_response(request)

        # 在响应中添加自定义头部
        response['X-Processed-By'] = 'lank'

        return response

    # 这个方法会在视图返回响应后被调用
    def process_response(self, request, response):
        logging.info(f"Adding custom header to response: {response['X-Processed-By']}")
        return response
class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # 获取视图响应
            response = self.get_response(request)
        except Exception as e:
            # 捕获异常并返回 JSON 格式的错误响应
            logging.error(f"An error occurred: {e}")
            response = JsonResponse({'error': 'An unexpected error occurred.'}, status=500)
        return response

    # 处理视图抛出的异常
    def process_exception(self, request, exception):
        logging.error(f"Exception occurred while processing request: {exception}")
        return JsonResponse({'error': 'A middleware error occurred during processing.'}, status=500)


from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 如果请求的路径需要登录并且用户未登录
        if not request.user.is_authenticated and not request.path.startswith('/login'):
            return redirect('/login')
        response = self.get_response(request)
        return response
