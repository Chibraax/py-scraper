#!/bin/python3

from bs4 import BeautifulSoup
import requests


__all__ = ['ProxyScraper'] #Limit import to ProxyScraper class

class ProxyScraper:

    def __init__(self) : 

        #Variable link to <tr> position on web sites
        self.count_ip=0
        self.count_port=1
        self.count_country=2

        #To refer each proxy to their country
        self.country_proxy = {'FR':[],'DE':[],'RU':[],'US':[],'TH':[],'IN':[],'SG':[],'BR':[],'FI':[],'IR':[],
                        'MY':[],'GB':[],'AR':[],'BD':[],'JP':[],'UG':[],'AF':[],'HK':[],'UA':[],'CL':[],'KE':[],'TJ':[],'MO':[],'NG':[],'KR':[],
                        'CZ':[],'RO':[],'GE':[],'UZ':[],'EC':[],'ES':[],'CA':[],'CO':[],'PY':[],'NL':[],'HU':[],'ID':[],'NP':[],'PE':[],'TR':[],
                        'NI':[],'GN':[],'ZA':[],'MW':[],'AL':[],'KZ':[],'AU':[],'MX':[],'CR':[],'PK':[],'TZ':[],'PL':[],'KH':[],'MZ':[],'BY':[],
                        'GT':[],'BA':[],'AM':[],'IL':[],'PH':[],'PR':[],'ML':[],'EG':[],'BW':[],'ZW':[],'MN':[],'CM':[],'MM':[],'TW':[],'SI':[],
                        'AT':[]
                        }


    def scrap(self,proxytype,country=None) : 
        'Scrap proxy'

        self.r = requests.get(proxytype) #GET content of web page
        self.soup1 = BeautifulSoup(self.r.content,'lxml') # bs4 object
        self.soup = self.soup1.tbody #GET <tbody> 
        self.all_td = self.soup.findAll('td') #GET all <td>

        for x in self.all_td : 
            try :
                if country == None : print(f'{self.all_td[self.count_ip].text}:{self.all_td[self.count_port].text}')
                #Add the proxy to country list
                if self.all_td[self.count_country].text in self.country_proxy.keys() : self.country_proxy[self.all_td[self.count_country].text] = self.country_proxy[self.all_td[self.count_country].text] + [f'{self.all_td[self.count_ip].text}:{self.all_td[self.count_port].text}']

                self.count_ip+=8
                self.count_port+=8
                self.count_country+=8
            except IndexError  : pass

        if country : 
            for xx in self.country_proxy.get(country) : 
                print(xx)

        return True


if __name__ == '__main__' : 

    prox = ProxyScraper()
    prox.scrap(proxytype='https://free-proxy-list.net/')
