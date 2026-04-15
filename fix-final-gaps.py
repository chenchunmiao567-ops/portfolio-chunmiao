import re

print('=' * 80)
print('修复 Apple 设计系统最后差距')
print('=' * 80)

# 读取 CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

original_len = len(css)

print('\n【修复 1: 统一阴影系统为 3 级】\n')

# Apple 标准阴影
shadows = {
    'sm': '0 2px 8px rgba(0, 0, 0, 0.04)',
    'md': '0 8px 16px rgba(0, 0, 0, 0.08)',
    'lg': '0 12px 32px rgba(0, 0, 0, 0.08)',
    'hover': '0 12px 32px rgba(0, 0, 0, 0.12)',
}

# 替换各种阴影为 Apple 标准
shadow_replacements = [
    # 小阴影 → sm
    (r'box-shadow:\s*0\s+1px\s+3px\s+rgba\([^)]+\)', f'box-shadow: {shadows["sm"]}'),
    (r'box-shadow:\s*0\s+1px\s+8px\s+rgba\([^)]+\)', f'box-shadow: {shadows["sm"]}'),
    (r'box-shadow:\s*0\s+2px\s+4px\s+rgba\([^)]+\)', f'box-shadow: {shadows["sm"]}'),
    
    # 中阴影 → md
    (r'box-shadow:\s*0\s+4px\s+8px\s+rgba\([^)]+\)', f'box-shadow: {shadows["md"]}'),
    (r'box-shadow:\s*0\s+4px\s+12px\s+rgba\([^)]+\)', f'box-shadow: {shadows["md"]}'),
    (r'box-shadow:\s*0\s+6px\s+16px\s+rgba\([^)]+\)', f'box-shadow: {shadows["md"]}'),
    
    # 大阴影 → lg/hover
    (r'box-shadow:\s*0\s+8px\s+24px\s+rgba\([^)]+\)', f'box-shadow: {shadows["lg"]}'),
    (r'box-shadow:\s*0\s+8px\s+32px\s+rgba\([^)]+\)', f'box-shadow: {shadows["lg"]}'),
    (r'box-shadow:\s*0\s+12px\s+48px\s+rgba\([^)]+\)', f'box-shadow: {shadows["lg"]}'),
]

for pattern, replacement in shadow_replacements:
    count = len(re.findall(pattern, css))
    if count > 0:
        css = re.sub(pattern, replacement, css)
        print(f'✅ 替换 {count} 处：{pattern[:40]}... → {replacement[:40]}...')

print('\n【修复 2: 统一间距为 8px 倍数】\n')

# Apple 间距系统（非 8px 倍数 → 8px 倍数）
spacing_fixes = [
    ('14px', '16px'),
    ('12px', '16px'),  # 特殊情况
    ('18px', '16px'),
    ('22px', '24px'),
    ('26px', '24px'),
    ('34px', '32px'),
    ('36px', '32px'),
    ('38px', '40px'),
    ('42px', '40px'),
    ('46px', '48px'),
    ('52px', '48px'),
    ('54px', '56px'),
    ('58px', '56px'),
    ('62px', '64px'),
    ('68px', '64px'),
    ('74px', '72px'),
    ('76px', '80px'),
    ('78px', '80px'),
    ('82px', '80px'),
    ('84px', '80px'),
    ('86px', '88px'),
    ('92px', '96px'),
    ('94px', '96px'),
    ('98px', '96px'),
    ('102px', '104px'),
    ('108px', '104px'),
    ('116px', '120px'),
    ('124px', '120px'),
    ('132px', '128px'),
    ('148px', '144px'),
    ('152px', '152px'),
]

for old_val, new_val in spacing_fixes:
    # 替换 margin: Xpx
    pattern_margin = rf'margin:\s*{old_val}'
    count_margin = len(re.findall(pattern_margin, css))
    if count_margin > 0:
        css = re.sub(pattern_margin, f'margin: {new_val}', css)
        print(f'✅ margin: {old_val} → {new_val} ({count_margin} 处)')
    
    # 替换 padding: Xpx
    pattern_padding = rf'padding:\s*{old_val}'
    count_padding = len(re.findall(pattern_padding, css))
    if count_padding > 0:
        css = re.sub(pattern_padding, f'padding: {new_val}', css)
        print(f'✅ padding: {old_val} → {new_val} ({count_padding} 处)')

# 写入
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

new_len = len(css)

print(f'\n【修复完成】')
print(f'原文件大小：{original_len} 字节')
print(f'新文件大小：{new_len} 字节')
print(f'变化：{new_len - original_len} 字节')

print('\n【验证修复结果】\n')

# 重新读取验证
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 检查阴影
shadows_found = re.findall(r'box-shadow:\s*([^;]+)', css)
shadow_vals = [s.strip() for s in shadows_found]
print(f'阴影系统：{len(set(shadow_vals))} 种不同值（目标：≤3）')

# 检查间距
spacing_props = re.findall(r'(?:margin|padding)[^;]*:\s*(\d+px)', css)
spacing_vals = [int(s) for s in re.findall(r'\d+', ' '.join(spacing_props))]
spacing_mod8 = [v for v in spacing_vals if v % 8 == 0]
spacing_ratio = len(spacing_mod8) / len(spacing_vals) * 100 if spacing_vals else 0
print(f'间距系统：{len(spacing_mod8)}/{len(spacing_vals)} = {spacing_ratio:.1f}% 符合 8px 倍数（目标：100%）')

print('\n' + '=' * 80)
