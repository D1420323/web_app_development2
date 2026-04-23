import sqlite3

# 資料庫檔案路徑，與 architecture 規劃相符
DB_PATH = 'instance/database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    # 設定 row_factory 讓回傳結果可以像 dict 一樣透過欄位名稱存取 (例如 row['title'])
    conn.row_factory = sqlite3.Row
    return conn

class Note:
    @staticmethod
    def create(title, content, rating, category=None):
        """新增一筆讀書筆記"""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO notes (title, content, rating, category) 
                   VALUES (?, ?, ?, ?)''',
                (title, content, rating, category)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        """取得所有讀書筆記，依照建立時間反序排列"""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM notes ORDER BY created_at DESC')
            return cursor.fetchall()

    @staticmethod
    def get_by_id(note_id):
        """根據 ID 取得單一筆記"""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM notes WHERE id = ?', (note_id,))
            return cursor.fetchone()

    @staticmethod
    def search(keyword):
        """透過關鍵字搜尋標題、內容或分類"""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            search_pattern = f"%{keyword}%"
            cursor.execute(
                '''SELECT * FROM notes 
                   WHERE title LIKE ? OR content LIKE ? OR category LIKE ?
                   ORDER BY created_at DESC''',
                (search_pattern, search_pattern, search_pattern)
            )
            return cursor.fetchall()

    @staticmethod
    def update(note_id, title, content, rating, category=None):
        """更新指定筆記的內容"""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''UPDATE notes 
                   SET title = ?, content = ?, rating = ?, category = ?
                   WHERE id = ?''',
                (title, content, rating, category, note_id)
            )
            conn.commit()
            return cursor.rowcount > 0

    @staticmethod
    def delete(note_id):
        """刪除指定筆記"""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
            conn.commit()
            return cursor.rowcount > 0
