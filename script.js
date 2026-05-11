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
  // 修复 2026-05-11 v2：按 section 分组 + 首个元素触发 + DOM 顺序严格递增
  // 参数来源：apple-animation-report.md
  //
  // 修复的问题：
  //   1. 旧版每个元素独立触发 setTimeout，滚动快时顺序混乱
  //   2. threshold: 0.01 在某些浏览器/缩放比例下不稳定
  //   3. 元素滚出视口再滚回时重复触发
  function initScrollAnimations() {
    const sections = document.querySelectorAll('.section, .hero');

    sections.forEach((section) => {
      // 收集该 section 内所有需要动画的元素（按 DOM 顺序）
      const elements = Array.from(section.querySelectorAll('.fade-in-up'));
      if (elements.length === 0) return;

      let triggered = false; // 每个 section 只触发一次

      const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          // 已经在动画中 或 已经显示 → 跳过
          if (triggered || entry.target.classList.contains('visible')) return;

          // 元素进入视口 → 以该元素为起点，按 DOM 顺序触发所有未显示的元素
          if (entry.isIntersecting) {
            triggered = true;
            const startIndex = elements.indexOf(entry.target);

            // 从触发元素开始，按 DOM 顺序依次添加 visible
            elements.forEach((el, index) => {
              if (index < startIndex) return; // 已经在视口上方，直接显示（无延迟）
              if (el.classList.contains('visible')) return;

              const delay = (index - startIndex) * 100;
              setTimeout(() => {
                el.classList.add('visible');
              }, delay);
            });

            // 停止监听该 section 的所有元素
            elements.forEach(el => sectionObserver.unobserve(el));
          }
        });
      }, {
        rootMargin: '0px 0px -40px 0px',  // 底部留出 40px 缓冲，避免边缘误触发
        threshold: 0.1                      // 10% 可见才触发（比 0.01 更稳定）
      });

      elements.forEach(el => sectionObserver.observe(el));
    });
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
