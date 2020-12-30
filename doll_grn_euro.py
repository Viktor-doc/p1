import requests 
from bs4 import BeautifulSoup

# блок получения курса валют от гугла
print('подождите идет загрузка...')
# доллары к евро
Dollar_EURO = 'https://www.google.com/search?newwindow=1&rlz=1C1SQJL_ruUA863UA863&sxsrf=ALeKk003vdOBtjNiFBYe_MhjduF_nuchow%3A1609165890725&ei=QuzpX-bnK9DJrgTN9JPQCQ&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%8B+%D0%B2+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%8B&gs_lcp=CgZwc3ktYWIQAxgAMgkIIxAnEEYQggIyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgcIABAUEIcCMgIIADICCAAyAggAMgIIADoECAAQRzoECCMQJzoLCAAQsQMQxwEQrwE6CAgAEMcBEK8BOgUILhCxAzoICAAQChABECo6BggAEAoQAToKCAAQxwEQrwEQCjoHCCMQ6gIQJzoHCC4Q6gIQJzoICAAQxwEQowI6BAgAEEM6BwgAELEDEEM6CggAELEDEIMBEEM6DAgjELECECcQRhCCAjoHCCMQsQIQJzoHCAAQsQMQCjoKCAAQsQMQgwEQCjoKCAAQsQMQFBCHAlCFVFjAhQFgro4BaAZwAngAgAHnAYgBwg2SAQYwLjEyLjGYAQCgAQGqAQdnd3Mtd2l6sAEKyAEIwAEB&sclient=psy-ab'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
full_page = requests.get(Dollar_EURO, headers = headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

de = float(convert[0].text.replace(',' , '.'))

print('doll/euro ', de)
print('euro/doll ', 1/de)


# доллары к гривне
Dollar_GRN = 'https://www.google.com/search?newwindow=1&rlz=1C1SQJL_ruUA863UA863&sxsrf=ALeKk03nSXh22ok7W56uTg2DnYlraj6YFQ%3A1609172095368&ei=fwTqX5CCFqGvrgTq9rWwAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&gs_lcp=CgZwc3ktYWIQARgFMgkIIxAnEEYQggIyBAgjECcyBAgjECcyCggAELEDEIMBEEMyBwgAELEDEEMyBwgAELEDEEMyBwgAELEDEEMyBAgAEEMyBAgAEEMyBAgAEEM6BAgAEEc6BwgjEOoCECc6BwgAEBQQhwI6AggAOggIABDHARCvAToICAAQxwEQowJQ3rYBWPW_AWCp8QFoAnACeACAAZIBiAHcBZIBAzEuNZgBAKABAaoBB2d3cy13aXqwAQrIAQjAAQE&sclient=psy-ab'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
full_page = requests.get(Dollar_GRN, headers = headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

dh = float(convert[0].text.replace(',' , '.'))

print('DOLL/GRN ', dh)
print('GRN/DOLL ', 1/dh)


# евро к гривне
EURO_GRN = 'https://www.google.com/search?newwindow=1&rlz=1C1SQJL_ruUA863UA863&sxsrf=ALeKk00IhTSayLeQ8b4ALEXQWOIFl_2CqA%3A1609172127300&ei=nwTqX4TvEemyrgTY4pbAAg&q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_lcp=CgZwc3ktYWIQAzIMCAAQsQMQQxBGEIICMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABANOgYIABAHEB5QycEIWPHHCGDTyghoAHABeACAAdUCiAGTB5IBBzAuMi4wLjKYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjEup6oifHtAhVpmYsKHVixBSgQ4dUDCA0&uact=5'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
full_page = requests.get(EURO_GRN, headers = headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

eh = float(convert[0].text.replace(',' , '.'))

print('EURO/GRN ', eh)
print('GRN/EURO ', 1/eh)


print('для выхода нажмите y')

# сделать визуальную оболочку

# цикл выбора валюты
while True:
    print('выберите валюты')
    money1 = str(input('что меняем? d, h, e? '))
    
    if money1 == 'y':
        print('спасибо, приходите еще!')
        break 
    money2 = str(input('на что меняем? d, h, e? '))
    
    if money2 == 'y':
        print('спасибо, приходите еще!')
        break 
        
# оптимизировать код с выбором валют: цикл фор выбирает из таблицы валют 

    if money1 == 'd' and money2 == 'h':
        kurs = 1/dh
        valuta = ('грн')
        sootn1 = ('1 долл это')
        sootn2 = (dh)
        
    elif money1 == 'd' and money2 == 'e':
        kurs = 1/de
        valuta = ('euro')
        sootn1 = ('1 долл это')
        sootn2 = (de)
        
    elif money1 == 'e' and money2 == 'd':
        kurs = de 
        valuta = ('doll')    
        sootn1 = ('1 евро это')
        sootn2 = (1/de)
        
    elif money1 == 'h' and money2 == 'd':
        kurs = dh
        valuta = ('doll')
        sootn1 = ('1 грн это')
        sootn2 = (1/dh)
        
    elif money1 == 'h' and money2 == 'e':
        kurs = eh
        valuta = ('euro')
        sootn1 = ('1 грн это')
        sootn2 = (1/eh)
        
    elif money1 == 'e' and money2 == 'h':
        kurs = 1/eh
        valuta = ('grn')
        sootn1 = ('1 евро это')
        sootn2 = (eh)
        
    else :
        print ('внимательней, бро')
        continue 

    print(sootn1, sootn2, valuta)

# обменный цикл

    while True:
        print('для смены валюты нажмите y')
        money3 = input('скока даешь? ')
        if money3 == 'y':
            print('для выхода нажмите y')
            break        
            
        else:
            def is_digit(money3):        # ф проверяет, чтоб было число с точкой. 
                if money3.isdigit():
                   return True
                else:
                    try:
                        float(money3)
                        return True
                    except ValueError:
                        return False
                
        if is_digit(money3) == False:
            print ('только цыфры,а копейки через точку!!!')
            continue
        else:
            print('ok')
               
        money = float(money3)
        cache = round(money / kurs, 2)
        
        print ('получишь', cache, valuta)
         
print('goodbay')







