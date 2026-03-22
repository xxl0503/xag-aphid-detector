import pandas as pd

# 模拟极飞场景：无人机拍摄的标注CSV（含脏数据）
raw_data = {
    'image_id': ['DJI_001.jpg', 'DJI_002.jpg', None, 'DJI_001.jpg', 'dji_003.JPG'],
    'pest_type': ['aphid', 'healthy', 'aphid', 'aphid', 'healthy '],
    'bbox': ['[100,200,50,50]', None, '[150,300,60,60]', '[100,200,50,50]', '[200,400,70,70]']
}
df = pd.DataFrame(raw_data)

def clean_field_data(df):
    """极飞数据验收标准：去重 + 空值处理 + 格式标准化"""
    # 1. 去重（避免重复标注）
    df = df.drop_duplicates(subset=['image_id'])
    # 2. 清理无效标注（去掉没有图片ID或边界框的行）
    df = df.dropna(subset=['image_id', 'bbox'])
    # 3. 标签标准化（去除空格，转小写）
    df['pest_type'] = df['pest_type'].str.strip().str.lower()
    # 4. 文件名统一（转大写）
    df['image_id'] = df['image_id'].str.upper()
    return df

# 执行清洗
clean_df = clean_field_data(df)

print("✅ 极飞数据清洗完成！")
print(clean_df.to_string(index=False))

# 保存结果
clean_df.to_csv('cleaned_field_data.csv', index=False)
print("\n💾 已自动保存为：cleaned_field_data.csv")