import re

def email_check(email):
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Z|a-z]{2,}\b')
    if email_regex.fullmatch(email) and len(list(re.finditer(r'(\D*)@.',email))) != 0:
        print('OK')
    else:
        print('WRONG')

email_check(email = input())