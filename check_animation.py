#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""检查动画相关的 HTML 和 CSS"""

import re

# 读取 HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 读取 CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("=" * 60)
print("📊 动画诊断报告")
print("=" * 60)

# 1. 检查 HTML 中的 fade-in-up 类
print("\n【1】HTML 检查 - fade-in-up 类分布")
print("-" * 60)

sections = {
    'Hero': r'(<section class="hero">.*?</section>)',
    '关于我': r'(<section id="about".*?</section>)',
    '品牌宣传片': r'(<section id="brand".*?</section>)',
    '三维动画': r'(<section id="3d".*?</section>)',
    'MG 动画': r'(<section id="mg".*?</section>)',
    '短视频': r'(<section id="short".*?</section>)',
    'AE 特效': r'(<section id="ae".*?</section>)',
    '联系我': r'(<section id="contact".*?</section>)',
}

for name, pattern in sections.items():
    match = re.search(pattern, html, re.DOTALL)
    if match:
        content = match.group(1)
        count = len(re.findall(r'fade-in-up', content))
        print(f"  ✅ {name}: {count} 个 fade-in-up 类")
    else:
        print(f"  ❌ {name}: 未找到板块")

# 2. 检查 CSS 基础类
print("\n【2】CSS 检查 - .fade-in-up 基础类")
print("-" * 60)

fade_in_up = re.search(r'\.fade-in-up\s*\{([^}]+)\}', css)
if fade_in_up:
    props = fade_in_up.group(1)
    has_opacity = 'opacity: 0' in props
    has_transform = 'transform: translateY' in props
    has_transition = 'transition:' in props
    print(f"  opacity: 0 → {'✅' if has_opacity else '❌'}")
    print(f"  transform: translateY → {'✅' if has_transform else '❌'}")
    print(f"  transition → {'✅' if has_transition else '❌'}")
else:
    print("  ❌ 未找到 .fade-in-up 基础类")

# 3. 检查 .fade-in-up.visible 类
print("\n【3】CSS 检查 - .fade-in-up.visible 类")
print("-" * 60)

visible = re.search(r'\.fade-in-up\.visible\s*\{([^}]+)\}', css)
if visible:
    props = visible.group(1)
    has_opacity = 'opacity: 1' in props
    has_transform = 'transform: translateY(0)' in props
    print(f"  opacity: 1 → {'✅' if has_opacity else '❌'}")
    print(f"  transform: translateY(0) → {'✅' if has_transform else '❌'}")
else:
    print("  ❌ 未找到 .fade-in-up.visible 类")

# 4. 检查 transition-delay 规则
print("\n【4】CSS 检查 - transition-delay 规则")
print("-" * 60)

delay_rules = re.findall(r'transition-delay:', css)
print(f"  共找到 {len(delay_rules)} 个 transition-delay 规则")

# 5. 检查 JavaScript Observer
print("\n【5】JavaScript 检查 - IntersectionObserver")
print("-" * 60)

has_observer = 'IntersectionObserver' in html
has_querySelector = 'querySelectorAll' in html and '.fade-in-up' in html
has_addClass = 'classList.add' in html and 'visible' in html

print(f"  IntersectionObserver 存在 → {'✅' if has_observer else '❌'}")
print(f"  选择 .fade-in-up 元素 → {'✅' if has_querySelector else '❌'}")
print(f"  添加 visible 类 → {'✅' if has_addClass else '❌'}")

# 6. 检查 rootMargin 配置
print("\n【6】JavaScript 检查 - Observer 配置")
print("-" * 60)

root_margin = re.search(r'rootMargin:\s*[\'"]([^\'"]+)[\'"]', html)
threshold = re.search(r'threshold:\s*([0-9.]+)', html)

if root_margin:
    print(f"  rootMargin: {root_margin.group(1)}")
if threshold:
    print(f"  threshold: {threshold.group(1)}")

# 7. 关键问题检查
print("\n【7】关键问题诊断")
print("-" * 60)

issues = []

# 检查 about-intro span 是否有 display: inline-block
intro_spans = re.findall(r'<span class="fade-in-up"[^>]*style="display:\s*inline-block"', html)
if intro_spans:
    print(f"  ✅ about-intro span 有 display: inline-block ({len(intro_spans)}个)")
else:
    issues.append("⚠️ about-intro span 可能缺少 display: inline-block")
    print(f"  ⚠️ about-intro span 可能缺少 display: inline-block")

# 检查 CSS 文件是否干净
if '\x00' in css:
    issues.append("❌ CSS 文件包含 null 字节（乱码）")
    print("  ❌ CSS 文件包含 null 字节（乱码）")
else:
    print("  ✅ CSS 文件干净，无乱码")

print("\n" + "=" * 60)
if issues:
    print("⚠️ 发现问题:")
    for issue in issues:
        print(f"  {issue}")
else:
    print("✅ 未发现问题，动画应该正常工作")
print("=" * 60)
