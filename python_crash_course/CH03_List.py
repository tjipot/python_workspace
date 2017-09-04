# CH03_List

## 列表中修改元素;
# 无;

## 列表中添加元素;
# 在列表末尾添加元素: append();
bicycles = ['trek', 'cannondale', 'redline', 'specialized'];
print(bicycles[0].title());
bicycles.append('giant');
print(bicycles);
# 在列表中插入元素: insert(索引, 值);
bicycles.insert(3, 'forever');
print(bicycles);

## 列表中删除元素:
# 删除列表中的元素: del;
del bicycles[3];
print(bicycles);
# 删除列表中的元素并使用其值: pop(), 也可指定索引;
popped_bicycle = bicycles.pop();
print(popped_bicycle);
print(bicycles);
# 根据值删除元素: remove('redline'), 会返回值, 只删除第一个匹配的值(要用循环来确保全部删除);

## 3.3_组织列表;
# 3.3.1_sort(), reverse=True;
# 3.3.2_sorted(), 对列表进行临时排序, 不影响原来的顺序, reversed=True;
# 3.3.3_reverse(), 倒着打印列表;
# 3.3.4_len(), 确定列表的长度;



