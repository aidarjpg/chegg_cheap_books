from bs4 import BeautifulSoup
import requests
import time
import random
import re

import requests

import requests

headers = {
    'authority': 'www.chegg.com',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.chegg.com/textbooks/fiction-1/1',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'cookie': 'user_geo_location=%7B%22country_iso_code%22%3A%22KZ%22%2C%22country_name%22%3A%22Kazakhstan%22%2C%22region%22%3A%22AST%22%2C%22region_full%22%3A%22Nur-Sultan%22%2C%22city_name%22%3A%22Nur-Sultan%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%5D%7D%7D; C=0; O=0; V=3b1d923f709674d92795555e1e8423e6611f3d24079d38.92528446; optimizelyEndUserId=oeu1629437225202r0.07314845927650726; _omappvp=AunRsMITonPY8gDQVDJ88Yugt7AG7aczLToIzTJ6IVTgHanVlbdVvfm22wMJMMysF3qWuzRZJXVAsysVHGUvnwGRUxtfzRvx; mcid=34170275019725926454610467429233929911; _pxvid=42c8dc76-0177-11ec-aee4-52684761666c; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; _ga=GA1.2.175503385.1629437242; _gcl_au=1.1.1842102386.1629437242; _rdt_uuid=1629437242151.4e6297a8-eb6c-483c-9cde-eec57cd5be09; s_ecid=MCMID%7C34170275019725926454610467429233929911; al_cell=main-1-control; _scid=d8000441-8ccb-4373-893a-c62990c3e69c; __ssid=06064b71af7a6d512ac1fd637ee1bab; PHPSESSID=e72o3874e8nquslkfrjjqkj0i5; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%206a2d72ad-56fd-48a3-9e95-ec9e7a23532e%2C%20%22created_date%22%20%3D%3E%202021-08-25T09%3A08%3A16.915Z%20%5D; DFID=web|9paue9ZllVi2Rs5H1nX8; U=cfa7edcfad8ded9c9602daeaf8f99dee; gid=1; gidr=MA; _sdsat_cheggUserUUID=6a2d72ad-56fd-48a3-9e95-ec9e7a23532e; chgcsdmtoken=%7B%22user_uuid%22%3A%226a2d72ad-56fd-48a3-9e95-ec9e7a23532e%22%2C%22created_date%22%3A%222021-08-25T09%3A08%3A44.293Z%22%2C%22account_sharing_device_management%22%3A1%7D; chgcsdmtoken=6a2d72ad-56fd-48a3-9e95-ec9e7a23532e++web|9paue9ZllVi2Rs5H1nX8++1629882562848; CVID=431f4acc-57b1-4f94-8f6e-3b3f65023a99; __CT_Data=gpv=33&ckp=tld&dm=chegg.com&apv_79_www33=33&cpv_79_www33=33; _iidt=oYzNEeV5yTKQlf7XHoIaXgqmd6IYWR3zBc+PAuxBAKLJoKW9xM6Tp+8ACCfK+hIet57BL1JB//7c/A==; _vid_t=cByaA2ZpYymsbc5oHQ5kEGufONCz2cEbsiyWII3qcpsx9lSrhAhtC/3tjUvZQPjXuhdvWtKA6wE5GQ==; id_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRhbnlhcmJlay5uaXNAZ21haWwuY29tIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsInN1YiI6IjZhMmQ3MmFkLTU2ZmQtNDhhMy05ZTk1LWVjOWU3YTIzNTMyZSIsImF1ZCI6IkNIR0ciLCJpYXQiOjE2MzEyNTEwMDYsImV4cCI6MTYzOTAxNDcxOSwicmVwYWNrZXJfaWQiOiJhcHcifQ.ft5juQBfmS7-wYZXIqjs1xbJfCqJHSmFpqEC_0XDR7TqueCG9rcs1vgaTeGntqossOqMNf81s5Xtw51Ey4DQ1UUpj55bKIRoKM91NZaQDXulAD7SLLz6CBOxMywhWQ1PhiRC1hdfybiRB1aD-ExJN20n6hxODmpTYO0a4zU5p1SpjhQzb0iCjry4c6xybsanTngZLqxuBvlm0VneHqrPt3Ysbb7w_UxgQBCNZrWQbgprUXtIrjjQLS6K5bWxwi-cOFsUKJsYRTMyCqKXb-nPtxtqw4ypr0EmRhJVfMFgOFkfNMt-4KqnAbqdJ23TOVb8G-HD3X3mrPFjxUfN046Nsw; refresh_token=ext.a0.t00.v1.MfBQ3-rErT3Tvj0I_0WOmuhTlXYU49_Z6qvF-u5vK0yVo8iy4hDPt8hq1snyHudbukhrvVv1iT5gbDK5irZ9yFs; chegg_web_cbr_id=a; aamsc=aam%3D2053348%2Caam%3D2756555%2Caam%3D5674360%2Caam%3D10684699; aam_uuid=34153174160243599994608790746554200717; aam_tnt=aam%3D2053348; IR_gbd=chegg.com; _cs_c=0; userData=%7B%22authStatus%22%3A%22Soft%20Logged%20In%22%2C%22email%22%3A%22danyarbek.nis%40gmail.com%22%2C%22attributes%22%3A%7B%22cheggUserUUID%22%3A%226a2d72ad-56fd-48a3-9e95-ec9e7a23532e%22%2C%22uvn%22%3A%223b1d923f709674d92795555e1e8423e6611f3d24079d38.92528446%22%7D%7D; usprivacy=1YNY; exp=A311C%7CA803B%7CC024A%7CA560B%7CA209A%7CA212A%7CA263A%7CA264A%7CA448A%7CA278C%7CA110B%7CA270C%7CA966F; expkey=96E75F75D49D71E73BBF5C3680DE9993; intlPaQExitIntentModal=hide; forterToken=7dec183faf4d4beb99ff5875bb959323_1634225092990__UDF43_13ck; _gid=GA1.2.1364236036.1634225098; _sctr=1|1634148000000; OneTrustWPCCPAGoogleOptOut=false; _sdsat_authState=Hard%20Logged%20In; omSeen-ohvoola2gvm5qhhnb5b1=1634239250174; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18915%7CMCMID%7C34170275019725926454610467429233929911%7CMCAAMLH-1634886274%7C6%7CMCAAMB-1634886274%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1634288674s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.6.0%7CMCCIDH%7C1801216295; SU=oHkzKMLhJ1LuJRYcrAAw5094ePcVdjITmmQpvx4Y_jH917L2TdXIO36bFiaE6hlyNTJP-yvWv9M_8h50XP2Xynt46tyEYdDlbMRP1oAyMLGTjC5f6wKiIv9xJlMQfrTX; CSessionID=a701c2fd-6fd8-42a5-8ece-f2e56b03d836; _sdsat_highestContentConfidence={%22__typename%22:%22ContentClassification%22%2C%22course_uuid%22:%221b5e0286-a1c8-498a-9d89-da8660523fe5%22%2C%22course_name%22:%22composition%22%2C%22year_in_school%22:1%2C%22subject%22:[{%22__typename%22:%22Subject%22%2C%22uuid%22:%226ac5fb72-b976-495b-aabe-03da6c4ad094%22%2C%22name%22:%22languages-and-literatures%22}]}; _cs_mk=0.5572590084204676_1634287232313; CSID=1634287232386; ab.storage.deviceId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%222fbb322d-6f9d-bdc3-8882-499135ad21a5%22%2C%22c%22%3A1629437240174%2C%22l%22%3A1634287240655%7D; ab.storage.userId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%226a2d72ad-56fd-48a3-9e95-ec9e7a23532e%22%2C%22c%22%3A1629882516299%2C%22l%22%3A1634287240657%7D; schoolapi=8a948500-a86e-403b-b487-a7f005087d2b|0.52173913; _cs_cvars=%7B%221%22%3A%5B%22Page%20Name%22%2C%22Rent%22%5D%2C%222%22%3A%5B%22Experience%22%2C%22desktop%22%5D%2C%223%22%3A%5B%22Page%20Type%22%2C%22seo%22%5D%2C%224%22%3A%5B%22Auth%20Status%22%2C%22Logged%20Out%22%5D%7D; _pxff_rf=1; _pxff_fp=1; _px3=5cd8fc214fd0f871231dbb246ccc444ae70bed24d83d748717d502dca6e419e9:tJ/5uyjJYV1Z0cO22sagzR1G35iRYeq698zklMKYd1KXRN92mssImkh7NpuJyHwuHojbr08QA48nIPSApAfCcw==:1000:exLdrNKaGvQkiXYapAPtZS0eFvT9/XyYAzmIk77BKxqyBOTxlbm2er+5tQhh4gzziRfeIYDyO2kqh8m9jjHwhUNQoek/2Zox6z8zbck2EKeVh1KMcVIUmMaCVj/1Px1MtrY0ssSHfQLJXVF7gRYrqoNkFhuC4AQG51frDG/BRH5pKCcF4sjJvkvEgG6ZcLftUcycdAbmM88ZzQMOg+/OMw==; _px=tJ/5uyjJYV1Z0cO22sagzR1G35iRYeq698zklMKYd1KXRN92mssImkh7NpuJyHwuHojbr08QA48nIPSApAfCcw==:1000:+OGgyGn/+dpfxRemgH02LOzTSXicgRzVw8Uy8+FTdcwHNPb3kESFk1Q2FVFWksABK+3PD+lSBPeIGu/UKssSZ5BflLol6d4oX6HG7uIb+2xbZSIs70yXfSPgqai3YIVLxwoTGuqOv9Aj5kgJAbOMjamNxPjV+xdyrLwWRPAVHJD3+SRqSyHjehLSvfyRKeupHpnYD1uqOCtWM0Yc0Cu8M487SnUjTnQKp4LgVakxrSfgCQlTTrEz2T9dWHYYQmh+RBvM96hZ5ycfeauUD8ws5Q==; OptanonConsent=isIABGlobal=false&datestamp=Fri+Oct+15+2021+14%3A59%3A01+GMT%2B0600+(East+Kazakhstan+Time)&version=6.18.0&hosts=&consentId=7a286c80-eab0-4683-a4d5-7efb73212928&interactionCount=1&landingPath=NotLandingPage&AwaitingReconsent=false&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1; s_pers=%20buFirstVisit%3Dcore%252Ctb%252Ccs%252Cseo%252Cothers%7C1791983065820%3B%20gpv_v6%3Dchegg%257Cweb%257Ctb%257Cseo%257Crent%7C1634290142244%3B; s_sess=%20buVisited%3Dcore%252Ctb%252Ccs%252Cseo%252Cothers%3B%20s_sq%3D%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D6CF1D600512CBD55-0B4DC2B6A3C133DC%3B%20s_cc%3Dtrue%3B%20s_ptc%3D0.01%255E%255E0.00%255E%255E0.00%255E%255E0.00%255E%255E0.80%255E%255E0.15%255E%255E6.59%255E%255E0.26%255E%255E7.66%3B; _uetsid=e4a4d4e02d0211ecafda1931db07b525; _uetvid=4b95e190017711ec8645550494a018ea; wcs_bt=s_4544d378d9e5:1634288347; ab.storage.sessionId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1=%7B%22g%22%3A%22eea95e86-1477-4175-e8fe-1c24d8dd9448%22%2C%22e%22%3A1634290147587%2C%22c%22%3A1634287240652%2C%22l%22%3A1634288347587%7D; _gat=1; IR_14422=1634288349818%7C0%7C1634288349818%7C%7C; _tq_id.TV-8145726354-1.ad8a=ec5a2e9ee161ecb6.1629437249.0.1634288350..; _cs_id=23f4d81d-b5bc-afbd-d045-d9b21c016626.1629437256.13.1634288351.1634286656.1.1663601256003; _cs_s=6.0.0.1634290151439',
}

books = set()
for i in range(50):
    try:
        url = 'https://www.chegg.com/textbooks/fiction-1/'+str(i+1);
        response = requests.get(url, headers=headers)
        print(response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')
        linkto_starter = soup.find_all('a', class_='title')
        for link in linkto_starter:
            link = 'https://www.chegg.com' + link['href']
            #print(link)
            books.add(link)
    except:
        print('failed at '+url)
        continue
    time.sleep(5)
ans = []
for url in books:
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        print(response.status_code)
        price = soup.find('span',class_ = 'PriceTabHeader__Price-sc-1494t2l-3 dUEhYD')
        price = float(price.text.replace("$",""))
        if(price > 10.0):
            continue
        name = soup.find('h1',class_ = 'styles__MainTitle-sc-3h4sqb-1 eDBkFr')
        name = name.text
        ans.append((price,name))
        time.sleep(5)
    except:
        print('Failed to fetch html: ' + url)
        continue
    
ans.sort()
for el in ans:
    print('Name: '+el[1])
    print('Price: '+str(el[0]))
    print('--------------------')