import re
from collections import Counter

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

print('=== CSS 文件结构检查 ===\n')

# 1. 检查 @import 和 @charset
imports = re.findall(r'@(?:import|charset)[^;]+;', css)
print(f'1. @规则：{len(imports)} 个')

# 2. 检查 :root 变量
root_vars = re.findall(r':root\s*\{([^}]+)\}', css, re.DOTALL)
if root_vars:
    vars_count = len(re.findall(r'--[\w-]+:', root_vars[0]))
    print(f'2. :root 变量：{vars_count} 个')

# 3. 检查主要选择器类型
selectors = {
    '类选择器': len(re.findall(r'\.[\w-]+\s*\{', css)),
    '@media': len(re.findall(r'@media[^{]+\{', css)),
}
print(f'3. 选择器统计:')
for name, count in selectors.items():
    print(f'   {name}: {count} 个')

# 4. 检查重复规则
rule_names = re.findall(r'([\.\w-]+)\s*\{', css)
duplicates = [(name, count) for name, count in Counter(rule_names).items() if count > 1]
print(f'4. 重复规则：{len(duplicates)} 个')
for name, count in duplicates[:10]:
    print(f'   {name}: {count} 次')

# 5. 检查 CSS 属性总数
properties = re.findall(r'[\w-]+:\s*[^;]+;', css)
print(f'5. CSS 属性总数：{len(properties)} 个')

# 6. 检查乱码
garbled = re.findall(r'[^\x00-\x7F\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\w\s\-\(\):;,.\'"\/\*@\{\}\[\]#]', css)
if garbled:
    print(f'6. 发现乱码字符：{len(garbled)} 个')
    print(f'   示例：{garbled[:5]}')
else:
    print(f'6. 无乱码字符')

print(f'\n=== 文件摘要 ===')
print(f'总行数：{len(css.splitlines())}')
print(f'总字符数：{len(css)}')
