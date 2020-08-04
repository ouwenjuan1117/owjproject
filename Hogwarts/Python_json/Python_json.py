

import json
# json.dump 表示把Python对象写入在文件中
# json.dumps 表示把python对象 ,转化成字符串（dumps 代表dump-> string）
dict_hogwarts ={
    'a': [1,2,3],
    'name':['sprider man','钢铁侠']
}
#  在data.json当中写入python object 数据
with open("data.json", "w") as f:
    json.dump(dict_hogwarts, f , ensure_ascii=False)

print(type(dict_hogwarts))
print(type(json.dumps(dict_hogwarts)))

#json.load 反序列化，是将json格式字符串转化问dict，读取文件
#json.loads基于string，是将string转换成为dict
json_load = json.load(open("data.json"))
print("使用json_load的数据为", type(json_load))

with open('data.json','r') as f:
    json_loads=json.loads(f.read())
print(type(json_loads))


json_str2 ='[{"name":"qiyue","age":18,"flag":false},{"name":"qiyue","age":18}]'
student2 = json.loads(json_str2)
print(type(student2))
print(student2)

