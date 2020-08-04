import yaml
#把列表转化成yaml格式
a = [[{'a':1},'admin2'],'admin3']
with open('data2','w') as f:
    yaml.safe_dump(a,f)