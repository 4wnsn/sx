### 新增内容开始 ###
from bs4 import BeautifulSoup
from lib.parser.BaseParser import BaseParser

class HtmlParser(BaseParser):
    def read(self):
        if r'://' in self.file_path:
            response = urllib.request.urlopen(self.file_path)
            html = response.read()
        else:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                html = f.read()

        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()

        idcard_result = self.idcard_search(text)
        if idcard_result:
            self.sensitive_dict['idcard'].append(idcard_result)

        phone_result = self.phone_search(text)
        if phone_result:
            self.sensitive_dict['phone'].append(phone_result)

        email_result = self.email_search(text)
        if email_result:
            self.sensitive_dict['email'].append(email_result)

        self.sensitive_word_search(text)

        self.reduce_error_report()
        return self.sensitive_dict
### 新增内容结束 ###