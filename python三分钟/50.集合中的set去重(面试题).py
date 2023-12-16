# -*- coding: utf-8 -*-
# @File : 50.集合中的set去重(面试题).py
# @Author : 阿波
# @Time : 2023/9/10 15:03
# @Software: PyCharm
old_name_list = ["张三", "李四", "王五", "赵六", "钱七", "胡八"]
new_name_list = ["王五", "赵六", "牛九", "杨十", "花千", "沈万"]

# 让“老名单”去“差”“新名单”，可以马上得到被裁员工名单。
bye_employees = set(old_name_list).difference(new_name_list)
print("被裁员工名单：", bye_employees)
# 让“新名单”去“差”“老名单”，可以马上得到新员工名单。
new_employees = set(new_name_list).difference(old_name_list)
print(f"新员工名单：", new_employees)
#
# # 并集
# set.union(set1, set2...)
# # 交集
# set.intersection(set1, set2...etc)
# # 差集
# set1.difference(set2)
# # 对称差集
# set.union(set1.difference(set2), set2.difference(set1))

