from flask import Flask, render_template_string, url_for

app = Flask(__name__)

server_info = {
    "name": "EverNightShop",
    "description": "اكتشف أفضل العروض واحصل على دعم فوري لشراء منتجاتك المفضلة!",
    "contact_number": "212713614717",
    "copyright": "© 2025 SMAX PRO"
}

items = [
    {"id": 1, "name": "BOOMBOX", "image": "boombox.jpg"},
    {"id": 2, "name": "CARS", "image": "cars.jpg"},
    {"id": 3, "name": "HOUSE", "image": "house.jpg"},
    {"id": 4, "name": "MA7AL", "image": "ma7al.jpg"},
    {"id": 5, "name": "TOYS", "image": "toys.jpg"},
    {"id": 6, "name": "MONEY", "image": "money.jpg"},
    {"id": 7, "name": "WEAPON", "image": "weapon.jpg"},
    {"id": 8, "name": "RANK", "image": "rank.jpg"},
    {"id": 9, "name": "UNBAN", "image": "unban.jpg"},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{ server.name }} - الرئيسية</title>
    <style>
        /* نفس التنسيقات السابقة */
        * {
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0; padding: 0;
        }
        body {
            background: #fff5f5;
            color: #7f1d1d;
            min-height: 100vh;
        }
        .container {
            display: flex;
            height: 100vh;
            flex-direction: row;
        }
        .sidebar {
            width: 280px;
            background: #b91c1c;
            padding: 20px;
            box-shadow: 2px 0 10px rgba(0,0,0,0.1);
            text-align: right;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            color: #fee2e2;
        }
        .sidebar h2 {
            margin-bottom: 15px;
            font-weight: 700;
            font-size: 24px;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .verified-icon {
            background-color: #3b82f6;
            color: white;
            font-weight: bold;
            font-size: 20px;
            padding: 0 6px;
            border-radius: 4px;
            user-select: none;
            line-height: 1;
        }
        .sidebar p {
            margin-bottom: 10px;
            font-size: 15px;
            line-height: 1.4;
        }
        .sidebar hr {
            border: 0;
            border-top: 1px solid rgba(254,226,226,0.4);
            margin: 15px 0;
        }
        .contact-btn {
            background: #dc2626;
            color: white;
            text-align: center;
            padding: 14px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 18px;
            text-decoration: none;
            display: block;
            margin-top: 20px;
            transition: background 0.3s ease;
        }
        .contact-btn:hover {
            background: #b91c1c;
        }
        .copyright {
            font-size: 13px;
            text-align: center;
            color: rgba(254,226,226,0.7);
            margin-top: 25px;
            user-select: none;
        }
        .main-content {
            flex-grow: 1;
            padding: 30px 40px;
            overflow-y: auto;
            background: #fef2f2;
        }
        .main-content h1 {
            margin-bottom: 25px;
            color: #b91c1c;
            font-weight: 700;
            font-size: 28px;
            letter-spacing: 1px;
        }
        .items-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }
        .item-card {
            background: #fee2e2;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(185, 28, 28, 0.2);
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .item-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(185, 28, 28, 0.4);
        }
        .item-card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            display: block;
            border-radius: 12px 12px 0 0;
        }
        .buy-btn {
            background-color: #b91c1c;
            color: white;
            text-align: center;
            text-decoration: none;
            border-radius: 0 0 12px 12px;
            padding: 12px 0;
            font-weight: 700;
            font-size: 18px;
            transition: background-color 0.3s ease;
            user-select: none;
            display: block;
        }
        .buy-btn:hover {
            background-color: #dc2626;
        }
        @media (max-width: 900px) {
            .items-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .container {
                flex-direction: column;
                height: auto;
            }
            .sidebar {
                width: 100%;
                height: auto;
                box-shadow: none;
                padding: 15px 20px;
                text-align: center;
            }
            .main-content {
                padding: 20px;
            }
            .sidebar h2 {
                justify-content: center;
            }
        }
        @media (max-width: 500px) {
            .items-grid {
                grid-template-columns: 1fr;
            }
            .sidebar h2 {
                font-size: 20px;
            }
            .contact-btn {
                font-size: 16px;
                padding: 12px;
            }
        }
    </style>
</head>
<body>
<div class="container">
    <aside class="sidebar">
        <div class="top-info">
            <h2>
                {{ server.name }}
                <span class="verified-icon" title="موثق">★</span>
            </h2>
            <p>{{ server.description }}</p>
            <hr>
        </div>
        <a href="https://wa.me/{{ server.contact_number }}" target="_blank" class="contact-btn">الدعم</a>
        <div class="copyright">{{ server.copyright }}</div>
    </aside>
    <main class="main-content">
        <h1>قائمة المنتجات</h1>
        <div class="items-grid">
            {% for item in items %}
            <div class="item-card">
                <img src="{{ url_for('static', filename='images/' + item.image) }}" alt="{{ item.name }}" />
                <a class="buy-btn" href="https://wa.me/{{ server.contact_number }}?text={{ ('مرحباً، أود شراء: ' + item.name) | urlencode }}" target="_blank">
                    شراء
                </a>
            </div>
            {% endfor %}
        </div>
    </main>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, server=server_info, items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
