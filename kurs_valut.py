'''получение курса валют из гугла.''' 


import requests 
from bs4 import BeautifulSoup




# доллары к евро
def kurs_dollar_euro():
    Dollar_EURO = 'https://www.google.com/search?newwindow=1&rlz=1C1SQJL_ruUA863UA863&sxsrf=ALeKk003vdOBtjNiFBYe_MhjduF_nuchow%3A1609165890725&ei=QuzpX-bnK9DJrgTN9JPQCQ&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%8B+%D0%B2+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%8B&gs_lcp=CgZwc3ktYWIQAxgAMgkIIxAnEEYQggIyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgcIABAUEIcCMgIIADICCAAyAggAMgIIADoECAAQRzoECCMQJzoLCAAQsQMQxwEQrwE6CAgAEMcBEK8BOgUILhCxAzoICAAQChABECo6BggAEAoQAToKCAAQxwEQrwEQCjoHCCMQ6gIQJzoHCC4Q6gIQJzoICAAQxwEQowI6BAgAEEM6BwgAELEDEEM6CggAELEDEIMBEEM6DAgjELECECcQRhCCAjoHCCMQsQIQJzoHCAAQsQMQCjoKCAAQsQMQgwEQCjoKCAAQsQMQFBCHAlCFVFjAhQFgro4BaAZwAngAgAHnAYgBwg2SAQYwLjEyLjGYAQCgAQGqAQdnd3Mtd2l6sAEKyAEIwAEB&sclient=psy-ab'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    full_page = requests.get(Dollar_EURO, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

    de = float(convert[0].text.replace(',' , '.'))
    
    return(de)

    # print('DOLL/EURO ', de)
    # print('EURO/DOLL ', 1/de)




# доллары к гривне
def kurs_doll_grn():
    Dollar_GRN = 'https://www.google.com/search?newwindow=1&rlz=1C1SQJL_ruUA863UA863&sxsrf=ALeKk03nSXh22ok7W56uTg2DnYlraj6YFQ%3A1609172095368&ei=fwTqX5CCFqGvrgTq9rWwAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&gs_lcp=CgZwc3ktYWIQARgFMgkIIxAnEEYQggIyBAgjECcyBAgjECcyCggAELEDEIMBEEMyBwgAELEDEEMyBwgAELEDEEMyBwgAELEDEEMyBAgAEEMyBAgAEEMyBAgAEEM6BAgAEEc6BwgjEOoCECc6BwgAEBQQhwI6AggAOggIABDHARCvAToICAAQxwEQowJQ3rYBWPW_AWCp8QFoAnACeACAAZIBiAHcBZIBAzEuNZgBAKABAaoBB2d3cy13aXqwAQrIAQjAAQE&sclient=psy-ab'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    full_page = requests.get(Dollar_GRN, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

    dh = float(convert[0].text.replace(',' , '.'))
    
    return(dh)
    
    # print('DOLL/GRN ', dh)
    # print('GRN/DOLL ', 1/dh)



# евро к гривне
def kurs_euro_grn():
    EURO_GRN = 'https://www.google.com/search?newwindow=1&rlz=1C1SQJL_ruUA863UA863&sxsrf=ALeKk00IhTSayLeQ8b4ALEXQWOIFl_2CqA%3A1609172127300&ei=nwTqX4TvEemyrgTY4pbAAg&q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_lcp=CgZwc3ktYWIQAzIMCAAQsQMQQxBGEIICMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABANOgYIABAHEB5QycEIWPHHCGDTyghoAHABeACAAdUCiAGTB5IBBzAuMi4wLjKYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjEup6oifHtAhVpmYsKHVixBSgQ4dUDCA0&uact=5'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    full_page = requests.get(EURO_GRN, headers = headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

    eh = float(convert[0].text.replace(',' , '.'))

    return(eh)

    # print('EURO/GRN ', eh)
    # print('GRN/EURO ', 1/eh)


# kurs_doll_grn()
# def kurs_vseh_valut():
    # kurs_doll_grn()
    # kurs_euro_grn()
    # kurs_dollar_euro()

