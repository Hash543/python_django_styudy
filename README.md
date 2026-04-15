# Django Blog 學習專案

使用 Django 6.0 建立的部落格專案，包含前端模板渲染與 REST API 兩種介面。

## 技術棧

- Python 3 + Django 6.0.3
- Django REST Framework 3.17.1
- SimpleJWT (JWT 認證)
- SQLite

## 安裝與啟動

```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境
source venv/Scripts/activate   # Git Bash
venv\Scripts\activate          # cmd

# 安裝套件
pip install django djangorestframework djangorestframework-simplejwt

# 資料庫遷移
python manage.py migrate

# 建立管理員帳號
python manage.py createsuperuser

# 啟動開發伺服器
python manage.py runserver
```

## 專案結構

```
myproject/          # Django 設定 (settings, urls, wsgi)
blog/               # 部落格應用程式
├── models.py       # Post 模型
├── views.py        # 模板視圖 + DRF ViewSet
├── serializers.py  # DRF 序列化器
├── permission.py   # 自訂權限 (IsAuthorOrReadOnly)
├── urls.py         # 模板路由
├── api_urls.py     # API 路由 (DefaultRouter)
├── admin.py        # 後台管理設定
└── templates/blog/ # HTML 模板 (base, index, detail)
```

## API 端點

| 方法 | 路徑 | 說明 | 權限 |
|------|------|------|------|
| POST | `/api/token/` | 取得 JWT Token | 公開 |
| POST | `/api/token/refresh/` | 刷新 Token | 公開 |
| GET | `/api/posts/` | 文章列表 | 公開 |
| POST | `/api/posts/` | 新增文章 | 需登入 |
| GET | `/api/posts/{id}/` | 文章詳情 | 公開 |
| PUT | `/api/posts/{id}/` | 更新文章 | 僅作者 |
| DELETE | `/api/posts/{id}/` | 刪除文章 | 僅作者 |

## 頁面路由

| 路徑 | 說明 |
|------|------|
| `/admin/` | Django 管理後台 |
| `/blog/` | 文章列表頁 |
| `/blog/{id}/` | 文章詳情頁 |

## API 使用範例

```bash
# 取得 Token
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'

# 新增文章 (帶 Token)
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "Hello", "content": "World"}'
```
