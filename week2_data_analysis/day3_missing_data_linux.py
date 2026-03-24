"""
Week 2 Day 3: 缺失值处理与 Linux 基础
业务场景：极飞数据验收中处理传感器偶发故障导致的空值
核心技能：Pandas缺失值处理, Linux基础命令
"""

import pandas as pd
import numpy as np
import os

# 创建一个包含缺失值的模拟数据
np.random.seed(42)
size = 50
data_with_nan = {
    'sensor_id': [f'sensor_{i}' for i in range(size)],
    'temperature': np.random.uniform(15, 35, size=size).round(2),
    'humidity': np.random.uniform(30, 80, size=size).round(2),
    'aphid_detected': np.random.choice([True, False, np.nan], size=size, p=[0.4, 0.4, 0.2]), # 20%的数据缺失
    'timestamp': pd.date_range('2023-06-01', periods=size, freq='H'),
}
df_nan = pd.DataFrame(data_with_nan)

print("📊 包含缺失值的模拟传感器数据:")
print(df_nan.head(10))

print("\n" + "="*50)
print("🔧 1. 检测缺失值")
print("="*50)

# 1. 检查每列有多少缺失值
missing_counts = df_nan.isnull().sum()
print("✅ 各列缺失值数量:")
print(missing_counts)

# 2. 检查是否有任何缺失值
has_missing = df_nan.isnull().any().any()
print(f"\n✅ 数据集中是否存在缺失值: {has_missing}")

print("\n" + "="*50)
print("🔧 2. 处理缺失值")
print("="*50)

# --- 策略1: 删除缺失值 ---
df_dropped = df_nan.dropna() # 删除任何包含缺失值的行
print(f"✅ 删除缺失值后，剩余 {len(df_dropped)} 行数据")

# --- 策略2: 填充缺失值 ---
df_filled = df_nan.copy()
# 对'aphid_detected'列，用最常见的值(True/False)填充
most_common_value = df_filled['aphid_detected'].mode()[0] # 获取众数
df_filled['aphid_detected'] = df_filled['aphid_detected'].fillna(most_common_value)
print(f"✅ 用众数 '{most_common_value}' 填充缺失值后，缺失值数量: {df_filled.isnull().sum()['aphid_detected']}")

# 对数值列，用均值填充
df_filled['temperature'] = df_filled['temperature'].fillna(df_filled['temperature'].mean())
df_filled['humidity'] = df_filled['humidity'].fillna(df_filled['humidity'].mean())
print(f"✅ 用均值填充数值列后，总缺失值数量: {df_filled.isnull().sum().sum()}")

print("\n📋 填充后的数据 (前5行):")
print(df_filled.head())

print("\n" + "="*50)
print("💻 3. Linux 基础命令 (模拟)")
print("="*50)
print("在真实的 AutoDL 服务器上，你会用到这些命令来管理文件:")
print("• ls : 列出当前目录文件")
print("• cd <目录名> : 进入指定目录")
print("• pwd : 显示当前路径")
print("• find . -name '*.csv' : 在当前目录下查找所有CSV文件")
print("• grep 'error' log.txt : 在log.txt中搜索包含'error'的行")
print("\n🎯 业务解读:")
print("• 缺失值处理: 确保数据完整性，避免模型训练出错")
print("• Linux基础: 在云端服务器高效工作必备技能")
print("• 极飞场景: 自动化脚本需能应对数据质量问题")