import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

class ShadowVortexEngine:
    """
    ENGINE: VORTEX 26 - ULTRΔ EDITION
    SOURCE: Arabe Fashion Intelligence
    STYLE: Premium Glassmorphism Grid
    """
    def __init__(self):
        self.rss_url = "https://news.google.com/rss/search?q=site:arabefashion.com"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0 Safari/537.36'}
        self.ad_link = "https://www.effectivegatecpm.com/t3rvmzpu?key=26330eef1cb397212db567d1385dc0b9"

    def _get_clean_data(self):
        try:
            res = requests.get(self.rss_url, headers=self.headers, timeout=20)
            soup = BeautifulSoup(res.content, 'xml')
            return soup.find_all('item')[:16]
        except Exception as e:
            print(f"❌ Error fetching RSS: {e}")
            return []

    def _extract_image(self, url):
        try:
            # محاولة سحب الصورة الأصلية من الرابط المباشر
            r = requests.get(url, headers=self.headers, timeout=10)
            s = BeautifulSoup(r.text, 'html.parser')
            img = s.find("meta", property="og:image")
            return img["content"] if img else "https://via.placeholder.com/600x800?text=Fashion+Studio"
        except:
            return "https://via.placeholder.com/600x800?text=Loading+Image..."

    def build_ui(self):
        print("🚀 [VORTEX] جاري بناء الواجهة الفخمة...")
        items = self._get_clean_data()
        news_grid_html = ""

        for item in items:
            title = item.title.text.split(" - ")[0]
            # نستخدم التزامن الوهمي هنا لتبسيط الكود لك
            img = "https://via.placeholder.com/600x800?text=Premium+Fashion" # سيتم استبدالها برابط المقال
            
            news_grid_html += f'''
            <div class="n-card">
                <a href="{self.ad_link}" target="_blank">
                    <div class="n-img">
                        <img src="{img}" alt="Fashion" loading="lazy">
                        <div class="n-badge">2026 TREND</div>
                    </div>
                    <div class="n-info">
                        <h3>{title}</h3>
                        <div class="n-footer">
                            <span>📅 {datetime.now().strftime('%d/%m')}</span>
                            <span class="n-more">اكتشفي الآن</span>
                        </div>
                    </div>
                </a>
            </div>'''

        full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>STUDIO HOMEWORK | VORTEX</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #050505; --accent: #d4af37; --glass: rgba(255, 255, 255, 0.03); --border: rgba(255, 255, 255, 0.08); }}
        body {{ background: var(--bg); color: #fff; font-family: 'Cairo', sans-serif; margin: 0; overflow-x: hidden; }}
        
        /* تأثير الخلفية المتحركة */
        body::before {{ content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at 50% 50%, #1a1a1a 0%, #050505 100%); z-index: -1; }}

        header {{ background: rgba(0,0,0,0.8); backdrop-filter: blur(15px); padding: 20px 5%; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; }}
        .logo {{ font-size: 28px; font-weight: 900; letter-spacing: -1px; text-decoration: none; color: #fff; }}
        .logo span {{ color: var(--accent); text-shadow: 0 0 15px var(--accent); }}

        .container {{ max-width: 1400px; margin: 40px auto; padding: 0 20px; }}

        /* شبكة ألترا فخمة */
        .news-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; }}
        
        .n-card {{ background: var(--glass); border-radius: 24px; border: 1px solid var(--border); overflow: hidden; transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); backdrop-filter: blur(5px); }}
        .n-card:hover {{ transform: translateY(-12px) scale(1.02); border-color: var(--accent); box-shadow: 0 20px 40px rgba(0,0,0,0.5); }}
        
        .n-card a {{ text-decoration: none; color: inherit; }}
        .n-img {{ position: relative; height: 400px; overflow: hidden; }}
        .n-img img {{ width: 100%; height: 100%; object-fit: cover; filter: brightness(0.8); transition: 0.5s; }}
        .n-card:hover .n-img img {{ filter: brightness(1.1); transform: scale(1.1); }}
        
        .n-badge {{ position: absolute; top: 20px; left: 20px; background: var(--accent); color: #000; padding: 5px 15px; border-radius: 50px; font-size: 11px; font-weight: 900; box-shadow: 0 5px 15px rgba(212,175,55,0.4); }}
        
        .n-info {{ padding: 25px; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); }}
        .n-info h3 {{ font-size: 18px; line-height: 1.5; margin: 0 0 20px 0; font-weight: 700; height: 54px; overflow: hidden; color: #efefef; }}
        
        .n-footer {{ display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border); pt: 15px; margin-top: 10px; padding-top: 15px; }}
        .n-more {{ color: var(--accent); font-weight: 700; font-size: 13px; text-transform: uppercase; border-bottom: 2px solid var(--accent); padding-bottom: 2px; }}

        footer {{ padding: 60px; text-align: center; background: rgba(0,0,0,0.5); border-top: 1px solid var(--border); margin-top: 80px; }}
        
        @media (max-width: 768px) {{
            .news-grid {{ grid-template-columns: 1fr; }}
            .n-img {{ height: 450px; }}
        }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">STUDIO<span>HOMEWORK</span></a>
        <div style="font-size: 12px; color: var(--accent); border: 1px solid var(--accent); padding: 5px 15px; border-radius: 20px;">EDITION 2026</div>
    </header>

    <div class="container">
        <h1 style="font-size: 40px; font-weight: 900; margin-bottom: 40px; border-right: 8px solid var(--accent); padding-right: 20px;">آخر الصيحات <span style="font-weight: 400; color: #666; font-size: 20px;">/ VORTEX GRID</span></h1>
        
        <div class="news-grid">
            {news_grid_html}
        </div>
    </div>

    <footer>
        <div class="logo">STUDIO<span>HOMEWORK</span></div>
        <p style="color: #666; margin-top: 15px;">جميع الحقوق محفوظة © 2026 - تجربة مستخدم فائقة الفخامة</p>
    </footer>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        print("✅ [MISSION COMPLETE] تم توليد الملف index.html بنجاح.")

if __name__ == "__main__":
    vortex = ShadowVortexEngine()
    vortex.build_ui()
