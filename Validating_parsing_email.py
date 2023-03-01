import email.utils
import re
n = int(input())
email_regex = re.compile(r'^[A-Za-z][\w\.-]+@[A-Za-z]+\.[A-Za-z]{1,3}$')
for _ in range(n):
    parsed = email.utils.parseaddr(input())
    if re.fullmatch(email_regex, parsed[1]):
        print (email.utils.formataddr(parsed))
