#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""检查 about-intro 的 span 标签"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 查找 about-intro 段落
about_intro = re.search(r'<p class="about-intro">(.*?)</p>', html, re.DOTALL)
if about_intro:
    content = about_intro.group(1)
    spans = re.findall(r'<span[^>]*>', content)
    print('about-intro 中的 span 标签:')
    for i, span in enumerate(spans):
        has_fade = 'fade-in-up' in span
        has_inline_block = 'display: inline-block' in span
        print(f'{i+1}. {span}')
        print(f'   fade-in-up: {"✅" if has_fade else "❌"}')
        print(f'   display:inline-block: {"✅" if has_inline_block else "❌"}')
        print()
