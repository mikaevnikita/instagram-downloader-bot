telegram_token=''

welcome_message="""
Привет. Я помогу тебе скачать фото из Instagram.
Пришлешь ссылку на профиль - скачаю все фото
Пришлешь ссылку на фото - скачаю
"""

class OldPatterns:
    hl_pattern = r'hl=[a-z]{2}(\-[a-z]{2})?'
    http_pattern = r'((http|https):\/\/)(www\.)?'
    login_pattern = r'[a-zA-Z0-9_\.]*[a-zA-Z]+[a-zA-Z0-9_\.]*'
    image_hash_pattern = r'[a-zA-Z0-9_\-]*[a-zA-Z]+[a-zA-Z0-9_\-]*'
    taken_by_pattern = r'taken-by=[a-zA-Z0-9_\.]*[a-zA-Z]+[a-zA-Z0-9_\.]*'
    account_link_pattern = r'^{0}instagram.com/{1}(\/\?{2})?\/?$'.format(http_pattern, login_pattern, hl_pattern)
    image_link_pattern = r'^{0}instagram.com/p/{1}(\/\?{2})?(\/\?{3})?(&{3})?\/?$'.format(http_pattern,
                                                                                          image_hash_pattern,
                                                                                          taken_by_pattern, hl_pattern)
class NewPatterns:
    hl_pattern = r'hl=[a-z]{2}(?:\-[a-z]{2})?'
    http_pattern = r'(?:(?:http|https):\/\/)(?:www\.)?'
    login_pattern = r'[a-zA-Z0-9_\.]*[a-zA-Z]+[a-zA-Z0-9_\.]*'
    image_hash_pattern = r'[a-zA-Z0-9_\-]*[a-zA-Z]+[a-zA-Z0-9_\-]*'
    taken_by_pattern = r'taken-by=[a-zA-Z0-9_\.]*[a-zA-Z]+[a-zA-Z0-9_\.]*'
    account_link_pattern = r'\b({0}instagram.com/{1}(?:\/\?{2})?\/?)\b'.format(http_pattern, login_pattern, hl_pattern)
    image_link_pattern = r'\b({0}instagram.com/p/{1}(?:\/\?{2})?(?:\/\?{3})?(?:&{3})?\/?)\b'.format(http_pattern,
                                                                                                    image_hash_pattern,
                                                                                                    taken_by_pattern,
                                                                                                    hl_pattern)
