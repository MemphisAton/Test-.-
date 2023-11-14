from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from datetime import datetime


def validate_phone(value):
    """
    Валидирует номер телефона в формате +7 xxx xxx xx xx.
    :param value: Значение поля номера телефона.
    :raises: ValidationError, если номер телефона не соответствует формату.
    """
    if not re.match(r"^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$", value):
        raise ValidationError("Номер телефона должен быть в формате +7 xxx xxx xx xx")


def validate_date(value):
    """
    Валидирует дату в форматах DD.MM.YYYY или YYYY-MM-DD.
    :param value: Значение поля даты.
    :raises: ValidationError, если дата не соответствует форматам.
    """
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            datetime.strptime(value, fmt)
            return
        except ValueError:
            continue
    raise ValidationError("Дата должна быть в формате DD.MM.YYYY или YYYY-MM-DD")


def validate_text(value):
    """
    Валидирует текстовое поле, проверяя, что оно не пустое.
    :param value: Значение текстового поля.
    :raises: ValidationError, если текстовое поле пустое.
    """
    if not value.strip():
        raise ValidationError("Текстовое поле не может быть пустым")


# Использование встроенной функции Django для валидации email
validate_email_field = validate_email
