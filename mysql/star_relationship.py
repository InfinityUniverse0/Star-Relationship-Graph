'''=======================创建数据表==========================='''

import pandas as pd
import pymysql
from database import database
db = database()
# 创建数据库连接
connect = pymysql.connect(
    host='127.0.0.1',  # 连接主机, 默认127.0.0.1
    user='root',      # 用户名
    passwd='147258Aa.',  # 密码
    port=3306,        # 端口，默认为3306
    db='star_relationship',        # 数据库名称
    charset='utf8'    # 字符编码
)

# 创建数据表
db.createTable(connect)
# 关闭连接
connect.close()

'''=======================插入人物数据========================'''

connect = pymysql.connect(
    host='127.0.0.1',  # 连接主机, 默认127.0.0.1
    user='root',      # 用户名
    passwd='147258Aa.',  # 密码
    port=3306,        # 端口，默认为3306
    db='star_relationship',        # 数据库名称
    charset='utf8'    # 字符编码
)
# 读取person.csv文件
person = pd.read_csv('person.csv', sep=',')
for index, row in person.iterrows():
    sql = "INSERT INTO 人物 VALUES (%s,%s,%s,%s,%s,%s);"
    attrs = (row[0], row[1], row[2], row[4], row[5], row[6])
    # 插入人物数据
    db.insert(connect, sql, attrs)

    # 插入演员及歌手数据
    # 是否是演员和歌手，如果为-1则不是,不为-1则是
    isActor = row[3].find('演员')
    isSinger = row[3].find('歌手')
    if isActor != -1:
        sql = "INSERT INTO 演员 VALUES (%s);"
        attrs = row[0]
        db.insert(connect, sql, attrs)
    if isSinger != -1:
        sql = "INSERT INTO 歌手 VALUES (%s);"
        attrs = row[0]
        db.insert(connect, sql, attrs)

# 关闭连接
connect.close()

'''=======================插入影视作品数据========================'''

# 创建数据库连接
connect = pymysql.connect(
    host='127.0.0.1',  # 连接主机, 默认127.0.0.1
    user='root',      # 用户名
    passwd='147258Aa.',  # 密码
    port=3306,        # 端口，默认为3306
    db='star_relationship',        # 数据库名称
    charset='utf8'    # 字符编码
)
# 读取csv文件
works = pd.read_csv('works.csv', sep=',')
for index, row in works.iterrows():
    sql = "INSERT INTO 影视作品 VALUES (%s,%s,%s,%s,%s);"
    attrs = (row[0], row[1], row[2], row[3], row[4])
    # 插入影视作品数据
    db.insert(connect, sql, attrs)

# 关闭连接
connect.close()

'''=======================插入歌曲数据========================'''

# 创建数据库连接
connect = pymysql.connect(
    host='127.0.0.1',  # 连接主机, 默认127.0.0.1
    user='root',      # 用户名
    passwd='147258Aa.',  # 密码
    port=3306,        # 端口，默认为3306
    db='star_relationship',        # 数据库名称
    charset='utf8'    # 字符编码
)
# 读取csv文件
music = pd.read_csv('music.csv', sep=',')
for index, row in music.iterrows():
    sql = "INSERT INTO 歌曲 VALUES (%s,%s,%s);"
    attrs = (row[0], row[1], row[2])
    # 插入歌曲数据
    db.insert(connect, sql, attrs)

# 关闭连接
connect.close()

'''=======================插入主演关系========================'''

# 创建数据库连接
connect = pymysql.connect(
    host='127.0.0.1',  # 连接主机, 默认127.0.0.1
    user='root',      # 用户名
    passwd='147258Aa.',  # 密码
    port=3306,        # 端口，默认为3306
    db='star_relationship',        # 数据库名称
    charset='utf8'    # 字符编码
)
# 读取csv文件
acting = pd.read_csv('acting.csv', sep=',')
for index, row in acting.iterrows():
    sql = "INSERT INTO 主演 VALUES (%s,%s);"
    attrs = (row[0], row[1])
    # 插入主演关系
    db.insert(connect, sql, attrs)

# 关闭连接
connect.close()

'''=======================插入所有的双向关系========================'''
# 创建数据库连接
connect = pymysql.connect(
    host='127.0.0.1',  # 连接主机, 默认127.0.0.1
    user='root',      # 用户名
    passwd='147258Aa.',  # 密码
    port=3306,        # 端口，默认为3306
    db='star_relationship',        # 数据库名称
    charset='utf8'    # 字符编码
)
# 读取csv文件
relationship = pd.read_csv('relationship.csv', sep=',')
# 对csv文件进行切片，分别为好友，恋人，旧爱，离异，亲属，绯闻
friend = relationship[relationship['关系'] == '好友']
lover = relationship[relationship['关系'] == '恋人']
oldlove = relationship[relationship['关系'] == '旧爱']
divorce = relationship[relationship['关系'] == '离异']
family = relationship[relationship['关系'] == '亲属']
feiwen = relationship[relationship['关系'] == '绯闻']

# 插入好友表
for index, row in friend.iterrows():
    sql = "INSERT INTO 好友 VALUES (%s,%s);"
    # 双向插入好友关系
    db.insert(connect, sql, (row[0], row[1]))
    db.insert(connect, sql, (row[1], row[0]))

# 插入恋人表
for index, row in lover.iterrows():
    sql = "INSERT INTO 恋人 VALUES (%s,%s);"
    # 双向插入恋人关系
    db.insert(connect, sql, (row[0], row[1]))
    db.insert(connect, sql, (row[1], row[0]))

# 插入旧爱表
for index, row in oldlove.iterrows():
    sql = "INSERT INTO 旧爱 VALUES (%s,%s);"
    # 双向插入旧爱关系
    db.insert(connect, sql, (row[0], row[1]))
    db.insert(connect, sql, (row[1], row[0]))

# 插入离异表
for index, row in divorce.iterrows():
    sql = "INSERT INTO 离异 VALUES (%s,%s);"
    # 双向插入离异关系
    db.insert(connect, sql, (row[0], row[1]))
    db.insert(connect, sql, (row[1], row[0]))

# 插入亲属表
for index, row in family.iterrows():
    sql = "INSERT INTO 亲属 VALUES (%s,%s);"
    # 双向插入亲属关系
    db.insert(connect, sql, (row[0], row[1]))
    db.insert(connect, sql, (row[1], row[0]))

# 插入绯闻表
for index, row in feiwen.iterrows():
    sql = "INSERT INTO 绯闻 VALUES (%s,%s);"
    # 双向插入绯闻关系
    db.insert(connect, sql, (row[0], row[1]))
    db.insert(connect, sql, (row[1], row[0]))

# 关闭连接
connect.close()
