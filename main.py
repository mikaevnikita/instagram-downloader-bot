import telebot
import service
import requests
import re
from correct import InstagramLinksCorrect
from bs4 import BeautifulSoup
import logging

class ParseHashes:
    patterns=service.OldPatterns()
    code_with_hash_pattern=re.compile(r'"code"[ ]*:[ ]*"{}"'.format(patterns.image_hash_pattern))
    hash_pattern=re.compile(patterns.image_hash_pattern)
    def get_hashes(self,page_source):
        temp_result=re.findall(self.code_with_hash_pattern,page_source)
        hashes = []
        for code_with_hash in temp_result:
            temp=re.findall(self.hash_pattern,code_with_hash)
            code,hash=temp[0],temp[1]
            hashes.append(hash)
        return tuple(hashes)

def get_source_by_link(link):
    links_tester=InstagramLinksCorrect()
    if not links_tester.ImageLinkIsValid(link):
        return None
    page_source=requests.get(link).text
    soup=BeautifulSoup(page_source,'html.parser')
    for meta_tag in soup.find_all('meta'):
        if meta_tag.get('property', None) == 'og:image':
            return meta_tag.get("content", None)


def get_tuple_of_sources_by_account(link):
    """Класс выдает кортеж ссылок по ссылке на профиль."""
    links_tester = InstagramLinksCorrect()
    if not links_tester.AccountLinkIsValid(link):
        return None

    page_source = requests.get(link).text
    parser=ParseHashes()
    hashes=parser.get_hashes(page_source)

    sources=[]
    for hash in hashes:
        source=get_source_by_link('http://instagram.com/p/{}'.format(hash))
        sources.append(source)
    return tuple(sources)

def get_links_from_message(message):
    patterns=service.NewPatterns()
    acc_reg=re.compile(patterns.account_link_pattern)
    im_reg=re.compile(patterns.image_link_pattern)
    account_links=re.findall(acc_reg,message)
    image_links=re.findall(im_reg,message)
    return account_links,image_links


bot=telebot.TeleBot(token=service.telegram_token)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, service.welcome_message)



@bot.message_handler(content_types=['text'])
def handle_message(message):
    account_links,image_links=get_links_from_message(message.text)
    sources=[]
    for account_link in account_links:
        sources_by_account_link=get_tuple_of_sources_by_account(account_link)
        sources.extend(sources_by_account_link)
    for image_link in image_links:
        source=get_source_by_link(image_link)
        sources.append(source)
    for i in range(len(sources)):
        link=sources[i]
        bot.send_message(message.chat.id,'<a href="{}">{}</a>'.format(link,i),parse_mode='HTML')

logger=telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot.polling(none_stop=True)