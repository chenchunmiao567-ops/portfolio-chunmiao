import re
from collections import Counter

print('=' * 80)
print('Apple 官网 vs 用户网站 完整对比审计')
print('=' * 80)

# 读取用户网站文件
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Apple 设计系统标准（基于 DESIGN.md 和 Apple 官网分析）
apple_standards = {
    '动画': {
        '时长': {'fast': '100ms', 'base': '400ms', 'slow': '800ms'},
        '缓动': 'cubic-bezier(0.16, 1, 0.3, 1)',
        '位移': 'translateY(20px)',
        '延迟间隔': '100ms（依次浮现）',
    },
    '圆角': {
        '卡片': '18px',
        '按钮': '10px',
        '大卡片': '28px',
        '标签': '6px',
    },
    '阴影': {
        'sm': '0 2px 8px rgba(0,0,0,0.04)',
        'md': '0 8px 16px rgba(0,0,0,0.08)',
        'lg': '0 12px 32px rgba(0,0,0,0.08)',
        'hover': '0 12px 32px rgba(0,0,0,0.12)',
    },
    '间距': {
        '系统': '8px 倍数',
        '区块': '120px（桌面）/ 80px（移动）',
        '卡片内边距': '24px',
    },
    '卡片 Hover': {
        '放大': 'scale(1.0161)',
        '上移': 'translateY(-6px)',
        '时长': '400ms',
    },
    '字体': {
        '标题': '68px/96px（响应式）',
        '副标题': '24px',
        '正文': '15px/17px',
        '字重': '700（标题）/ 400（正文）',
        '字间距': '-0.03em（标题）',
    },
    '颜色': {
        '背景': '#FFFFFF / #F5F5F7',
        '标题': '#1D1D1F',
        '正文': '#86868B',
        '链接': '#0071E3',
    },
    '导航栏': {
        '高度': '48px',
        '背景': 'rgba(255,255,255,0.95)',
        '模糊': 'backdrop-filter: saturate(180%) blur(20px)',
    },
}

print('\n【Apple 设计系统标准】\n')
for category, items in apple_standards.items():
    print(f'{category}:')
    for key, value in items.items():
        print(f'  {key}: {value}')
    print()

print('\n' + '=' * 80)
print('【用户网站当前状态检查】')
print('=' * 80)

# 检查各项
checks = []

# 1. 动画时长
transitions = re.findall(r'transition:[^;]+', css)
durations = re.findall(r'\d+ms', ' '.join(transitions))
duration_counts = Counter(durations)
checks.append({
    '项目': '动画时长',
    'Apple 标准': '400ms（基础）',
    '当前值': str(duration_counts.most_common(3)),
    '状态': '✅' if '400ms' in duration_counts else '❌',
})

# 2. 缓动函数
easings = set(re.findall(r'cubic-bezier\([^)]+\)', css))
checks.append({
    '项目': '缓动函数',
    'Apple 标准': 'cubic-bezier(0.16, 1, 0.3, 1)',
    '当前值': str(easings),
    '状态': '✅' if len(easings) <= 2 else '❌',
})

# 3. 位移
transforms = re.findall(r'translateY\([^)]+\)', css)
transform_counts = Counter(transforms)
checks.append({
    '项目': 'translateY',
    'Apple 标准': '20px（淡入）/ -6px（hover）',
    '当前值': str(transform_counts.most_common(5)),
    '状态': '✅' if 'translateY(20px)' in transform_counts else '❌',
})

# 4. 圆角
radius = re.findall(r'border-radius:\s*(\d+px)', css)
radius_counts = Counter(radius)
checks.append({
    '项目': '圆角',
    'Apple 标准': '18px/10px/28px',
    '当前值': str(radius_counts.most_common(5)),
    '状态': '✅' if '18px' in radius_counts or '10px' in radius_counts or '28px' in radius_counts else '❌',
})

# 5. 阴影
shadows = re.findall(r'box-shadow:\s*([^;]+)', css)
shadow_vals = [s.strip() for s in shadows]
checks.append({
    '项目': '阴影系统',
    'Apple 标准': '3 级（sm/md/lg）',
    '当前值': f'{len(set(shadow_vals))} 种不同值',
    '状态': '✅' if len(set(shadow_vals)) <= 5 else '❌',
})

# 6. 卡片 Hover
hover_scale = 'scale(1.0161)' in css
hover_translate = 'translateY(-6px)' in css
checks.append({
    '项目': '卡片 Hover',
    'Apple 标准': 'scale(1.0161) + translateY(-6px)',
    '当前值': f'scale={hover_scale}, translate={hover_translate}',
    '状态': '✅' if hover_scale and hover_translate else '❌',
})

# 7. 间距系统
spacing_props = re.findall(r'(?:margin|padding)[^;]*:\s*(\d+px)', css)
spacing_vals = [int(s) for s in re.findall(r'\d+', ' '.join(spacing_props))]
spacing_mod8 = [v for v in spacing_vals if v % 8 == 0]
spacing_ratio = len(spacing_mod8) / len(spacing_vals) if spacing_vals else 0
checks.append({
    '项目': '间距系统',
    'Apple 标准': '8px 倍数',
    '当前值': f'{len(spacing_mod8)}/{len(spacing_vals)} 符合 8px 倍数',
    '状态': '✅' if spacing_ratio > 0.8 else '❌',
})

# 8. 字体层级
font_sizes = re.findall(r'font-size:\s*(\d+px)', css)
checks.append({
    '项目': '字体大小',
    'Apple 标准': '68px/96px（标题）, 15px/17px（正文）',
    '当前值': str(set(font_sizes)),
    '状态': '✅' if '68px' in font_sizes or '96px' in font_sizes else '❌',
})

# 9. 导航栏
navbar_height = re.findall(r'height:\s*(\d+px)', css)
backdrop = 'backdrop-filter' in css
checks.append({
    '项目': '导航栏',
    'Apple 标准': '48px + backdrop-filter blur(20px)',
    '当前值': f'height={navbar_height}, backdrop={backdrop}',
    '状态': '✅' if '48px' in navbar_height and backdrop else '❌',
})

# 10. 动画延迟逻辑
delay_logic = 'index * 100' in js or 'delay = index' in js
checks.append({
    '项目': '动画延迟',
    'Apple 标准': '按 DOM 顺序 100ms 间隔',
    '当前值': f'延迟逻辑={delay_logic}',
    '状态': '✅' if delay_logic else '❌',
})

# 输出检查结果
print('\n| 项目 | Apple 标准 | 当前值 | 状态 |')
print('|------|-----------|--------|------|')
for check in checks:
    print(f"| {check['项目']} | {check['Apple 标准']} | {check['当前值'][:40]}... | {check['状态']} |")

# 统计
passed = sum(1 for c in checks if c['状态'] == '✅')
total = len(checks)
percentage = (passed / total * 100) if total else 0

print(f'\n总体符合度：{passed}/{total} = {percentage:.1f}%')

print('\n' + '=' * 80)
print('【待修复项目】')
print('=' * 80)

for check in checks:
    if check['状态'] == '❌':
        print(f"\n❌ {check['项目']}")
        print(f"   Apple 标准：{check['Apple 标准']}")
        print(f"   当前值：{check['当前值']}")

print('\n' + '=' * 80)
