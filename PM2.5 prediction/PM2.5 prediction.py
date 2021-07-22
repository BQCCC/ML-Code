import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path='C:\\Users\\18480\\Desktop\\train.csv'
df=pd.read_csv(path,encoding='utf-8')

new_df=df[df['測項'] == 'PM2.5']  # 抽取PM2.5的行
data_df=new_df.iloc[:,3:]   # 抽取PM2.5的数据

x_list=[]  # 定义一个二维数组对 x 进行存储
y_list=[]    # 定义一个数组对 Y 进行存储   

#开始抽取数据，赋值给x和y
for i in range(240):  # 240行数据，一行一行抽取
    y_list.extend(list(map(int,data_df.iloc[i,9:].tolist())))    # 直接获取一行的后15个数据，作为y
    for j in range(15): 
        temp_list=list(map(int,data_df.iloc[i,j:j+9]))
        temp_list.insert(0,1)          # 首位插入1,与w[0]（即b）相乘
        x_list.append(temp_list)

x_matrix=np.array(x_list)
y_matrix=np.array(y_list)

# for i in range(3200):
#     print("x: ",x_list[i],"  y: ",y_list[i])
# print(len(y_list))

# # 到这一步，数据全部取出来了 
# #设置训练次数，为10000次
# repeat=10000
# alpha=0.0001   # 根据实际情况，自己进行设置

# # 最开始所有的参数全部设置为0
# w=[0]*10   # 九个x的参数，b 为 w[0]
# w_grade=[0]*10  # 初试梯度为0

# for i in range(repeat):
#     # 第一步是计算LOSS
#     # 计算求和公式
#     loss = 0
#     for a in range(3200):
#         loss += (np.dot(x_matrix[a],w)-y_matrix[a])**2
#     loss = loss/6400

#     # 根据公式求梯度
#     for p in range(3200):
#         for k in range(10):
#             w_grade[k] += (np.dot(x_matrix[p],w)-y_matrix[p])*x_matrix[p][k]

#     # 根据梯度更新参数值
#     for h in range(10):
#         w_grade[h] = w_grade[h]/3200 
#         w[h] = w[h]-alpha*w_grade[h]

#     print("w_grade: ",w_grade)
#     print("repeat: ",i," loss: ",loss,"  w: ",w)
# print("结果：")
# print(" loss: ",loss,"  w: ",w)

w=[0.5414245570319668, 0.020082135796932972, -0.045910419128109156, 0.21262265164385652, -0.20625466185953498, -0.04444239545827025, 0.4544521021948807, -0.5370753208755685, 0.047595282028861256, 1.0731548824366408]


# 跑完了以后，用后面400组数据进行测试
# loss_test = 0
# for a in range(3200,3600):
#     loss_test += (np.dot(x_matrix[a],w)-y_matrix[a])**2
# loss_test = loss_test/400
# print("最后400组数据测试loss结果为：",loss_test)


# 绘制一个图像
# for g in range(3600):
    # plt.scatter(g,y_matrix[g],c="blue") # 全部用蓝色标注
    # plt.scatter(g,np.dot(x_matrix[g],w),c="red") # 红色标注预测数据



x = [i for i in range(3200,3600)]

y_1=y_matrix[3200:3600]
y_2=[]
for g in range(3200,3600):
    y_2.append(np.dot(x_matrix[g],w))
y_2=np.array(y_2)

# plt.plot(x,y_1,color="blue",linestyle='-')
# plt.plot(x,y_2,color="red",linestyle='-')

plt.plot(x,y_1-y_2,color="red",linestyle='-')
plt.show()


