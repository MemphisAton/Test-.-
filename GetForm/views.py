from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .tinydb_connector import FormTemplateDB
from .validators import validate_email_field, validate_phone, validate_date, validate_text
import logging

logger = logging.getLogger(__name__)


@require_http_methods(["POST"])
def get_form(request):
    """
    Обработчик запроса для получения формы.
    Ограничивает доступ только к HTTP-методу POST.
    Принимает данные формы и возвращает результат обработки.
    :param request: Объект запроса Django.
    :return: JSON-ответ с результатом обработки.
    """
    try:
        # request.POST для данных, отправленных в формате application/x-www-form-urlencoded
        data = request.POST
        for template in FormTemplateDB.get_all_form_templates():
            if all(field_name in data for field_name in template['fields']):
                try:
                    for field_name, field_type in template['fields'].items():
                        value = data[field_name]
                        if field_type == 'email':
                            validate_email_field(value)
                        elif field_type == 'phone':
                            validate_phone(value)
                        elif field_type == 'date':
                            validate_date(value)
                        elif field_type == 'text':
                            validate_text(value)
                        else:
                            raise ValueError("Неизвестный тип поля")
                    return JsonResponse({'template_name': template['name']})
                except (ValidationError, ValueError) as e:
                    logger.info(f"Validation error: {e}")
                    return JsonResponse({'error': 'Невалидные данные'}, status=400)
        # Если подходящий шаблон не найден
        return JsonResponse({key: "text" for key in data.keys()})
    except Exception as e:
        logger.error(f"Error processing form: {e}")
        return JsonResponse({'error': 'Ошибка обработки запроса'}, status=500)
