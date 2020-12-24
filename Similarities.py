import pyodbc
import pandas as pd
from math import*
import nltk
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-65BJT1KQ;'
                      'Database=nixdb;'
                      'Trusted_Connection=yes;')

print("Database Connected")

cursor = conn.cursor()

cursor.execute('''SELECT * FROM nixdb.dbo.VTargetMail WHERE CustomerKey=11000 OR CustomerKey=11001''')
# cursor.execute('''SELECT * FROM nixdb.dbo.VTargetMail WHERE CustomerKey=11000 OR CustomerKey=11012''')
for row in cursor:
    print(row)

cursor.commit()

VTargetBuyLat = pd.read_csv('F:/Cleveland State University/Fall 19/CIS 660/Assign 1/VTargetBuyUpdated_Occ.csv')

# print(VTargetBuyLat)

num = VTargetBuyLat.values[0,[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]
den = VTargetBuyLat.values[1,[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]

print(num)
print(den)
# ---------------------Jaccard Similarity---------------------
def jaccard(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))

print("Jaccard Simmilarity:",jaccard(num, den))

# ----------------------cosine similarity--------------------
def cosine(list1, list2):
    prod=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    mod_x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    mod_y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(list1)):
        # print(i)
        prod[i] = list1[i] * list2[i]
        mod_x[i] = list1[i] * list1[i]
        mod_y[i] = list2[i] * list2[i]

    # print(prod)
    # print(mod_x)
    # print(mod_y)

    dot_prod = sum(prod)
    mod_sum_x = sum(mod_x)
    mod_sum_y = sum(mod_y)

    # print(mod_sum_x)
    # print(mod_sum_y)
    # print(dot_prod)

    sqrt_mod_x = sqrt(mod_sum_x)
    sqrt_mod_y = sqrt(mod_sum_y)

    # print(sqrt_mod_x)
    # print(sqrt_mod_y)

    denominator = sqrt_mod_x * sqrt_mod_y

    cos_sim = (dot_prod/denominator)
    print("Cosine Similarity: ",cos_sim)


cosine(num,den)

