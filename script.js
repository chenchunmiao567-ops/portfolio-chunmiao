/**
 * Chunmiao Portfolio - Apple Style
 * 核心交互逻辑 v2.0
 */

(function() {
  'use strict';

  // DOM Ready
  document.addEventListener('DOMContentLoaded', init);

  function init() {
    initNavigation();
    initNavbarScroll();
    initCarousel();
    initCopyToClipboard();
    initScrollAnimations();
    initBackToTop();
  }

  // ========== 导航平滑滚动 ==========
  function initNavigation() {
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href === '#' || !href.startsWith('#')) return;

      link.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.getElementById(href.slice(1));
        if (!target) return;

        const offset = target.offsetTop - 48; // 导航栏高度
        window.scrollTo({ top: offset, behavior: 'smooth' });
      });
    });
  }

  // ========== 导航栏滚动效果 ==========
  function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;

    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          navbar.classList.toggle('scrolled', window.scrollY > 50);
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  // ========== 轮播图 ==========
  function initCarousel() {
    const container = document.querySelector('.carousel-container');
    const track = document.querySelector('.carousel-track');
    const prevBtn = document.querySelector('.carousel-prev');
    const nextBtn = document.querySelector('.carousel-next');
    const dotsContainer = document.querySelector('.carousel-dots');

    if (!track || !prevBtn || !nextBtn) return;

    const originalItems = Array.from(track.querySelectorAll('.carousel-item'));
    const itemCount = originalItems.length;
    
    if (itemCount === 0) return;

    // 克隆首尾项实现无缝循环
    const firstClone = originalItems[0].cloneNode(true);
    const lastClone = originalItems[itemCount - 1].cloneNode(true);
    firstClone.classList.add('carousel-clone');
    lastClone.classList.add('carousel-clone');
    
    track.appendChild(firstClone);
    track.insertBefore(lastClone, track.firstChild);

    const allItems = Array.from(track.querySelectorAll('.carousel-item'));
    let currentIndex = 1; // 从第一个真实项开始
    let isTransitioning = false;
    let autoPlayTimer = null;

    // 创建指示点
    function createDots() {
      if (!dotsContainer) return;
      dotsContainer.innerHTML = '';
      
      for (let i = 0; i < itemCount; i++) {
        const dot = document.createElement('button');
        dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
        dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
        dot.addEventListener('click', () => {
          stopAutoPlay();
          goToSlide(i + 1);
          startAutoPlay();
        });
        dotsContainer.appendChild(dot);
      }
    }

    // 更新轮播位置
    function updatePosition(animate = true) {
      const itemWidth = allItems[0].offsetWidth;
      const gap = parseInt(getComputedStyle(track).gap) || 0;
      const offset = currentIndex * (itemWidth + gap);
      
      track.style.transition = animate ? 'transform 0.5s cubic-bezier(0.16, 1, 0.3, 1)' : 'none';
      track.style.transform = `translateX(-${offset}px)`;

      // 更新指示点
      const dots = dotsContainer?.querySelectorAll('.carousel-dot');
      dots?.forEach((dot, i) => {
        dot.classList.toggle('active', i === (currentIndex - 1 + itemCount) % itemCount);
      });
    }

    // 跳转到指定索引
    function goToSlide(index) {
      if (isTransitioning) return;
      isTransitioning = true;
      currentIndex = index;
      updatePosition(true);
      
      setTimeout(() => {
        isTransitioning = false;
      }, 500);
    }

    // 下一张
    function next() {
      if (isTransitioning) return;
      currentIndex++;
      updatePosition(true);

      // 检查是否到达克隆项
      if (currentIndex >= allItems.length - 1) {
        setTimeout(() => {
          currentIndex = 1;
          updatePosition(false);
        }, 500);
      }
    }

    // 上一张
    function prev() {
      if (isTransitioning) return;
      currentIndex--;
      updatePosition(true);

      // 检查是否到达克隆项
      if (currentIndex <= 0) {
        setTimeout(() => {
          currentIndex = allItems.length - 2;
          updatePosition(false);
        }, 500);
      }
    }

    // 自动播放
    function startAutoPlay() {
      stopAutoPlay();
      autoPlayTimer = setInterval(next, 4000);
    }

    function stopAutoPlay() {
      if (autoPlayTimer) {
        clearInterval(autoPlayTimer);
        autoPlayTimer = null;
      }
    }

    // 事件绑定
    prevBtn.addEventListener('click', () => {
      stopAutoPlay();
      prev();
      startAutoPlay();
    });

    nextBtn.addEventListener('click', () => {
      stopAutoPlay();
      next();
      startAutoPlay();
    });

    // 鼠标悬停暂停
    container?.addEventListener('mouseenter', stopAutoPlay);
    container?.addEventListener('mouseleave', startAutoPlay);

    // 触摸滑动
    let touchStartX = 0;
    container?.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    container?.addEventListener('touchend', (e) => {
      const touchEndX = e.changedTouches[0].screenX;
      const diff = touchStartX - touchEndX;
      
      if (Math.abs(diff) > 50) {
        stopAutoPlay();
        diff > 0 ? next() : prev();
        startAutoPlay();
      }
    }, { passive: true });

    // 窗口大小改变时重置
    window.addEventListener('resize', () => {
      updatePosition(false);
    });

    // 初始化
    createDots();
    updatePosition(false);
    startAutoPlay();
  }

  // ========== 复制到剪贴板 ==========
  function initCopyToClipboard() {
    const items = document.querySelectorAll('.contact-clickable');
    
    items.forEach(item => {
      item.addEventListener('click', async () => {
        const text = item.dataset.copy;
        const tooltip = item.querySelector('.copy-tooltip');
        if (!text || !tooltip) return;

        try {
          await navigator.clipboard.writeText(text);
          showCopied(tooltip);
        } catch (err) {
          // 降级方案
          const textarea = document.createElement('textarea');
          textarea.value = text;
          textarea.style.cssText = 'position:fixed;opacity:0;';
          document.body.appendChild(textarea);
          textarea.select();
          
          try {
            document.execCommand('copy');
            showCopied(tooltip);
          } catch (e) {
            console.error('Copy failed:', e);
          }
          
          document.body.removeChild(textarea);
        }
      });
    });

    function showCopied(tooltip) {
      const original = tooltip.textContent;
      tooltip.textContent = 'Copied!';
      tooltip.style.cssText = 'background:var(--color-blue);color:var(--color-white);';
      
      setTimeout(() => {
        tooltip.textContent = original;
        tooltip.style.cssText = '';
      }, 1500);
    }
  }

  // ========== 滚动动画（Apple 官方标准） ==========
  // 参数来源：apple-animation-report.md
  function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.fade-in-up, .section-title, .section-subtitle');
    
    const observerOptions = {
      rootMargin: '0px 0px 0px 0px',  // 元素底部接触视口底部时立即触发（修复：之前要进入 150px 才触发，导致动画太晚）
      threshold: 0.01                     // 1% 可见就触发（Apple 标准）
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('visible')) {
          // ✅ 按板块类型精确分组
          let siblings;
          let index = -1;
          
          if (entry.target.classList.contains('stat-inline')) {
            // 统计数据：最先进入（索引 0-1）
            const statsContainer = entry.target.closest('.about-stats-inline');
            if (statsContainer) {
              siblings = Array.from(statsContainer.querySelectorAll('.stat-inline'));
              index = siblings.indexOf(entry.target);
            }
          } else if (entry.target.classList.contains('skills-title')) {
            // 核心技能标题：在统计数据之后（索引 2）
            index = 2;
            siblings = [entry.target];
          } else if (entry.target.classList.contains('skill-tag')) {
            // 核心技能标签：按 data-order 排序（标签 1-10，延迟 300-1200ms）
            const skillsContainer = entry.target.closest('.skills-grid');
            if (skillsContainer) {
              siblings = Array.from(skillsContainer.querySelectorAll('.skill-tag[data-order]'));
              siblings.sort((a, b) => parseInt(a.dataset.order) - parseInt(b.dataset.order));
              index = siblings.indexOf(entry.target) + 3;  // +3 因为统计数据 2 个 + 标题 1 个
            }
          } else if (entry.target.classList.contains('advantages-title')) {
            // 核心优势标题：和卡片统一分组，标题索引 0，卡片索引 1-6
            const section = entry.target.closest('.about-advantages') || entry.target.closest('.section');
            if (section) {
              siblings = Array.from(section.querySelectorAll('.advantages-title, .advantage-card'));
              index = siblings.indexOf(entry.target);
            }
          } else if (entry.target.classList.contains('advantage-card')) {
            // 核心优势卡片：和标题统一分组，前 3 个快，后 3 个慢
            const section = entry.target.closest('.about-advantages') || entry.target.closest('.section');
            if (section) {
              siblings = Array.from(section.querySelectorAll('.advantages-title, .advantage-card'));
              index = siblings.indexOf(entry.target);
            }
          } else if (entry.target.closest('.experience-item')) {
            // 工作经历：统一按 DOM 顺序计算（时间→公司→职位→项目 1→服务对象→项目 2→...）
            const experienceItem = entry.target.closest('.experience-item');
            const allElements = Array.from(experienceItem.querySelectorAll(':scope > .fade-in-up, :scope .experience-details p.fade-in-up'));
            index = allElements.indexOf(entry.target);
            siblings = allElements;
          } else {
            // 其他板块：按 section 分组
            const parent = entry.target.closest('.section') || entry.target.parentElement;
            siblings = parent ? Array.from(parent.querySelectorAll('.fade-in-up')) : [];
            index = siblings.indexOf(entry.target);
          }
          
          // Apple 标准：100ms 间隔，依次浮现
          const delay = index >= 0 ? index * 100 : 0;
          
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, delay);
          
          // 动画触发后停止监听，避免重复触发
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    animatedElements.forEach(el => observer.observe(el));
  }

  // ========== 回到顶部 ==========
  function initBackToTop() {
    const btn = document.getElementById('backToTop');
    if (!btn) return;

    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          const scrollTop = window.scrollY;
          const windowHeight = window.innerHeight;
          const docHeight = document.documentElement.scrollHeight;
          
          btn.classList.toggle('visible', scrollTop + windowHeight >= docHeight - 300);
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

})();
