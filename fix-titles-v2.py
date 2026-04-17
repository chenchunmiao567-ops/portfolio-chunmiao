#!/usr/bin/env python
"""
恢复标题格式：<h4>项目一：华为茶思...</h4>
但添加 span 包裹"项目一"用于分散对齐
"""

import re
from pathlib import Path

html_path = Path(__file__).parent / "experience-demo.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 替换所有 <h4>项目 X：标题</h4> 格式
def replace_title(match):
    num = match.group(1)
    title = match.group(2)
    return f'<h4><span class="project-label">项目{num}</span>{title}</h4>'

# 查找并替换所有 h4 标签
content = re.sub(r'<h4>项目 ( [一二三四五六七八九十]+)：(.*?)</h4>', replace_title, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 标题格式已更新！")
