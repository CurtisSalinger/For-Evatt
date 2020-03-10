import json

# load the files
filenames=[
    'condensed_2009.json',
    'condensed_2010.json',
    'condensed_2011.json',
    'condensed_2012.json',
    'condensed_2013.json',
    'condensed_2014.json',
    'condensed_2015.json',
    'condensed_2016.json',
    'condensed_2017.json',
    'condensed_2018.json',
    ]
tweets=[]
for filename in filenames:
    with open(filename,'r') as f:
        text=f.read()
        tweets+=json.loads(text)
print('len(tweets)=',len(tweets))

# count the occurrences of each tweet
counts={
    'obama':0,
    'trump':0,
    'daca':0,
    'wall':0,
    'russia':0,
    'mexico':0,
    'fake news':0,
    'mainstream media':0,
    }
for tweet in tweets:
    for phrase in counts.keys():
        if phrase in tweet['text'].lower():
            counts[phrase]+=1
print('counts=',counts)

# print the results
print('percentage of tweets using phrase:')
for k in sorted(counts.keys()):
    print(k.rjust(18), ':', '%05.2f'%(100*counts[k]/len(tweets)))

#plot the results
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(counts.keys(),(counts.values()))
plt.xticks()
plt.savefig('trumpChart.png')

#Obama year counts
obama_counts={}
for tweet in tweets:
    year = tweet['created_at'][-4:]
    if 'obama' in tweet['text'].lower():
        if year in obama_counts:
            obama_counts[year]+=1
        else:
            obama_counts[year]=1

from pprint import pprint
pprint(obama_counts)

fig, ax = plt.subplots()
x = obama_counts.keys()
y = obama_counts.values()



x2 = []
y2 = []
#To sort the data by x value
for key in sorted(obama_counts.keys()):
    x2.append(key)
    y2.append(obama_counts[key])
ax.plot(x2,y2)
plt.show()
