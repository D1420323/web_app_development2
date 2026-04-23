# 路由與頁面設計 — 讀書筆記本系統

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 筆記列表 (首頁) | GET | `/` | `templates/index.html` | 顯示所有筆記，並處理關鍵字搜尋功能 |
| 新增筆記頁面 | GET | `/notes/new` | `templates/create.html` | 顯示填寫新筆記的表單 |
| 建立筆記 | POST | `/notes` | — | 接收表單資料並存入資料庫，完成後重導向至首頁 |
| 筆記詳情 | GET | `/notes/<id>` | `templates/view.html` | 顯示單一筆記詳細內容 |
| 編輯筆記頁面 | GET | `/notes/<id>/edit` | `templates/edit.html` | 顯示編輯表單，並帶入原有內容 |
| 更新筆記 | POST | `/notes/<id>/update` | — | 接收表單資料並更新資料庫，完成後重導向至詳情頁 |
| 刪除筆記 | POST | `/notes/<id>/delete` | — | 刪除筆記，完成後重導向至首頁 |

## 2. 每個路由的詳細說明

### `GET /` (筆記列表與搜尋)
- **輸入**：URL 參數 `?q=keyword` (選擇性)。
- **處理邏輯**：若有提供 `q` 參數，則呼叫 `Note.search(keyword)`；否則呼叫 `Note.get_all()` 取得所有列表資料。
- **輸出**：渲染 `index.html`，並傳遞筆記列表資料及搜尋關鍵字。
- **錯誤處理**：無特定錯誤。

### `GET /notes/new` (新增筆記頁面)
- **輸入**：無。
- **處理邏輯**：準備表單。
- **輸出**：渲染 `create.html`。
- **錯誤處理**：無。

### `POST /notes` (建立筆記)
- **輸入**：表單資料 (`title`, `content`, `rating`, `category`)。
- **處理邏輯**：驗證 `title` 必填。若驗證通過，呼叫 `Note.create(...)`。
- **輸出**：重導向至首頁 `/`。
- **錯誤處理**：若 `title` 為空，設定 flash 錯誤訊息並重新渲染 `create.html`。

### `GET /notes/<id>` (筆記詳情)
- **輸入**：URL 參數 `id`。
- **處理邏輯**：呼叫 `Note.get_by_id(id)`。
- **輸出**：渲染 `view.html` 並傳入取得的單筆資料。
- **錯誤處理**：若資料不存在，回傳 404 Not Found。

### `GET /notes/<id>/edit` (編輯筆記頁面)
- **輸入**：URL 參數 `id`。
- **處理邏輯**：呼叫 `Note.get_by_id(id)` 取得舊有資料。
- **輸出**：渲染 `edit.html` 供使用者修改。
- **錯誤處理**：若資料不存在，回傳 404 Not Found。

### `POST /notes/<id>/update` (更新筆記)
- **輸入**：URL 參數 `id`，表單資料 (`title`, `content`, `rating`, `category`)。
- **處理邏輯**：驗證 `title`。若驗證通過，呼叫 `Note.update(...)`。
- **輸出**：重導向至 `/notes/<id>`。
- **錯誤處理**：若資料不存在回傳 404；若表單驗證失敗，設定 flash 並重新渲染 `edit.html`。

### `POST /notes/<id>/delete` (刪除筆記)
- **輸入**：URL 參數 `id`。
- **處理邏輯**：呼叫 `Note.delete(id)` 進行刪除。
- **輸出**：重導向至首頁 `/`。
- **錯誤處理**：若資料不存在回傳 404。

## 3. Jinja2 模板清單

所有模板檔案放置於 `app/templates/` 資料夾下，採用繼承架構：

- `base.html`：基礎網頁佈局，包含通用的標題、導覽列 (Navbar) 與頁尾 (Footer)。
- `index.html`：繼承自 `base.html`。負責呈現筆記列表與搜尋框。
- `create.html`：繼承自 `base.html`。呈現新增筆記表單。
- `view.html`：繼承自 `base.html`。呈現單筆筆記的所有詳細資訊。
- `edit.html`：繼承自 `base.html`。呈現編輯筆記表單。

## 4. 路由骨架程式碼

路由的骨架程式碼採用 Flask Blueprint 的形式建置，已放置於 `app/routes/note_routes.py`。
