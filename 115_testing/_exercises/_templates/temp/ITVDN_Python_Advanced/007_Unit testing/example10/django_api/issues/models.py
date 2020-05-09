____ django.conf ______ settings
____ django.db ______ models


c_ Issue(models.Model):
    name _ models.CharField('Название', max_length_512)
    description _ models.TextField('Описание', default_'')
    due_date _ models.DateField('Выполнить к дате')

    c_ Meta:
        verbose_name _ 'Заметка'
        verbose_name_plural _ 'Заметки'

    ___ __str__
        r_ name

    ___ set_due_date  due_date):
        due_date _ due_date

    ___ foo
        if settings.DEBUG:
            r_ name
        r_ 'stub'

    ___ bar
        if settings.ADMINS_NAME in settings.CUSTOM_LIST:
            r_ name
        r_ 'stub'
