from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")


### MONKEY TYPE ###

# driver.get("https://www.monkeytype.com/")
#
# ####### METHOD 1 #######
# words = []
# words_typed = []
#
# while True:
#     #add words
#     words_all = driver.find_elements_by_class_name("word")
#
#     for word in words_all:
#         if word in words:
#             continue
#         else:
#             try:
#                 if word.text =='':
#                     pass
#                 else:
#                     words.append(word.text)
#                     print(f"Word: {word.text}")
#             except Exception as e:
#                 print(e)
#
#     for i in range(0, len(words)):
#         if words[i] in words_typed:
#             continue
#         else:
#             print(words[i])
#             actions = ActionChains(driver)
#             actions.send_keys(words[i] + ' ')
#             actions.perform()
#             words_typed.append(words[i])
#
# ####### METHOD 2 #######
#
#
# driver.close()
# driver.quit()


# ### 10 fast fingers ###
#
# driver.get("https://10fastfingers.com/typing-test/english")
#
# highlighted = driver.find_element_by_xpath('''//*[@id="row1"]//span[class='highlight']''')
#
# word = []
#
# for words in highlighted:
#     word.append(words.text)
#     print(words)
#
# print(word)

###local hosted site lol ###

#threading to make it faster lul
import threading

driver.get('http://localhost:1010/')

def auto():
    for i in range(0, 500):
        word = driver.find_element_by_id('text')
        txtinput = driver.find_element_by_id('typing')

        txtinput.send_keys(word.text)
        txtinput.send_keys(Keys.ENTER)

threads = [];

for i in range(0, 10):
    thread = threading.Thread(target=auto)
    threads.append(thread)
    thread.start()
    for thread in threads:
        thread.join()
