#! python3
# phoneAndEmail.py - Find phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)                           # separator
    (\d{4})                             # last4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
)''', re.VERBOSE)

# Email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
)''', re.VERBOSE)

# TODO: Find matches in clipboard text.

text = str(pyperclip.paste())

extPhone = phoneRegex.findall(text)
extEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extPhone:
    allPhoneNumbers.append(phoneNumber[0]) 

allEmails = []
for emails in extEmail:
    allEmails.append(emails[0])

""" for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' X' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0]) """

# TODO: Copy results to the clipboard.

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmails)
pyperclip.copy(results)