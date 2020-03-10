import json
from pprint import pprint
op = []

with open ('condensed_2009.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2010.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2011.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2012.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2013.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2014.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2015.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2016.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2017.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)
with open ('condensed_2018.json','r') as f:
    text = f.read()
    add = json.loads(text)

    op.append(add)


count = 0
ret = {}
add = 0
perc = 0
words = ['obama','trump','mexico','russia','fake news','wall','swamp', 'great','amazing','huge','best', 'witch hunt', 'mueller','news','rocket man', 'very']
for spot in words:
    count = 0
    add = 0
    for tweet in op:
        add += len(tweet)
        for dtc in tweet:
            said = dtc['text'].lower()
            if spot in said:
                count += 1
    ret[spot] = [count, (count/add) * 100]
    print(spot, ret[spot])
    perc=((count/add)*100)
    p = str(spot) + ' : ' + (f'%05.2f' % ((count/add)*100))
    print("{:>20}".format(p))
