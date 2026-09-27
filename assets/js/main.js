(function () {
  'use strict';
  var root = document.documentElement;

  /* ---------- Theme toggle ---------- */
  var themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var current = root.dataset.theme ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      var next = current === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  /* ---------- Mobile menu ---------- */
  var menuBtn = document.getElementById('menu-toggle');
  var nav = document.getElementById('site-nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open);
    });
  }

  /* ---------- Filters (projects, publications, notes) ---------- */
  document.querySelectorAll('[data-filter]').forEach(function (box) {
    var buttons = box.querySelectorAll('[data-filter-value]');
    var items = box.querySelectorAll('[data-filter-item]');
    var search = box.querySelector('[data-filter-search]');
    var empty = box.querySelector('[data-filter-empty]');
    var state = { cat: '', q: '' };

    function apply() {
      var shown = 0;
      items.forEach(function (el) {
        var okCat = !state.cat || (el.dataset.cats || '').indexOf('|' + state.cat + '|') !== -1;
        var text = el.dataset.text || el.textContent.toLowerCase();
        var okQ = !state.q || text.indexOf(state.q) !== -1;
        el.hidden = !(okCat && okQ);
        if (!el.hidden) shown++;
      });
      box.querySelectorAll('[data-filter-section]').forEach(function (sec) {
        sec.hidden = !sec.querySelector('[data-filter-item]:not([hidden])');
      });
      if (empty) empty.hidden = shown !== 0;
    }

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        state.cat = btn.dataset.filterValue;
        buttons.forEach(function (b) { b.classList.toggle('active', b === btn); });
        apply();
      });
    });
    if (search) {
      search.addEventListener('input', function () {
        state.q = search.value.trim().toLowerCase();
        apply();
      });
    }
  });

  /* ---------- Tabs (CV page) ---------- */
  document.querySelectorAll('[data-tabs]').forEach(function (box) {
    var links = box.querySelectorAll('[data-tab-link]');
    var panes = box.querySelectorAll('[data-tab]');
    box.classList.add('tabs-ready');

    function show(id, push) {
      var found = false;
      panes.forEach(function (p) { if (p.dataset.tab === id) found = true; });
      if (!found) return;
      links.forEach(function (l) { l.classList.toggle('active', l.dataset.tabLink === id); });
      panes.forEach(function (p) { p.classList.toggle('active', p.dataset.tab === id); });
      if (push) history.replaceState(null, '', '#' + id);
    }
    links.forEach(function (l) {
      l.addEventListener('click', function (e) {
        e.preventDefault();
        show(l.dataset.tabLink, true);
      });
    });
    if (location.hash) show(location.hash.slice(1), false);
  });

  /* ---------- Workshop cards (project pages) ----------
     Builds one card per <section class="workshop-panel"> (cover, label, title,
     module count). Clicking a card opens its panel below; without JS every
     panel simply stays visible. */
  document.querySelectorAll('[data-workshop-cards]').forEach(function (grid) {
    var panels = grid.parentNode.querySelectorAll('.workshop-panel[id]');
    if (!panels.length) return;
    var cards = [];

    function open(id, scroll) {
      panels.forEach(function (p) { p.hidden = p.id !== id; });
      cards.forEach(function (c) {
        var on = c.dataset.target === id;
        c.classList.toggle('active', on);
        c.setAttribute('aria-expanded', on);
      });
      if (id) history.replaceState(null, '', '#' + id);
      else history.replaceState(null, '', location.pathname + location.search);
      var target = id && document.getElementById(id);
      if (target && scroll) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    panels.forEach(function (panel) {
      var h = panel.querySelector('h3');
      var cover = panel.querySelector('.workshop-cover');
      var label = panel.querySelector('.workshop-no');
      var modules = panel.querySelectorAll('.module-list > li:not(.module-goal)').length;
      var videos = panel.querySelector('.workshop-info a[href*="youtube.com"]');

      var card = document.createElement('button');
      card.type = 'button';
      card.className = 'workshop-card';
      card.dataset.target = panel.id;
      card.setAttribute('aria-controls', panel.id);
      card.setAttribute('aria-expanded', 'false');
      if (cover) card.appendChild(cover.cloneNode(true));
      var body = document.createElement('span');
      body.className = 'workshop-card-body';
      if (label) body.insertAdjacentHTML('beforeend', '<span class="workshop-no">' + label.innerHTML + '</span>');
      var title = h ? h.textContent.replace(/^\s*Workshop\s*\d+\s*[—–:-]\s*/i, '') : panel.id;
      body.insertAdjacentHTML('beforeend', '<strong class="workshop-card-title"></strong>');
      body.lastChild.textContent = title;
      var meta = [];
      if (modules) meta.push(modules + ' modules');
      if (videos) meta.push('Lecture videos');
      body.insertAdjacentHTML('beforeend', '<span class="workshop-card-meta">' + meta.join(' · ') +
        '<span class="workshop-card-toggle" aria-hidden="true"></span></span>');
      card.appendChild(body);
      card.addEventListener('click', function () {
        open(card.classList.contains('active') ? '' : panel.id, true);
      });
      grid.appendChild(card);
      cards.push(card);
    });

    grid.parentNode.classList.add('workshops-ready');
    var initial = decodeURIComponent(location.hash.slice(1));
    var exists = Array.prototype.some.call(panels, function (p) { return p.id === initial; });
    open(exists ? initial : '', exists);
  });

  /* ---------- Site search ---------- */
  var modal = document.getElementById('search-modal');
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  var openBtn = document.getElementById('search-open');
  var index = null;

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function loadIndex() {
    if (index) return Promise.resolve(index);
    return fetch(window.SEARCH_URL).then(function (r) { return r.json(); }).then(function (d) {
      index = [].concat(d.notes || [], d.projects || [], d.publications || []);
      return index;
    });
  }

  function render(q) {
    q = q.trim().toLowerCase();
    if (!q) { results.innerHTML = '<li class="search-hint">Type to search notes, projects and publications.</li>'; return; }
    loadIndex().then(function (all) {
      var hits = all.filter(function (it) {
        return (it.title + ' ' + it.meta + ' ' + it.text).toLowerCase().indexOf(q) !== -1;
      }).slice(0, 12);
      if (!hits.length) { results.innerHTML = '<li class="search-hint">No results for “' + escapeHtml(q) + '”.</li>'; return; }
      results.innerHTML = hits.map(function (it) {
        return '<li><a href="' + escapeHtml(it.url) + '"><span class="sr-title">' + escapeHtml(it.title) +
          '</span><span class="sr-meta">' + escapeHtml(it.meta) + '</span></a></li>';
      }).join('');
    }).catch(function () {
      results.innerHTML = '<li class="search-hint">Search is unavailable right now.</li>';
    });
  }

  function openSearch() {
    if (!modal) return;
    modal.hidden = false;
    document.body.style.overflow = 'hidden';
    input.value = '';
    render('');
    setTimeout(function () { input.focus(); }, 10);
  }
  function closeSearch() {
    if (!modal) return;
    modal.hidden = true;
    document.body.style.overflow = '';
  }

  if (modal) {
    openBtn.addEventListener('click', openSearch);
    modal.querySelectorAll('[data-search-close]').forEach(function (el) { el.addEventListener('click', closeSearch); });
    input.addEventListener('input', function () { render(input.value); });
    document.addEventListener('keydown', function (e) {
      var typing = /input|textarea|select/i.test((e.target && e.target.tagName) || '');
      if (e.key === '/' && !typing && modal.hidden) { e.preventDefault(); openSearch(); }
      else if (e.key === 'Escape' && !modal.hidden) closeSearch();
    });
  }
})();
