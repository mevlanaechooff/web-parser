import requests
from bs4 import BeautifulSoup
import time

print("""

    WEB PARSER'E HOŞGELDİNİZ

            coderby: @mevlanaechooff ' @sehogrkan
    
""")

url = input("URL GİRİNİZ: ")
print("***İşlem başlıyor***")
time.sleep(3)
response = requests.get(url)

soup = BeautifulSoup(response.text , "html.parser")

print("***Devam ediliyor***")
time.sleep(3)

print("""

        Parçalama yapabileceğiniz etiketler:
    1    H1
    2    H2 
    3    H3 
    4    H4
    5    a
    6    pre
    7    p
    8    body
    9    head
    10    title

""")

while True:
    a = int(input("Etiket Giriniz: "))

    if a == 1:
        h1 = soup.find('h1')

        if h1:
            print(h1.text)
        else:
            print("Etiket bulunamadı")

    elif a == 2:
        h2 = soup.find('h2')

        if h2:
            print(h2.text)
        else:
            print("Etiket bulunamadı")

    elif a == 3:
        h3 = soup.find('h3')

        if h3:
            print(h3.text)
        else:
            print("Etiket bulunamadı")

    elif a == 4:
        h4 = soup.find('h4')

        if h4:
            print(h4.text)
        else:
            print("Etiket bulunamadı")

    elif a == 5:
        links = soup.find_all('a')

        if links:
            for link in links:
                print(link.text)
        else:
            print("Etiket bulunamadı")

    elif a == 6:
        pre = soup.find('pre')

        if pre:
            print(pre.text)
        else:
            print("Etiket bulunamadı")

    elif a == 7:
        p = soup.find('p')

        if p:
            print(p.text)
        else:
            print("Etiket bulunamadı")

    elif a == 8:
        body = soup.find('body')

        if body:
            print(body.text)
        else:
            print("Etiket bulunamadı")

    elif a == 9:
        head = soup.find('head')

        if head:
            print(head.text)
        else:
            print("Etiket bulunamadı")

    elif a == 10:
        title
