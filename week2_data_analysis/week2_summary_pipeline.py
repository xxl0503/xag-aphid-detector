"""
Week 2 总结：数据洞察与分析流水线
融合技能：DataFrame操作 + 统计分析 + 缺失值处理
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
# 1. 加载数据 (模拟)
np.random.seed(42)
data = {
    'field_id': [f'field_{i}' for i in range(1, 201)],
    'region': np.random.choice(['North', 'South', 'East', 'West'], size=200),
    'crop_type': np.random.choice(['wheat', 'corn', 'soybean'], size=200),
    'aphid_count': np.random.randint(0, 1000, size=200),
    'pesticide_sprayed': np.random.choice([True, False, np.nan], size=200, p=[0.45, 0.45, 0.1]),
    'timestamp': pd.date_range('2023-01-01', periods=200, freq='D'),
}
df = pd.DataFrame(data)

print("="*60)
print("🚀 Week 2 数据洞察流水线启动")
print("="*60)

# 2. 数据清洗
print(f"📦 原始数据: {len(df)} 行")
df_clean = df.dropna() # 简单清洗
print(f"🧹 清洗后数据: {len(df_clean)} 行")

# 3. 数据分析
high_risk = df_clean[df_clean['aphid_count'] > df_clean['aphid_count'].quantile(0.8)]
print(f"⚠️  高风险田块 (Top 20%): {len(high_risk)} 个")

# 4. 统计汇总
summary = df_clean.groupby(['region', 'crop_type']).agg({
    'aphid_count': ['mean', 'max'],
    'pesticide_sprayed': 'sum' # 喷药次数
}).round(2)

print("\n📋 区域-作物类型汇总报告 (部分):")
print(summary.head(6))

# 5. 可视化
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
region_avg = df_clean.groupby('region')['aphid_count'].mean()
plt.bar(region_avg.index, region_avg.values)
plt.title('各区域平均蚜虫数量')

plt.subplot(1, 2, 2)
crop_dist = df_clean['crop_type'].value_counts()
plt.pie(crop_dist.values, labels=crop_dist.index, autopct='%1.1f%%')
plt.title('作物类型分布')

plt.tight_layout()
plt.show()

print("\n🎯 Week 2 业务价值:")
print("• 一键式数据洞察流水线")
print("• 从原始数据到可视化报告")
print("• 为决策提供数据支撑")

print("\n" + "="*60)
print("🎊 Week 2 任务圆满完成！")
print("="*60)