__author__ = 'Mark'
import MySQLdb
from matplotlib import pyplot as plt
from matplotlib import style

con = MySQLdb.connect(host='localhost',user='root', passwd='passw0rd', db='nvdbase');
cursor = con.cursor()
resultCount=[0,0,0]
resultTotalNum=0
resultPercent=[0.0,0.0,0.0]
sql = "select accessvector from cvetable"
cursor.execute(sql);
resultTotalNum=cursor.rowcount
rs = cursor.fetchall()
print
for accessvector in rs:
    if accessvector[0]=="LOCAL":
        resultCount[0]+=1
    elif accessvector[0]=="ADJACENT_NETWORK":
        resultCount[1]+=1
    elif accessvector[0]=="NETWORK":
        resultCount[2]+=1
    else:
        print "Exception Occur"

for i in [0,1,2]:
    resultPercent[i]= resultCount[i]*100.0/resultTotalNum
    resultPercent[i]=round(resultPercent[i],1)

print "Total Vulnerabilities: "+str(resultTotalNum)
print "LOCAL: "+str(resultCount[0])+" ADJACENT_NETWORK "+str(resultCount[1])+ " NETWORK: "+str(resultCount[2])
print "LOCALP: "+str(resultPercent[0])+" ADJACENT_NETWORKP "+str(resultPercent[1])+ " NETWORKP: "+str(resultPercent[2])

style.use('ggplot')
plt.bar([0,1,2], resultPercent,align='center')
ax= plt.gca()
ax.set_xticks([0,1,2])
ax.set_xticklabels(('LOCAL','ADJACENT_NETWORK','NETWORK'));
ax.set_title("ACCESS VECTOR")
plt.show()
con.commit();

