# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         classPractice
# Description:  
# Author:       Dell
# Date:         2019/10/15
#-------------------------------------------------------------------------------

def text_create(name, msg):
    desktop_path = 'C://Users//Dell//Desktop//'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')

def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)

def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)
    print(clean_msg)

censored_text_create('Try', 'lame!lame!lame!')

# text_create('hello', 'Hello World, python')

print(text_filter('Python is lame!'))