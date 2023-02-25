from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests

class Stock(ABC):

    def __init__(self,ticket):
        self.stockTicket = stockTicket #股票代號
        
    @abstractmethod
    def scrape(self):
        pass
        
class YahooStock(Stock):

    def scrape(self):
        
        content += "我是yahoo"
        
        #url = "https://tw.stock.yahoo.com/quote/" + self.stockTicket
        
        #content += url
        
        #response = requests.get(
        #    "https://tw.stock.yahoo.com/quote/" + self.stockTicket )
            
        #soup = BeautifulSoup(response.content, "html.parser")
    
        #cards = soup.find_all(
        #    'div',{'class':'D(f) Ai(fe) Mb(4px)'})
    
        #content += "沒有找到網頁"
    
        #for card in cards:
    
        #    price = card.find( #股票價格
        #        "span",{"class":"Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"}).getText()
    
        #content += f"股票價格:{price}"
      
        return content
    
 