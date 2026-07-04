#!/usr/bin/env python3
"""
generate_notes.py — 為沒有 notes 的論文自動生成基礎分析筆記

從現有的 abstract、tags、topics、methods 等 metadata 組合出 notes，
再呼叫 build_viewpoints.py 產出 viewpoints + diagram。

Usage:
  python3 generate_notes.py
"""

import json, re, os, sys

PAPERS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "papers.json")

# 研究方法對應（根據 tags/topics/abstract 判斷）
METHOD_KEYWORDS = {
    "QVAR": "QVAR (Quantile Vector Autoregression)",
    "TVP-VAR": "TVP-VAR (Time-Varying Parameter VAR)",
    "QQGC": "QQGC (Quantile-on-Quantile Granger Causality)",
    "QARDL": "QARDL (Quantile Autoregressive Distributed Lag)",
    "WQC": "WQC (Wavelet Quantile Correlation)",
    "QTVAR": "QTVAR (Quantile Time-Varying Autoregression)",
    "jQIRF": "jQIRF (Joint Quantile Impulse Response Function)",
    "jQFEVD": "jQFEVD (Joint Quantile Forecast Error Variance Decomposition)",
    "GARCH": "GARCH 族模型",
    "DCC": "DCC-GARCH",
    "copula": "Copula 模型",
    "wavelet": "Wavelet 分析",
    "VAR": "VAR (Vector Autoregression)",
    "NARDL": "NARDL (Nonlinear ARDL)",
    "ARDL": "ARDL (Autoregressive Distributed Lag)",
    "bootstrap": "Bootstrap 檢定",
    "Granger": "Granger 因果檢定",
    "spillover": "DY (2012) Spillover Index / Connectedness",
    "connectedness": "Connectedness 網絡分析",
    "machine learning": "機器學習",
    "LSTM": "LSTM 深度學習",
    "wavelet coherence": "Wavelet Coherence (WTC)",
}

def guess_methods(tags, topics, abstract):
    """從 tags + topics + abstract 猜研究方法"""
    methods = []
    text = " ".join((tags or []) + (topics or []) + [abstract or ""])
    for kw, method in METHOD_KEYWORDS.items():
        if kw.lower() in text.lower():
            if method not in methods:
                methods.append(method)
    return methods[:3]  # 最多3個

def guess_variables(tags, topics, abstract):
    """從 abstract/tags/topics 猜主要變數"""
    variables = []
    
    # 常見經濟/金融變數
    VAR_KEYWORDS = {
        "oil": "原油價格 / Oil Price",
        "crude oil": "原油價格 / Crude Oil",
        "gold": "黃金價格 / Gold Price",
        "stock": "股價 / Stock Price",
        "equity": "股價 / Equity",
        "CO₂": "CO₂ 排放 / CO₂ Emissions",
        "CO2": "CO₂ 排放 / CO₂ Emissions",
        "carbon": "碳排放 / Carbon Emissions",
        "emission": "碳排放 / Emissions",
        "renewable": "再生能源 / Renewable Energy",
        "green": "綠色指標 / Green Variable",
        "energy": "能源價格 / Energy Price",
        "GDP": "GDP / 經濟成長",
        "inflation": "通膨 / Inflation",
        "CPI": "消費者物價指數 / CPI",
        "uncertainty": "不確定性指數 / Uncertainty Index",
        "EPU": "經濟政策不確定性 / EPU",
        "CPU": "氣候政策不確定性 / CPU",
        "GPR": "地緣政治風險 / GPR",
        "geopolitical": "地緣政治風險 / Geopolitical Risk",
        "volatility": "波動度 / Volatility",
        "VIX": "VIX 波動率指數",
        "ESG": "ESG 評分",
        "green bond": "綠色債券 / Green Bond",
        "bond": "債券報酬 / Bond Return",
        "bitcoin": "比特幣 / Bitcoin",
        "crypto": "加密貨幣 / Cryptocurrency",
        "blockchain": "區塊鏈 / Blockchain",
        "tech": "科技股 / Tech Stock",
        "AI": "人工智慧 / AI",
        "natural gas": "天然氣價格 / Natural Gas",
        "exchange rate": "匯率 / Exchange Rate",
        "interest rate": "利率 / Interest Rate",
        "FDI": "外國直接投資 / FDI",
        "trade": "貿易開放度 / Trade Openness",
    }
    text = " ".join([abstract or ""] + (tags or []) + (topics or [])).lower()
    
    for kw, var in VAR_KEYWORDS.items():
        if kw in text and var not in variables:
            variables.append(var)
    
    return variables[:5]

def generate_notes(p):
    """為一篇論文生成基礎 notes"""
    notes = []
    title = p.get("title", "")
    authors = p.get("authors", "")
    year = p.get("year", "")
    journal = p.get("journal", "")
    abstract = p.get("abstract", "")
    tags = p.get("tags", [])
    topics = p.get("topics", [])
    doi = p.get("doi", "")
    citations = p.get("citations", 0)
    
    # 論文基本資訊
    notes.append(f"作者：{authors}" if authors else None)
    notes.append(f"年份：{year}" if year else None)
    notes.append(f"期刊：{journal}" if journal else None)
    
    # 研究主題
    if topics:
        notes.append(f"主題：{'、'.join(topics)}")
    
    # 研究方法
    methods = guess_methods(tags, topics, abstract)
    if methods:
        notes.append(f"方法：{' + '.join(methods)}")
    
    # 變數猜測
    variables = guess_variables(tags, topics, abstract)
    if variables:
        notes.append(f"變數：{'、'.join(variables)}")
    
    # 從 abstract 推論發現
    if abstract:
        clean_abs = abstract.strip()
        if clean_abs:
            notes.append("---")
            notes.append(f"【摘要】{clean_abs}")
            # 嘗試產生一個 findings 行
            findings = []
            # 中文「發現」
            if '發現' in clean_abs:
                parts = clean_abs.split('發現')
                for part in parts[1:]:
                    finding = part.strip().rstrip('。.,;')
                    if finding:
                        findings.append(finding)
            # 中文「影響」
            if '影響' in clean_abs and not findings:
                # 至少把「X對Y的影響」抓出來
                imp_match = re.search(r'([^，。]{2,20}?對[^，。]{2,30}?的影響)', clean_abs)
                if imp_match:
                    findings.append(imp_match.group(1))
            # 英文模式
            if not findings and clean_abs.startswith('This'):
                # Keep the abstract as is
                pass
            for finding in findings[:2]:
                notes.append(f"發現：{finding}")
    
    # DOI 與引用
    if doi:
        notes.append(f"---")
        notes.append(f"DOI：{doi}")
    if citations:
        notes.append(f"被引次數：{citations}")
    
    # 濾掉 None
    notes = [n for n in notes if n is not None]
    
    return notes

def main():
    data = json.load(open(PAPERS_JSON, "r", encoding="utf-8"))
    papers = data["papers"]
    
    updated = 0
    for i, p in enumerate(papers):
        if p.get("notes"):
            continue  # 跳過已有 notes 的
        
        notes = generate_notes(p)
        if notes:
            data["papers"][i]["notes"] = notes
            updated += 1
            print(f"  [{i+1}/{len(papers)}] ✅ {p['title'][:50]} → {len(notes)} notes")
    
    print(f"\n📊 Generated notes for {updated} papers")
    
    # Save
    from build_viewpoints import save
    save(data)
    print("✅ 已儲存，接下來執行 build_viewpoints.py 補觀點圖譜")

if __name__ == "__main__":
    main()
