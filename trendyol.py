import requests
from bs4 import BeautifulSoup
from sendMail import sendMail
import time


url = "https://www.trendyol.com/pull-bear/hafif-sisme-mont-p-762234575"


def checkPrice(url,paramPrice):
        headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
        page = requests.get(url, headers=headers)

        htmlPage = BeautifulSoup(page.content,'html.parser')

        productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

        price = htmlPage.find("span", class_="prc-dsc").getText()

        image = htmlPage.find("div", classs_="base-product-image")

        convertedPrice = float(price.replace(",",".").replace(" TL",""))

        if (convertedPrice <= paramPrice):
            print ("Ürünün fiyatı düştü...")
            htmlEmailContent = """\
                <html>
                <head></head>
                <body>
                <h3>{0}</h3>
                <br/>
                {1}
                <br/>
                <p>Ürün Linki: {2}</p>
                </body>
                </html>
            """.format(productTitle,image,url)
            sendMail("kajeho4820@rdluxe.com", "Ürünün Fiyatı Düştü...",htmlEmailContent)
        else:
            price("Ürünün Fiyatı Düşmedi")

while(True):
    checkPrice(url,2000)
    time.sleep(3)