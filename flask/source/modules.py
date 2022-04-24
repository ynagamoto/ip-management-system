import pymysql.cursors
import hashlib

user_table_name = "users"

def GetConnection():
  connection = pymysql.connect(
    host="mariadb",
    port=3306,
    user="root",
    password="root00",
    db="lesson_db",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
  )
  return connection

def GetUsers():
  sql = "SELECT * FROM %s;" % user_table_name
  connection = GetConnection()
  result = []
  with connection:
    with connection.cursor() as cursor:
      cursor.execute(sql)    
      result = cursor.fetchall()
  return result

def AddUser(name, passwd):
  sql = "INSERT INTO %s (name, passwd)" % user_table_name
  sql = sql + " VALUES (%s, %s);"
  hashpw = Pw2Hash(passwd)
  connection = GetConnection()
  with connection:
    with connection.cursor() as cursor:
      cursor.execute(sql, (name, hashpw))    
      connection.commit()

def GetHash(uid):
  sql = "SELECT passwd FROM &s" % user_table_name
  sql = sql + " WHERE id = %s;"
  with connection:
    with connection.cursor() as cursor:
      cursor.execute(sql, uid)
      result = cursor.fetchone()
  return result['passwd']

def Pw2Hash(passwd):
  hashpw = hashlib.pbkdf2_hmac('sha3-512', bytes(passwd, 'utf-8'), b'', 1000).hex()
  return hashpw

def CompPw(uid, passwd):
  hashpw = GetHash(uid)
  tmp_hash = Pw2Hash(passwd)
  if tmp_hash == hashpw:
    return True
  else:
    return False 
