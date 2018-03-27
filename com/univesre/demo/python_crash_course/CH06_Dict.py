# CH06_Dict
# 6.1_a dict
alien_0 = {'color':'green', 'points':5};
print(alien_0['color']);
print(alien_0['points']);

# 6.2.5_删除键/值对;
del alien_0['points'];
print(alien_0);


# 6.3_遍历字典;
# 6.3.1_遍历所有键/值对: items();
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
for key, value in user_0.items():
    print("\nKey: " + key);
    print("Value: " + value);

# 6.3.2_遍历字典中的所有键: keys();
# 6.3.3_按顺序遍历字典中的所有键: sorted();
# 6.3.4_遍历字典中的所有值: values(), 消除重复: set();


# 6.4_嵌套
# 6.4.1_字典列表
# 6.4.2_字典中存储列表





