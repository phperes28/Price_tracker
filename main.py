from bs4 import BeautifulSoup
import requests
import smtplib
from creds import MY_EMAIL, MY_PASSWORD

product_url = "https://produto.mercadolivre.com.br/MLB-1242679647-estaco-de-musculaco-com-80kg-aparelho-ginastica-academia-_JM#position=4&search_layout=stack&type=item&tracking_id=57ac4255-99e3-401b-b325-798cfafa75dd"
response = requests.get(product_url)
ml_response = response.text

all_prices =[]

soup = BeautifulSoup(ml_response,"html.parser")


prices = soup.find_all(name="span", class_="price-tag-fraction")

for price in prices:
    just_price = price.getText()
    all_prices.append(just_price)

print(all_prices)

#Deppending if price is disccounted or not
if len(all_prices) == 3:  #3 different prices showing on page
    current_price = all_prices[1].replace(".", "")
else:
    current_price = all_prices[0].replace(".", "")

print(current_price)

if int(current_price) < 2600:  
    with smtplib.SMTP('smtp.gmail.com') as connection:

                connection.starttls()  #secures connection
                connection.login(user= MY_EMAIL, password= MY_PASSWORD)
                connection.sendmail(
                    from_addr= MY_EMAIL,
                    to_addrs= 'someemail@gmail.com',
                    msg=f'Subject: Price Update! \n\nThe price for the workout station dropped to {current_price}!\n{product_url}'
                    )

