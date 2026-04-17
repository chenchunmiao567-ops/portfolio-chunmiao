#!/usr/bin/env python
"""
更新 HTML 中的标题格式：项目一：→ 项  目  一：
"""

import re
from pathlib import Path

html_path = Path(__file__).parent / "experience-demo.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 替换所有 <h4>项目 X：标题</h4> 格式
def replace_title(match):
    full_match = match.group(0)
    # 提取"项目 X："部分
    label_match = re.search(r'>项目 ( [一二三四五六七八九十]+)：', full_match)
    if label_match:
        num = label_match.group(1)
        # 添加 letter-spacing 的 span
        new_label = f'><span class="project-label">项目{num}</span>'
        return full_match.replace('>项目', new_label)
    return full_match

# 查找所有 h4 标签
content = re.sub(r'<h4>项目 ( [一二三四五六七八九十]+)：', replace_title, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 标题格式已更新！")
