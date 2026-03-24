import pandas as pd
import  os
csv_file_path = os.path.join(os.path.dirname(__file__), "fake_labels.csv")
df = pd.read_csv(csv_file_path)
print("=" * 50)
print("【Pandas vs CSV模块】效率对比")
print("=" * 50)
print(f"✅ 数据形状: {df.shape[0]} 行 × {df.shape[1]} 列")
print(f"✅ 标签列预览: {df['label'].tolist()[:5]} ...")
print(f"✅ 标签统计: {df['label'].value_counts().to_dict()}")
empty_labels = df[df['label'] == '']  # 筛选所有空标签行
print(f"✅ 发现 {len(empty_labels)} 个空标签 (自动质检!)")
print("\n📊 DataFrame预览（类似Excel表格）:")
print(df.head(3))  # 只看前3行
print("\n💡 业务解读:")
print("• csv模块: 读取→循环→手动统计 (10行代码)")
print("• Pandas: 一行读取→无数种分析 (1行代码)")
print("• 极飞场景: 千万级标注数据→秒级洞察!")