from feapder.db.mysqldb import MysqlDB

db = MysqlDB(host='localhost', port=3306, user='root', password='root', db='py_spider')
sql = """
CREATE TABLE IF NOT EXISTS `douban` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `score` varchar(255) DEFAULT NULL,
  `detail_url` varchar(255) DEFAULT NULL,
  `detail_text` text,
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  """
db.execute(sql)
print('创建成功')
insert_sql_test="""
insert into douban(title,score,detail_url,detail_text) values('测试','9.9','https://movie.douban.com/subject/1292052/','测试')
"""
db.execute(insert_sql_test)
print('插入成功')