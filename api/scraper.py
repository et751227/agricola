from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests

class Stock(ABC):

    def __init__(self,ticket):
        self.stockTicket = ticket #股票代號
        
    @abstractmethod
    def scrape(self):
        pass
        
class YahooStock(Stock):

    def scrape(self):
    
        content = ""
   
        response = requests.get(
            "https://tw.stock.yahoo.com/quote/" + self.stockTicket )
            
        soup = BeautifulSoup(response.content, "html.parser")
    
        cards = soup.find_all(
            'div',{'class':'D(f) Ai(c) Mb(6px)'})
            
        for card in cards:
        
            stock_name = card.find( #股票名稱
                "h1",{"class":"C($c-link-text) Fw(b) Fz(24px) Mend(8px)"}).getText()
            
            stock_ticket = card.find( #股票代號
                "span",{"class":"C($c-icon) Fz(24px) Mend(20px)"}).getText()
                
        cards = soup.find_all(
            'div',{'class':'D(f) Ai(fe) Mb(4px)'})      

        for card in cards:
        
            stock_price = card.find( #股票價格
                "span",{"class":"Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"})
            
            if not stock_price:
                price = card.find( #股票價格
                "span",{"class":"Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"}).getText()
            else:
                price = card.find( #股票價格
                "span",{"class":"Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"}).getText()
                
        content += f"股票名稱:{stock_name} \n 股票代號:{stock_ticket} \n 股票價格:{price}"
      
        return content
    
 