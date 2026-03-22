bugs = ['aphid','healthy','aphid',None,'aphid','','']
count_aphid = 0
for label in bugs:
    if label is None or label == '':
        continue
    if label == 'aphid':
        count_aphid += 1
        print(f"✓ 找到蚜虫！当前总数:{count_aphid}")
print(f"\n【验收报告】本图共检测到 {count_aphid} 只蚜虫")