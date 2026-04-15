import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 找到关于我板块的完整结构
about_match = re.search(r'<section[^>]*id="about"[^>]*>(.*?)</section>', html, re.DOTALL)

if about_match:
    about_section = about_match.group(1)
    
    # 查找所有带 fade-in-up 的元素
    fade_elements = re.findall(r'class="([^"]*fade-in-up[^"]*)"', about_section)
    
    print(f'关于我板块中找到 {len(fade_elements)} 个 fade-in-up 元素:\n')
    
    # 按顺序打印
    for i, classes in enumerate(fade_elements, 1):
        print(f'{i}. {classes}')
    
    print(f'\n\n容器结构:')
    # 查找容器
    containers = re.findall(r'<div[^>]*class="([^"]*)"[^>]*>(?:[^<]*fade-in-up)', about_section)
    unique_containers = set(containers)
    for c in unique_containers:
        print(f'  - {c}')
else:
    print('未找到关于我板块')
