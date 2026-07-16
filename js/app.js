/* ===== papers/js/app.js — 論文文獻庫前端邏輯 ===== */

let allPapers = [];
let allTopics = [];
let filteredPapers = [];
let currentTag = 'all';
let currentTopic = 'all';
let currentPage = 1;
const PER_PAGE = 20;

async function loadPapers() {
  try {
    document.getElementById('paperList').innerHTML = '<p style="text-align:center;color:var(--muted);padding:40px">⏳ 正在載入論文資料庫…</p>';
    const res = await fetch('papers.json?_=' + Date.now());
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const data = await res.json();
    allPapers = data.papers || [];
    allTopics = data.topics || [];
    document.getElementById('stat-total').textContent = allPapers.length;
    document.getElementById('stat-date').textContent = data.updated || '—';
    document.getElementById('searchInput').placeholder = '🔍 即時搜尋 ' + allPapers.length + ' 篇論文 — 輸入標題、作者、關鍵字…';
    buildTopicTabs();
    applyFilters();
  } catch (e) {
    console.error('papers.json load error:', e);
    document.getElementById('paperList').innerHTML = '<p style="text-align:center;color:#dc2626;padding:40px">❌ 論文資料載入失敗：' + e.message + '<br><small>請重整頁面再試（Ctrl+Shift+R）</small></p>';
  }
}

function buildTopicTabs() {
  const container = document.getElementById('topicTags');
  container.innerHTML = '<button class="tag active" data-topic="all">🌐 全部</button>';
  
  // Preferred order for topics
  const preferred = [
    "綠債/ESG", "潔淨能源", "碳市場/碳交易", "氣候風險/政策", "能源市場",
    "金融市場", "地緣政治/國防", "加密貨幣/數位金融", "原物料/商品",
    "宏觀總體", "AI/科技", "方法論", "其他"
  ];
  
  const ordered = [];
  for (const t of preferred) {
    if (allTopics.includes(t)) ordered.push(t);
  }
  for (const t of allTopics) {
    if (!ordered.includes(t)) ordered.push(t);
  }
  
  for (const topic of ordered) {
    const btn = document.createElement('button');
    btn.className = 'tag';
    btn.dataset.topic = topic;
    btn.textContent = topic;
    container.appendChild(btn);
  }
  
  container.querySelectorAll('.tag').forEach(btn => {
    btn.addEventListener('click', () => {
      container.querySelectorAll('.tag').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentTopic = btn.dataset.topic;
      currentPage = 1;
      applyFilters();
    });
  });
}

function applyFilters() {
  const q = document.getElementById('searchInput').value.toLowerCase().trim();
  
  filteredPapers = allPapers.filter(p => {
    // Method tag filter
    if (currentTag !== 'all') {
      if (currentTag === 'upload') {
        if (p.type !== 'upload') return false;
      } else {
        if (!p.tags || !p.tags.includes(currentTag)) return false;
      }
    }
    
    // Topic filter
    if (currentTopic !== 'all') {
      if (!p.topics || !p.topics.includes(currentTopic)) return false;
    }
    
    // Search text
    if (q) {
      const text = (p.title + ' ' + p.authors + ' ' + p.journal + ' ' + (p.abstract||'') + ' ' + (p.tags||[]).join(' ') + ' ' + (p.topics||[]).join(' ')).toLowerCase();
      if (!text.includes(q)) return false;
    }
    
    return true;
  });
  
  currentPage = 1;
  render();
}

