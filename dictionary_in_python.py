d={101:"vikash",102:"suraj",104:"rahul",105:"abhay"}
print(d)
d={}
d["priyanshu"]=200
d["krishna"]=300
d["sachin"]=600
d["bipul"]=900
print(d)
print(d["krishna"])


print("------------------------------")
d={10:"xyz",11:"abc",12:"bcd"}
print(d.get(10))
print(d.get(11))
print(d.get(12))
print(d.get(125,"na"))
if 125 in d:
    print(d[125])
else:
    print("not found")


print("------------------------------")
d={110:"zbc",101:"abc",105:"pqr",106:"xyz"}
d[101]="cba"
print(d)    
print(len(d))
print(d.keys())
print(d.values())
print(d.items())
print(d.pop(105))
print(d)
print(d.popitem())
del d[101]
print(d)
d[108]="cde"
print(d)

# Outputs

# {110: 'zbc', 101: 'cba', 105: 'pqr', 106: 'xyz'}
# 4
# dict_keys([110, 101, 105, 106])
# dict_values(['zbc', 'cba', 'pqr', 'xyz'])
# dict_items([(110, 'zbc'), (101, 'cba'), (105, 'pqr'), (106, 'xyz')])
# pqr
# {110: 'zbc', 101: 'cba', 106: 'xyz'}
# (106, 'xyz')
# {110: 'zbc'}
# {110: 'zbc', 108: 'cde'}