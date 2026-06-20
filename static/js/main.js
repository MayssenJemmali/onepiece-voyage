/* ═══════════════════════════════════════════════════════════════
   GRAND VOYAGE — Main JavaScript
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── Stars Generator ───────────────────────────────────────────── */
  function generateStars() {
    const container = document.querySelector('.stars');
    if (!container) return;

    const count = 120;
    for (let i = 0; i < count; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      const size = Math.random() * 2.5 + 0.5;
      star.style.cssText = `
        left: ${Math.random() * 100}%;
        top: ${Math.random() * 60}%;
        width: ${size}px;
        height: ${size}px;
        --dur: ${Math.random() * 4 + 2}s;
        --delay: ${Math.random() * 4}s;
        opacity: ${Math.random() * 0.5 + 0.1};
      `;
      container.appendChild(star);
    }
  }

  /* ── Scroll Reveal ─────────────────────────────────────────────── */
  function initReveal() {
    const elements = document.querySelectorAll('.reveal');
    if (!elements.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    elements.forEach((el) => observer.observe(el));
  }

  /* ── Nav Scroll Effect ─────────────────────────────────────────── */
  function initNav() {
    const nav = document.querySelector('.nav');
    if (!nav) return;

    window.addEventListener('scroll', () => {
      nav.style.boxShadow = window.scrollY > 50
        ? '0 4px 20px rgba(0,0,0,0.5)'
        : 'none';
    }, { passive: true });
  }

  /* ── Island Map Hover ──────────────────────────────────────────── */
  function initMap() {
    const islands = document.querySelectorAll('.island-node');
    islands.forEach((island) => {
      // Click to "visit" unvisited islands
      island.addEventListener('click', () => {
        if (island.classList.contains('unvisited')) {
          island.classList.remove('unvisited');
          island.classList.add('just-visited');

          const pin = island.querySelector('.island-pin');
          const originalBg = pin.style.background;

          // Pulse animation
          pin.style.transition = 'background 0.3s, transform 0.3s';
          pin.style.transform = 'rotate(-45deg) scale(1.3)';
          setTimeout(() => {
            pin.style.transform = 'rotate(-45deg) scale(1)';
          }, 300);
        }
      });
    });
  }

  /* ── Wanted Poster Tilt on Mouse ──────────────────────────────── */
  function initPosters() {
    const posters = document.querySelectorAll('.wanted-poster');
    posters.forEach((poster) => {
      poster.addEventListener('mousemove', (e) => {
        const rect = poster.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        poster.style.transform = `
          perspective(800px)
          rotateY(${x * 8}deg)
          rotateX(${-y * 6}deg)
          translateY(-8px) scale(1.02)
        `;
      });

      poster.addEventListener('mouseleave', () => {
        const baseTilt = poster.style.getPropertyValue('--tilt') || '-1deg';
        poster.style.transform = `rotate(${baseTilt})`;
        setTimeout(() => {
          poster.style.transform = '';
        }, 300);
      });
    });
  }

  /* ── Crew Card Sparkle on Hover ──────────────────────────────── */
  function initCrewCards() {
    const cards = document.querySelectorAll('.crew-card');
    cards.forEach((card) => {
      card.addEventListener('mouseenter', () => {
        card.style.zIndex = '10';
      });
      card.addEventListener('mouseleave', () => {
        card.style.zIndex = '';
      });
    });
  }

  /* ── Foam Dots Generator ─────────────────────────────────────── */
  function generateFoam() {
    const lines = document.querySelectorAll('.foam-line');
    lines.forEach((line) => {
      for (let i = 0; i < 60; i++) {
        const dot = document.createElement('div');
        dot.className = 'foam-dot';
        dot.style.opacity = Math.random() * 0.6 + 0.1;
        dot.style.width = `${Math.random() * 8 + 3}px`;
        line.appendChild(dot);
      }
    });
  }

  /* ── Adventure Log Entry Interaction ─────────────────────────── */
  function initLog() {
    const entries = document.querySelectorAll('.log-entry');
    entries.forEach((entry) => {
      entry.addEventListener('mouseenter', () => {
        const dot = entry.querySelector('.dot-circle');
        if (dot) dot.style.transform = 'scale(1.15)';
      });
      entry.addEventListener('mouseleave', () => {
        const dot = entry.querySelector('.dot-circle');
        if (dot) dot.style.transform = '';
      });
    });
  }

  /* ── Parallax on Hero ─────────────────────────────────────────── */
  function initParallax() {
    const ship = document.querySelector('.hero-ship');
    const moon = document.querySelector('.hero-moon');
    if (!ship || !moon) return;

    window.addEventListener('scroll', () => {
      const scrolled = window.scrollY;
      if (scrolled < window.innerHeight) {
        const shipY = scrolled * 0.3;
        const moonY = scrolled * 0.1;
        ship.style.transform = `translateX(-50%) translateY(${shipY}px) rotate(-1deg)`;
        moon.style.transform = `translateY(${moonY}px)`;
      }
    }, { passive: true });
  }

  /* ── Smooth Anchor Scroll ─────────────────────────────────────── */
  function initAnchors() {
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener('click', (e) => {
        const target = document.querySelector(anchor.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  /* ── Map Route Drawing ────────────────────────────────────────── */
  function initMapRoutes() {
    const svg = document.querySelector('.route-path-svg');
    if (!svg) return;

    // Animate the route drawing
    const paths = svg.querySelectorAll('.route-path');
    paths.forEach((path, i) => {
      const length = path.getTotalLength ? path.getTotalLength() : 200;
      path.style.strokeDasharray = `${length}`;
      path.style.strokeDashoffset = `${length}`;
      path.style.transition = `stroke-dashoffset 2s ease ${i * 0.5 + 0.5}s`;

      // Trigger when map section is visible
      const mapSection = document.querySelector('.map-section');
      if (!mapSection) return;

      const observer = new IntersectionObserver(
        (entries) => {
          if (entries[0].isIntersecting) {
            paths.forEach((p, j) => {
              const len = p.getTotalLength ? p.getTotalLength() : 200;
              p.style.strokeDasharray = `${len}`;
              p.style.strokeDashoffset = '0';
            });
            observer.disconnect();
          }
        },
        { threshold: 0.3 }
      );
      observer.observe(mapSection);
    });
  }

  /* ── Easter Egg ─────────────────────────────────────────────── */
  let konamiBuffer = [];
  const konamiCode = ['ArrowUp','ArrowUp','ArrowDown','ArrowDown','ArrowLeft','ArrowRight','ArrowLeft','ArrowRight','b','a'];

  document.addEventListener('keydown', (e) => {
    konamiBuffer.push(e.key);
    if (konamiBuffer.length > konamiCode.length) {
      konamiBuffer.shift();
    }
    if (JSON.stringify(konamiBuffer) === JSON.stringify(konamiCode)) {
      showEasterEgg();
      konamiBuffer = [];
    }
  });

  function showEasterEgg() {
    const egg = document.createElement('div');
    egg.style.cssText = `
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: rgba(13,33,55,0.97);
      border: 3px solid #f4c430;
      border-radius: 8px;
      padding: 2.5rem 3rem;
      z-index: 9999;
      text-align: center;
      font-family: 'Pirata One', cursive;
      color: #f4c430;
      font-size: 1.8rem;
      box-shadow: 0 0 60px rgba(244,196,48,0.4);
      cursor: pointer;
      max-width: 90vw;
    `;
    egg.innerHTML = `
      🏴‍☠️<br>
      <span style="display:block;margin:0.5rem 0">"I'm gonna be King of the Pirates!"</span>
      <span style="font-size:0.9rem;color:#7ec8e3;font-family:'Crimson Text',serif;font-style:italic">
        — Monkey D. Luffy, probably right now
      </span>
      <span style="display:block;margin-top:1rem;font-size:0.7rem;letter-spacing:3px;color:#c9a84c;font-family:'Cinzel',serif">CLICK TO DISMISS</span>
    `;
    egg.addEventListener('click', () => document.body.removeChild(egg));
    document.body.appendChild(egg);
  }

  /* ── Init All ────────────────────────────────────────────────── */
  function init() {
    generateStars();
    generateFoam();
    initReveal();
    initNav();
    initMap();
    initPosters();
    initCrewCards();
    initLog();
    initParallax();
    initAnchors();
    // initMapRoutes(); // called after DOM ready with slight delay
    setTimeout(initMapRoutes, 100);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
