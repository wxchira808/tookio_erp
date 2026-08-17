/**
 * TOOKIO SOLUTIONS — Enterprise Website Interactive Engine
 * Handles Mega Menus, Mobile Drawer, Tabs, Accordions, Sticky Navigation
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileDrawer();
  initTabs();
  initAccordions();
  initMegaMenus();
});

// Sticky Header with Dynamic Shadow
function initStickyHeader() {
  const headerWrapper = document.querySelector('.tookio-header-wrapper');
  if (!headerWrapper) return;

  const handleScroll = () => {
    if (window.scrollY > 20) {
      headerWrapper.style.boxShadow = '0 10px 30px -10px rgba(10, 22, 40, 0.15)';
    } else {
      headerWrapper.style.boxShadow = 'var(--t-shadow-sm)';
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
}

// Mobile Slide-Out Drawer
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');
  const overlay = document.querySelector('.mobile-drawer-overlay');
  const closeBtn = document.querySelector('.mobile-drawer-close');

  if (!toggleBtn || !drawer) return;

  const openDrawer = () => {
    drawer.classList.add('open');
    if (overlay) overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  const closeDrawer = () => {
    drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
  };

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  if (overlay) overlay.addEventListener('click', closeDrawer);

  drawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

// Interactive Tab Switcher
function initTabs() {
  // Support .tookio-tab-btn
  const tookioTabButtons = document.querySelectorAll('.tookio-tab-btn');
  if (tookioTabButtons.length) {
    tookioTabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab');
        const section = btn.closest('section') || document;
        
        section.querySelectorAll('.tookio-tab-btn').forEach(b => b.classList.remove('active'));
        section.querySelectorAll('.tookio-tab-pane').forEach(p => p.classList.remove('active'));
        
        btn.classList.add('active');
        const targetPane = document.getElementById(targetId);
        if (targetPane) targetPane.classList.add('active');
      });
    });
  }

  // Also support data-tab-container
  const tabContainers = document.querySelectorAll('[data-tab-container]');
  tabContainers.forEach(container => {
    const tabButtons = container.querySelectorAll('.tab-btn');
    const tabPanes = container.querySelectorAll('.tab-pane');

    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab-target');

        tabButtons.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        const activePane = container.querySelector(`#${targetId}`);
        if (activePane) {
          activePane.classList.add('active');
        }
      });
    });
  });
}

// Accordion Toggles
function initAccordions() {
  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.closest('.accordion-item');
      if (!item) return;

      const isOpen = item.classList.contains('open');

      const parentGroup = item.closest('.accordion-group');
      if (parentGroup && !parentGroup.hasAttribute('data-allow-multiple')) {
        parentGroup.querySelectorAll('.accordion-item').forEach(other => {
          if (other !== item) other.classList.remove('open');
        });
      }

      if (isOpen) {
        item.classList.remove('open');
      } else {
        item.classList.add('open');
      }
    });
  });
}

// Mega Menu Hover & Touch Support
function initMegaMenus() {
  const navItemsWithDropdown = document.querySelectorAll('.nav-item.has-dropdown');

  navItemsWithDropdown.forEach(item => {
    let timeout;

    item.addEventListener('mouseenter', () => {
      clearTimeout(timeout);
      navItemsWithDropdown.forEach(other => {
        if (other !== item) other.classList.remove('active');
      });
      item.classList.add('active');
    });

    item.addEventListener('mouseleave', () => {
      timeout = setTimeout(() => {
        item.classList.remove('active');
      }, 150);
    });
  });

  // Automatically close any open mega menus when user scrolls the page
  window.addEventListener('scroll', () => {
    navItemsWithDropdown.forEach(item => {
      item.classList.remove('active');
    });
  }, { passive: true });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.tookio-header-wrapper')) {
      navItemsWithDropdown.forEach(item => {
        item.classList.remove('active');
      });
    }
  });
}
