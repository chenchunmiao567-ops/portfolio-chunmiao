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
}

// 页面加载后初始化
document.addEventListener('DOMContentLoaded', function() {
  console.log('工作经历折叠功能已加载');
});
