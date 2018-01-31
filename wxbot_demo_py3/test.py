from wxbot_demo_py3.save_message import MysqlDao

dao = MysqlDao()
dao.openConn()
cursor = dao.conn.cursor()
sql = 'SELECT message,msgType FROM wx_message WHERE msgid=%s'
cursor.execute(sql, "5131500405145741716")
result = cursor.fetchone()

print(result[0])
print(result[1])

dao.conn.commit()
cursor.close()
dao.closeConn()
