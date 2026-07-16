/* ===== papers/js/app.js — 論文文獻庫前端邏輯 (ES5/ES6 相容) ===== */

var allPapers = [];
var allTopics = [];
var filteredPapers = [];
var currentTag = 'all';
var currentTopic = 'all';
var currentPage = 1;
var PER_PAGE = 20;

function loadPapers() {
  document.getElementById('paperList').innerHTML = '<p style="text-align:center;color:var(--muted);padding:40px">⏳ 正在載入論文資料庫…</p>';
  
  fetch('papers.json?_=' + Date.now())
    .then(function(res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    })
    .then(function(data) {
      allPapers = data.papers || [];
      allTopics = data.topics || [];
      document.getElementById('stat-total').textContent = allPapers.length;
      document.getElementById('stat-date').textContent = data.updated || '—';
      var si = document.getElementById('searchInput');
      if (si) si.placeholder = '🔍 即時搜尋 ' + allPapers.length + ' 篇論文 — 輸入標題、作者、關鍵字…';
      buildTopicTabs();
      applyFilters();
    })
    .catch(function(e) {
      document.getElementById('paperList').innerHTML = '<p style="text-align:center;color:#dc2626;padding:40px">❌ 論文資料載入失敗：' + e.message + '<br><small>請重整頁面再試（Ctrl+Shift+R）</small></p>';
    });
}

function buildTopicTabs() {
  var container = document.getElementById('topicTags');
  container.innerHTML = '<button class="tag active" data-topic="all">🌐 全部</button>';
  
  var preferred = [
    "綠債/ESG", "潔淨能源", "碳市場/碳交易", "氣候風險/政策", "能源市場",
    "金融市場", "地緣政治/國防", "加密貨幣/數位金融", "原物料/商品",
    "宏觀總體", "AI/科技", "方法論", "其他"
  ];
  
  var ordered = [];
  var i, t;
  for (i = 0; i < preferred.length; i++) {
    t = preferred[i];
    if (allTopics.indexOf(t) !== -1) ordered.push(t);
  }
  for (i = 0; i < allTopics.length; i++) {
    t = allTopics[i];
    if (ordered.indexOf(t) === -1) ordered.push(t);
  }
  
  var btn;
  for (i = 0; i < ordered.length; i++) {
    btn = document.createElement('button');
    btn.className = 'tag';
    btn.setAttribute('data-topic', ordered[i]);
    btn.textContent = ordered[i];
    container.appendChild(btn);
  }
  
  var btns = container.querySelectorAll('.tag');
  for (i = 0; i < btns.length; i++) {
    (function(b) {
      b.addEventListener('click', function() {
        var all = container.querySelectorAll('.tag');
        for (var j = 0; j < all.length; j++) all[j].classList.remove('active');
        b.classList.add('active');
        currentTopic = b.getAttribute('data-topic');
        currentPage = 1;
        applyFilters();
      });
    })(btns[i]);
  }
}

function applyFilters() {
  var q = document.getElementById('searchInput').value.toLowerCase().trim();
  
  filteredPapers = allPapers.filter(function(p) {
    if (currentTag !== 'all') {
      if (currentTag === 'upload') {
        if (p.type !== 'upload') return false;
      } else {
        if (!p.tags || p.tags.indexOf(currentTag) === -1) return false;
      }
    }
    
    if (currentTopic !== 'all') {
      if (!p.topics || p.topics.indexOf(currentTopic) === -1) return false;
    }
    
    if (q) {
      var text = (p.title + ' ' + p.authors + ' ' + p.journal + ' ' + (p.abstract||'') + ' ' + (p.tags||[]).join(' ') + ' ' + (p.topics||[]).join(' ')).toLowerCase();
      if (text.indexOf(q) === -1) return false;
    }
    
    return true;
  });
  
  currentPage = 1;
  render();
}

