import re
import json

from lib.utils.regex import PHONE_REGEX, EMAIL_REGEX, IDCARD_REGEX
### 新增内容开始 ###
# 加载敏感词数据集
with open('WSPIH/data/SensitiveLexicon.json', 'r') as f:
    SENSITIVE_LEXICON = set(json.load(f))
### 新增内容结束 ###

class BaseParser():
    def __init__(self, file_path):
        self.file_path = file_path
        self.sensitive_dict = {'phone': [], 'idcard': [], 'email': [], 'sensitive_words': []}  ### 新增内容：添加敏感词汇检测结果

    @classmethod
    def re_search(cls, regex_patern, item_value):
        result = re.search(regex_patern, item_value)
        if result:
            return result.group()

    @classmethod
    def phone_search(cls, item_value):
        return cls.re_search(PHONE_REGEX, item_value)

    @classmethod
    def idcard_search(cls, item_value):
        return cls.re_search(IDCARD_REGEX, item_value)

    @classmethod
    def email_search(cls, item_value):
        return cls.re_search(EMAIL_REGEX, item_value)

    ### 新增内容开始 ###
    @classmethod
    def sensitive_word_search(cls, item_value):
        found_words = []
        for word in SENSITIVE_LEXICON:
            if word in item_value:
                found_words.append(word)
        return found_words
    ### 新增内容结束 ###

    def reduce_error_report(self):
        '''
        减少误报
        '''
        for key, sensitive_list in self.sensitive_dict.items():
            if len(sensitive_list) < 4:
                self.sensitive_dict[key] = []