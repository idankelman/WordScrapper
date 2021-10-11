from selenium import webdriver
import json

driver = webdriver.Chrome()
driver.get('https://anvaka.github.io/common-words/#?lang=cs')

input("wait")
TextBox = driver.find_elements_by_class_name('word')
# TextBox.send_keys('IdanHai')

#SearchBtn = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# SearchBtn.click()
T = []
i = 1


rank = 'rank'
word = 'word'
maxWords = 120
print(len(TextBox))
for t in TextBox:
    if len(t.text)>2:
        f = '{'
        f += '"{}": {} , "{}": "{}"'.format(rank, i, word, t.text)
        f += '}'
        if i != len(TextBox) or i != maxWords:
            f += ','
        T.append(f)
        if(i == maxWords):
            break
        print(f)
        # input("wait")
        i = i+1


with open('new_states.json', 'w') as f:
    json.dump(T, f)

input("waiting")
