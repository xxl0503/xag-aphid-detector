"""
Week 2 Day 1: 深入 Pandas DataFrame 操作
业务场景：极飞TB级遥感数据中快速定位特定区域/作物/病虫害
核心技能：数据切片、条件筛选、排序
"""

import pandas as pd
import numpy as np
import os

# 创建一个模拟的“田间数据” DataFrame
# 这里模拟了无人机采集的100条数据
np.random.seed(42)  # 保证每次生成的数据一样，方便复现
data = {
    'field_id': [f'field_{i}' for i in range(1, 101)],  # 田块ID
    'crop_type': np.random.choice(['wheat', 'corn', 'soybean'], size=100),  # 作物种类
    'aphid_count': np.random.randint(0, 1000, size=100),  # 蚜虫数量
    'pesticide_sprayed': np.random.choice([True, False], size=100),  # 是否喷洒农药
    'last_inspection_date': pd.date_range('2023-01-01', periods=100, freq='D'), # 最后检查日期
}

df = pd.DataFrame(data)
print("📊 模拟田间数据 (前5行):")
print(df.head())

print("\n" + "="*50)
print("🔍 1. DataFrame 基础切片操作")
print("="*50)

# 1. 选择单列
print("✅ 选择'作物种类'列:")
print(df['crop_type'].head(3))

# 2. 选择多列
print("\n✅ 选择'田块ID'和'蚜虫数量'两列:")
print(df[['field_id', 'aphid_count']].head(3))

# 3. 选择行（切片）
print("\n✅ 选择前3行:")
print(df[0:3])

print("\n" + "="*50)
print("🔍 2. 条件筛选（核心技能）")
print("="*50)

# 4. 筛选：找出蚜虫数量大于500的田块
high_risk_fields = df[df['aphid_count'] > 500]
print(f"✅ 发现 {len(high_risk_fields)} 个高风险田块 (蚜虫 > 500):")
print(high_risk_fields[['field_id', 'aphid_count', 'crop_type']].head())

# 5. 多条件筛选：作物为小麦 且 蚜虫数量大于500
wheat_high_risk = df[(df['crop_type'] == 'wheat') & (df['aphid_count'] > 500)]
print(f"\n✅ 小麦中的高风险田块: {len(wheat_high_risk)} 个")
print(wheat_high_risk[['field_id', 'aphid_count', 'crop_type']])

print("\n" + "="*50)
print("🔍 3. 数据排序")
print("="*50)

# 6. 按蚜虫数量降序排列，找出最严重的10个田块
top_10_riskiest = df.sort_values(by='aphid_count', ascending=False).head(10)
print("✅ 蚜虫数量最多的 Top 10 田块:")
print(top_10_riskiest[['field_id', 'aphid_count', 'crop_type']])

# 7. 按日期升序排列
recent_observations = df.sort_values(by='last_inspection_date', ascending=True).head(5)
print(f"\n✅ 最早检查的5个田块:")
print(recent_observations[['field_id', 'last_inspection_date']])

print("\n🎯 业务解读:")
print("• 切片: 快速提取关心的指标列")
print("• 筛选: 精准定位问题区域 (如高虫害、未喷药)")
print("• 排序: 优先处理最紧急的地块")
print("• 极飞场景: TB级数据秒级洞察，指导精准农业决策")