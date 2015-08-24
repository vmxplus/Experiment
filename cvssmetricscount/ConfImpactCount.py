__author__ = 'Mark'
import MySQLdb
from matplotlib import pyplot as plt
from matplotlib import style

con = MySQLdb.connect(host='localhost',user='root', passwd='passw0rd', db='nvdbase');
cursor = con.cursor()
resultCount=[0,0,0]
resultTotalNum=0
resultPercent=[0.0,0.0,0.0]
sql = "select confimpact from cvetable"
cursor.execute(sql);
resultTotalNum=cursor.rowcount
rs = cursor.fetchall()
print
for accessvector in rs:
    if accessvector[0]=="NONE":
        resultCount[0]+=1
    elif accessvector[0]=="PARTIAL":
        resultCount[1]+=1
    elif accessvector[0]=="COMPLETE":
        resultCount[2]+=1
    else:
        print "Exception Occur"

for i in [0,1,2]:
    resultPercent[i]= resultCount[i]*100.0/resultTotalNum
    resultPercent[i]=round(resultPercent[i],1)

print "Total Vulnerabilities: "+str(resultTotalNum)
print "NONE: "+str(resultCount[0])+" PARTIAL "+str(resultCount[1])+ " COMPLETE: "+str(resultCount[2])
print "NONEP: "+str(resultPercent[0])+" PARTIALP "+str(resultPercent[1])+ " COMPLETEP: "+str(resultPercent[2])

style.use('ggplot')
plt.bar([0,1,2], resultPercent,align='center')
ax= plt.gca()
ax.set_xticks([0,1,2])
ax.set_xticklabels(('NONE','PARTIAL','COMPLETE'));
ax.set_title("CONFIDENTIALITY IMPACT")
plt.show()
con.commit();
