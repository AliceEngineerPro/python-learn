# -*- coding: utf-8 -*-
import datetime
import json
import re
import requests
import ssl
import urllib.parse

# from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 构建SESSION
session = requests.session()
session.verify = False

headers = {
    'Host': 'kyfw.12306.cn',
    'If-Modified-Since': '0',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

#############################获取验证码图片########################
tu = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.19990641718474977'
req = session.get(tu, headers=headers)
req = req.content
with open('tu.png', 'wb') as f:
    f.write(req)

##########################用户输入#############################
user = input('请输入12306账户:')
password = input('请输入您的密码:')
today = datetime.date.today()
cf = input("请输入出发站:")
zd = input("请输入终点站:")
time = input("请输入出发时间:")

##########################验证码输入#############################
dcit = {'1': '41,52', '2': '110,50', '3': '178,50', '4': '255,52',
        '5': '41,117 ', '6': '111,122', '7': '182,125', '8': '252,117'}
shuru = input('请输入(1-8):')
d_list = []
for i in shuru.split():
    d_list.append(dcit[i])
yanz = ','.join(d_list)
print(yanz)
##########################验证码提交校验#############################
yz_tj = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
data = {
    'answer': yanz,
    'login_site': 'E',
    'rand': 'sjrand'
}
yz = session.post(yz_tj, data=data, headers=headers)
req_yz = json.loads(yz.text)  #####验证码状态############
if req_yz['result_code'] == '4':
    print("验证码校验成功。。。")
else:
    print("验证码校验失败。。。请重新输入验证码！！")
    exit()

##########################用户登陆#############################
login = 'https://kyfw.12306.cn/passport/web/login'
data = {
    'username': user,
    'password': password,
    'appid': 'otn'
}
lo = session.post(login, data=data, headers=headers).text
req = json.loads(lo)  #####登陆状态############
if req['result_code'] == 0:
    print("用户登陆成功。。。")
else:
    print("用户登陆失败。。。账号密码出错，请重新输入！！")
    exit()

##########################用户登陆确认#############################
qr = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
data = {'appid': 'otn'}
req = session.post(qr, data=data, headers=headers).text
qr_json = json.loads(req)
if qr_json['result_code'] != 0:
    print("用户登陆验证失败。。。请检查您的输入!!!")
    exit()
else:
    print("用户登陆确认完成。。。")
    if qr_json['apptk']:
        tk = qr_json['apptk']
    if qr_json['newapptk']:
        tk = qr_json['newapptk']
    qr2 = 'https://kyfw.12306.cn/otn/uamauthclient'
    data = {'tk': tk}
    req = session.post(qr2, data=data, headers=headers).text
    req = json.loads(req)
    if req["result_code"] != 0:
        print("用户登陆验证失败。。。请重新检查您的输入!!!")
        exit()
    else:
        print("登陆用户为：" + req["username"])

##########################火车站的加载##########################
zhan = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9033'
req = session.get(zhan).text
txt = req.split('|')
##########################查询数据的输入##########################
chufa = txt[txt.index(cf) + 1]
zhongdian = txt[txt.index(zd) + 1]  ###替换站点对应字母

##########################火车票的查询显示##########################
cp = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=' + time + '&leftTicketDTO.from_station=' + chufa + '&leftTicketDTO.to_station=' + zhongdian + '&purpose_codes=ADULT'
che = session.get(cp).text
ht = json.loads(che)
che = ht['data']['result']
chufa = txt[txt.index(chufa) - 1]
zhongdian = txt[txt.index(zhongdian) - 1]  ###显示站点中文字体
print('###################################余票显示界面###################################')
for j in che:
    c2 = j.split('|')
    # print (c2[0])
    print("从" + chufa + "到" + zhongdian + "的" + c2[3] + "列车车次余票显示:")
    for i in c2[32]:
        if i == "有":
            print("商务座：" + c2[32] + "票")
        elif i == "无":
            print("商务座：" + c2[32] + "票")
        elif float(str(i)):
            print("商务座：" + c2[32] + " 张票")
    for i in c2[31]:
        if i == "有":
            print("一等座：" + c2[31] + "票")
        elif i == "无":
            print("一等座：" + c2[31] + "票")
        elif float(str(i)):
            print("一等座：" + c2[31] + " 张票")
    for i in c2[30]:
        if i == "有":
            print("二等座：" + c2[30] + "票")
        elif i == "无":
            print("二等座：" + c2[30] + "票")
        elif float(str(i)):
            print("二等座：" + c2[30] + " 张票")
    for i in c2[21]:
        if i == "有":
            print("高级软卧：" + c2[21] + "票")
        elif i == "无":
            print("高级软卧：" + c2[21] + "票")
        elif float(str(i)):
            print("高级软卧：" + c2[21] + " 张票")
    for i in c2[23]:
        if i == "有":
            print("软卧：" + c2[23] + "票")
        elif i == "无":
            print("软卧：" + c2[23] + "票")
        elif float(str(i)):
            print("软卧：" + c2[23] + " 张票")
    for i in c2[28]:
        if i == "有":
            print("硬卧：" + c2[28] + "票")
        elif i == "无":
            print("硬卧：" + c2[28] + "票")
        elif float(str(i)):
            print("硬卧：" + c2[28] + " 张票")
    for i in c2[29]:
        if i == "有":
            print("硬座：" + c2[29] + "票")
        elif i == "无":
            print("硬座：" + c2[29] + "票")
        elif float(str(i)):
            print("硬座：" + c2[29] + " 张票")
    for i in c2[26]:
        if i == "有":
            print("无座：" + c2[26] + "票")
        elif i == "无":
            print("无座：" + c2[26] + "票")
        elif float(str(i)):
            print("无座：" + c2[26] + " 张票")

print('###################################余票显示结束###################################')
print('\n')
print('###################################车票选择界面###################################')
print('1:  商务座       2：一等座        3：二等座   ')
print('4： 软  卧       5：硬   卧       6：硬  座')
zuo = input("请输入乘坐座位类型（1-6）：")

###################################车辆信息变量定义界面###################################
zuo_name = ''
key = ''
tran_no = ''
zw = ''
left = ''
train_location = ''

###################################车票信息传递###################################
if zuo == '1':
    xb = '32'  ####C2的下标
    zw = '9'
    zuo_name = '商务座'
elif zuo == '2':
    xb = '31'
    zw = 'M'
    zuo_name = '一等座'
elif zuo == '3':
    xb = '30'
    zw = 'O'
    zuo_name = '二等座'
elif zuo == '4':
    xb = '23'
    zw = '4'
    zuo_name = '软卧'
elif zuo == '5':
    xb = '28'
    zw = '3'
    zuo_name = '硬卧'
elif zuo == '6':
    xb = '29'
    zw = '1'
    zuo_name = '硬座'
else:
    print("输入错误请输入正确编号....")
    exit()
###################################车票信息采集###################################
for j in che:
    c2 = j.split('|')
    print("从" + chufa + "到" + zhongdian + "的" + c2[3] + "列车车次余票显示:")
    xb = int(xb)
    for i in c2[xb]:
        print('出发时间：' + c2[8])
        if i and i != '无':
            if i == "有":
                print(zuo_name + "：" + c2[xb] + "票")
                key = c2[0]
                left = c2[12]
                train_location = c2[15]
                break
            elif float(str(i)):
                print(zuo_name + "：" + c2[xb] + " 张票")
                key = c2[0]
                left = c2[12]
                train_location = c2[15]
                break
        else:
            print('无票')
            break
    else:
        continue
    break

##########################火车票预定篇##########################
key = urllib.parse.unquote(key)
url = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'  ############预定URL
data = {
    ##################点击预定按钮然后产生的secrestr值############
    'secretStr': key,
    'train_date': time,
    'back_train_date': today,
    'tour_flag': 'dc',
    'purpose_codes': 'ADULT',
    'query_from_station_name': chufa,
    'query_to_station_name': zhongdian,
    'undefined': ''
}
yd = session.post(url, data=data, headers=headers).text
yd_json = json.loads(yd)
# print(yd_json)
if yd_json['status'] == True:
    print('预订订单请求成功...')
else:
    print('预订订单请求失败...', yd_json)
    exit()

##########################火车票预定详情篇##########################
url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
data = {'_json_att=': ''}
req = session.post(url, data=data, headers=headers).text  ############预定完成验证详情
#####################返回的网页的源代码
gl = re.findall(r"var globalRepeatSubmitToken = '(.*.)'", req)
# key_check_isChange = re.findall(r"'key_check_isChange':'(.*.)'" ,req)
key_check_isChange = re.findall("'key_check_isChange':'(.*?)'", req)

##########################火车票订票确认详情篇##########################
url = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
data = {'_json_att=': '', 'REPEAT_SUBMIT_TOKEN': gl}
req = session.post(url, data=data).text  ###########订单详情确认######################
req = json.loads(req)
if req['status'] == True:
    print("订票人获取成功。。")
else:
    print("订票人信息获取失败。。。", req)

##########################订票人信息获取##########################
re = session.post('https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs', data={'REPEAT_SUBMIT_TOKEN': gl}).text
re_js = json.loads(re)
xx = re_js['data']['normal_passengers']
a = []
b = 0
for i in xx:
    a.append(str(b) + '：' + i['passenger_name'])
    b += 1
rens = "     ".join(str(x) for x in a)  ########订票人信息显示再同一行
b = b - 1
print('###################################乘车人选择界面###################################')
print(rens)
ren = input("请选择乘车人(0-N)：")
ren = int(ren)
if b < ren:
    print("乘车人编号输入有误，请重新输入:")
    exit()
xx = xx[ren]

##########################火车票订票人##########################
url = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
data = {
    'cancel_flag': '2',
    'bed_level_order_num': '000000000000000000000000000000',
    'passengerTicketStr': '{},{},{},{},1,{},{},N'.format(zw,
                                                         xx['passenger_flag'], xx['passenger_id_type_code'],
                                                         xx['passenger_name'], xx['passenger_id_no'], xx['mobile_no']),
    'oldPassengerStr': '{},1,{},1_'.format(xx['passenger_name'], xx['passenger_id_no']),
    'tour_flag': 'dc',
    'randCode': '',
    '_json_att': '',
    'REPEAT_SUBMIT_TOKEN': gl
}
req = session.post(url, data=data, verify=False).text
req = json.loads(req)
if req['data']['submitStatus'] == True and req['status'] == True:
    print("乘车人已确定。。。")
else:
    print("信息添加错误。。。", req)
    exit()

#########################火车票订单提交##########################
url = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'
data = {
    'passengerTicketStr': '{},{},{},{},1,{},{},N'.format(zw,
                                                         xx['passenger_flag'], xx['passenger_id_type_code'],
                                                         xx['passenger_name'], xx['passenger_id_no'], xx['mobile_no']),
    'oldPassengerStr': '{},1,{},1_'.format(xx['passenger_name'], xx['passenger_id_no']),
    'randCode': '',
    'purpose_codes': '00',
    'key_check_isChange': key_check_isChange,
    'leftTicketStr': left,
    'train_location': train_location,
    'choose_seats': '',
    'seatDetailType': '000',
    'roomType': '00',
    'dwAll': 'N',
    '_json_att': '',
    'REPEAT_SUBMIT_TOKEN': gl
}
req = session.post(url, data=data, headers=headers).text
req = json.loads(req)
if req['data']['submitStatus'] == True and req['status'] == True:
    print("购票成功。。。请前往官网支付订单！！！")
else:
    print("购票失败，请检查输入!!!", req)
