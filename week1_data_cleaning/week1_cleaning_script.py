"""
Week 1 综合脚本：一键数据清洗与质检
业务场景：极飞标注数据验收与预处理流水线
融合技能：W1D2(质检函数) + W1D4(Pandas数据处理)
"""

import pandas as pd
import os

# =============== 1. 复制 W1D2 的质检函数 ===============
def check_label(label):
    """检查单个标签是否合格"""
    if label is None or str(label).strip() == '':
        return "❌ 空标签"
    if len(str(label).strip()) < 2:
        return "❌ 标签过短"
    valid_categories = ['aphid', 'healthy', 'pest']
    clean_label = str(label).lower().strip()
    if clean_label not in valid_categories:
        return "❌ 无效类别"
    return "✅ 合格"

# =============== 2. 执行数据清洗流程 ===============
# 定义文件路径
current_dir = os.path.dirname(__file__)
input_file = os.path.join(current_dir, "fake_labels.csv")
output_file = os.path.join(current_dir, "cleaned_annotations.csv")

print("=" * 60)
print("🚀 开始执行极飞标注数据清洗任务...")
print("=" * 60)

# 1. 读取原始数据
df = pd.read_csv(input_file)
print(f"📦 已读取原始数据: {len(df)} 行")

# 2. 应用质检函数，创建“质检结果”列
df['quality_check'] = df['label'].apply(check_label)

# 3. 分析质检结果
report = df['quality_check'].value_counts()
print("\n📋 质检报告:")
for issue, count in report.items():
    print(f"   {issue}: {count} 行")

# 4. 筛选出合格的数据
cleaned_df = df[df['quality_check'] == '✅ 合格'].copy()

# 5. 丢弃质检时添加的辅助列，恢复原始列
cleaned_df = cleaned_df.drop(columns=['quality_check'])

print(f"\n✅ 清洗完成！合格数据: {len(cleaned_df)} 行")

# 6. 保存清洗后的数据
cleaned_df.to_csv(output_file, index=False)
print(f"💾 已保存清洗结果到: {output_file}")

print("\n🎯 业务解读:")
print("• 一键完成：加载→质检→筛选→保存")
print("• 极飞场景：每日TB级标注数据自动化验收")
print("• 为高质量模型训练提供纯净数据源")

print("\n📊 原始数据预览 (含问题):")
print(df.head())
print("\n📋 清洗后数据预览 (仅合格):")
print(cleaned_df.head())

print("\n" + "=" * 60)
print("🎊 Week 1 任务圆满完成！")
print("   你已掌握：函数封装、文件IO、Pandas分析、脚本融合")
print("=" * 60)