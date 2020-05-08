import uuid
from datetime import datetime
from flask import jsonify, abort, request, Blueprint
from ..util.dto import TaskContentSchema

api = Blueprint('request_api', __name__)

taskContentSchema=TaskContentSchema()

TASK_REQUEST={}

@api.route('/tasks/', methods=['GET'])
def get_tasks():
    """list of all tasks"""
    result=TASK_REQUEST
    return jsonify(result)


@api.route('/tasks/<string:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    """ get a task given its identifier"""

    if task_id not in TASK_REQUEST:
        abort(404)

    result=taskContentSchema.dump(TASK_REQUEST[task_id])
    return jsonify(result)


@api.route('/tasks/', methods=['POST'])
def create_task():
    """create a new task"""

    if not request.get_json():
        abort(400)

    errors = taskContentSchema.validate(request.get_json())
    if errors:
        abort(400)

    data = request.get_json(force=True)

    if not data.get('text'):
        abort(400)

    new_uuid = str(uuid.uuid4())
    book_request = {
        'text': data['text'],
        'created_on': datetime.utcnow()
    }


    TASK_REQUEST[new_uuid] = book_request
    return jsonify({"task_id": new_uuid}), 201


@api.route('/tasks/<string:task_id>', methods=['PUT'])
def edit_task(task_id):

    """update a task given its identifier"""

    if task_id not in TASK_REQUEST:
        abort(404)

    if not request.get_json():
        abort(400)

    errors = taskContentSchema.validate(request.get_json())
    if errors:
        abort(400)

    data = request.get_json(force=True)

    if not data.get('text'):
        abort(400)
    TASK_REQUEST[task_id]['text'] = data.get('text')
    TASK_REQUEST[task_id]['updated_on']=datetime.utcnow()

    result=taskContentSchema.dump(TASK_REQUEST[task_id])
    return jsonify(result), 204