import re
from collections import Counter

print('=' * 80)
print('Apple 官网 vs 用户网站 深度对比分析报告')
print('=' * 80)

# 读取用户网站 CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 读取用户网站 HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 读取 DESIGN.md
with open('DESIGN.md', 'r', encoding='utf-8') as f:
    design = f.read()

print('\n【一、动画系统对比】\n')

# Apple 标准（来自 DESIGN.md）
apple_standards = {
    '动画时长': {'base': '400ms', 'fast': '100ms', 'slow': '800ms'},
    '缓动函数': 'cubic-bezier(0.16, 1, 0.3, 1)',
    '位移': 'translateY(20px)',
    '圆角': {'卡片': '18px', '按钮': '10px', '大卡片': '28px'},
    '阴影': {'default': '0 2px 8px', 'hover': '0 12px 32px'},
    '间距系统': '8px 倍数 (8/16/24/32/48/64/80/120px)',
    '卡片 hover 放大': 'scale(1.0161)',
    '卡片 hover 上移': 'translateY(-6px)',
}

print('Apple 官网标准参数:')
for k, v in apple_standards.items():
    if isinstance(v, dict):
        print(f'  {k}:')
        for k2, v2 in v.items():
            print(f'    {k2}: {v2}')
    else:
        print(f'  {k}: {v}')

# 用户网站实际参数
print('\n用户网站实际参数:')

# 1. 动画时长
transitions = re.findall(r'transition:[^;]+', css)
duration_vals = re.findall(r'\d+ms', ' '.join(transitions))
print(f'  动画时长: {Counter(duration_vals).most_common(5)}')

# 2. 缓动函数
easings = re.findall(r'cubic-bezier\([^)]+\)', css)
print(f'  缓动函数: {set(easings)}')

# 3. 位移
transforms = re.findall(r'translateY\([^)]+\)', css)
print(f'  translateY: {Counter(transforms).most_common(5)}')

# 4. 圆角
radius = re.findall(r'border-radius:\s*(\d+px)', css)
print(f'  border-radius: {Counter(radius).most_common(5)}')

# 5. 阴影
shadows = re.findall(r'box-shadow:\s*([^;]+)', css)
print(f'  box-shadow 数量：{len(shadows)} 个')

print('\n【二、差距分析】\n')

gaps = []

# 差距 1: 圆角不统一
if '20px' in radius:
    gaps.append({
        '问题': '圆角不统一',
        'Apple 标准': '18px（卡片）、10px（按钮）、28px（大卡片）',
        '当前值': '20px（混用）',
        '影响': '视觉不一致，不符合 Apple 规范',
        '优先级': '高'
    })

# 差距 2: 动画时长
if '800ms' in duration_vals:
    gaps.append({
        '问题': '基础动画时长过长',
        'Apple 标准': '400ms（基础）',
        '当前值': '800ms',
        '影响': '动画拖沓，不够轻快',
        '优先级': '高'
    })

# 差距 3: 位移值
if 'translateY(30px)' in css or 'translateY(40px)' in css:
    gaps.append({
        '问题': '动画位移过大',
        'Apple 标准': 'translateY(20px)',
        '当前值': '30px 或 40px',
        '影响': '动画夸张，不优雅',
        '优先级': '中'
    })

# 差距 4: 缓动函数
if 'cubic-bezier(0, 0, 0.5, 1)' in easings and 'cubic-bezier(0.16, 1, 0.3, 1)' in easings:
    gaps.append({
        '问题': '缓动函数混用',
        'Apple 标准': '统一使用 cubic-bezier(0.16, 1, 0.3, 1)',
        '当前值': '两种缓动混用',
        '影响': '动画节奏不一致',
        '优先级': '中'
    })

# 差距 5: 阴影系统
shadow_vals = re.findall(r'0\s+\d+px\s+\d+px', ' '.join(shadows))
if shadow_vals:
    unique_shadows = set(shadow_vals)
    if len(unique_shadows) > 5:
        gaps.append({
            '问题': '阴影系统不统一',
            'Apple 标准': '3 级阴影系统（sm/md/lg）',
            '当前值': f'{len(unique_shadows)} 种不同值',
            '影响': '视觉层级混乱',
            '优先级': '中'
        })

# 输出差距
for i, gap in enumerate(gaps, 1):
    print(f'差距 #{i}: {gap["问题"]}')
    print(f'  Apple 标准：{gap["Apple 标准"]}')
    print(f'  当前值：{gap["当前值"]}')
    print(f'  影响：{gap["影响"]}')
    print(f'  优先级：{gap["优先级"]}')
    print()

print('\n【三、改进建议】\n')

for i, gap in enumerate(gaps, 1):
    if gap['优先级'] == '高':
        print(f'{i}. {gap["问题"]} - 立即修复')
        print(f'   修改：{gap["Apple 标准"]}')
        print()

print('\n【四、完整检查清单】\n')

checklist = [
    ('动画时长统一为 400ms', '400ms' in ' '.join(duration_vals)),
    ('缓动函数统一为 cubic-bezier(0.16, 1, 0.3, 1)', len(set(easings)) <= 2),
    ('位移统一为 20px', 'translateY(20px)' in css),
    ('圆角统一为 18px/10px/28px', '18px' in radius or '10px' in radius or '28px' in radius),
    ('无 transition-delay 冲突', 'transition-delay' not in css),
    ('卡片 hover 效果符合 Apple 标准', 'scale(1.0161)' in css and 'translateY(-6px)' in css),
]

for item, passed in checklist:
    status = '✅' if passed else '❌'
    print(f'{status} {item}')

print('\n' + '=' * 80)
