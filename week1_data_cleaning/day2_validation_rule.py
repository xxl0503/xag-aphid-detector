def check_label(label):
    if label is None or str(label).strip() == '':
        return"❌ 空标签（漏标）"
    if len(str(label).strip()) < 2:
        return "❌ 标签过短（格式错误）"
    valid_categories = ['aphid', 'healthy', 'pest']
    clean_label = str(label).lower().strip()
    if clean_label not in valid_categories:
        return f"❌ 无效类别（应为{valid_categories}）"
    return "✅ 合格"
print("=" * 50)
print("【极飞数据验收测试】模拟抽查5条标注记录")
print("=" * 50)
test_cases = [
    ('aphid', '正常蚜虫标注'),
    ('', '空字符串（漏标）'),
    ('a', '单字母（格式错误）'),
    ('APHID', '大写（需标准化）'),    # ✅ 规则3会自动转小写通过
    ('invalid_label', '不存在的类别') # ❌ 规则3触发
]
for i ,(label,desc) in enumerate(test_cases,1):
    result = check_label(label)
    if "✅" in result:
        status_icon = "🟢"  # 合格用绿色圆圈
    else:
        status_icon = "🔴"
        print(f"{status_icon} 样本{i} | 描述: {desc:15} | 原始值: '{label:15}' → {result}")