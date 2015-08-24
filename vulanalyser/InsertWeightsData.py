import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root",passwd="passw0rd",db="nvdbase")
cursor = conn.cursor()
sql="insert into nvdbase.weightstable (name,confnone,confpartial, confcomplete,integnone, integpartial,\
integcomplete, availnone,availpartial,availcomplete) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(sql,("WIVSS1","0.0","1.9","3.8","0.0","1.0","2.0","0.0","0.6","1.2"))
cursor.execute(sql,("WIVSS2","0.0","1.8","3.6","0.0","1.1","2.2","0.0","0.6","1.2"))
cursor.execute(sql,("WIVSS3","0.0","1.8","3.6","0.0","1.0","2.0","0.0","0.7","1.4"))
cursor.execute(sql,("WIVSS4","0.0","1.7","3.4","0.0","1.1","2.2","0.0","0.7","1.4"))
cursor.execute(sql,("WIVSS5","0.0","1.6","3.2","0.0","1.2","2.4","0.0","0.7","1.4"))
cursor.execute(sql,("WIVSS6","0.0","1.5","3.0","0.0","1.3","2.6","0.0","0.7","1.4"))
cursor.execute(sql,("WIVSS7","0.0","1.7","3.4","0.0","1.0","2.0","0.0","0.8","1.6"))
cursor.execute(sql,("WIVSS8","0.0","1.5","3.0","0.0","1.2","2.4","0.0","0.8","1.6"))
cursor.execute(sql,("WIVSS9","0.0","1.4","2.8","0.0","1.3","2.6","0.0","0.8","1.6"))
cursor.execute(sql,("WIVSS10","0.0","1.6","3.2","0.0","1.0","2.0","0.0","0.9","1.8"))
cursor.execute(sql,("WIVSS11","0.0","1.5","3.0","0.0","1.1","2.2","0.0","0.9","1.8"))
cursor.execute(sql,("WIVSS12","0.0","1.4","2.8","0.0","1.2","2.4","0.0","0.9","1.8"))
cursor.execute(sql,("WIVSS13","0.0","1.4","2.8","0.0","1.1","2.2","0.0","1.0","2.0"))
cursor.execute(sql,("WIVSS14","0.0","1.3","2.6","0.0","1.2","2.4","0.0","1.0","2.0"))
cursor.execute("select * from weightstable")
rs = cursor.fetchall()
for row in rs:
    print row
conn.commit()


