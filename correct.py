import service
import re
import requests


class InstagramLinksCorrect:
    patterns=service.OldPatterns()
    """Класс предоставляющий методы для проверки корректности ссылок"""
    account_link_pattern=re.compile(patterns.account_link_pattern)
    image_link_pattern=re.compile(patterns.image_link_pattern)
    def isAccountLink(self,link):
        if re.match(self.account_link_pattern,link):
            return True
        return False

    def isImageLink(self,link):
        if re.match(self.image_link_pattern,link):
            return True
        return False

    def ImageLinkIsValid(self,link):
        if self.isImageLink(link):
            resp=requests.get(link)
            if(resp.status_code == 404):
                return False
            return True
        return False

    def AccountLinkIsValid(self,link):
        if self.isAccountLink(link):
            resp=requests.get(link)
            if(resp.status_code == 404):
                return False
            return True
        return False