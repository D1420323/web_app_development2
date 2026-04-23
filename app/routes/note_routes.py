from flask import Blueprint, render_template, request, redirect, url_for, flash, abort

# 建立 Blueprint 物件來管理所有筆記相關的路由
note_bp = Blueprint('note_routes', __name__)

@note_bp.route('/')
def index():
    """
    GET /
    處理筆記列表與搜尋請求。
    若有 URL 參數 q，則進行搜尋；否則列出所有筆記。
    渲染模板: index.html
    """
    pass

@note_bp.route('/notes/new')
def create_page():
    """
    GET /notes/new
    顯示新增筆記的表單頁面。
    渲染模板: create.html
    """
    pass

@note_bp.route('/notes', methods=['POST'])
def create_note():
    """
    POST /notes
    接收表單資料並建立新筆記。
    成功後重導向至 /
    """
    pass

@note_bp.route('/notes/<int:id>')
def view_note(id):
    """
    GET /notes/<id>
    根據 ID 顯示單一筆記的詳細資訊。
    渲染模板: view.html
    """
    pass

@note_bp.route('/notes/<int:id>/edit')
def edit_page(id):
    """
    GET /notes/<id>/edit
    顯示編輯筆記的表單頁面，並帶入現有資料。
    渲染模板: edit.html
    """
    pass

@note_bp.route('/notes/<int:id>/update', methods=['POST'])
def update_note(id):
    """
    POST /notes/<id>/update
    接收表單資料並更新指定 ID 的筆記內容。
    成功後重導向至 /notes/<id>
    """
    pass

@note_bp.route('/notes/<int:id>/delete', methods=['POST'])
def delete_note(id):
    """
    POST /notes/<id>/delete
    刪除指定 ID 的筆記。
    成功後重導向至 /
    """
    pass
