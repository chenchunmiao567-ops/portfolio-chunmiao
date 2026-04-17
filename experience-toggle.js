// 折叠展开功能
function toggleDetails(button) {
  const content = button.nextElementSibling;
  const isExpanded = content.classList.contains('expanded');
  
  // 切换状态
  content.classList.toggle('expanded');
  button.classList.toggle('active');
  
  // 更新按钮文字
  const textNode = button.childNodes[0];
  if (isExpanded) {
    textNode.textContent = '查看完整项目详情 ';
  } else {
    textNode.textContent = '收起详情 ';
  }
  
  // 展开时：逐行显示内容
  if (!isExpanded) {
    animateDetailSections(content);
  }
}

// 逐行动画函数
function animateDetailSections(container) {
  const sections = container.querySelectorAll('.detail-section');
  
  sections.forEach((section, index) => {
    // 清除之前的动画状态
    section.classList.remove('visible');
    
    // 延迟显示（每行间隔 100ms）
    setTimeout(() => {
      section.classList.add('visible');
    }, index * 100);
  });
}

// 页面加载后初始化
document.addEventListener('DOMContentLoaded', function() {
  console.log('工作经历折叠功能已加载');
});
