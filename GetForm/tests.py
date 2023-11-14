from django.test import TestCase, Client
from .tinydb_connector import FormTemplateDB


class FormTemplateTests(TestCase):

    def setUp(self):
        """
        Очистка тестовых данных и создание новых
        """
        FormTemplateDB.clear_all_form_templates()
        FormTemplateDB.add_form_template("TestForm", {"email": "email", "phone": "phone"})
        self.client = Client()

    def test_valid_data(self):
        """
        Тестирование с валидными данными
        """
        response = self.client.post('/get_form/',
                                    {'email': 'test@example.com', 'phone': '+7 123 456 78 90'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'template_name': 'TestForm'})

    def test_invalid_data(self):
        """
        Тестирование с невалидными данными
        """
        response = self.client.post('/get_form/', {'email': 'test@example', 'phone': '+7 123 456 78 90'})
        self.assertNotEqual(response.status_code, 200)

    def test_unmatched_data(self):
        """
        Тестирование с данными, которые не соответствуют ни одному шаблону
        """
        response = self.client.post('/get_form/', {'random_field': 'some_value'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('random_field', response.json())

    @classmethod
    def tearDownClass(cls):
        """"
        Очистка тестовых данных после выполнения всех тестов
        """
        FormTemplateDB.clear_all_form_templates()
