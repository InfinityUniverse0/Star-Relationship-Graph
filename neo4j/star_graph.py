'''star_graph.py
明星关系图谱类
'''

# 导入所需的模块
from py2neo import Graph
from py2neo import Node, Relationship
from py2neo import NodeMatcher, RelationshipMatcher
from os.path import join
import pandas as pd

class StarGraph():
    '''
    明星关系图谱
    '''

    # 相关配置(默认)
    config = {
        'profile': 'bolt://localhost:7687',
        'auth': ('neo4j', '12345678')
    }

    def __init__(self, profile = config['profile'], auth = config['auth']):
        '''
        初始化
        '''

        # 重新设置配置信息
        self.config['profile'] = profile
        self.config['auth'] = auth

        # 图数据库
        self.graph = Graph(profile, auth = auth)
    
    def initial(self):
        '''
        初始化图数据库中的 架构(节点 & 关系) 和 数据
        '''

        # 首先，清空数据库
        clear = '''
        Match (n)
        Optional Match (n)-[r]-()
        Delete n, r
        '''
        self.graph.run(clear)

        # 执行初始化操作
        path = './data'

        # 1. 初始化`人物`节点
        person = pd.read_csv(join(path, 'person.csv'))
        for _, row in person.iterrows():
            # type有多个时，用 & 分割
            row['type'] = row['type'].split('&')
            node = Node('人物', **row)
            self.graph.create(node)
        
        # 2. 初始化`影视作品`节点
        works = pd.read_csv(join(path, 'works.csv'))
        for _, row in works.iterrows():
            node = Node('影视作品', **row)
            self.graph.create(node)
        
        # 3. 初始化`歌曲`节点
        music = pd.read_csv(join(path, 'music.csv'))
        for _, row in music.iterrows():
            node = Node('歌曲', **row)
            self.graph.create(node)
        
        # 4. 初始化关系
        relationships = pd.read_csv(join(path, 'relationships.csv'))
        for _, row in relationships.iterrows():
            if row['label'] in ['好友', '恋人', '旧爱', '绯闻', '亲属', '离异']:
                # 人物关系，双向关系
                node_s = Node('人物', name = row['start'])
                node_t = Node('人物', name = row['end'])
                self.create_relationship(node_s, node_t, row['label'])
                self.create_relationship(node_t, node_s, row['label'])
            else:
                if row['label'] == '主演':
                    node_s = Node('人物', name = row['start'])
                    node_t = Node('影视作品', name = row['end'])
                    self.create_relationship(node_s, node_t, row['label'])
                if row['label'] == '原唱':
                    node_s = Node('人物', name = row['start'])
                    node_t = Node('歌曲', name = row['end'])
                    self.create_relationship(node_s, node_t, row['label'])

    def create_node(self, tag, attrs = {}):
        '''
        增加节点操作：向图数据库中增加一个节点
        - 若标签`tag`不满足要求，抛出`ValueError`异常

        :params `tag` 增加的节点的标签，须是 `['人物', '影视作品', '歌曲']` 三者其中之一
        :params `attrs` 增加的节点的属性，`dict`类型，默认为空字典

        :return `py2neo.data.Node`
        '''
        
        if tag in ['人物', '影视作品', '歌曲']:
            # 设置标签及属性
            node = Node(tag, **attrs)
            # 保存到图数据库
            self.graph.create(node)
            # 返回Node
            return node
        raise ValueError("节点的标签必须是 `['人物', '影视作品', '歌曲']` 三者其中之一")
    
    def create_relationship(self, node_start, node_end, tag, attrs = {}):
        '''
        增加关系操作：向图数据库中增加一条关系边(有向边)
        - tips: 使用前，可以先自行创建`py2neo.data.Node`作为节点参数传入
        - 若节点不满足要求，抛出`ValueError`异常
        
        :params `node_start` 关系边的起点，`py2neo.data.Node`类型
        :params `node_end` 关系边的终点，`py2neo.data.Node`类型
        :params `tag` 增加的关系的标签
        :params `attrs` 增加的关系的属性，`dict`类型，默认为空字典

        :return `py2neo.data.关系标签`
        '''

        # 匹配首尾节点
        matcher = NodeMatcher(self.graph)
        node_s = matcher.match(str(node_start.labels).split(':')[1], **dict(node_start.items())).first()
        node_t = matcher.match(str(node_end.labels).split(':')[1], **dict(node_end.items())).first()

        if node_s and node_t:
            # 设置关系的标签及属性
            relationship = Relationship(node_s, tag, node_t, **attrs)
            # 保存到图数据库
            self.graph.create(relationship)
            # 返回
            return relationship
        raise ValueError("无效的节点！")
    
    def exec_cypher(self, cypher):
        '''
        执行Cypher语句

        :params `cypher` 待执行的Cypher语句
        
        :return `py2neo.cypher.Cursor`
        '''

        return self.graph.run(cypher)
    
    


# 用于测试：
if __name__ == '__main__':
    mygraph = StarGraph()
    mygraph.initial()
    cypher = "Match p = ()-[]-() Return p"
    cur = mygraph.exec_cypher(cypher)
    for iten in cur:
        print(cur)
    pass
