import matplotlib.pyplot as plt

bubble1 = yvals1 = [101, 111, 121, 131, 138, 143, 148, 153, 158]
bubble2 = yvals2 = [130, 142, 155, 160, 170, 180, 190, 194, 200]
bubble3 = yvals3 = [125, 139, 157, 171, 183, 194, 205, 212, 220]
xvals = ['500', '600', '700', '800', '900', '1000', '1100', '1200', '1300']

for i in range(9):  
  bubble1[i] = bubble1[i] * 50 
  bubble2[i] = bubble2[i] * 50 
  bubble3[i] = bubble3[i] * 50 

(fig, ax) = plt.subplots(figsize=(10, 12))

ax.set_axisbelow(True)
ax.grid(True)

plt1 = ax.scatter(xvals, yvals1, c = '#d82730', s = bubble1, alpha = 0.5)
plt2 = ax.scatter(xvals, yvals2, c = '#2077b4', s = bubble2, alpha = 0.5)
plt3 = ax.scatter(xvals, yvals3, c = '#ff8010', s = bubble3, alpha = 0.5)

# 그래프 및 축제목 설정
ax.set_xlabel('X_axis_title', fontsize = 16)
ax.set_ylabel('Y_axis_title', fontsize = 16)
ax.set_title('Plot Title', fontsize = 20)

# 범례
ax.legend((plt1, plt2, plt3), 
          ('A', 'B', 'C'),
          scatterpoints = 1, 
          loc = 'upper left', 
          markerscale = 0.17,
          fontsize = 10,
          ncol = 3)
fig.tight_layout()
#plt.show()
