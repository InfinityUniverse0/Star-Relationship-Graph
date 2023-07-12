import pymysql


class database():
    # 数据库的操作类

    # 创建数据表
    def createTable(self, connect):
        '''
        创建数据表
        connect:数据库的连接
        '''
        sqls = ["""
        Create Table IF NOT EXISTS 人物(
            id bigint Unsigned NOT NULL Auto_Increment, # 代理主键
            name varchar(64) NOT NULL,
            gender varchar(8),
            birth_date date,
            nationality varchar(64),
            description text,
            Primary Key (id)
        );      """,
                """
        Create Table IF NOT EXISTS 演员(
            id bigint Unsigned NOT NULL, # 代理主键
            Foreign Key (id) References 人物(id),
            Primary Key (id)
        );      """,
                """
        Create Table IF NOT EXISTS 歌手(
            id bigint Unsigned NOT NULL, # 代理主键
            Foreign Key (id) References 人物(id),
            Primary Key (id)
        );      """,
                """
        Create Table IF NOT EXISTS 影视作品(
            id bigint Unsigned NOT NULL Auto_Increment, # 代理主键
            name varchar(128) NOT NULL,
            director varchar(64),
            type varchar(64),
            pub_date date,
            Primary Key (id)
        );      """,
                """
        Create Table IF NOT EXISTS 歌曲(
            id bigint Unsigned NOT NULL Auto_Increment, # 代理主键
            name varchar(128) NOT NULL,
            singer bigint Unsigned NOT NULL,
            Foreign Key (singer) References 歌手(id),
            Primary Key (id)
        );      """,
                """
        Create Table IF NOT EXISTS 好友(
            person1 bigint Unsigned,
            person2 bigint Unsigned,
            Foreign Key (person1) References 人物(id),
            Foreign Key (person2) References 人物(id),
            Primary Key (person1, person2)
        );      """,
                """
        Create Table IF NOT EXISTS 恋人(
            person1 bigint Unsigned Unique, # Unique
            person2 bigint Unsigned Unique, # Unique
            Foreign Key (person1) References 人物(id),
            Foreign Key (person2) References 人物(id),
            Primary Key (person1, person2)
        );      """,
                """
        Create Table IF NOT EXISTS 旧爱(
            person1 bigint Unsigned,
            person2 bigint Unsigned,
            Foreign Key (person1) References 人物(id),
            Foreign Key (person2) References 人物(id),
            Primary Key (person1, person2)
        );      """,
                """
        Create Table IF NOT EXISTS 绯闻(
            person1 bigint Unsigned,
            person2 bigint Unsigned,
            Foreign Key (person1) References 人物(id),
            Foreign Key (person2) References 人物(id),
            Primary Key (person1, person2)
        );      """,
                """
        Create Table IF NOT EXISTS 主演(
            person bigint Unsigned,
            works bigint Unsigned,
            Foreign Key (person) References 人物(id),
            Foreign Key (works) References 影视作品(id),
            Primary Key (person, works)
        );      """,
                """
        Create Table IF NOT EXISTS 亲属(
            person1 bigint Unsigned,
            person2 bigint Unsigned,
            Foreign Key (person1) References 人物(id),
            Foreign Key (person2) References 人物(id),
            Primary Key (person1, person2)
        );
                """,
                """
        Create Table IF NOT EXISTS 离异(
            person1 bigint Unsigned,
            person2 bigint Unsigned,
            Foreign Key (person1) References 人物(id),
            Foreign Key (person2) References 人物(id),
            Primary Key (person1, person2)
        );
                """


                ]
        for sql in sqls:
            # 生成游标对象
            cursor = connect.cursor()
            # 创建表
            cursor.execute(sql)
            # 关闭游标
            cursor.close()

    def insert(self, connect, sql, attrs):
        '''
        向数据库添加数据操作：执行插入的sql语句

        connect:数据库的连接
        sql:sql插入语句
        attrs:要插入的值的元组
        '''

        # 生成游标对象
        cursor = connect.cursor()
        # 执行sql
        cursor.execute(sql, attrs)
        connect.commit()
        # 关闭游标
        cursor.close()

    def search(self, connect, sql):
        '''
        数据库查询操作：执行查询的sql语句

        connect:数据库的连接
        sql:sql查询语句
        '''

        # 生成游标对象
        cursor = connect.cursor()
        # 创建表
        cursor.execute(sql)
        connect.commit()
        # 关闭游标
        cursor.close()

    def delete(self, connect, sql):
        '''
        数据库删除操作：执行删除数据的sql语句

        connect:数据库的连接
        sql:sql删除语句
        '''
        # 生成游标对象
        cursor = connect.cursor()
        # 创建表
        cursor.execute(sql)
        # 关闭游标
        cursor.close()

    def update(self, connect, sql):
        '''
        数据库更新操作：执行更新的sql语句

        connect:数据库的连接
        sql:sql更新语句
        '''
        # 生成游标对象
        cursor = connect.cursor()
        # 创建表
        cursor.execute(sql)
        # 关闭游标
        cursor.close()
