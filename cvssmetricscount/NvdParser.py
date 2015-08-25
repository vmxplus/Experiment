from lxml import etree
import MySQLdb


con = MySQLdb.connect(host='localhost',user='root', passwd='passw0rd', db='nvdbase');
cursor = con.cursor()
nvdTree = etree.parse("F:\NvdDataSet\\nvdcve-2.0-2015.xml")
nsdv = {"vuln":"http://scap.nist.gov/schema/vulnerability/0.4"}
nsdc = {"cvss":"http://scap.nist.gov/schema/cvss-v2/0.2"}
root = nvdTree.getroot()

count=0

for entry in root:
    cveId = entry.get("id");
    publishedDateTime = entry.find("vuln:published-datetime",nsdv);
    cvss=entry.find("vuln:cvss",namespaces=nsdv);
    # judge if there is cvss
    if cvss is None:
        continue;
    else:
        base_metrics=cvss.find("cvss:base_metrics",namespaces=nsdc);

    # judge if there are base_metrics
    if base_metrics is None:
        continue;
    else:
        baseScore = base_metrics.find("cvss:score",namespaces=nsdc);
        accessVector=base_metrics.find("cvss:access-vector",namespaces=nsdc);
        accessComplexity=base_metrics.find("cvss:access-complexity", namespaces=nsdc);
        authentication=base_metrics.find("cvss:authentication", namespaces=nsdc);
        confImpact=base_metrics.find("cvss:confidentiality-impact", namespaces=nsdc);
        integImpact=base_metrics.find("cvss:integrity-impact",namespaces=nsdc);
        availImpact=base_metrics.find("cvss:availability-impact",namespaces=nsdc);
        generatedDateTime=base_metrics.find("cvss:generated-on-datetime",namespaces=nsdc);

    print cveId;
    print baseScore.text;
    print accessVector.text;
    print accessComplexity.text;
    print authentication.text;
    print confImpact.text;
    print integImpact.text;
    print availImpact.text;
    print generatedDateTime.text;
    count=count+1;
    print count
    print "----------------------------------------"+"fuck"
    sql = "insert into cvetable (cveid, basescore, accessvector, accesscomplexity, authentication, confimpact, integimpact, availimpact) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(cveId,baseScore.text,accessVector.text,accessComplexity.text,authentication.text, confImpact.text,integImpact.text,availImpact.text))

con.commit();


