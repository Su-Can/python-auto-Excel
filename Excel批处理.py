# 引用 pandas
import pandas as pd

# 获取文件
path = r"D:\wendang\python\test.xlsx"  # 文件路径
# 打开表格
data = pd.read_excel(path)  # 打开表格：如果是其他格式，需要改为read_XXX
# 执行条件
newData = data.drop([0, 1])  # 删除指定行：多行用列表"[]",axis默认为0
newData_1 = newData.drop(['Unnamed: 10'], axis=1)  # 删除指定列：删除列需要指定axis=1
# 删除列中含有特殊字符的行
newData_1 = newData_1.astype(str)  # 转换字符类型为str
newData_2 = newData_1[~newData_1['Unnamed: 9'].str.contains('（暂定）')]  # 反选'Unnamed: 9'列中，包含（暂定）的行，正向选择删掉”~“

print(newData_2)
# 加一个交互
a = input("是否确认？\nY/是；N/否（请输入大写）\n")
if str(a) == "Y":
    newData_2.to_excel(r"D:\wendang\python\test_1.xlsx", index=False)   #保存：index=false意味着输出的表格不会带着dataframe的索引
    print(r'新建文件保存成功，路径为：D:\wendang\python\test_1.xlsx')
else:
    print("好的再见")
