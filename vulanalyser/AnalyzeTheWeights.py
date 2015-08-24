import MySQLdb
import numpy as np
from scipy import stats
from collections import Counter
def calcScore(vulInfo, weights,bias):
    #accessvector
    if vulInfo[3]=="LOCAL":
        accessvector=0.395
    elif vulInfo[3]=="ADJACENT_NETWORK":
        accessvector=0.646
    elif vulInfo[3]=="NETWORK":
        accessvector=1

    #accesscomplexity
    if vulInfo[4]=="HIGH":
        accesscomplexity=0.35
    elif vulInfo[4]=="MEDIUM":
        accesscomplexity=0.61
    elif vulInfo[4]=="LOW":
        accesscomplexity=0.71

    #Authentication
    if vulInfo[5]=="MULTIPLE_INSTANCES":
        authentication=0.45
    elif vulInfo[5]=="SINGLE_INSTANCE":
        authentication=0.56
    elif vulInfo[5]=="NONE":
        authentication=0.704

    #bias 1 conf  > integ > avail
    if bias==1:
        if vulInfo[6]=="NONE":
            confImpact=weights[2]
        elif vulInfo[6]=="PARTIAL":
            confImpact=weights[3]
        elif vulInfo[6]=="COMPLETE":
            confImpact=weights[4]

        if vulInfo[7]=="NONE":
            integImpact=weights[5]
        elif vulInfo[7]=="PARTIAL":
            integImpact=weights[6]
        elif vulInfo[7]=="COMPLETE":
            integImpact=weights[7]

        if vulInfo[8]=="NONE":
            availImpact=weights[8]
        elif vulInfo[8]=="PARTIAL":
            availImpact=weights[9]
        elif vulInfo[8]=="COMPLETE":
            availImpact=weights[10]

    #bias 2 conf  > avail > integ
    if bias==2:
        if vulInfo[6]=="NONE":
            confImpact=weights[2]
        elif vulInfo[6]=="PARTIAL":
            confImpact=weights[3]
        elif vulInfo[6]=="COMPLETE":
            confImpact=weights[4]

        if vulInfo[8]=="NONE":
            integImpact=weights[5]
        elif vulInfo[8]=="PARTIAL":
            integImpact=weights[6]
        elif vulInfo[8]=="COMPLETE":
            integImpact=weights[7]

        if vulInfo[7]=="NONE":
            availImpact=weights[8]
        elif vulInfo[7]=="PARTIAL":
            availImpact=weights[9]
        elif vulInfo[7]=="COMPLETE":
            availImpact=weights[10]

     #bias 3 integ > conf  > avail
    if bias==3:
        if vulInfo[7]=="NONE":
            confImpact=weights[2]
        elif vulInfo[7]=="PARTIAL":
            confImpact=weights[3]
        elif vulInfo[7]=="COMPLETE":
            confImpact=weights[4]

        if vulInfo[6]=="NONE":
            integImpact=weights[5]
        elif vulInfo[6]=="PARTIAL":
            integImpact=weights[6]
        elif vulInfo[6]=="COMPLETE":
            integImpact=weights[7]

        if vulInfo[8]=="NONE":
            availImpact=weights[8]
        elif vulInfo[8]=="PARTIAL":
            availImpact=weights[9]
        elif vulInfo[8]=="COMPLETE":
            availImpact=weights[10]

    #bias 4 integ > avail > conf
    if bias==4:
        if vulInfo[7]=="NONE":
            confImpact=weights[2]
        elif vulInfo[7]=="PARTIAL":
            confImpact=weights[3]
        elif vulInfo[7]=="COMPLETE":
            confImpact=weights[4]

        if vulInfo[8]=="NONE":
            integImpact=weights[5]
        elif vulInfo[8]=="PARTIAL":
            integImpact=weights[6]
        elif vulInfo[8]=="COMPLETE":
            integImpact=weights[7]

        if vulInfo[6]=="NONE":
            availImpact=weights[8]
        elif vulInfo[6]=="PARTIAL":
            availImpact=weights[9]
        elif vulInfo[6]=="COMPLETE":
            availImpact=weights[10]

    #bias 5 avail > conf  > integ
    if bias==5:
        if vulInfo[8]=="NONE":
            confImpact=weights[2]
        elif vulInfo[8]=="PARTIAL":
            confImpact=weights[3]
        elif vulInfo[8]=="COMPLETE":
            confImpact=weights[4]

        if vulInfo[6]=="NONE":
            integImpact=weights[5]
        elif vulInfo[6]=="PARTIAL":
            integImpact=weights[6]
        elif vulInfo[6]=="COMPLETE":
            integImpact=weights[7]

        if vulInfo[7]=="NONE":
            availImpact=weights[8]
        elif vulInfo[7]=="PARTIAL":
            availImpact=weights[9]
        elif vulInfo[7]=="COMPLETE":
            availImpact=weights[10]

    #bias 6 avail > integ > conf
    if bias==6:
        if vulInfo[8]=="NONE":
            confImpact=weights[2]
        elif vulInfo[8]=="PARTIAL":
            confImpact=weights[3]
        elif vulInfo[8]=="COMPLETE":
            confImpact=weights[4]

        if vulInfo[7]=="NONE":
            integImpact=weights[5]
        elif vulInfo[7]=="PARTIAL":
            integImpact=weights[6]
        elif vulInfo[7]=="COMPLETE":
            integImpact=weights[7]

        if vulInfo[6]=="NONE":
            availImpact=weights[8]
        elif vulInfo[6]=="PARTIAL":
            availImpact=weights[9]
        elif vulInfo[6]=="COMPLETE":
            availImpact=weights[10]


    impactScore=confImpact+integImpact+availImpact
    if impactScore==0:
        return 0
    else:
        exploitabilityScore=6*accessvector*accesscomplexity*authentication
        return round(impactScore+exploitabilityScore,1)


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user="root",passwd="passw0rd",db="nvdbase")
    cursor = conn.cursor()
    cursor.execute("select * from weightstable")
    rsWeights = cursor.fetchall()
    cursor.execute("select * from cvetable")
    rsInfo=cursor.fetchall()

    #bias 1 conf  > integ > avail
    #bias 2 conf  > avail > integ
    #bias 3 integ > conf  > avail
    #bias 4 integ > avail > conf
    #bias 5 avail > conf  > integ
    #bias 6 avail > integ > conf
    scoreList=[]
    resultList=[]
    for bias in [1,2,3,4,5,6]:
        print "name\tmean\tmin\t tfpoint\t median\t sfpoint\tmax\tstddev\tcv\t scoreNums"
        for weights in rsWeights:
            scoreList=[]
            resultList=[]
            print weights[1]+":",
            for vulInfo in rsInfo:
                basicScore=calcScore(vulInfo,weights,bias)
                scoreList.append(basicScore)

            size=len(scoreList)
            narray=np.array(scoreList)
            mean=round(narray.mean(),1)
            min=round(narray.min(),1)
            tfpoint=round(stats.scoreatpercentile(narray,25),1)
            median=round(np.median(scoreList),1)
            sfpoint=round(stats.scoreatpercentile(narray,75),1)
            max=round(narray.max(),0)
            stddev=round(narray.std(),2)
            cv = round(narray.std()/narray.mean(),3)
            diffScores=len(Counter(scoreList))
            count=0
            for x in scoreList:
                if x <= 6.5:
                    count=count+1
            print count*1.0/len(scoreList)
            break;
            print mean,'\t',min,'\t',tfpoint,'\t',median,'\t',sfpoint,'\t',max,'\t',stddev,'\t',cv,'\t',diffScores
        print "============================================================================="


