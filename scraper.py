
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random
import time
import json
import os

# إعدادات الكاشط
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'
}

# رابط الموقع المستهدف
TARGET_URL = "https://www.alhadath.net/"

# تأخير عشوائي لتجنب الحظر
def random_delay():
    delay = random.uniform(1, 3)
    print(f"⏳ Waiting for {delay:.2f} seconds...")
    time.sleep(delay)

# كشط الموقع
def scrape_alhadath():
    try:
        print("🔍 Starting scrape...")
        random_delay()  # تأخير عشوائي قبل البدء

        response = requests.get(TARGET_URL, headers=HEADERS, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'lxml')
        news_items = []

        # استخراج الأخبار
        for item in soup.select('.news-item, .post')[:20]:  # تحديد 20 خبراً فقط
            title_element = item.select_one('.news-title, h2, h3')
            link_element = item.select_one('a[href]')
            img_element = item.select_one('img')

            if title_element and link_element:
                title = title_element.get_text(strip=True)
                link = link_element.get('href')
                if not link.startswith('http'):
                    link = f"https://www.alhadath.net{link}"

                img_url = img_element.get('src') if img_element else "https://via.placeholder.com/400x300?text=الحدث"

                news_items.append({
                    "title": title,
                    "link": link,
                    "img": img_url,
                    "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })

        # حفظ البيانات في ملف JSON
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(news_items, f, ensure_ascii=False, indent=2)

        # إنشاء ملف HTML
        generate_html(news_items)

        print("✅ Scrape completed successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

# إنشاء ملف HTML
def generate_html(news_items):
    html_content = f'''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>آخر أخبار الحدث 24</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --gold: #c5a059; --dark: #121212; --light: #f8f8f8; }}
        body {{
            font-family: 'Cairo', sans-serif;
            background: var(--dark);
            color: var(--light);
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 15px;
        }}
        .header {{
            text-align: center;
            padding: 20px 0;
            border-bottom: 2px solid var(--gold);
        }}
        .news-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        .news-card {{
            background: #1e1e1e;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s;
        }}
        .news-card:hover {{
            transform: translateY(-5px);
        }}
        .news-img {{
            height: 200px;
            overflow: hidden;
        }}
        .news-img img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }}
        .news-card:hover .news-img img {{
            transform: scale(1.05);
        }}
        .news-body {{
            padding: 15px;
        }}
        .news-title {{
            font-size: 16px;
            margin: 0 0 10px 0;
            line-height: 1.4;
        }}
        .news-time {{
            color: #888;
            font-size: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .news-link {{
            color: var(--gold);
            text-decoration: none;
            font-weight: bold;
        }}
        footer {{
            text-align: center;
            padding: 20px;
            border-top: 1px solid #333;
            margin-top: 40px;
            color: #888;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>آخر أخبار <span style="color: var(--gold);">الحدث 24</span></h1>
        </div>
        <div class="news-grid">
            {"".join(f'''
            <div class="news-card">
                <div class="news-img">
                    <img src="{item['img']}" alt="{item['title']}" loading="lazy">
                </div>
                <div class="news-body">
                    <h3 class="news-title">{item['title']}</h3>
                    <div class="news-time">
                        <span>⏱ {item['time']}</span>
                        <a href="{item['link']}" class="news-link" target="_blank">قراءة المزيد</a>
                    </div>
                </div>
            </div>
            ''' for item in news_items)}
        </div>
    </div>
    <footer>
        <p>© 2024 كاشط أخبار الحدث 24 | جميع الحقوق محفوظة</p>
    </footer>
</body>
</html>
    '''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("📄 HTML file generated: index.html")

# تشغيل الكاشط
if __name__ == "__main__":
    scrape_alhadath()