function render() {
  const total = filteredPapers.length;
  const totalPages = Math.ceil(total / PER_PAGE);
  const start = (currentPage - 1) * PER_PAGE;
  const pagePapers = filteredPapers.slice(start, start + PER_PAGE);
  
  const list = document.getElementById('paperList');
  
  // 顯示搜尋結果摘要
  const q = document.getElementById('searchInput').value.trim();
  let summaryHtml = '';
  if (q && allPapers.length > 0) {
    summaryHtml = '<div class="search-summary">🔍 「' + escapeHtml(q) + '」— 找到 <strong>' + total + '</strong> 篇</div>';
  }
  
  if (pagePapers.length === 0) {
    const msg = q 
      ? '📭 找不到包含「' + escapeHtml(q) + '」的論文，請試試其他關鍵字'
      : '📭 沒有符合條件的論文';
    list.innerHTML = '<p style="text-align:center;color:var(--muted);padding:60px 20px">' + msg + '</p>';
    document.getElementById('pagination').innerHTML = '';
    return;
  }
  
  list.innerHTML = summaryHtml + pagePapers.map(p => {
    const tags = (p.tags||[]).slice(0, 3);
    const topics = (p.topics||[]).slice(0, 2);
    return `
    <div class="paper-card" onclick="openModal('${escapeHtml(p.id)}')">
      <div class="paper-meta">
        <span class="paper-date">${p.search_date || p.date || ''}</span>
        ${p.type === 'upload' ? '<span class="paper-badge upload">📁 上傳</span>' : ''}
        ${p.arxiv_url ? '<span class="paper-badge arxiv">📄 arXiv</span>' : ''}
        ${p.year ? `<span>(${p.year})</span>` : ''}
        ${topics.map(t => `<span class="topic-badge">${t}</span>`).join('')}
      </div>
      <h3>${escapeHtml(p.title)}</h3>
      ${p.authors ? `<div class="paper-authors">${escapeHtml(p.authors)}</div>` : ''}
      ${p.journal ? `<div class="paper-journal">${escapeHtml(p.journal)}</div>` : ''}
      <div class="paper-tags">
        ${tags.map(t => `<span>${t}</span>`).join('')}
        ${tags.length < (p.tags||[]).length ? `<span>+${(p.tags||[]).length - tags.length}</span>` : ''}
      </div>
    </div>`;
  }).join('');
  
  // Pagination
  if (totalPages <= 1) {
    document.getElementById('pagination').innerHTML = '';
    return;
  }
  
  let pgHtml = `<button ${currentPage <= 1 ? 'disabled' : ''} onclick="goPage(${currentPage - 1})">‹</button>`;
  for (let i = 1; i <= totalPages; i++) {
    if (i === 1 || i === totalPages || Math.abs(i - currentPage) <= 2) {
      pgHtml += `<button class="${i === currentPage ? 'active' : ''}" onclick="goPage(${i})">${i}</button>`;
    } else if (i === currentPage - 3 || i === currentPage + 3) {
      pgHtml += `<button disabled>…</button>`;
    }
  }
  pgHtml += `<button ${currentPage >= totalPages ? 'disabled' : ''} onclick="goPage(${currentPage + 1})">›</button>`;
  document.getElementById('pagination').innerHTML = pgHtml;
}

