#!/usr/bin/env python
"""
工作经历优化：将平铺式改为折叠展开式
"""

import re
from pathlib import Path

html_path = Path(__file__).parent / "index.html"

with open(html_path, "r", encoding="utf-8-sig") as f:
    content = f.read()

# 示例：替换第一个华为经历（2023.03 - 2025.06）
old_huawei_1 = '''<div class="experience-item">
            <div class="experience-time fade-in-up">2023.03 - 2025.06</div>
            <div class="experience-company fade-in-up">华为技术有限公司 企业业务品牌部/茶思屋科技网站</div>
            <div class="experience-role fade-in-up">视频编辑</div>
            <div class="experience-details">'''

new_huawei_1 = '''<div class="experience-item">
            <div class="experience-time fade-in-up">2023.03 - 2025.06</div>
            <div class="experience-company fade-in-up">华为技术有限公司 企业业务品牌部/茶思屋科技网站</div>
            <div class="experience-role fade-in-up">视频编辑</div>
            
            <!-- 摘要（固定显示） -->
            <div class="project-summary">
              <h4>核心项目</h4>
              <p>• <strong>华为茶思下午茶高端访谈栏目</strong>：打造高质量科学家访谈栏目，通过数据驱动优化实现视频浏览量提升 1973.6%</p>
              <p>• <strong>华为全联接大会全流程影像服务</strong>：12 小时内完成紧急成片，成功经验固化为标准操作流程</p>
              <p>• <strong>巴塞罗那 MWC 客户证言视频</strong>：视频成为海外市场拓展的关键品牌背书资产</p>
            </div>
            
            <!-- 详情（折叠，点击展开） -->
            <button class="expand-toggle" onclick="toggleDetails(this)">
              查看完整项目详情
              <svg class="arrow" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M6 9l6 6 6-6"/>
              </svg>
            </button>
            
            <div class="collapsible-content">
              <div class="experience-details">'''

content = content.replace(old_huawei_1, new_huawei_1)

# 在最后一个</div> 前添加闭合标签
# 找到第一个华为经历的结束位置
pattern = r'(</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*