
import yaml

data = yaml.safe_load(open('game.yml'))
#打印出来yaml转换的字典
print(data)
# 打印出来yaml转换的字典中，key值为me对应的value
print(data["me"])
# 打印出来yaml转换的字典中，key值为me对应的value 的 key值对应为"hp"
print(data["me"]["hp"])
