from flask import request, Blueprint

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
def index():
    print('aaaa')
    return {}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """

    :return:
    """
    request_data = request.data
    print(request_data, type(request_data))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    return {'aaa': 'bbb'}

