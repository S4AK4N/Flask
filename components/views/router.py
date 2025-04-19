from flask import Blueprint, render_template, request
from components.views.Top.top import views as top_routes
from components.views.TaskList.form import form_routes
from components.views.TaskNameDelete.delete_name_page import delete_routes as delete_page_routes
from components.views.TaskNameDelete.delete_name import delete_routes as delete_action_routes
from components.views.TaskNameRegister.register_name_page import register_routes as register_name_page_routes
from components.views.TaskNameRegister.register_name import register_routes as register_name_routes
from components.views.Post.result import post_routes as result_routes
from components.views.Post.past import past_routes
from components.views.Delete_Post.delete_post import delete_post_routes
from components.views.Post.edit_post import edit_post_routes

# viewsをインスタンス化
views = Blueprint("views", __name__)

# Topページ
views.register_blueprint(top_routes)
# 基本フォーム
views.register_blueprint(form_routes)
# 名前登録ページレンダリング
views.register_blueprint(register_name_page_routes)
# 名前登録処理
views.register_blueprint(register_name_routes)
# 名前削除フォーム
views.register_blueprint(delete_page_routes)
# 名前削除処理
views.register_blueprint(delete_action_routes)
# 内容表示
views.register_blueprint(result_routes)
# 過去書き込み表示
views.register_blueprint(past_routes)
# タスクの削除
views.register_blueprint(delete_post_routes)
# 編集
views.register_blueprint(edit_post_routes)