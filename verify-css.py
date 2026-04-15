import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

print('=== 验证修复结果 ===\n')

# 1. transition-delay
delays = re.findall(r'transition-delay:\s*\d+ms;', css)
status = '✅' if len(delays)==0 else '❌'
print(f'1. transition-delay: {len(delays)} 个 {status}')

# 2. fade-in-up 初始状态
fade_rules = re.findall(r'\.fade-in-up\s*\{([^}]+)\}', css)
if fade_rules:
    rule = fade_rules[0]
    has_20px = 'translateY(20px)' in rule
    has_400ms = '400ms' in rule
    status2 = '✅' if has_20px else '❌'
    status3 = '✅' if has_400ms else '❌'
    print(f'2. translateY: 20px {status2}')
    print(f'3. transition: 400ms {status3}')

print(f'\n4. 文件大小：{len(css)} 字节')
