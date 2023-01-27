import config

# &&&     Messages    &&&
START_MESSAGE = """Привет, {name}!


Создавай контент или сгенерируй темы для контент-плана с помощью искусственного интеллекта

Чтобы начать, нажми на нужную кнопку"""


WAITING_RESULT_MESSAGE = "Происходит магия. Пожалуйста, подожди немного"

BAD_RESULTAT_MESSAGE = "Бывает такое, что я не совсем понимаю тему, " \
    "поэтому не могу дать ответ." \
    "Попробуй переформулировать тему или выбрать другую"

MAIN_MENU_TEXT = "Нажми на нужную кнопку"

# &&&     BUTTONS     &&&

MAIN_MENU_BUTTON = "Главное меню"

BACK_BUTTON = "Назад"


SANDBOX_HELLO_MESSAGE = """Ты запустил песочницу. Чтобы выйти пиши /menu.

Теперь каждое твоё сообщение воспринимается как вопрос."""

SERVICE_IS_UNAVAILABLE = """
Сервис временно не доступен.
Системные администраторы уже уведомлены о проблеме.

Приносим извинения за данный инцидент.
"""


UNEXCEPTED_ERROR = """
Произошла непредвиденная ошибка.
Системные администраторы уже уведомлены о проблеме.

Приносим извинения за данный инцидент.
"""
# --- CAPTCHA ---

CAPTCHA_IS_RIGHT = "Поздравляю ты не робот!"
CAPTCHA_QUESTION = "Проверка, что ты не робот\n{}"
CAPTCHA_TEMPLATE = "{first_value}{operation}{second_value}="


# --- REFERAL ---

REFERAL_URL_TEMPLATE = "vk.me/" + config.VK_GROUP_NAME
REFERAL_URL_TEMPLATE += "?ref={ref}&ref_source={ref_source}"

MESSAGE_WITH_REFERAL_URL_TEMP = "Твоя реферальная ссылка\n\n{url}"
