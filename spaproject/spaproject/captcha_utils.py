from PIL import Image, ImageDraw, ImageFont
import random
import string
import io
from django.core.cache import cache

CAPTCHA_EXPIRATION_TIME = 300  # Срок действия капчи (в секундах)

def generate_captcha():
    # Генерация текста капчи
    chars = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(chars) for _ in range(3))
    
    # Генерация уникального ключа для капчи
    captcha_key = f"captcha_{random.randint(1000, 9999)}_{random.randint(1000, 9999)}"
    
    # Создание изображения капчи
    image_width, image_height = 40, 20
    background_color = (0, 0, 0)
    text_color = (255, 255, 255)
    font_path = "/static/comments/FreeMonoBold.ttf" 
    
    image = Image.new('RGB', (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, 18)
    
    text_bbox = draw.textbbox((0, 0), captcha_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_x = (image_width - text_width) // 2
    text_y = (image_height - 1.4 * text_height) // 2
    draw.text((text_x, text_y), captcha_text, font=font, fill=text_color)
    
    # Сохранение изображения в память
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    image_data = buffer.getvalue()
    
    # Сохранение капчи в Redis
    cache.set(captcha_key, captcha_text, timeout=CAPTCHA_EXPIRATION_TIME)
    
    return captcha_key, image_data
