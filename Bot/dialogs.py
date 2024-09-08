RU_ru = {
    '/start_success': """, добро пожаловать, перед вами главное меню для управления мной
    """,
    '/menu': """📋 Главное меню:""",
    '/start_unsuccessful': """Приветствую, к сожалению не узнал Вас.
Если Вы являетесь членом команды, 
попросите добавить вас в белый список, 
чтобы продолжить пользоваться моими функциями
    """,
    'add_user_int_err': """Ошибка ID.
Проверьте правильность написания, пример: `1234567890`
    """,
    'not_admin': """Вы не можете пользоваться этой функцией.

Если вы считаете, что это ошибка, то обратитесь к администратору""",
    'white_list': """Это белый список.
Вы можете нажать на пользователя для просмотра дополнительной информации.
""",
    'tokens_list': """Это список подключенных токенов.
Вы можете нажать на элемент для управления им.""",
    'help_services': """<code>Facebook</code> - для управления Marketing API Facebook
<code>GetCourse</code> - для управления GetCourse API

Введите <code>/add_token {service} {token}</code> для добавления нового токена""",
    'wait': """Подождите, запрос обрабатывается...
Обычно это занимает до минуты.

Вы можете продолжать пользоваться мной, как только файл будет готов, отправлю его""",

    'fast_report_ok': """, вот Ваш файл с отчетом в формате CSV
А так же все данные записаны в базу данных для дальнейшего использования""",

    'fast_report_bad': """К сожалению отчет не был получен, либо произошла ошибка.
Попробуйте снов через 10 минут, если ошибка повторится, обратитесь к обслуживающему специалисту""",

    'choose': 'Выбор:',

    'request_facebook': {
        '401': 'Ошибка авторизации. Перепроверьте правильность написания токена или права доступа.',
        'else': 'Ошибка запроса. Пожалуйста, обратитесь к обслуживающему специалисту.'
    },
    'user': {
        'name': 'Имя:',
        'username': 'Никнейм:',
        'id': 'ID:',
        'admin': 'Администратор:',
        'is_admin': {
            'true': '✅',
            'false': '❌'
        }
    },
    'adaccount': {
        'reports': 'Получать отчет:',
        'name': 'Название:',
        'id': 'ID:',
        'is_active': {
            'true': '✅',
            'false': '❌'
        }
    },
    'navigation': {
        'back': 'Назад',
        'forward': 'Вперед',
        'downgrade': 'Понизить',
        'upgrade': 'Повысить',
        'delete': 'Удалить',
        'delete_all': 'Удалить все',
        'add': 'Добавить',
        'activate': 'Получать отчеты',
        'deactivate': 'Не получать отчеты',
        'message': 'Написать',
        'reports': 'Настройка отчетов',
        'activate_all': 'Включить все',
        'deactivate_all': 'Выключить все',
        'date_preset': 'Время',
        'level': 'Уровень',
        'increment': 'Разбивка',
        'menu': 'Главное меню',
        'white_list': 'Белый список',
        'token': 'Токены',
        'scheduler': 'Планировщик',
        'fast_report': 'Моментальный отчет',
        'edit_scheduler': 'Редактировать',
        'help': 'Помощь',
        'tokens': 'Токены',
    },
    'adacc_settings': {
        'fields': {
            'account_name': 'Название аккаунта:',
            'account_id': 'ID аккаунта:',
            'campaign_name': 'Название кампании:',
            'campaign_id': 'ID кампании:',
            'adset_name': 'Название рекламной группы:',
            'adset_id': 'ID рекламной группы:',
            'ad_name': 'Название рекламы',
            'ad_id': 'ID рекламы',
            'impressions': 'Показы:',
            'frequency': 'Частота показов:',
            'clicks': 'Клики:',
            'unique_clicks': 'Уникальные клики:',
            'spend': 'Потрачено:',
            'reach': 'Охват:',
            'cpp': 'Средняя стоимость охвата 1000 человек:',
            'cpm': 'Средняя стоимость за 1000 показов:',
            'cpc': 'Средняя стоимость каждого клика (всего):',
            'ctr': 'Процентное соотношение людей, увидевших ваше объявление и совершивших клик:',
            'unique_link_clicks_ctr': 'Название аккаунта:',
            'unique_ctr': 'Уникальные клики по ссылкам, деленные на охват:',
            'cost_per_unique_click': 'Средняя стоимость каждого уникального клика:',
            'objective': 'Цель:',
            'buying_type': 'Метод, с помощью которого вы платите за рекламу:',
            'created_time': 'Дата создания:',
        },

        'level': {
            'text': '<b>Отчет на уровне:</b>',
            'ad': '<b>Рекламы</b>',
            'adset': '<b>Группы реклам</b>',
            'campaign': '<b>Кампании</b>',
            'account': '<b>Аккаунта</b>'
        },

        'date_preset': {
            'text': '<b>Временной диапазон:</b>',
            'today': '<b>Сегодня</b>',
            'yesterday': '<b>Вчера</b>',
            'this_week': '<b>Текущая неделя(до тек.дня)</b>',
            'last_week': '<b>Прошлая неделя</b>',
            'this_month': '<b>Текущий месяц(до тек.дня)</b>',
            'last_month': '<b>Прошлый месяц</b>',
            'this_quarter': '<b>Текущий квартал(до тек.дня)</b>',
            'last_quarter': '<b>Прошлый квартал</b>',
            'this_year': '<b>Текущий год(до тек.дня)</b>',
            'last_year': '<b>Прошлый год</b>',
            'maximum': '<b>Максимум(37 месяцев)</b>',
        },
        'increment': {
            'text': '<b>Разбивка по колличеству дней:</b>',
            1: 1,
            7: 7,
            15: 15,
            30: 30,
            90: 90,

        }
    },
    'scheduler': {
        'None': """В данный момент в планировщике пусто
Но вы можете добавить задачи на Ваш выбор""",
        'notNone': 'Список задач планировщика:',
        'which': 'Какой тип задачи вы хотите создать или изменить?',
        'all': 'Для всех аккаунтов',
        'all_text': """Добавление задачи для всех аккаунтов
        
Вы можете добавить до 8 временных точек в сутках
Это будет означать, что планер будет запускать процесс выгрузки данных, когда текущее время будет совпадать с указанным

Отправьте мне шаблон, по которому планер должен работать

Пример:
<code>1. 00:00
2. 01:00
3. 02:35</code>
и так далее...

Или:
<code>1. 00:00 2. 01:00 3. 02:35</code> и так далее...
""",
        'all_text_done': """Добавление задачи для всех аккаунтов завершено
        
Теперь планировщик будет работать по следующему шаблону:\n""",

        },
    'help_cmd': {
        'help_menu': '🆘 Меню помощи:',
        'white_list': """<b>Белый список</b>
    
Нажав на кнопку в главном меню или вызвав меню с помощью команды /white_list вы получите список пользователей, 
которые имеют доступ к боту.

Нажав на одну из кнопок открывается карточка этого пользователя
Здесь вы можете:
    1. Написать ему/ей
    2. Повысить до администратора или понизить до обычного пользователя
    3. Удалить из белого списка""",

        'tokens_st1': """<b>Список токенов</b>

Нажав на кнопку в главном меню или вызвав меню с помощью команды /tokens вы получите список токенов доступа,
которые подключены к боту.

У каждого токена есть префикс, например [FACEBOOK], что означает, что этот токен относится к сервису Facebook

Нажав на кнопку с префиксом [FACEBOOK] откроется список рекламных аккаунтов, 
к которым есть доступ по этому токену.

Далее, выбрав один из доступных аккаунтов, откроется карточка этого аккаунта, 
в которой вы можете активировать получение отчетов и тонко настроить формат отчетов""",

        'tokens_st2': """Здесь вы можете:
    1. 1-24 включить или выключить выбранное поле
    2. Настроить временной диапазон
    3. Настроить уровень отчета
    4. Настроить разбивку по кол-ву дней
    5. Включить сразу все поля
    6. Выключить сразу все поля
""",

        'tokens_st3': """<b>Описание настроек:</b>
        
<b>1. Временной диапазон имеет следующие варианты:</b>
        1.1. Сегодня
        1.2. Вчера
        1.3. Текущая неделя. Первым днем считается понедельник текущей недели, а последним - сегодня
        1.4. Прошлая неделя. Первым днем считается понедельник прошлой недели, а последним воскресенье той же недели
        1.5. Текущий месяц. Первым днем считается первое число текущего месяца, а последним - сегодня
        1.6. Прошлый месяц. Первым днем считается первое число прошлого месяца, а последним последний день того же месяца
        1.7. Текущий квартал. Первым днем считается первое число текущего квартала, а последним - сегодня
        1.8. Прошлый квартал. Первым днем считается первое число прошлого квартала, а последним последний день того же квартала
        1.9. Текущий год. Первым днем считается 1 января текущего года, а последним - сегодня
        1.10. Прошлый год. Первым днем считается 1 января прошлого года, а 31 декабря прошлого года
        1.11. Максимум. Максимальный временной диапазон. Начиная от сегодня, заканчивая 37 месяцами назад
    
<b>2. Уровень глубины отчета имеет следующие варианты:</b>
        2.1. Аккаунт. Самый высокий уровень. Отчеты на уровне всего аккаунта. Не детально
        2.2. Кампания. Отчеты на уровне рекламных кампаний. В рекламном аккаунте может быть несколько кампаний. Более детально
        2.3. Группа реклам. Средний уровень. В каждой кампании может быть несколько групп. Еще более детально
        2.4. Реклама. Самый глубокий уровень. Отчеты по каждой рекламе. Максимальная детальность
        
<b>3. Разбивка по времени имеет следующие варианты:</b>
        3.1. 1 - Ежедневный отчет. Отчет будет содержать статистику за каждый день временного диапазона. Детально
        3.2. 7 - Еженедельный отчет. Отчет будет содержать статистику за каждую неделю временного диапазона
        3.3. 15 - Полумесячный отчет. Отчет будет содержать статистику за каждые пол месяца временного диапазона
        3.4. 30 - Месячный отчет. Отчет будет содержать статистику за каждый месяц временного диапазона
        3.5. 90 - Квартальный отчет. Отчет будет содержать статистику за каждый квартал временного диапазона
""",

        'scheduler': """<b>Планировщик</b>

Нажав на кнопку в главном меню или вызвав меню с помощью команды /scheduler вы получите список активных точек(задач) 
планировщика.

Если планировщик пустой, то бот предложит добавить задачи. Для этого необходимо нажать на кнопку Добавить
Далее выбрать тип задачи, затем отправить список точек(задач) в виде <code>1. 00:00 2. 01:00 3. 02:35 и так далее</code> 
или 
<code>1. 00:00
2. 01:00
3. 02:35
и так далее</code>
 
 
Если планировщик имеет задачи, то появится список активных точек(задач) и будет предложено отредактировать или удалить
задачи
    1. Редактирование - полностью заменяет активные точки(задачи) у выбранного типа по отправленному вами шаблону
    2. Удаление - полностью удаляет точки(задачи) планировщика
""",
        'fast_report': """<b>Быстрый отчет</b>

Бот собирает информацию по всем активным аккаунтам, затем заносит полученные данные в базу данных 
и отправляет готовый отчет в формате .scv""",
        'add_user': """<b>Добавление пользователя в белый список</b>

Что-бы добавить пользователя в белый список, необходимо:
Отправить команду <code>/add_user *user_id*</code>, где user_id - ID пользователя
Для того, чтобы узнать ID, попросите этого пользователя воспользоваться ботом, в ответе от него будет указан ID""",
        'add_token': """<b>Добавление токена</b>
        
Что-бы добавить токен, необходимо:
Отправить команду <code>/add_token *service* *token*</code>, где
    *service* - сервис, для которого добавляется новый токен
    *token* - токен доступа. Выдается на сайте сервиса
    
На данный момент из доступных сервисов есть:
    1. Facebook - <code>Facebook</code>
    2. GetCourse - <code>GetCourse</code>

Для того, чтобы повторно увидеть актуальный список сервисов воспользуйтесь командой <code>/add_token services</code>""",
        'add_user_btn': 'Добавление пользователя',
        'add_tokens_btn': 'Добавление токена',
        'tokens_btn': 'Токены',
    },
}

commands = [
    {'command': '/start', 'description': 'Возврат к началу или обновить бота'},
    {'command': '/menu', 'description': 'Главное меню'},
    {'command': '/help', 'description': 'Помощь'},
    {'command': '/add_user', 'description': '<user_ID> - Добавить пользователя в белый список'},
    {'command': '/white_list', 'description': 'Посмотреть белый список'},
    {'command': '/tokens', 'description': 'Посмотреть список токенов'},
    {'command': '/add_token', 'description': '<service> <token> - Добавить новый токен'},
    {'command': '/fast_report', 'description': 'Получить быстрый отчет по всем доступным кампаниям'},
    {'command': '/scheduler', 'description': 'Настройка планировщика'}
]
