# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:25:17 2021
From Automate the Boring stuff with Python
@author: kueif
"""

import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

maxLen = len(messages) - 1  # There's a -1, index starts at 0
randInt = random.randint(0, maxLen)

print(messages[randInt])