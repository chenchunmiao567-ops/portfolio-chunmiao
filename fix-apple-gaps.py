import re
from collections import Counter

print('=' * 80)
print('修复 Apple 设计系统差距')
print('=' * 80)

# 读取 CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

original_len = len(css)

print('\n【修复 1: 统一圆角】\n')

# border-radius: 20px → 18px（卡片）
css = re.sub(r'border-radius:\s*20px', 'border-radius: 18px', css)
print('✅ border-radius: 20px → 18px（卡片）')

# 确保按钮是 10px
css = re.sub(r'(button[^{]*\{[^}]*)border-radius:\s*\d+px', r'\1border-radius: 10px', css, flags=re.DOTALL)
print('✅ 按钮 border-radius: 10px')

# 确保大卡片（视频/优势）是 28px
css = re.sub(r'(\.(?:video-card|advantage-card)[^{]*\{[^}]*)border-radius:\s*\d+px', r'\1border-radius: 28px', css, flags=re.DOTALL)
print('✅ 大卡片 border-radius: 28px')

print('\n【修复 2: 统一动画时长】\n')

# 800ms → 400ms（基础动画）
css = re.sub(r'transition:\s*opacity\s+800ms', 'transition: opacity 400ms', css)
css = re.sub(r'transition:\s*transform\s+800ms', 'transition: transform 400ms', css)
print('✅ transition: 800ms → 400ms')

print('\n【修复 3: 统一缓动函数】\n')

# cubic-bezier(0, 0, 0.5, 1) → cubic-bezier(0.16, 1, 0.3, 1)
css = re.sub(r'cubic-bezier\(0,\s*0,\s*0\.5,\s*1\)', 'cubic-bezier(0.16, 1, 0.3, 1)', css)
print('✅ 缓动函数统一为 cubic-bezier(0.16, 1, 0.3, 1)')

print('\n【修复 4: 统一阴影系统】\n')

# 定义 Apple 标准阴影
shadows = {
    'sm': '0 2px 8px rgba(0, 0, 0, 0.04)',
    'md': '0 8px 16px rgba(0, 0, 0, 0.08)',
    'lg': '0 12px 32px rgba(0, 0, 0, 0.08)',
    'hover': '0 12px 32px rgba(0, 0, 0, 0.12)',
}

# 替换常见阴影模式
css = re.sub(r'box-shadow:\s*0\s+1px\s+3px\s+rgba\([^)]+\)', f'box-shadow: {shadows["sm"]}', css)
print(f'✅ box-shadow: 0 1px 3px → {shadows["sm"]}')

css = re.sub(r'box-shadow:\s*0\s+1px\s+8px\s+rgba\([^)]+\)', f'box-shadow: {shadows["sm"]}', css)
print(f'✅ box-shadow: 0 1px 8px → {shadows["sm"]}')

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

# 检查圆角
radius = re.findall(r'border-radius:\s*(\d+px)', css)
print(f'border-radius 分布：{dict(Counter(radius))}')

# 检查动画时长
durations = re.findall(r'transition:[^;]*(\d+ms)', css)
print(f'transition 时长分布：{dict(Counter(durations))}')

# 检查缓动
easings = re.findall(r'cubic-bezier\([^)]+\)', css)
print(f'缓动函数：{set(easings)}')

print('\n' + '=' * 80)
