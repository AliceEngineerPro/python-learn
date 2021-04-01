import os

import pymysql

connection = pymysql.connect(host='gitlab.galaiot.cn',
                             user='root',
                             password='123456',
                             db='renren',
                             port=3306,
                             charset='utf8')
cursor = connection.cursor()
sql = "select * from *"
cursor.execute(sql)
cmptIdList = cursor.fetchall()

for cmptId in cmptIdList:
    cmptidStr = str(cmptId[0])
    print(cmptidStr)
    file_name = os.path.join('D:\logs', 'cmpt-' + cmptidStr + '.log')
    score_open = open(file_name, 'w', encoding='utf-8')
    scoreSql = "select * from * '"
    cursor.execute(scoreSql)
    scoreList = cursor.fetchall()
    for score in scoreList:
        score_open.write(str(score[1]) + "," + str(score[2]) + "," + str(score[3]) + "," + str(score[4]) + "\n")
    score_open.close()
cursor.close()
