from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import validate_timestamp

@csrf_exempt  # 禁用CSRF校验（仅供演示，实际应用中请根据需要使用）
def my_api_view(request):
    if request.method == "GET":
        # 获取请求中的时间戳参数
        timestamp_with_check = request.GET.get('timestamp')

        if timestamp_with_check is None:
            return JsonResponse({'error': 'Timestamp is required'}, status=400)

        try:
            timestamp_with_check = int(timestamp_with_check)
        except ValueError:
            return JsonResponse({'error': 'Invalid timestamp format'}, status=400)

        # 校验时间戳
        if validate_timestamp(timestamp_with_check):
            return JsonResponse({'message': 'Timestamp is valid'})
        else:
            return JsonResponse({'error': 'Invalid timestamp'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

