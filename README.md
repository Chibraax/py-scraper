Python proxy scraper
=============================

This package can scrap HTTP/HTTPS/SOCKS proxy from specific country

You can install with pip : 

pip3 install py-scraper


Example : 

    python3 py-scraper.py --https --socks --country US

    OR If you want use it at module 

    import py_scraper

Argument : 

    --socks : Scrap only socks proxy
    --https : Scrap only HTTPS proxy
    --country <??> : Scrap only proxy from specific country (see --countrycode)
    --countrycode : See all code country
    By default py_scraper will scrap HTTP/HTTPS proxy

py-scraper scrap his proxy on : 

    https://free-proxy-list.net/
    https://www.socks-proxy.net/
    https://www.sslproxies.org/
