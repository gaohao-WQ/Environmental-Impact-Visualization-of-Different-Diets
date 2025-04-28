import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: 加载数据
df = pd.read_csv("gh.csv")

# Step 2: 提取所需字段
radar_columns = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut',
    'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid'
]
diet_groups = df['diet_group'].unique()
mean_values = df.groupby('diet_group')[radar_columns].mean()

# Step 3: 归一化指标（每列缩放至0-1）
normed_means = (mean_values - mean_values.min()) / (mean_values.max() - mean_values.min())

# Step 4: 设置雷达图参数
labels = [col.replace('mean_', '').upper() for col in radar_columns]
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # 闭合图形

# Step 5: 创建图形
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))
plt.title('Environmental Impact by Diet Group (Normalized Metrics)', size=16, y=1.1)

# Step 6: 绘制每个饮食组的线
for i, group in enumerate(normed_means.index):
    values = normed_means.loc[group].tolist()
    values += values[:1]  # 闭合雷达图
    ax.plot(angles, values, label=group, linewidth=2)
    ax.fill(angles, values, alpha=0.1)

# Step 7: 设置坐标轴和标签
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=12)
ax.set_rlabel_position(0)
ax.tick_params(colors='#999999')
ax.grid(color='gray', linestyle='dotted', linewidth=0.8)
ax.set_ylim(0, 1)

# Step 8: 图例
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

plt.tight_layout()
plt.show()