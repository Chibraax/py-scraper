#!/bin/python3

import argparse
from scrap import ProxyScraper

code_country = {'FR':'France','DE':'Germany','RU':'Russian Federation','US':'United States',
                'TH':'Thailand','IN':'India','SG':'Singapour','BR':'Brazil','FI':'Finland','IR':'Iran',
                'MY':'Malaysia','GB':'United Kingdom','AR':'Argentina','BD':'Bangladesh','JP':'Japan',
                'UG':'Uganda','AF':'Afghanistan','HK':'Hong Kong','UA':'Ukraine','CL':'Chile','KE':'Kenya',
                'TJ':'Tajikistan','MO':'Macau','NG':'Nigeria','KR':'Korea','CZ':'Czech Republic','RO':'Romania',
                'GE':'Georgia','UZ':'Uzbekistan','EC':'Ecuador','ES':'Spain','CA':'Canada','CO':'Colombia',
                'PY':'Paraguay','NL':'Netherlands','HU':'Hungary','ID':'Indonesia','PE':'Peru','TR':'Turkey',
                'GN':'Guinea','ZA':'South Africa','MW':'Malawi','AL':'Albania','KZ':'Kazakhstan','AU':'Australia',
                'MX':'Mexico','CR':'Costa Rica','PK':'Pakistan','TZ':'Tanzania','PL':'Poland','KH':'Cambodia',
                'MZ':'Mozambique','BY':'Belarus','GT':'Guatemala','BA':'Bosnia and Herzegovina','AM':'Armenia','IL':'Israel',
                'PH':'Philippines','PR':'Puerto Rico','ML':'Mali','EG':'Egypt','BW':'Botswana','ZW':'Zimbabwe','MN':'Mongolia',
                'CM':'Cameroon','MM':'Myanmar','TW':'Taiwan','SI':'Slovenia','AT':'Austria'
                }

        
classiq_url = 'https://free-proxy-list.net/'
socks_url = 'https://www.socks-proxy.net/'
ssl_url = 'https://www.sslproxies.org/'

#Parser
parser = argparse.ArgumentParser(description='default scrap HTTP/HTTPS proxy \nEx : python3 py-scraper.py --https --socks --country US')
group1 = parser.add_mutually_exclusive_group()
parser.add_argument("--https",help="Only HTTPS proxy will be scrap",action="store_true")
parser.add_argument("--socks",help="Only SOCKS proxy will be scrap",action="store_true")
parser.add_argument("--country",help="Select country of proxy Ex: US")
group1.add_argument("--countrycode",help="See all countrycode",action="store_true")
args = parser.parse_args()




if args.https and args.socks and args.country : #scrap socks/https with country
    print('\n=============== HTTPS ===============\n')
    prox_ssl = ProxyScraper()
    prox_ssl.scrap(proxytype=ssl_url,country=args.country)
    print('\n=============== SOCKS ===============\n')
    prox_socks = ProxyScraper()
    prox_socks.scrap(proxytype=socks_url,country=args.country)
    print()

elif args.https and args.socks : #scrap socks/https 
    print('\n=============== HTTPS ===============\n')
    prox_ssl = ProxyScraper()
    prox_ssl.scrap(proxytype=ssl_url)
    print('\n=============== SOCKS ===============\n')
    prox_socks = ProxyScraper()
    prox_socks.scrap(proxytype=socks_url)
    print()



elif args.https and args.country : #scrap https proxy with country
    prox_ssl = ProxyScraper()
    prox_ssl.scrap(proxytype=ssl_url,country=args.country)

    
elif args.socks and args.country : #scrap socks proxy with country 
    prox_socks = ProxyScraper()
    prox_socks.scrap(proxytype=socks_url,country=args.country)

elif args.socks : #scrap socks proxy
    prox_socks = ProxyScraper()
    prox_socks.scrap(proxytype=socks_url)

elif args.https : #scrap https
    prox_ssl = ProxyScraper()
    prox_ssl.scrap(proxytype=ssl_url)


elif args.countrycode : #Display all country code
    for code,country in code_country.items() : print(f'{country} : {code}')

elif args : #Default
    prox = ProxyScraper()
    prox.scrap(classiq_url)


