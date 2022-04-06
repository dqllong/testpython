import time, telnetlib
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import socket
import struct
import pandas as pd

# 新建一个账号
username = "03383"
password = "0680"


def login():
    print('正在登录...')
    token = ''

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.get("http://192.168.100.1")
    time.sleep(0.1)
    driver.find_element('id', 'login_username').send_keys(username)
    driver.find_element('id', 'login_passwd').send_keys(password)
    driver.find_element('id', 'login_button').click()
    time.sleep(1)
    # token
    print('正在等待验证登录...')
    cookies = driver.get_cookies()
    for c in cookies:
        if c['name'] == 'token':
            # print(c['value'])
            token = c['value']
    # print(cookies)
    driver.quit()
    if not token == '':
        print('已经拿到token, %s' % token)
    else:
        print('无法拿到token.')

    return token


def getBigs():
    print('正在开始获取当前流量较大列表...')
    host = "192.168.100.1"
    command = "show statistics-set predef_user_bw current sort-by down"
    tn = telnetlib.Telnet(host)

    tn.read_until(b'Username: ', timeout=8)
    tn.write(username.encode('ascii') + b"\n")
    tn.read_until(b"Password: ", timeout=8)
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)

    tn.write(command.encode('ascii') + b"\n")
    time.sleep(1)
    v_result = tn.read_very_eager().decode('ascii')
    # print(v_result)

    ip_array = re.findall(r'[0-9]+(?:\.[0-9]+){3}', v_result)
    # print(ip_array)
    lt = []
    for ip in ip_array:
        n = {}
        n['ip'] = ip
        lt.append(n)
        # print(ip)

    return lt


def getvpns(token):
    cookies = {
        'PHPSESSID': 'id7oig7ckmlilril58hh8a9k4n',
        'HS.frame.lang': 'zh_CN',
        'oemid': 'HILLSTONE',
        'platform': 'T',
        'series': 'T',
        'hw_platform': 'SG-6000-T1860',
        'host_name': 'SG-6000',
        'company': 'Hillstone%20Networks',
        'ha_peer_state': '0',
        'soft_version': 'Hillstone%20StoneOS%20Software%20Version%205.5',
        'sw_version_det': '5.5R7',
        'sw_version': 'Version%205.5',
        'sw_bootfile': 'SG6000-T-3-5.5R7P7.bin%202020%2F08%2F20%2010%3A37%3A24',
        'ipv6': '0',
        'support_vlan': '1',
        'fromrootvsys': 'true',
        'storage_boost': '0',
        'vsysId': '0',
        'vsysName': 'root',
        'role': 'admin',
        'authServer': 'local',
        'license': '%7B%22license%22%3A%5B%22app%22%2C%22sslvpn%22%2C%22ipsec%22%5D%7D',
        'httpProtocol': 'http',
        'bid': '20200820160714714',
        'overseaLicense': '%7B%22license%22%3A%7B%22isOversea%22%3A%220%22%2C%22overseaLicense%22%3A%5B%22vpn%22%2C%22isp%22%2C%22app%22%5D%7D%7D',
        'zoneinfo': 'Asia%2FChongqing',
        'username': '03383',
        'token': token,
    }

    headers = {
        'Connection': 'keep-alive',
        'X-Auth-Token': token,
        'X-API-Language': 'zh_CN',
        'X-Requested-With': 'XMLHttpRequest',
        'X-API-Version': '5.5',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        'token': token,
        'Accept': '*/*',
        'Referer': 'http://192.168.100.1/',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    }

    params = (
        ('target', 'ribv4'),
        ('isDynamic', '1'),
        ('query',
         '{"fields":[],"conditions":[{"field":"ribv4.gate_ifname","operator":0,"value":"ethernet0/0","logical":0},{"field":"vr_name","value":"ALL"},{"field":"ribv4.route_type","value":"4"}],"sorts":[],"start":0,"limit":200,"page":1}'),
    )
    print('正在开始获取国际线路IP列表...')
    response = requests.get('http://192.168.100.1/rest/vr_vrouter', headers=headers, params=params, cookies=cookies,
                            verify=False)
    # print(response.text)
    result = json.loads(response.text)['result']['ribv4']
    lt = []
    for r in result:
        # print(socket.inet_ntoa(struct.pack("!I", int(r['destination']))), r['description'])
        # socket.inet_ntoa(struct.pack("!I", int(r['destination']))), r['description']
        n = {}
        n['ip'] = socket.inet_ntoa(struct.pack("!I", int(r['destination'])))
        n['name'] = r['description']
        lt.append(n)

    return lt


token = login()
lt1 = getvpns(token)
lt2 = getBigs()

# print(lt1)
# print(lt2)

data1 = pd.DataFrame(list(lt1))
data2 = pd.DataFrame(list(lt2))

# print(data1)
# print(data2)

# data1 = pd.read_json(lt1)
data = pd.merge(data2, data1, how='left', left_on='ip', right_on='ip', suffixes=['_big', '_vpn'])

print(data)

# for index,row in data.iterrows():
# print(row[])
