"""
Week 2 Day 2: Pandas 统计分析与可视化
业务场景：极飞数据验收报告 - 统计各区域虫害分布，生成可视化图表
核心技能：groupby, value_counts, matplotlib绘图
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 使用与前一天相同的数据
np.random.seed(42)
data = {
    'field_id': [f'field_{i}' for i in range(1, 101)],
    'region': np.random.choice(['North', 'South', 'East', 'West'], size=100),
    'crop_type': np.random.choice(['wheat', 'corn', 'soybean'], size=100),
    'aphid_count': np.random.randint(0, 1000, size=100),
    'pesticide_sprayed': np.random.choice([True, False], size=100),
    'last_inspection_date': pd.date_range('2023-01-01', periods=100, freq='D'),
}
df = pd.DataFrame(data)

print("📊 模拟田间数据加载完成！")
print(df.head(3))

print("\n" + "="*50)
print("📈 1. 数据统计分析")
print("="*50)

# 1. 统计各作物类型的田块数量
crop_counts = df['crop_type'].value_counts()
print("✅ 各作物类型田块数量:")
print(crop_counts)

# 2. 按区域分组，计算平均蚜虫数量
avg_aphids_by_region = df.groupby('region')['aphid_count'].mean().round(2)
print(f"\n✅ 各区域平均蚜虫数量:")
print(avg_aphids_by_region)

# 3. 更复杂的分组：按区域和作物类型统计平均蚜虫数
complex_groupby = df.groupby(['region', 'crop_type'])['aphid_count'].mean().round(2)
print(f"\n✅ 各区域-作物类型的平均蚜虫数 (多级索引):")
print(complex_groupby)

print("\n" + "="*50)
print("📊 2. 数据可视化 (使用 Matplotlib)")
print("="*50)

# 设置中文字体，防止乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建一个包含两个子图的画布
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 图1: 各作物类型田块数量柱状图
axes[0].bar(crop_counts.index, crop_counts.values, color='skyblue')
axes[0].set_title('各作物类型田块数量分布')
axes[0].set_xlabel('作物类型')
axes[0].set_ylabel('田块数量')

# 图2: 各区域平均蚜虫数量饼图
axes[1].pie(avg_aphids_by_region.values, labels=avg_aphids_by_region.index, autopct='%1.1f%%', startangle=140)
axes[1].set_title('各区域平均蚜虫数量占比')

# 调整布局，防止重叠
plt.tight_layout()
# 显示图表
plt.show()

print("\n🎯 业务解读:")
print("• value_counts: 快速了解数据分布 (如各虫害类型占比)")
print("• groupby: 按维度聚合分析 (如不同区域/作物的效果对比)")
print("• 可视化: 图表化验收报告，直观展示洞察结果")
print("• 极飞场景: 自动化生成日报/周报，提升汇报效率")