from flask import Blueprint

blueprint = Blueprint(
    'livro_blueprint',
    __name__,
    url_prefix=''
)