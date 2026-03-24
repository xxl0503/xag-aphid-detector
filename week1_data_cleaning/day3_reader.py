import csv, os
fp = os.path.join(os.path.dirname(__file__), "fake_labels.csv")
try:
    data = list(csv.DictReader(open(fp, encoding='utf-8')))
    print(f"✅ 读取 {len(data)} 行 | 前3行：")
    for i, r in enumerate(data[:3], 1):
        print(f"{i}. {r['image_id']} | {r['label']:12} | 置信度: {r['confidence']}")
except FileNotFoundError:
    print("❌ 文件不存在")