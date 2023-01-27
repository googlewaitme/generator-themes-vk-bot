from utils.skill import Skill


content_plan_skill = Skill(
    short_name='create_content_plan',
    verbose_name='Создать контент план',
    name='generate content plan',

    request_for_skill_description="""Напиши нишу, под которую требуются темы

Например, \"Недвижимость\"""",

    openai_data={
        "model": 'text-davinci-003',
        "max_tokens": 2000,
        "temperature": 0.3,
        "top_p": 1.0,
        "frequency_penalty": 0.1,
        "presence_penalty": 0.1,
        "stop": ['16.']
    },
    prompt_template="Придумай 15 тем для постов в соцсетях по теме {request}",
    button_name="Придумать темы",
    restart_button_name='Ещё темы'
)


create_article_skill = Skill(
    short_name='create_article_skill',
    verbose_name='Сгенерировать статью',
    name='create article',

    request_for_skill_description="""Напиши тему для поста

Например, "Как выгодно вложить деньги в недвижимость?""",

    openai_data={
        "model": 'text-davinci-003',
        "max_tokens": 2000,
        "temperature": 0.3,
        "top_p": 1.0,
        "frequency_penalty": 0.1,
        "presence_penalty": 0.1,
        "stop": ['16.']
    },
    prompt_template="Напиши статью на тему {request}",
    button_name="Создать пост",
    restart_button_name="Новый вариант"
)
