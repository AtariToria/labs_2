import json

text=({"Name":"John","Age":"21"},{"Name":"Anne","Age":"23"})
print(type(text))
print(type(json.dumps(text)))
print(json.dumps(text))

text1 =[{"Name":"John","Age":"21"},{"Name":"Anne","Age":"23"}]
print(type(text1))
print(type(json.dumps(text1)))
print(json.dumps(text1))

pdict = {"Name":"John","Age":"21"}
print(type(pdict))
print(type(json.dumps(pdict)))
print(json.dumps(pdict))