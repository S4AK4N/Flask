from flask import Blueprint, render_template, request
from components.views.Top.top import views as top_routes
from components.views.NameRegister.register import register_routes
from components.views.NameDelete.delete import delete_routes
from components.views.Post.post import post_routes

# viewsをインスタン化
views = Blueprint("views", __name__)

# Blueprint登録
views.register_blueprint(top_routes)
views.register_blueprint(top_routes)
views.register_blueprint(register_routes)
views.register_blueprint(delete_routes)
views.register_blueprint(post_routes)