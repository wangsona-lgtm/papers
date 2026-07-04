#!/usr/bin/env python3
"""
build_viewpoints.py — 從 papers.json 的 notes 自動產出觀點與論述圖譜

從現有結構化 notes 中解析：
  ◆ 【Step/結果】→ 定量發現 → viewpoints
  ◆ 【政策意涵】→ 政策建議 → viewpoints
  ◆ 【貢獻】→ 研究貢獻 → viewpoints
  ◆ 變數間關係 → Mermaid 論述圖譜

Usage:
  python3 build_viewpoints.py                     # 重新生成全部
  python3 build_viewpoints.py --dry-run            # 預覽不寫入
  python3 build_viewpoints.py --only-missing       # 只補還沒有 viewports 的
"""

import json, re, sys, os, copy

PAPERS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "papers.json")

def load():
    with open(PAPERS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def save(data):
    data["updated"] = __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["total"] = len(data["papers"])
    with open(PAPERS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ saved {len(data['papers'])} papers to {PAPERS_JSON}")

def extract_viewpoints(notes):
    """從 notes 中萃取觀點，回傳 viewpoints list"""
    vps = []
    if not notes:
        return vps
    
    text = "\n".join(notes)
    
    # ── 1. 定量結果（Step / 發現）──
    # 匹配 【Step 1】CO₂→EG: +2.1680(p<0.001)
    step_pattern = re.compile(r'【[^】]*[Ss]tep\s*\d+[^】]*】\s*([^:：]+)[:：]\s*([^【\n]+)')
    for m in step_pattern.finditer(text):
        rel = m.group(1).strip()
        result = m.group(2).strip()
        # 只保留包含顯著性的結果
        if 'p<' in result or '顯著' in result or 'signif' in result.lower():
            vps.append({
                "claim": f"{rel}：{result.split(',')[0]}",
                "evidence": result,
                "confidence": "high",
                "source": "定量分析",
                "connections": []
            })
        elif any(c in result for c in ['+', '-', '→', '不顯著', 'ns']):
            vps.append({
                "claim": f"{rel}：{result}",
                "evidence": result,
                "confidence": "mid",
                "source": "定量分析",
                "connections": []
            })
    
    # ── 2. 【核心】發現
    core_pattern = re.compile(r'【[^】]*核心[^】]*】\s*([^【\n]+)')
    for m in core_pattern.finditer(text):
        content = m.group(1).strip()
        if len(content) > 10:
            vps.append({
                "claim": content[:120] + ("…" if len(content) > 120 else ""),
                "evidence": content,
                "confidence": "high",
                "source": "核心發現",
                "connections": []
            })
    
    # ── 3. 【H1/H2/H3】假設檢定結果
    hyp_pattern = re.compile(r'【([Hh]\d)[^】]*】\s*([^【\n]+)')
    for m in hyp_pattern.finditer(text):
        label = m.group(1).upper()
        content = m.group(2).strip()
        conf = "high" if '✅' in content or '成立' in content or '顯著' in content else "mid"
        if len(content) > 10:
            vps.append({
                "claim": f"{label}：{content[:120]}",
                "evidence": content,
                "confidence": conf,
                "source": "假設檢定",
                "connections": []
            })
    
    # ── 4. 【貢獻】
    contrib_pattern = re.compile(r'【[^】]*貢獻[^】]*】\s*(\d+[)）]?\s*[^【\n]+(?:\n\d+[)）]?\s*[^【\n]+)*)')
    for m in contrib_pattern.finditer(text):
        content = m.group(1).strip()
        items = re.split(r'\n(?=\d+[)）])', content)
        for item in items:
            item = item.strip()
            if item and len(item) > 10:
                # Remove leading number
                clean = re.sub(r'^\d+[)）]?\s*', '', item)
                vps.append({
                    "claim": clean[:120] + ("…" if len(clean) > 120 else ""),
                    "evidence": clean,
                    "confidence": "high",
                    "source": "研究貢獻",
                    "connections": []
                })
    
    # ── 5. 【政策意涵】
    policy_pattern = re.compile(r'【[^】]*政策[^】]*】\s*(\d+[)）]?\s*[^【\n]+(?:\n\d+[)）]?\s*[^【\n]+)*)')
    for m in policy_pattern.finditer(text):
        content = m.group(1).strip()
        items = re.split(r'\n(?=\d+[)）])', content)
        for item in items:
            item = item.strip()
            if item and len(item) > 10:
                clean = re.sub(r'^\d+[)）]?\s*', '', item)
                vps.append({
                    "claim": f"政策建議：{clean[:120]}",
                    "evidence": clean,
                    "confidence": "mid",
                    "source": "政策意涵",
                    "connections": []
                })
    
    # ── 6. 【限制】→ limitation viewpoint
    limit_pattern = re.compile(r'【[^】]*限制[^】]*】\s*([^【\n]+)')
    for m in limit_pattern.finditer(text):
        content = m.group(1).strip()
        if content and len(content) > 10:
            vps.append({
                "claim": f"研究限制：{content[:120]}",
                "evidence": content,
                "confidence": "low",
                "source": "研究限制",
                "connections": []
            })
    
    # ── 7. 一般發現（含 Step 但沒被上面抓到）
    other_findings = re.findall(r'【[^】]*發現[^】]*】\s*([^【\n]+)', text)
    for item in other_findings:
        item = item.strip()
        if item and len(item) > 20:
            vps.append({
                "claim": item[:120] + ("…" if len(item) > 120 else ""),
                "evidence": item,
                "confidence": "mid",
                "source": "發現",
                "connections": []
            })
    
    # 去重（基於 claim 前 80 字）
    seen = set()
    unique_vps = []
    for vp in vps:
        key = vp["claim"][:80]
        if key not in seen:
            seen.add(key)
            unique_vps.append(vp)
    
    # 限制最多 12 個 viewpoint
    return unique_vps[:12]


def extract_viewpoints(notes):
    """從 notes 中萃取觀點，回傳 viewpoints list（含結構化與非結構化筆記）"""
    vps = []
    if not notes:
        return vps
    
    text = "\n".join(notes)
    
    # ───── 一般用途：從任意文字擷取箭頭關係 ─────
    # 匹配 X→Y 或 X→Y↑↓ 或 X→Y(+/-) 模式
    arrow_items = re.findall(r'([A-Za-z0-9_/\s&\u0391-\u03c9]{1,20}?)\s*[→➔]\s*([A-Za-z0-9_/\s&↑↓→➔+\-\u0391-\u03c9]{1,30})', text)
    for src, tgt in arrow_items[:6]:
        src = src.strip()
        tgt = tgt.strip()
        if src and tgt and len(src) > 1 and len(tgt) > 1:
            # 判斷正負向
            direction = ""
            if '↑' in tgt or '+**' in tgt:
                direction = "（正向）"
            elif '↓' in tgt or '-**' in tgt or '負' in tgt:
                direction = "（負向）"
            vps.append({
                "claim": f"{src} → {tgt}{direction}",
                "evidence": f"{src}對{tgt}的影響",
                "confidence": "mid",
                "source": "變數關係",
                "connections": []
            })
    
    # ───── 一般用途：中文關係句 ─────
    # 匹配「X 降低/提高/促進/抑制/改善 Y」模式
    cn_rel_pattern = re.compile(r'([^，。、\n]{2,20}?)(降低|提高|促進|抑制|改善|增加|減少|驅動|調節|顯著升高|顯著降低|正向影響|負向影響)([^，。、\n]{0,30})')
    for m in cn_rel_pattern.finditer(text):
        src = m.group(1).strip()
        verb = m.group(2)
        tgt = m.group(3).strip()
        if src and len(src) > 1:
            if tgt and len(tgt) > 1:
                vps.append({
                    "claim": f"{src}{verb}{tgt}",
                    "evidence": f"{src}對{tgt}的影響：{verb}",
                    "confidence": "mid",
                    "source": "變數關係",
                    "connections": []
                })
            else:
                # 句子以動詞結尾，如「COVID期間溢散顯著升高」
                vps.append({
                    "claim": f"{src} {verb}",
                    "evidence": f"{src}{verb}",
                    "confidence": "mid",
                    "source": "發現",
                    "connections": []
                })
    
    # ───── 一般用途：關鍵結論句 ─────
    for line in notes:
        line = line.strip()
        if not line or line.startswith('---') or line.startswith('arXiv'):
            continue
        if len(line) < 15:
            continue
        # 跳過 metadata / 方法 / 資料行
        if any(line.startswith(p) for p in ['樣本', '資料庫', '方法', 'DOI', 'http', 'Tags', '---', '方法：', '資料庫：']):
            continue
        # 跳過變數清單
        if line.startswith('【變數】') or line.startswith('DV=') or line.startswith('IV='):
            continue
        
        # 已經有箭頭關係的用上面處理
        if '→' in line or '➔' in line:
            continue
        
        # 包含關鍵字的行
        if any(kw in line for kw in ['發現', '結果', '貢獻', '核心', '政策', '限制', '建議']):
            vps.append({
                "claim": line[:120] + ("…" if len(line) > 120 else ""),
                "evidence": line,
                "confidence": "mid",
                "source": "陳述",
                "connections": []
            })
        elif any(kw in line for kw in ['成立', '不成立', '中介', '調節', '異質']):
            vps.append({
                "claim": line[:120] + ("…" if len(line) > 120 else ""),
                "evidence": line,
                "confidence": "mid",
                "source": "檢定結果",
                "connections": []
            })
        # 數字結果行（如 TCI=26.54%, +20.66）
        elif re.search(r'[=][\d.]+%?', line) and len(line) > 10:
            vps.append({
                "claim": line[:120] + ("…" if len(line) > 120 else ""),
                "evidence": line,
                "confidence": "mid",
                "source": "數據",
                "connections": []
            })
    
    # ───── Pass 2: 結構化【】筆記 ─────
    
    # 1. 定量結果（Step / H1-H3）
    for pattern in [
        r'【[^】]*[Ss]tep\s*\d+[^】]*】\s*([^:：]+)[:：]\s*([^【\n]+)',
        r'【([Hh]\d)[^】]*】\s*([^【\n]+)',
    ]:
        for m in re.finditer(pattern, text):
            groups = m.groups()
            rel = groups[0].strip()
            result = groups[1].strip() if len(groups) > 1 else ""
            if not result:
                continue
            # 判斷信心
            conf = "mid"
            if 'p<' in result or '顯著' in result or '✅' in result or '成立' in result:
                conf = "high"
            elif '不顯著' in result or 'ns' in result.lower() or '❌' in result:
                conf = "low"
            vps.append({
                "claim": f"{rel}：{result[:100]}",
                "evidence": result,
                "confidence": conf,
                "source": "假設檢定",
                "connections": []
            })
    
    # 2. 【核心】/【貢獻】/【政策意涵】/【限制】
    for section_key, source_label, default_conf in [
        (r'核心', '核心發現', 'high'),
        (r'貢獻', '研究貢獻', 'high'),
        (r'政策', '政策意涵', 'mid'),
        (r'限制', '研究限制', 'low'),
        (r'發現', '發現', 'mid'),
    ]:
        pattern = re.compile(rf'【[^】]*{section_key}[^】]*】\s*([^【\n]+(?:\n(?!【|---)[^【\n]+)*)')
        for m in pattern.finditer(text):
            content = m.group(1).strip()
            if len(content) < 10:
                continue
            # 拆多行
            items = re.split(r'\n(?=\d+[)）])', content)
            for item in items:
                item = item.strip()
                if not item or len(item) < 10:
                    continue
                clean = re.sub(r'^\d+[)）]?\s*', '', item)
                prefix = "政策建議：" if '政策' in section_key else "研究限制：" if '限制' in section_key else ""
                vps.append({
                    "claim": f"{prefix}{clean[:120]}" + ("…" if len(clean) > 120 else ""),
                    "evidence": clean,
                    "confidence": default_conf,
                    "source": source_label,
                    "connections": []
                })
    
    # ───── Pass 3: 從【摘要】中萃取觀點（針對自動生成簡短 notes）──
    abs_lines = [l for l in notes if l.startswith('【摘要】') or l.startswith('【Abstract】')]
    for abs_line in abs_lines:
        text_abs = abs_line.replace('【摘要】', '').replace('【Abstract】', '').strip()
        if not text_abs or len(text_abs) < 15:
            continue
        
        # 1. 英文關係模式: X affects/influences/leads to Y, X and Y
        en_matches = re.findall(r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*?)\s+(affects|influences|leads? to|impacts?|drives|increases|decreases|reduces|enhances|boosts|lowers|examines?|analyz?es?|investigates?|assesses?)\s+([^\.,;]+)', text_abs)
        for src, verb, tgt in en_matches:
            src = src.strip()
            tgt = tgt.strip()
            if src and tgt and len(src) > 2 and len(tgt) > 2:
                vps.append({
                    "claim": f"{src} {verb} {tgt}",
                    "evidence": text_abs,
                    "confidence": "mid",
                    "source": "摘要",
                    "connections": []
                })
        
        # 2. 中文「發現」「使用」「分析」模式
        cn_findings = re.findall(r'發現([^。；]+)', text_abs)
        for finding in cn_findings:
            finding = finding.strip()
            if len(finding) > 8:
                vps.append({
                    "claim": f"發現：{finding[:120]}",
                    "evidence": text_abs,
                    "confidence": "mid",
                    "source": "摘要",
                    "connections": []
                })
        
        # 3. 使用 ... 分析/評估... 模式
        cn_method = re.findall(r'(使用|採用|透過|利用)([^，。]+?)(分析|評估|探討|研究|檢驗)([^，。]+)', text_abs)
        for _, method, action, target in cn_method:
            method = method.strip()
            target = target.strip()
            if method and target:
                vps.append({
                    "claim": f"研究方法：{method} 用於分析 {target}",
                    "evidence": text_abs,
                    "confidence": "mid",
                    "source": "方法",
                    "connections": []
                })
    
    # ───── Pass 4: 保底觀點（從 metadata / abstract 組合）──
    if len(vps) < 2:
        # 從 notes 提取「方法」「主題」「變數」行
        method_line = ""
        topic_line = ""
        var_line = ""
        abs_line = ""
        for note in notes:
            if note.startswith('方法：'):
                method_line = note.replace('方法：', '')
            elif note.startswith('主題：'):
                topic_line = note.replace('主題：', '')
            elif note.startswith('變數：'):
                var_line = note.replace('變數：', '')
            elif note.startswith('【摘要】'):
                abs_line = note.replace('【摘要】', '').strip()
        
        # 方法觀點
        if method_line:
            vps.append({
                "claim": f"研究方法：{method_line[:80]}",
                "evidence": method_line,
                "confidence": "mid",
                "source": "方法",
                "connections": []
            })
        
        # 主題觀點
        if topic_line:
            vps.append({
                "claim": f"研究主題：{topic_line[:80]}",
                "evidence": topic_line,
                "confidence": "mid",
                "source": "主題",
                "connections": []
            })
        
        # 變數觀點
        if var_line:
            vps.append({
                "claim": f"主要變數：{var_line[:80]}",
                "evidence": var_line,
                "confidence": "mid",
                "source": "變數",
                "connections": []
            })
        
        # 摘要本身做為一個觀點
        if abs_line and len(abs_line) > 15:
            vps.append({
                "claim": abs_line[:120] + ("…" if len(abs_line) > 120 else ""),
                "evidence": abs_line,
                "confidence": "mid",
                "source": "摘要",
                "connections": []
            })
    
    # ───── 去重 ─────
    seen = set()
    unique_vps = []
    for vp in vps:
        key = vp["claim"][:60]
        if key not in seen:
            seen.add(key)
            unique_vps.append(vp)
    
    # 最多 12 個
    return unique_vps[:12]


def extract_relations(notes):
    """從 notes 中解析變數間的因果關係（含結構化與非結構化），用於 Mermaid 圖譜"""
    relations = []
    if not notes:
        return relations
    
    text = "\n".join(notes)
    
    # ───── 一般用途：從任意文字擷取 X→Y ─────
    # 匹配 X→Y 或 X→Y↑↓ 模式
    arrow_items = re.findall(r'([A-Za-z0-9_/\s&\u0391-\u03c9]{1,20}?)\s*[→➔]\s*([A-Za-z0-9_/\s&↑↓→➔+\-\u0391-\u03c9]{1,30})', text)
    for src, tgt in arrow_items:
        src = src.strip()
        tgt_stripped = tgt.strip()
        if src and tgt_stripped and len(src) > 1 and len(tgt_stripped) > 1:
            # Clean up trailing markers
            tgt_clean = re.sub(r'[↑↓*]+', '', tgt_stripped).strip()
            is_positive = '↑' in tgt_stripped or '+**' in tgt_stripped
            is_negative = '↓' in tgt_stripped or '-**' in tgt_stripped or '負' in tgt_stripped
            relations.append({
                "source": src,
                "target": tgt_clean,
                "positive": is_positive,
                "negative": is_negative,
                "significant": True,
                "label": tgt_stripped
            })
    
    # ───── 一般用途：中文關係（降低/提高/促進/抑制）──
    cn_rel_pattern = re.compile(r'([^，。、\n]{2,25}?)(降低|提高|促進|抑制|改善|增加|減少|驅動|調節|顯著升高|顯著降低|正向影響|負向影響)([^，。、\n]{0,30})')
    for m in cn_rel_pattern.finditer(text):
        src = m.group(1).strip()
        verb = m.group(2)
        tgt = m.group(3).strip()
        if src and len(src) > 1:
            is_positive = verb in ('提高', '促進', '增加', '改善', '驅動', '顯著升高', '正向影響')
            is_negative = verb in ('降低', '抑制', '減少', '顯著降低', '負向影響')
            if tgt and len(tgt) > 1:
                relations.append({
                    "source": src,
                    "target": tgt,
                    "positive": is_positive,
                    "negative": is_negative,
                    "significant": True,
                    "label": verb
                })
    
    # ───── 一般用途：英文關係（affects/influences/leads to）──
    en_rel = re.findall(r'([A-Z][a-z]+(?:\s+(?:of|the|and|in|on|to)\s+[A-Za-z]+)*?)\s+(affects|influences|leads? to|impacts?|drives|increases|decreases|reduces|enhances|boosts|lowers)\s+([^\.,;]+)', text)
    for src, verb, tgt in en_rel:
        src = src.strip()
        tgt = tgt.strip()
        if src and tgt and len(src) > 2 and len(tgt) > 2:
            is_positive = verb in ('increases', 'enhances', 'boosts', 'drives')
            is_negative = verb in ('decreases', 'reduces', 'lowers')
            relations.append({
                "source": src,
                "target": tgt,
                "positive": is_positive,
                "negative": is_negative,
                "significant": True,
                "label": verb
            })
    
    # ───── 結構化【Step】──
    step_pattern = re.compile(r'【[^】]*[Ss]tep\s*\d+[^】]*】\s*([^:：]+)[:：]\s*([^【\n]+)')
    for m in step_pattern.finditer(text):
        rel_str = m.group(1).strip()
        result = m.group(2).strip()
        
        arrow_match = re.match(r'([A-Za-z0-9_/\s&]+?)\s*[→➔]\s*([A-Za-z0-9_/\s&]+)', rel_str)
        if arrow_match:
            source = arrow_match.group(1).strip()
            target = arrow_match.group(2).strip()
            is_positive = '+' in result.split(',')[0] if ',' in result else '+' in result[:10]
            is_significant = 'p<' in result or '顯著' in result or 'signif' in result.lower()
            relations.append({
                "source": source,
                "target": target,
                "positive": is_positive,
                "negative": not is_positive if is_significant else False,
                "significant": is_significant,
                "label": result[:40]
            })
    
    # ───── 結構化【H1/H2/H3】──
    hyp_pattern = re.compile(r'【([Hh]\d)[^】]*】\s*([^【\n]+)')
    for m in hyp_pattern.finditer(text):
        label = m.group(1).upper()
        content = m.group(2).strip()
        arrow_match = re.search(r'([A-Za-z0-9_/\s&]+?)\s*[→➔]\s*([A-Za-z0-9_/\s&]+)', content)
        if arrow_match:
            source = arrow_match.group(1).strip()
            target = arrow_match.group(2).strip()
            is_significant = '成立' in content or '顯著' in content or '✅' in content
            relations.append({
                "source": source,
                "target": target,
                "positive": '正' in content or '+' in content[:20],
                "negative": '負' in content or '-' in content[:20],
                "significant": is_significant,
                "label": content[:40]
            })
    
    # ───── 結構化【變數】──
    var_pattern = re.compile(r'【[^】]*變數[^】]*】\s*([^【\n]+(?:\n[^【\n]+)*)')
    for m in var_pattern.finditer(text):
        content = m.group(1).strip()
        dv_match = re.search(r'DV\s*[=：:=]\s*([^,，\n]+)', content)
        iv_match = re.search(r'IV\s*[=：:=]\s*([^,，\n]+)', content)
        if dv_match and iv_match:
            dv = dv_match.group(1).strip()
            iv = iv_match.group(1).strip()
            iva = [x.strip() for x in re.split(r'[,，+]', iv) if x.strip()]
            for iv_i in iva[:3]:
                relations.append({
                    "source": iv_i,
                    "target": dv,
                    "positive": None,
                    "negative": None,
                    "significant": None,
                    "label": ""
                })
    
    # 去重
    seen = set()
    unique_rel = []
    for r in relations:
        key = f"{r['source']}->{r['target']}"
        if key not in seen:
            seen.add(key)
            unique_rel.append(r)
    
    return unique_rel[:8]


def generate_mermaid(viewpoints, relations, title_short):
    """從 viewpoints + relations 產出 Mermaid flow chart"""
    lines = ["graph TD"]
    
    # 壓縮節點名稱為簡短代碼
    used_labels = set()
    
    def short_name(text):
        """生成簡短節點 ID"""
        # 取前 15 個中英文/數字字元
        clean = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff]', '', text)[:15]
        if not clean:
            clean = "var"
        # 確保唯一
        base = clean
        i = 1
        while clean in used_labels:
            clean = f"{base}{i}"
            i += 1
        used_labels.add(clean)
        return clean
    
    # 添加論文標題節點
    title_id = short_name(title_short[:20])
    lines.append(f'    {title_id}["📄 {title_short[:50]}"]')
    lines.append(f'    style {title_id} fill:#2563eb,color:#fff,font-weight:bold')
    
    # 添加 viewpoints 節點
    vp_ids = []
    for i, vp in enumerate(viewpoints):
        vp_id = short_name(f"vp{i}_{vp['claim'][:10]}")
        vp_ids.append(vp_id)
        claim_short = vp['claim'][:40].replace('"', "'")
        lines.append(f'    {vp_id}["💡 {claim_short}"]')
        # 依信心水準標色
        if vp['confidence'] == 'high':
            lines.append(f'    style {vp_id} fill:#dbeafe,stroke:#2563eb')
        elif vp['confidence'] == 'mid':
            lines.append(f'    style {vp_id} fill:#fef3c7,stroke:#d97706')
        else:
            lines.append(f'    style {vp_id} fill:#fee2e2,stroke:#dc2626')
        
        # 連結到論文標題
        lines.append(f'    {title_id} --> {vp_id}')
    
    # 添加 relations 邊
    used_relations = set()
    for rel in relations:
        src = short_name(rel['source'][:15])
        tgt = short_name(rel['target'][:15])
        key = f"{src}->{tgt}"
        if key in used_relations:
            continue
        used_relations.add(key)
        
        # 用線條表示正負/顯著
        pos = rel.get('positive')
        neg = rel.get('negative', False)
        sig = rel.get('significant')
        
        style = "-->"
        if sig == False:
            style = "-.->"  # 虛線 = 不顯著
        elif neg:
            style = "--x"  # X結尾 = 負向
        elif pos:
            style = "==>"  # 粗線 = 正向顯著
        
        label = rel['label'][:20].replace('"', "'") if rel['label'] else ""
        if label:
            lines.append(f'    {src}{style}|"{label}"|{tgt}')
        else:
            lines.append(f'    {src}{style}{tgt}')
    
    # 如果關係太少，用 viewpoint 之間的 Connections 產生更多邊
    if len(relations) < 2 and len(viewpoints) >= 2:
        for i in range(min(len(viewpoints)-1, 3)):
            lines.append(f'    {vp_ids[i]} --- {vp_ids[i+1]}')
    
    # 限制 diagram 大小
    if len(lines) > 40:
        lines = lines[:40]
        lines.append(f'    note["⋯ 還有 {len(viewpoints)} 個觀點"]')
    
    return "\n".join(lines)


def process_paper(p, dry_run=False):
    """處理單篇論文，回傳更新後的 dict"""
    p_out = copy.deepcopy(p)
    
    # 如果已有且不強制覆蓋，跳過
    if p_out.get("viewpoints") and p_out.get("diagram"):
        return p_out
    
    notes = p_out.get("notes", [])
    if not notes:
        return p_out
    
    # 產出 viewpoints
    vps = extract_viewpoints(notes)
    if vps:
        p_out["viewpoints"] = vps
    
    # 產出 relations
    relations = extract_relations(notes)
    
    # 產出 Mermaid diagram
    title_short = p_out.get("title", "論文")
    diagram = generate_mermaid(vps, relations, title_short)
    if diagram:
        p_out["diagram"] = diagram
    
    return p_out


def main():
    dry_run = "--dry-run" in sys.argv
    only_missing = "--only-missing" in sys.argv
    
    data = load()
    papers = data["papers"]
    
    updated_count = 0
    skipped_count = 0
    
    for i, p in enumerate(papers):
        has_notes = bool(p.get("notes"))
        has_vp = bool(p.get("viewpoints"))
        has_dg = bool(p.get("diagram"))
        
        if only_missing and has_vp and has_dg:
            skipped_count += 1
            continue
        
        if not has_notes:
            skipped_count += 1
            continue
        
        title_short = p.get("title", f"Paper {i}")[:40]
        
        if dry_run:
            vps = extract_viewpoints(p.get("notes", []))
            print(f"  [{i+1}/{len(papers)}] {title_short} → {len(vps)} viewpoints")
            updated_count += 1
            continue
        
        updated = process_paper(p)
        if updated.get("viewpoints") != p.get("viewpoints") or updated.get("diagram") != p.get("diagram"):
            data["papers"][i] = updated
            updated_count += 1
            vp_count = len(updated.get("viewpoints", []))
            dg_len = len(updated.get("diagram", ""))
            print(f"  [{i+1}/{len(papers)}] ✅ {title_short} → {vp_count} viewpoints, {dg_len} chars diagram")
        else:
            skipped_count += 1
    
    if dry_run:
        print(f"\n📊 Dry run: {updated_count} would update, {skipped_count} skip")
    else:
        print(f"\n📊 Updated: {updated_count}, Skipped: {skipped_count}")
        if updated_count > 0:
            data["total"] = len(papers)
            data["updated"] = data.get("updated", "").replace(
                data["updated"].split()[0] if " " in data.get("updated","") else data.get("updated",""),
                __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ) if "updated" in data else __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save(data)


if __name__ == "__main__":
    main()
