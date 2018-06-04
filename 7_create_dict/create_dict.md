
# 创建字典的方法

### 1. 直接创建
```
dict = {'name' : 'earth', 'port' :'80'}
```
### 2. 工厂方法
```
items = [('name', 'earth'), ('port', '80')]
dict = dict(items)
```
### 3.fromkeys()方法
```
dict1 = {}.fromkeys(('x', 'y'), 1)
```
