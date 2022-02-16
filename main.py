from flask import app


@app.route('/list', methods=['POST'])
def list_add():
    return 'CREATE LIST'


@app.route('/list/<list_id>', methods=['GET'])
def list_get(list_id):
    return 'SHOW LIST'


@app.route('/list/<list_id>', methods=['DELETE'])
def list_delete(list_id):
    return 'DELETE LIST'


@app.route('/users', methods=['GET'])
def users_get():
    return 'SHOW ALL USERS'


@app.route('/user', methods=['POST'])
def user_add():
    return 'CREATE USER'


@app.route('/user/<user_id>', methods=['DELETE'])
def user_delete(user_id):
    return 'DELETE USER'


@app.route('/list/<list_id>/entry', methods=['POST'])
def entry_add():
    return 'CREATE ENTRY'


@app.route('/list/<list_id>/entry/<entry_id>', methods=['POST'])
def entry_update():
    return 'UPDATE ENTRY'


@app.route('/list/<list_id>/entry/<entry_id>', methods=['DELETE'])
def entry_delete():
    return 'DELETE ENTRY'


app.run()
