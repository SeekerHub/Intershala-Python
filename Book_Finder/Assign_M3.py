import Assign
from Newas import batscore, bowlscore


player = [
{'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0,'balls':119, 'field':0},
{'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2,'balls':112, 'field':0},
{'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10,'runs':71, 'field':1},
{'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10,'runs':45, 'field':0},
{'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34,'field':0}
]
# l2=[{'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10, 'runs':71, 'field':1},
# {'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10, 'runs':45, 'field':0},
# {'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0}]
#
# l1=[{'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0, 'balls':119, 'field':0},
# {'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2, 'balls':112, 'field':0}]
#
#
# for i in l1:
#     print (batscore(i))
# for i in l2:
#     print (bowlscore(i))
# k = p1
for i in range(len(player)):
    if player[i]['role']=='bat':
        print(player[i]['name'])
        runs = player[i]['runs']
        four = player[i]['4']
        six = player[i]['6']
        balls = player[i]['balls']
        field = player[i]['field']
        print(runs,four,six,field)
        Assign.Batting(runs,four,six,balls,field)
    else:
        wkts = player[i]['wkts']
        overs = player[i]['overs']
        runs = player[i]['runs']
        field = player[i]['field']
        Assign.Bowling(wkts,overs,runs,field)
