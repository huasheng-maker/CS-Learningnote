import matplotlib.pyplot as plt
import numpy as np

# 计算不同n值的概率
n_values = np.arange(1, 21)
probabilities = [1 - (n + 1) / (2 ** n) for n in n_values]

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(n_values, probabilities, 'b-', linewidth=2, marker='o')
plt.xlabel('切割次数 n')
plt.ylabel('构成(n+1)边形的概率')
plt.title('随机切割构成多边形的概率')
plt.grid(True, alpha=0.3)
plt.ylim(0, 1.1)

# 添加一些关键点的标注
for n in [1, 2, 3, 5, 10, 15, 20]:
    prob = 1 - (n + 1) / (2 ** n)
    plt.annotate(f'n={n}\n{prob:.4f}', 
                xy=(n, prob), 
                xytext=(5, 5), 
                textcoords='offset points',
                fontsize=8)

plt.tight_layout()
plt.show()