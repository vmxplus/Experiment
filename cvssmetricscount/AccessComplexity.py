__author__ = 'Mark'
import MySQLdb
from matplotlib import pyplot as plt
from matplotlib import style

con = MySQLdb.connect(host='localhost',user='root', passwd='passw0rd', db='nvdbase');
cursor = con.cursor()
resultCount=[0,0,0]
resultTotalNum=0
resultPercent=[0.0,0.0,0.0]
sql = "select accesscomplexity from cvetable"
cursor.execute(sql);
resultTotalNum=cursor.rowcount
rs = cursor.fetchall()
print
for accessvector in rs:
    if accessvector[0]=="HIGH":
        resultCount[0]+=1
    elif accessvector[0]=="MEDIUM":
        resultCount[1]+=1
    elif accessvector[0]=="LOW":
        resultCount[2]+=1
    else:
        print "Exception Occur"

for i in [0,1,2]:
    resultPercent[i]= resultCount[i]*100.0/resultTotalNum
    resultPercent[i]=round(resultPercent[i],2)

print "Total Vulnerabilities: "+str(resultTotalNum)
print "HIGH: "+str(resultCount[0])+" MEDIUM "+str(resultCount[1])+ " LOW: "+str(resultCount[2])
print "HIGHP: "+str(resultPercent[0])+" MEDIUMP "+str(resultPercent[1])+ " LOW: "+str(resultPercent[2])

style.use('ggplot')
plt.bar([0,1,2], resultPercent,align='center')
ax= plt.gca()
ax.set_xticks([0,1,2])
ax.set_xticklabels(('HIGH','MEDIUM','LOW'));
ax.set_title("Access Complexity")
plt.show()
con.commit();