function goPage(n) {
  currentPage = n;
  render();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function openModal(id) {
  const p = allPapers.find(x => x.id === id);
  if (!p) return;
  
  const body = document.getElementById('modalBody');
  body.innerHTML = `
    <h2>${escapeHtml(p.title)}</h2>
    ${p.authors ? `<div class="meta-line"><strong>作者</strong> ${escapeHtml(p.authors)}</div>` : ''}
    ${p.journal ? `<div class="meta-line"><strong>期刊</strong> ${escapeHtml(p.journal)}</div>` : ''}
    ${p.year ? `<div class="meta-line"><strong>年份</strong> ${p.year}</div>` : ''}
    ${p.search_date ? `<div class="meta-line"><strong>搜尋日期</strong> ${p.search_date}</div>` : ''}
    ${p.date ? `<div class="meta-line"><strong>上傳日期</strong> ${p.date}</div>` : ''}
    ${p.citations ? `<div class="meta-line"><strong>被引次數</strong> ${p.citations}</div>` : ''}
    <div class="tags">
      ${(p.tags||[]).map(t => `<span>${t}</span>`).join('')}
      ${(p.topics||[]).map(t => `<span class="topic-tag">${t}</span>`).join('')}
    </div>
    ${p.abstract ? `
      <div class="section">
        <h4>📄 摘要</h4>
        <p>${escapeHtml(p.abstract)}</p>
      </div>
    ` : ''}
    ${p.doi ? `
      <div class="section">
        <h4>🔗 連結</h4>
        <p><a href="https://doi.org/${p.doi.replace('https://doi.org/','').replace(/^\//,'')}" target="_blank" rel="noopener">${p.doi}</a></p>
      </div>
    ` : ''}
    ${p.openalex_url ? `
      <p><a href="${p.openalex_url}" target="_blank" rel="noopener">📖 OpenAlex</a></p>
    ` : ''}
    ${p.pdf ? `
      <div class="section">
        <h4>📁 檔案</h4>
        <p><a href="${p.pdf}" target="_blank">📄 下載 PDF</a></p>
      </div>
    ` : ''}
    ${p.arxiv_url ? `
      <div class="section">
        <h4>🔗 arXiv</h4>
        <p><a href="${p.arxiv_url}" target="_blank" rel="noopener">${p.arxiv_url}</a></p>
      </div>
    ` : ''}
    ${p.notes && p.notes.length > 0 ? `
      <div class="section">
        <h4>📝 筆記</h4>
        ${p.notes.map(n => `<p style="margin-top:4px">• ${escapeHtml(n)}</p>`).join('')}
      </div>
    ` : ''}
    ${p.diagram ? `
      <div class="diagram-section">
        <h4>🕸️ 論述圖譜</h4>
        <div class="mermaid">
${p.diagram}
        </div>
        <button class="diagram-toggle" onclick="toggleDiagramCode(this)">📋 顯示原始碼</button>
      </div>
    ` : ''}
    ${p.viewpoints && p.viewpoints.length > 0 ? `
      <div class="section">
        <h4>💡 觀點與論證（${p.viewpoints.length}）</h4>
      </div>
      <div class="viewpoints-section">
        ${p.viewpoints.map((vp, i) => `
          <div class="vp-card vp-confidence-${vp.confidence||'mid'}">
            <div class="vp-card-header" onclick="toggleVP(this)">
              <span class="vp-num">${i+1}</span>
              <span class="vp-claim">${escapeHtml(vp.claim)}</span>
              <span class="vp-expand">▾</span>
            </div>
            <div class="vp-card-body">
              ${vp.evidence ? `<div class="vp-evidence-label">📊 證據</div><div class="vp-evidence">${escapeHtml(vp.evidence)}</div>` : ''}
              ${vp.source ? `<div class="vp-evidence-label">📄 來源</div><div class="vp-evidence">${escapeHtml(vp.source)}</div>` : ''}
              ${vp.connections && vp.connections.length > 0 ? `<div class="vp-connections">🔗 關聯觀點：${vp.connections.map(c => `<span>#${c}</span>`).join('')}</div>` : ''}
            </div>
          </div>
        `).join('')}
      </div>
    ` : ''}
    ${p.type === 'upload' ? `<div class="section"><p style="font-size:12px;color:var(--muted)">📁 使用者上傳文章</p></div>` : ''}
  `;
  
  document.getElementById('paperModal').classList.add('open');

  // Re-render Mermaid diagrams
  setTimeout(() => {
    if (window.mermaid) {
      try { mermaid.run({ nodes: [document.querySelector('.mermaid')].filter(Boolean) }); } catch(e) {}
    }
  }, 200);
}

function closeModal() {
  document.getElementById('paperModal').classList.remove('open');
}

function escapeHtml(s) {
  if (!s) return '';
  s = String(s);
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

// Viewpoint toggle
function toggleVP(el) {
  const body = el.nextElementSibling;
  const expand = el.querySelector('.vp-expand');
  body.classList.toggle('open');
  expand.classList.toggle('open');
}

// Diagram code toggle
function toggleDiagramCode(el) {
  const mermaid = el.previousElementSibling;
  if (mermaid.style.background) {
    mermaid.style.background = '';
    mermaid.style.padding = '';
    mermaid.style.fontFamily = '';
    mermaid.style.fontSize = '';
    mermaid.style.whiteSpace = '';
    mermaid.style.borderRadius = '';
    mermaid.textContent = mermaid.getAttribute('data-orig') || mermaid.textContent;
    el.textContent = '📋 顯示原始碼';
    // Re-render mermaid
    if (window.mermaid) mermaid.run();
  } else {
    const code = mermaid.textContent.trim();
    mermaid.setAttribute('data-orig', code);
    mermaid.style.background = '#1e293b';
    mermaid.style.padding = '12px 16px';
    mermaid.style.fontFamily = 'monospace';
    mermaid.style.fontSize = '12px';
    mermaid.style.whiteSpace = 'pre-wrap';
    mermaid.style.borderRadius = '6px';
    mermaid.textContent = code;
    el.textContent = '🔄 顯示圖譜';
  }
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
  loadPapers();
  
  const si = document.getElementById('searchInput');
  si.addEventListener('input', applyFilters);
  // Enter 鍵支援：捲動到結果區
  si.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      applyFilters();
      document.getElementById('paperList').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
  // Slash 快捷鍵聚焦搜尋框
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== si && document.activeElement?.tagName !== 'INPUT') {
      e.preventDefault();
      si.focus();
    }
  });
  
  document.querySelectorAll('.filter-tags .tag').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-tags .tag').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentTag = btn.dataset.tag;
      currentPage = 1;
      applyFilters();
    });
  });
  
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeModal();
  });
});
