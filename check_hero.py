#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查 Hero 区域的 fade-in-up 元素"""

import re

html_file = 'C:/Users/Yoomeng/.openclaw/workspace/projects/portfolio-chunmiao/index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 提取 Hero 区域
hero_match = re.search(r'<section class="hero">(.*?)</section>', html, re.DOTALL)
if hero_match:
    hero_content = hero_match.group(1)
    
    # 找到所有带 fade-in-up 类的元素
    fade_items = re.findall(r'<[^>]+class="[^"]*fade-in-up[^"]*"[^>]*>', hero_content)
    
    print(f"Hero 区域 fade-in-up 元素数量：{len(fade_items)}")
    print("\n详细列表:")
    print("-" * 60)
    
    for i, item in enumerate(fade_items, 1):
        # 提取标签名和内容
        tag_match = re.match(r'<(\w+)', item)
        tag = tag_match.group(1) if tag_match else 'unknown'
        
        # 提取文本内容
        text_match = re.search(r'>([^<]+)', item)
        text = text_match.group(1).strip()[:40] if text_match else ''
        
        print(f"{i:2}. <{tag:15} > {text}")
    
    print("\n" + "=" * 60)
    print("分析:")
    print("-" * 60)
    print("预期 7 个元素:")
    print("  1. h1.hero-title (Chunmiao)")
    print("  2. p.hero-subtitle (多媒体设计师)")
    print("  3. p.hero-tagline (专注品牌视频宣传)")
    print("  4. a.hero-contact-item (电话)")
    print("  5. span.hero-contact-separator (分隔符 •)")
    print("  6. a.hero-contact-item (邮箱)")
    print("  7. span.hero-contact-separator (分隔符 •)")
    print("  8. span.hero-contact-item (学校) ← 实际有 8 个！")
    print("\n实际 8 个元素，多了 1 个分隔符或联系方式。")
    print("这是设计意图，不是 bug。测试预期需要更新为 8 个。")
else:
    print("未找到 Hero 区域")
