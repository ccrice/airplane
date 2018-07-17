# coding:utf8
# created at 2018/7/17.

import requests
import json
from prettytable import PrettyTable
from send_mail import send_mail

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Host':'flights.ctrip.com',
    'Refere':'http://flights.ctrip.com/booking/HGH-XNN-day-1.html?DDate1=2018-09-20',
    'Cookie':'_abtest_userid=3e29ba88-a874-449f-8a4f-61ee80c11e72; _RSG=S64jIcGH7tAYaF7OHjrE19; _RDG=28c287f0dc66712bb90032366341fb3705; _RGUID=adc74509-92b4-419c-904e-d6d4581cf922; _ga=GA1.2.974086885.1527218159; Session=SmartLinkCode=U457771&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; __utma=1.974086885.1527218159.1528956676.1528956676.1; __utmz=1.1528956676.1.1.utmcsr=xiecheng.com|utmccn=(referral)|utmcmd=referral|utmcct=/; StartCity_Pkg=PkgStartCity=2; Favorite_Products=Pkg_0=1943639|2; DomesticUserHostCity=SHA|%c9%cf%ba%a3; adscityen=Shanghai; _gid=GA1.2.508792682.1531709745; MKT_Pagesource=PC; appFloatCnt=8; _RF1=202.96.204.14; Union=AllianceID=13963&SID=457771&OUID=000401app-; FD_SearchHistorty={"type":"S","data":"S%24%u676D%u5DDE%28HGH%29%24HGH%242018-09-20%24%u897F%u5B81%28XNN%29%24XNN"}; _bfi=p1%3D101027%26p2%3D101027%26v1%3D41%26v2%3D40; _bfa=1.1527218156139.37mrtl.1.1531709742600.1531723478147.7.42; _bfs=1.10; _gat=1; Mkt_UnionRecord=%5B%7B%22aid%22%3A%2213963%22%2C%22timestamp%22%3A1531725003690%7D%5D; _jzqco=%7C%7C%7C%7C1531709745335%7C1.363904067.1527218159049.1531724474051.1531725003781.1531724474051.1531725003781.undefined.0.0.33.33; __zpspc=9.6.1531723480.1531725003.8%231%7C%7C%7C%7C%7C%23'
}
#以上信息通过浏览器获取

with open('config.json') as f:
    params = json.load(f)

with open('hkgs.json',encoding='UTF-8') as f:
    hk_name = json.load(f)

def generate_tr(x,alc,dpbn,apbn,dt,at,lp,line):
    if lp < line:
        x.add_row([alc,dpbn,apbn,dt,at,lp])


for i in range(len(params)):
    r = requests.get('http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights',params=params[i],headers=headers)
    r_json = json.loads(r.text)

    x = PrettyTable(["航空公司","出发地","到达地","出发时间","到达时间","价格"])
    x.align["航空公司"] = "1"
    x.padding_width = 1

    for i in range(len(r_json['fis'])):
        alc = hk_name[r_json['fis'][i]['alc']]
        dpbn = r_json['fis'][i]['dpbn']
        apbn = r_json['fis'][i]['apbn']
        dt = r_json['fis'][i]['dt']
        at = r_json['fis'][i]['at']
        lp = r_json['fis'][i]['lp']
        line = 1500
        generate_tr(x,alc,dpbn,apbn,dt,at,lp,line)

    data_html = x.get_html_string()
    send_mail(data_html)