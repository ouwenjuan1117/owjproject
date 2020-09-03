# yield生成器,只能通过next方法来获取值
def provider():
    for i in range(0, 10):
        print('开始操作')
        yield i  # 相当于 return i ，同时记录了上一次的执行位置
        print('结束操作')


p = provider()
print(p)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

for i in p:
    print(i)
