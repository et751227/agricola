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
        
        dividends_response = requests.get(
            "https://tw.stock.yahoo.com/quote/" + self.stockTicket + "/dividend")
        
        dividends_soup = BeautifulSoup(dividends_response.content, "html.parser")
                
        stock_dividends = dividends_soup.find_all('div',{"class":'Bgc(#fff) table-row D(f) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider) H(40px)'})
        
        for stock_dividend in stock_dividends:
                stock_dividends_season = stock_dividend.find('div',{"class":'D(f) W(84px) Ta(start)'}).get_text()
                stock_dividends_money = stock_dividend.find('div',{"class":'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(62px)'}).get_text()
                stock_dividends_son = stock_dividend.find('div',{"class":'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(62px)'}).get_text()
                stock_dividends_delete = stock_dividend.find('div',{"class":'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(108px)'}).get_text()
                stock_dividends_get = stock_dividend.find('div',{"class":'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(108px)'}).get_text()
                stock_dividends_recover = stock_dividend.find('div',{"class":'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(70px)'}).get_text()
        
        content += f"股票名稱:{stock_name} \n"\
                    f"股票代號:{stock_ticket} \n"\
                    f"股票價格:{price} \n"\
                    "------------------------ \n"\
                    f"股利所屬期間:{stock_dividends_season} \n"\
                    f"現金股利:{stock_dividends_money} \n"\
                    f"股票股利:{stock_dividends_son} \n"\
                    f"除息日:{stock_dividends_delete} \n"\
                    f"發放日:{stock_dividends_get} \n"\
                    f"填息天數:{stock_dividends_recover} \n"
      
        return content
    
 