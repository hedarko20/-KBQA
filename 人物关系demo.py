import csv
import py2neo
from py2neo import Graph,Node,Relationship,NodeMatcher

g=Graph('http://localhost:7474',user='neo4j',password='hedarko')
with open('/Users/Hedarko/Desktop/论文/三国志10.csv','r',encoding='gbk') as f:
    reader=csv.reader(f)
    for i in reader:
        if reader.line_num == 1:
            continue
        print("line:",reader.line_num,"的内容为:",i,"\n")
        person = Node("Person",name=i[0])
        g.merge(person,"Person","name")
        if i[1] != "" :
            person["字"] = i[1]
        person['sex'] = i[2]
        if i[3] != "" :
            personTem = Node("Person",name=i[3])
            personTem['sex']="男"
            father = Relationship(personTem,"父亲",person)
            g.merge(personTem,"Person","name")
            g.merge(father,"Person","name")
            pass
        if i[5] != "" :
            personTem = Node("Person",name=i[5])
            personTem['sex']="女"
            mother = Relationship(personTem,"母亲",person)
            g.merge(personTem,"Person","name")
            g.merge(mother,"Person","name")
            pass
        if i[7] != "" :
            personTem = Node("Person",name=i[5])
            #personTem['sex']="女"
            parterner = Relationship(personTem,"配偶",person)
            g.merge(personTem,"Person","name")
            g.merge(parterner,"Person","name")
        