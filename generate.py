import pandas as pd
import sqlite3
from parse_jyutping import parse_jyutping
from pypinyin.contrib.tone_convert import to_initials, to_finals
from pypinyin.contrib.tone_convert import to_tone3
from pypinyin import Style, pinyin
import re

# create tables
con = sqlite3.connect('wenshu.sqlite')
con.executescript(open('tables.sql').read())

# load reading data
v = pd.read_csv('./unihan/readings.csv', header=None, names=["zi","relation","data"])

# import pinyin data
Mandarin    = v[v["relation"] == "Mandarin"]
md = []
def c_py(x):
    y = to_tone3(x[2])
    ini = to_initials(y, strict=False)
    fin = to_finals(y)
    ton = y[-1]
    if not ton.isdigit():
        ton = 5
    pppy = pinyin(x[0], style=Style.TONE3, heteronym=True)
    pppy = [i for x in pppy for i in x]
    for y in pppy:
        yini = to_initials(y, strict=False)
        yfin = to_finals(y)
        yton = y[-1]
        if not yton.isdigit():
            yton = 5
        if yfin != "":
            md.append([x[0],yini, yfin, yton])
    if fin != "":
        md.append([x[0],ini, fin, ton])
Mandarin.apply(c_py,axis=1)
Mandarin = pd.DataFrame(md,columns=["zi","shengmu","yunmu","diao"])
Mandarin = Mandarin.drop_duplicates()
data = tuple(Mandarin.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO PINYIN VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import jyutping data
Cantonese   = v[v["relation"] == "Cantonese"]
ct = []
def c_ct(x):
    [init, finals, last, tone] = parse_jyutping(x[2])
    ct.append([x[0],init, finals, last, tone])
Cantonese.apply(c_ct,axis=1)
Cantonese = pd.DataFrame(ct,columns=["zi","shengmu","yunmu","yunjiao","diao"])
data = tuple(Cantonese.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO JYUTPING VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import chaizi data
ids = pd.read_csv('./chaizi/ids.csv')
ids["chaizi"] = ids["chaizi"].apply(lambda x: re.sub(r"[\u2ff0-\u2ffb]", "", x))
data = []
def transform_ids(row):
    for i,c in enumerate(row[1]):
        data.append([row[0],c,i])
ids.apply(transform_ids, axis=1)
data = pd.DataFrame(data, columns=["zi","chaizi","index"])
data = tuple(data.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO CHAIZI VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import bihua data
bihua = pd.read_csv('./unihan/bihua.csv')
data = tuple(bihua.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO BIHUA VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import zipin data
freq = pd.read_csv('./unihan/freq.csv')
data = tuple(freq.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO ZIPIN VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

#import bianti data
bianti = pd.read_csv('./unihan/variants.csv')
data = tuple(bianti.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO BIANTI VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import definitions
Definitions    = v[v["relation"] == "Definition"]
Definitions.drop(columns=["relation"], inplace=True)
data = tuple(Definitions.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO DEFINITION VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import kangxi
kangxi = pd.read_csv('./kangxi/kangxi.csv', sep="\t")
data = tuple(kangxi.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO KANGXI VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import ciyu
ciyu = pd.read_csv('./dict/ciyu.csv')
data = tuple(ciyu.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO CIYU VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import xiehouyu
xiehouyu = pd.read_csv('./dict/xiehouyu.csv')
data = tuple(xiehouyu.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO XIEHOUYU VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

# import shuzi
shuzi = pd.read_csv('./unihan/shuzi.csv')
data = tuple(shuzi.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert = 'INSERT INTO SHUZI VALUES({})'.format(wildcards)
con.executemany(insert, data)
con.commit()

print("Done")