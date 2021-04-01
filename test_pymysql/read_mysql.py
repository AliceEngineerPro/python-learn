import pymysql
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# 获取数据库实例的方法
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


# 获取数据库实例
db = create_engine('mysql+pymysql://', creator=connect_sql)

# 建立映射关系
Base = declarative_base()


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


# 创建会话
obj_session = sessionmaker(db)
# 打开会话
db_session = obj_session()
# 查询表中所有数据
all_list = db_session.query(sys_user).all()
for obj in all_list:
    print(obj.user_id,obj.username,obj.department)
# 关闭会话
db_session.close()

# # 创建表
# Base.metadata.create_all(db)
# # 向表中添加记录
# obj = User(name='小明',age=12)
# # 创建会话
# obj_session = sessionmaker(db)
# # 打开会话
# db_session = obj_session()
# # 向表中添加数据,此时数据保存在内存中
# db_session.add(obj)
# # 提交数据，将数据保存到数据库中
# db_session.commit()
# # 关闭会话
# db_session.close()




# from sqlalchemy import Column, Integer, String
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# # 使用pymysql获取连接对象
# def connect_sql():
#     connect = pymysql.connect(
#         host='数据库地址',
#         user='用户名',
#         password='密码',
#         db='数据库',
#         charset='utf8',
#     )
#     return connect
#
#
# # 获取数据库实例
# dbname = create_engine('mysql+pymysql://', creator=connect_sql)
#
# # 用url的方式连接mysql
# engine = create_engine(
#     'mysql+pymysql://root:mysql123@localhost/dbname?charset=utf-8", '
#     'echo=True,'
#     'max_overflow=0'
# )
#
# # 查询输出
# # c = create_engine('select * from * :')
# # print(c.fetchall)
#
# 获取mysql实例
#
# engine = create_engine('mysql+pymysql://root:mysql123@localhost/test_python')
#
# # 建立映射关系
# Base = declarative_base()
# session = sessionmaker(engine)()
#
#
# class User(Base):
#     __tablename__ = "test_user"  # 设置表明
#
#     name = Column(String(4), primary_key=True)
#     age = Column(Integer,10)
#     sex = Column(String(2))
#
#
# def __repr__(self):
#     return 'name:%s,age:%s,sex:%s' % (self.name, self.age, self.sex)
#
#
# def add_data():
#     User_test = User(name='Tom', age=20, sex='男')
#
#
# session.add(User_test)
# session.commit()
# 查询输出
# c = create_engine('select * from sys_user :')
# print(c.fetchall)
#
# dbname = declarative_base()
#
#
# class User(dbname):
#     __tablename__ = 'users'  # 设置表明
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     age = Column(Integer)
#
#
# # 创建表
# dbname.metadata.create_all(db)
#
# # 创建会话
# dbname_session = sessionmaker(db)
#
# # 打开会话
# db_session = dbname.session()
#
# # 提交数据，将数据保存到数据库中
# db_session.commit()