function render() {
  var total = filteredPapers.length;
  var totalPages = Math.ceil(total / PER_PAGE);
  var start = (currentPage - 1) * PER_PAGE;
  var pagePapers = filteredPapers.slice(start, start + PER_PAGE);
  
  var list = document.getElementById('paperList');
  
  var q = document.getElementById('searchInput').value.trim();
  var summaryHtml = '';
  if (q && allPapers.length > 0) {
    summaryHtml = '<div class="search-summary">🔍 「' + escapeHtml(q) + '」— 找到 <strong>' + total + '</strong> 篇</div>';
  }
  
  if (pagePapers.length === 0) {
    var msg = q 
      ? '📭 找不到包含「' + escapeHtml(q) + '」的論文，請試試其他關鍵字'
      : '📭 沒有符合條件的論文';
    list.innerHTML = '<p style="text-align:center;color:var(--muted);padding:60px 20px">' + msg + '</p>';
    document.getElementById('pagination').innerHTML = '';
    return;
  }
  
  var cardsHtml = '';
  for (var i = 0; i < pagePapers.length; i++) {
    var p = pagePapers[i];
    var tags = (p.tags||[]).slice(0, 3);
    var topics = (p.topics||[]).slice(0, 2);
    var topicsHtml = '';
    for (var ti = 0; ti < topics.length; ti++) {
      topicsHtml += '<span class="topic-badge">' + escapeHtml(topics[ti]) + '</span>';
    }
    var tagsHtml = '';
    for (var tj = 0; tj < tags.length; tj++) {
      tagsHtml += '<span>' + escapeHtml(tags[tj]) + '</span>';
    }
    if (tags.length < (p.tags||[]).length) {
      tagsHtml += '<span>+' + ((p.tags||[]).length - tags.length) + '</span>';
    }
    
    cardsHtml += '<div class="paper-card" onclick="openModal(\'' + escapeHtml(p.id).replace(/'/g, "\\'") + '\')">' +
      '<div class="paper-meta">' +
        '<span class="paper-date">' + (p.search_date || p.date || '') + '</span>' +
        (p.type === 'upload' ? '<span class="paper-badge upload">📁 上傳</span>' : '') +
        (p.arxiv_url ? '<span class="paper-badge arxiv">📄 arXiv</span>' : '') +
        (p.year ? '<span>(' + p.year + ')</span>' : '') +
        topicsHtml +
      '</div>' +
      '<h3>' + escapeHtml(p.title) + '</h3>' +
      (p.authors ? '<div class="paper-authors">' + escapeHtml(p.authors) + '</div>' : '') +
      (p.journal ? '<div class="paper-journal">' + escapeHtml(p.journal) + '</div>' : '') +
      '<div class="paper-tags">' + tagsHtml + '</div>' +
    '</div>';
  }
  
  list.innerHTML = summaryHtml + cardsHtml;
  
  if (totalPages <= 1) {
    document.getElementById('pagination').innerHTML = '';
    return;
  }
  
  var pgHtml = '';
  pgHtml += '<button ' + (currentPage <= 1 ? 'disabled' : '') + ' onclick="goPage(' + (currentPage - 1) + ')">‹</button>';
  for (var pi = 1; pi <= totalPages; pi++) {
    if (pi === 1 || pi === totalPages || Math.abs(pi - currentPage) <= 2) {
      pgHtml += '<button class="' + (pi === currentPage ? 'active' : '') + '" onclick="goPage(' + pi + ')">' + pi + '</button>';
    } else if (pi === currentPage - 3 || pi === currentPage + 3) {
      pgHtml += '<button disabled>…</button>';
    }
  }
  pgHtml += '<button ' + (currentPage >= totalPages ? 'disabled' : '') + ' onclick="goPage(' + (currentPage + 1) + ')">›</button>';
  document.getElementById('pagination').innerHTML = pgHtml;
}

function goPage(n) {
  currentPage = n;
  render();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function openModal(id) {
  var p = null;
  for (var i = 0; i < allPapers.length; i++) {
    if (allPapers[i].id === id) { p = allPapers[i]; break; }
  }
  if (!p) return;
  
  var body = document.getElementById('modalBody');
  var html = '';
  html += '<h2>' + escapeHtml(p.title) + '</h2>';
  if (p.authors) html += '<div class="meta-line"><strong>作者</strong> ' + escapeHtml(p.authors) + '</div>';
  if (p.journal) html += '<div class="meta-line"><strong>期刊</strong> ' + escapeHtml(p.journal) + '</div>';
  if (p.year) html += '<div class="meta-line"><strong>年份</strong> ' + p.year + '</div>';
  if (p.search_date) html += '<div class="meta-line"><strong>搜尋日期</strong> ' + p.search_date + '</div>';
  if (p.date) html += '<div class="meta-line"><strong>上傳日期</strong> ' + p.date + '</div>';
  if (p.citations) html += '<div class="meta-line"><strong>被引次數</strong> ' + p.citations + '</div>';
  
  html += '<div class="tags">';
  for (var ti = 0; ti < (p.tags||[]).length; ti++) html += '<span>' + escapeHtml(p.tags[ti]) + '</span>';
  for (var tj = 0; tj < (p.topics||[]).length; tj++) html += '<span class="topic-tag">' + escapeHtml(p.topics[tj]) + '</span>';
  html += '</div>';
  
  if (p.abstract) html += '<div class="section"><h4>📄 摘要</h4><p>' + escapeHtml(p.abstract) + '</p></div>';
  if (p.doi) html += '<div class="section"><h4>🔗 連結</h4><p><a href="https://doi.org/' + p.doi.replace('https://doi.org/','').replace(/^\//,'') + '" target="_blank" rel="noopener">' + escapeHtml(p.doi) + '</a></p></div>';
  if (p.openalex_url) html += '<p><a href="' + escapeHtml(p.openalex_url) + '" target="_blank" rel="noopener">📖 OpenAlex</a></p>';
  if (p.pdf) html += '<div class="section"><h4>📁 檔案</h4><p><a href="' + escapeHtml(p.pdf) + '" target="_blank">📄 下載 PDF</a></p></div>';
  if (p.arxiv_url) html += '<div class="section"><h4>🔗 arXiv</h4><p><a href="' + escapeHtml(p.arxiv_url) + '" target="_blank" rel="noopener">' + escapeHtml(p.arxiv_url) + '</a></p></div>';
  
  if (p.notes && p.notes.length > 0) {
    html += '<div class="section"><h4>📝 筆記</h4>';
    for (var ni = 0; ni < p.notes.length; ni++) html += '<p style="margin-top:4px">• ' + escapeHtml(p.notes[ni]) + '</p>';
    html += '</div>';
  }
  
  body.innerHTML = html;
  document.getElementById('paperModal').classList.add('open');
}

function closeModal() {
  document.getElementById('paperModal').classList.remove('open');
}

function escapeHtml(s) {
  if (!s) return '';
  s = String(s);
  var d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

function toggleVP(el) {
  var body = el.nextElementSibling;
  var expand = el.querySelector('.vp-expand');
  if (body) body.classList.toggle('open');
  if (expand) expand.classList.toggle('open');
}

// ===== Event Listeners =====
document.addEventListener('DOMContentLoaded', function() {
  loadPapers();
  
  var si = document.getElementById('searchInput');
  if (!si) return;
  
  // 即時篩選（打字就搜）
  si.addEventListener('input', function() {
    applyFilters();
  });
  
  // Enter 鍵支援
  si.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.keyCode === 13) {
      e.preventDefault();
      applyFilters();
      var list = document.getElementById('paperList');
      if (list) list.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
  
  // 方法標籤
  var methodBtns = document.querySelectorAll('#methodTags .tag');
  for (var i = 0; i < methodBtns.length; i++) {
    (function(btn) {
      btn.addEventListener('click', function() {
        var all = document.querySelectorAll('#methodTags .tag');
        for (var j = 0; j < all.length; j++) all[j].classList.remove('active');
        btn.classList.add('active');
        currentTag = btn.getAttribute('data-tag');
        currentPage = 1;
        applyFilters();
      });
    })(methodBtns[i]);
  }
  
  // Esc 關 modal
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' || e.keyCode === 27) closeModal();
  });
});
