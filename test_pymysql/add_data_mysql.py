import pymysql
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 获取数据库
def connect_sql():
    # 使用pymysql获取连接对象
    connect = pymysql.connect(
        host='gitlab.galaiot.cn',
        user='root',
        password='123456',
        db='renren',
        charset='utf8',
    )
    return connect


# 获取数据库
db = create_engine('mysql+pymysql://', creator=connect_sql)

# 建立映射
Base = declarative_base()

# 一个类
class sys_user(Base):
    __tablename__ = 'sys_user'
    user_id = Column(Integer,primary_key=True)
    username = Column(String(50))
    password = Column(String(100))
    salt = Column(String(20))
    email = Column(String(100))
    mobile = Column(String(100))
    department = Column(String(255))
    status = Column(Integer)
    create_user_id = Column(Integer)
    # create_time = Column(RuntimeError)

# 向表中添加记录
obj = sys_user(user_id=261,username='机械公司',password='216216216',salt='asdasdasd')
# 创建会话
obj_session = sessionmaker(db)
# 打开会话
db_session = obj_session()
# 向表中添加数据,此时数据保存在内存中
db_session.add(obj)
# 提交数据，将数据保存到数据库中
db_session.commit()
# 关闭会话
db_session.close()

print('exit')