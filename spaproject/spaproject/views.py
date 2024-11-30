from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
import json

from .captcha_utils import generate_captcha


@csrf_exempt
def get_captcha(request):
    captcha_key, captcha_image = generate_captcha()
    response = HttpResponse(captcha_image, content_type="image/png")
    response['Captcha-Key'] = captcha_key
    return response

@csrf_exempt
def verify_captcha(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            captcha_key = data.get('captcha_key')
            captcha_answer = data.get('captcha_value')
            expected_value = cache.get(captcha_key)
            if expected_value and expected_value == captcha_answer:
                cache.delete(captcha_key)
                return JsonResponse({"success": True, "message": "Captcha verification passed."})
            else:
                return JsonResponse({"success": False, "message": "Captcha verification failed."})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=400)

