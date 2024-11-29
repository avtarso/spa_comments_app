from django.http import JsonResponse
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from django.views.decorators.csrf import csrf_exempt
import json

# def check_captcha(request):
#     """Проверка капчи и возвращение результата."""
#     if request.method == 'POST':
#         captcha_key = request.POST.get('captcha_key')
#         captcha_answer = request.POST.get('captcha_answer')

#         try:
#             captcha_entry = CaptchaStore.objects.get(hashkey=captcha_key)
#             if captcha_entry.response == captcha_answer:
#                 return JsonResponse({'success': True})
#         except CaptchaStore.DoesNotExist:
#             pass

#         return JsonResponse({'success': False, 'error': 'Invalid captcha'})

#     return JsonResponse({'error': 'Invalid method'}, status=405)

# def get_captcha(request):
#     """Генерация новой капчи."""
#     new_captcha = CaptchaStore.generate_key()
#     captcha_url = captcha_image_url(new_captcha)
#     return JsonResponse({'captcha_key': new_captcha, 'captcha_url': captcha_url})




#Временное хранилище капч (заменить на базу данных для продакшена)
CAPTCHA_STORAGE = {}

@csrf_exempt
def get_captcha(request):
    """Генерация капчи"""
    if request.method == 'GET':
        # Генерируем ключ и значение капчи
        captcha_key = '1234'  # Здесь должен быть уникальный идентификатор
        captcha_value = 'ABCD'  # Здесь может быть сгенерированное значение капчи
        CAPTCHA_STORAGE[captcha_key] = captcha_value  # Сохраняем капчу в хранилище

        print(f"Generated captcha_key: {captcha_key}, captcha_answer: {captcha_value}")


        # Возвращаем данные для клиента
        return JsonResponse({
            'captcha_key': captcha_key,
            'captcha_url': f'/static/comments/{captcha_value}.png',  # Заглушка (замени на реальную генерацию)
        })
    return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt
def check_captcha(request):
    """Проверка капчи"""
    if request.method == 'POST':
        try:
            # Получаем данные из тела запроса
            print("Получаем данные из тела запроса")
            print(request.body)
            data = json.loads(request.body)
            
            captcha_key = data.get('captcha_key')
            captcha_answer = data.get('captcha_answer')

            print(f"Received captcha_key: {captcha_key}, captcha_answer: {captcha_answer}")


            # Проверяем, совпадает ли ответ с сохранённым значением
            if CAPTCHA_STORAGE.get(captcha_key) == captcha_answer:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid captcha'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=400)

