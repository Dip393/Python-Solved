/* ── Animated counters ── */
function animateCounters() {
  document.querySelectorAll('.counter-num').forEach(el => {
    const target = +el.dataset.target;
    const duration = 1800;
    const step = target / (duration / 16);
    let current = 0;
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = Math.floor(current);
      if (current >= target) clearInterval(timer);
    }, 16);
  });
}

/* ── Skill bars ── */
function animateSkillBars() {
  document.querySelectorAll('.skill-bar__fill').forEach(bar => {
    const level = bar.dataset.level;
    // Trigger after a short delay to let the CSS animation play
    setTimeout(() => { bar.style.width = level + '%'; }, 300);
  });
}

/* ── Intersection observer for scroll animations ── */
function initScrollObserver() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Animate skill bars when section enters view
        if (entry.target.classList.contains('skills-section') ||
            entry.target.closest('.section')) {
          animateSkillBars();
        }
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.skill-card').forEach(el => observer.observe(el));
}

/* ── Mobile hamburger ── */
function toggleMenu() {
  document.querySelector('.nav__links').classList.toggle('open');
}

/* ── Contact form ── */
function handleSubmit(e) {
  e.preventDefault();
  const feedback = document.getElementById('form-feedback');
  feedback.textContent = '✅ Message sent! (Demo — no backend connected yet)';
  e.target.reset();
}

/* ── Init ── */
document.addEventListener('DOMContentLoaded', () => {
  animateCounters();
  initScrollObserver();
  // Animate skill bars visible on load
  animateSkillBars();
});
