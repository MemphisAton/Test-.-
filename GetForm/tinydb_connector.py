from tinydb import TinyDB, Query

db = TinyDB('db.json')  # путь к файлу базы данных


class FormTemplateDB:
    @staticmethod
    def add_form_template(name, fields):
        """
        Добавляет новый шаблон формы в базу данных.

        :param name: Имя шаблона формы.
        :param fields: Словарь полей формы в формате {'field_name': 'field_type'}.
        :return: True, если шаблон был успешно добавлен, False, если шаблон с таким именем уже существует.
        """
        FormTemplate = Query()
        if db.contains(FormTemplate.name == name):
            return False  # Шаблон с таким именем уже существует
        db.insert({'type': 'form_template', 'name': name, 'fields': fields})
        return True

    @staticmethod
    def get_all_form_templates():
        """
        Получает список всех шаблонов формы из базы данных.
        :return: Список словарей, представляющих шаблоны формы.
        """
        FormTemplate = Query()
        return db.search(FormTemplate.type == 'form_template')

    @staticmethod
    def get_form_template_by_name(name):
        """
        Получает шаблон формы по его имени.
        :param name: Имя шаблона формы.
        :return: Словарь, представляющий найденный шаблон, или None, если шаблон не найден.
        """
        FormTemplate = Query()
        result = db.search(FormTemplate.name == name)
        return result[0] if result else None

    @staticmethod
    def clear_all_form_templates():
        """
        Удаляет все шаблоны формы из базы данных.
        """
        FormTemplate = Query()
        db.remove(FormTemplate.type == 'form_template')
