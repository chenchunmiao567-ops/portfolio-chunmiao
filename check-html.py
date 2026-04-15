import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('=== index.html 结构检查 ===\n')

# 1. 检查 DOCTYPE 和 html 标签
doctype = html[:100]
status = '✅' if doctype.startswith('<!DOCTYPE html>') else '❌'
print(f'1. DOCTYPE: {status}')

# 2. 检查 head 部分
head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
if head_match:
    head = head_match.group(1)
    print(f'2. head 部分:')
    s1 = '✅' if 'charset="UTF-8"' in head else '❌'
    s2 = '✅' if 'viewport' in head else '❌'
    s3 = '✅' if '<title>' in head else '❌'
    s4 = '✅' if 'styles.css' in head else '❌'
    print(f'   - charset: {s1}')
    print(f'   - viewport: {s2}')
    print(f'   - title: {s3}')
    print(f'   - styles.css: {s4}')

# 3. 检查 Hero 区域
hero_match = re.search(r'<section class="hero">(.*?)</section>', html, re.DOTALL)
if hero_match:
    hero = hero_match.group(1)
    print(f'\n3. Hero 区域:')
    s1 = '✅' if 'hero-title' in hero else '❌'
    s2 = '✅' if 'hero-subtitle' in hero else '❌'
    s3 = '✅' if 'fade-in-up' in hero else '❌'
    print(f'   - hero-title: {s1}')
    print(f'   - hero-subtitle: {s2}')
    print(f'   - fade-in-up 类：{s3}')

# 4. 检查 JS Observer
observer_match = re.search(r'new IntersectionObserver', html)
s1 = '✅' if observer_match else '❌'
print(f'\n4. IntersectionObserver: {s1}')

# 5. 检查 visible 类添加逻辑
add_visible = re.findall(r"classList\.add\('visible'\)", html)
print(f'5. classList.add("visible"): {len(add_visible)} 处')

# 6. 检查 fade-in-up 元素数量
fade_elements = re.findall(r'fade-in-up', html)
print(f'6. fade-in-up 元素：{len(fade_elements)} 个')

# 7. 检查是否有语法错误
unclosed_tags = re.findall(r'<(div|section|p|span|h[1-6])(?:[^>]*)(?!/>)$', html, re.MULTILINE)
if unclosed_tags:
    print(f'\n7. ⚠️ 可能未闭合的标签：{len(unclosed_tags)} 个')
else:
    print(f'\n7. ✅ 未发现明显未闭合标签')

print(f'\n8. 文件总大小：{len(html)} 字节')
print(f'9. 总行数：{len(html.splitlines())} 行')
