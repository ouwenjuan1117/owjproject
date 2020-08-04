import yaml
document = '''
  a: 1
  b:
    c: 3
    d: 4
'''
print(yaml.safe_dump(yaml.safe_load(document)))
print(yaml.safe_load(document))
print(yaml.safe_dump(document))
print(type(yaml.safe_load(document)))
print(type(yaml.safe_dump(document)))

print(yaml.safe_load(open('data11.yml')))

