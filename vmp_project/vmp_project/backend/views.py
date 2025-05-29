from django.http import JsonResponse
from utils.sign_vm import compile_input, interpret

def protected_view(request):
    sign = request.GET.get("sign")
    ts = request.GET.get("ts")
    ua = request.headers.get("User-Agent")

    if not sign or not ts:
        return JsonResponse({"error": "Missing parameters"}, status=400)

    raw = f"{ts}:{ua}"
    bytecode = compile_input(raw)
    expected_sign = interpret(bytecode)

    if sign != expected_sign:
        return JsonResponse({"error": "Invalid sign"}, status=403)

    return JsonResponse({"message": "VMP sign verification passed"})
