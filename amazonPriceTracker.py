import bs4
import urllib.request
import smtplib
import time

prices_list = []

def check_price():
    url = "https://www.amazon.in/Harry-Potter-ChildrenS-Paperback-Boxed/dp/1408856778/ref=sr_1_1?crid=3TPFSHOT3RL42&dchild=1&keywords=harry+potter+books+set&qid=1617425627&sprefix=harry+potter+books%2Caps%2C436&sr=8-1"
    url_cont = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(url_cont, "html.parser")

    print(soup.prettify())

    prices = soup.find(id="a-autoid-8").get_text()
    prices = float(prices.replace(",", "").replace("₹", ""))
    prices_list.append(prices)
    return prices

def send_email(message, sender_email, sender_password, receiver_email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    s.sendmail(sender_email, receiver_email, message)
    s.quit()

def price_decrease_check(price_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False

count = 1
while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(prices_list)
        if flag:
            decrease = prices_list[-1] - prices_list[-2]
            message = f"The price decrease by {decrease} rupees."
            send_email(message, sender_email, sender_password, receiver_email)
    time.sleep(43000)
    count += 1
