import re
import matplotlib.pyplot as plt

file = open('logs/log.txt')  #打开文档
data = file.readlines() #读取文档数据

epoch = []
loss_ce = []
top_1 = []
top_5 = []
def split_line(line):
    line_split = re.split(r'[,\[\]\s]\s*',line)
    return line_split

for i in range(0,len(data)):
    sl = split_line(data[i])
    if len(sl)>5:
        if (sl[2]=='Start') and (sl[3]=='evaluating') and (sl[4]=='epoch'):
            slp = split_line(data[i+1])
            epoch.append(float(slp[4]))
            #loss_ce.append(float(slp[14]))
            top_1.append(float(slp[17]))
            top_5.append(float(slp[20]))

plt.figure()
plt.title('loss')
#plt.plot(epoch, loss_ce , color='green', label='train_loss')
plt.plot(epoch, top_1, color='red', label='top1')
plt.plot(epoch, top_5, color='blue', label='top5')
plt.xlabel('itr_num')
plt.ylabel('loss')
plt.legend() # 显示图例
plt.savefig('train_cc_kl_11_20.jpg')
plt.show()