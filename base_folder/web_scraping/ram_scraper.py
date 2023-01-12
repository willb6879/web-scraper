from bs4 import BeautifulSoup
import requests
from lxml import etree
import datetime
import csv

MY_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

def get_dom( url, USER_AGENT ):
    html_text = requests.get( url, headers={'User-Agent':
        MY_USER_AGENT} ).text
    soup = BeautifulSoup( html_text, 'html.parser')
    dom = etree.HTML(str(soup)) # creates dom object
    return dom

def update():
    # SK Hynix Samsung DDR4 16Gb (2Gx8) 2666 Spot Prices
    hynix_ddr4_spot_dh = dom.xpath('/html/body/div/div/table/tbody/tr[2]/td[1]/div[2]/div[1]/table[2]/tbody/tr[2]/td[2]')[0].text 
    hynix_ddr4_spot_dl = dom.xpath('/html/body/div/div/table/tbody/tr[2]/td[1]/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]')[0].text

    # SK Hynix Samsung, Spectek, DDR4 16Gb (2Gx8) eTT Spot Prices
    spectek_ddr4_spot_dh = dom.xpath('/html/body/div/div/table/tbody/tr[2]/td[1]/div[2]/div[1]/table[2]/tbody/tr[3]/td[2]')[0].text
    spectek_ddr4_spot_dl = dom.xpath('/html/body/div/div/table/tbody/tr[2]/td[1]/div[2]/div[1]/table[2]/tbody/tr[3]/td[3]')[0].text

    # SK Hynix、Spectek、Samsung、CXMT DDR3 4Gb 512Mx8 1600/1866 Spot Prices
    spectek_ddr3_spot_dh = dom.xpath('/html/body/div/div/table/tbody/tr[2]/td[1]/div[2]/div[1]/table[2]/tbody/tr[7]/td[2]')[0].text
    spectek_ddr3_spot_dl = dom.xpath('/html/body/div/div/table/tbody/tr[2]/td[1]/div[2]/div[1]/table[2]/tbody/tr[7]/td[3]')[0].text

    cur_time = datetime.datetime.now() # gets current time
    writer.writerow([
        cur_time,
        hynix_ddr4_spot_dh, hynix_ddr4_spot_dl,
        spectek_ddr4_spot_dh, spectek_ddr4_spot_dl,
        spectek_ddr3_spot_dh, spectek_ddr3_spot_dl
    ])
       

# MAIN
ram_csv = open("ram_data.csv", "a", newline='')
writer = csv.writer(ram_csv)
dom = get_dom('https://www.dramexchange.com/#mobile',MY_USER_AGENT) # dom gets prices from websites with XPATH

update() # updates prices
        
        

        