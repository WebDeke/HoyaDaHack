from flask import Flask, Response, request
from flask_cors import CORS
import json
from datetime import datetime
from resources.users_resource import Users
# from resources.scenes_resource import Scenes
# from resources.movies_resource import Movies

import rest_utils


app = Flask(__name__)
CORS(app)

service_factory = dict()

##################################################################################################################

# DFF TODO A real service would have more robust health check methods.
# This path simply echoes to check that the app is working.
# The path is /health and the only method is GETs
@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)
    rsp = Response(rsp_str, status=200, content_type="application/json")
    return rsp


# TODO Remove later. Solely for explanatory purposes.
# The method take any REST request, and produces a response indicating what
# the parameters, headers, etc. are. This is simply for education purposes.
#
@app.route("/api/demo/<parameter1>", methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/api/demo/", methods=["GET", "POST", "PUT", "DELETE"])
def demo(parameter1=None):
    """
    Returns a JSON object containing a description of the received request.

    :param parameter1: The first path parameter.
    :return: JSON document containing information about the request.
    """

    # DFF TODO -- We should wrap with an exception pattern.
    #

    # Mostly for isolation. The rest of the method is isolated from the specifics of Flask.
    inputs = rest_utils.RESTContext(request, {"parameter1": parameter1})

    # DFF TODO -- We should replace with logging.
    r_json = inputs.to_json()
    msg = {
        "/demo received the following inputs": inputs.to_json()
    }
    print("/api/demo/<parameter> received/returned:\n", msg)

    rsp = Response(json.dumps(msg), status=200, content_type="application/json")
    return rsp

##################################################################################################################


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/api/<resource_collection>', methods=['GET', 'POST'])
def do_resource_collection(resource_collection):
    """
    1. HTTP GET return all resources.
    2. HTTP POST with body --> create a resource, i.e --> database.
    :return:
    """
    request_inputs = rest_utils.RESTContext(request, resource_collection)
    svc = service_factory.get(resource_collection, None)

    #print("DEBUG request inputs", request_inputs)
    #print("DEBUG resource collection", resource_collection)
    #print("DEBUG svc", svc)

    if request_inputs.method == "GET":
        res = svc.get_by_template(path=None,
                                  template=request_inputs.args,
                                  field_list=request_inputs.fields,
                                  limit=request_inputs.limit,
                                  offset=request_inputs.offset)

        res = request_inputs.add_pagination(res)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")

    elif request_inputs.method == "POST":
        data = request_inputs.data

        #print("DEBUG POST REQUEST_INPUTS ", request_inputs)

        res = svc.create(data)

        headers = [{"Location", "/users/" + str(res)}]
        rsp = Response("CREATED", status=201, headers=headers, content_type="text/plain")
    else:
        rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    return rsp


@app.route('/api/<resource_collection>/<resource_id>', methods=['GET', 'PUT', 'DELETE'])
def specific_resource(resource_collection, resource_id):
    """
    1. Get a specific one by ID.
    2. Update body and update.
    3. Delete would ID and delete it.
    :param user_id:
    :return:
    """
    request_inputs = rest_utils.RESTContext(request, resource_collection)
    svc = service_factory.get(resource_collection)

    if request_inputs.method == "GET":
        res = svc.get_resource_by_id(resource_id)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    elif request_inputs.method == "PUT":
        #print("DEBUG PUT REQUEST_INPUTS ", request_inputs)
        res = svc.update_resource_by_id(resource_id, request_inputs.data)
        rsp = Response(json.dumps(res, indent=2, default=str), status=200, content_type="application/json")
    elif request_inputs.method == "DELETE":
        res = svc.delete_resource_by_id(resource_id)
        rsp = Response(json.dumps(res, indent=2, default=str), status=200, content_type="application/json")
    else:
        rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    return rsp

# @app.route('/api/person', methods=['GET'])
# def retrieve_persons():
#     svc = service_factory['person']
#     res = svc.get_resource_all()
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     #print(rsp)
#     return rsp

# @app.route('/api/person/<name>/acted_in', methods=['GET'])
# def retrieve_movies_person_actedin(name):
#     svc = service_factory['person']
#     res = svc.get_movies_person_actedin(name)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     #print(rsp)
#     return rsp

# @app.route('/api/seasons', methods=['GET'])
# def retrieve_seasons():
#     svc = service_factory['seasons']
#     res = svc.get_resource_all()
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     #print(rsp)
#     return rsp

# @app.route('/api/seasons/<int:season_num>', methods=['GET'])
# def retrieve_season_by_name(season_num):
#     svc = service_factory['seasons']
#     res = svc.get_resource_by_num(season_num)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp

# # @app.route('/api/seasons/<int:season_num>/episodes', methods=['GET'])
# # def retrieve_episode_by_season_name_query(season_num):
# #     svc = service_factory['episodes']
# #     res = svc.get_resource_all(season_num)
# #     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
# #     return rsp

# @app.route('/api/seasons/<int:season_num>/episodes/<int:episode_num>', methods=['GET'])
# def retrieve_episode_by_season_name_epname(season_num, episode_num):
#     svc = service_factory['episodes']
#     res = svc.get_resource_by_num(season_num, episode_num)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp

# @app.route('/api/seasons/<int:season_num>/episodes/<int:episode_num>/scenes', methods=['GET'])
# def retrieve_scenes(season_num, episode_num):
#     svc = service_factory['scenes']
#     res = svc.get_resource_all(season_num, episode_num)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp

# @app.route('/api/seasons/<int:season_num>/episodes/<int:episode_num>/scenes/<int:scene_num>', methods=['GET'])
# def retrieve_scenes_by_num(season_num, episode_num, scene_num):
#     svc = service_factory['scenes']
#     res = svc.get_resource_by_num(season_num, episode_num, scene_num)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp

# @app.route('/api/seasons/<int:season_num>/episodes', methods=['GET'])
# def retrieve_episode_with_query(season_num):
#     request_inputs = rest_utils.RESTContext(request)
#     #print(request_inputs)
#     svc = service_factory['episodes']

#     res = svc.get_resource_by_template(path=None,
#                               seasonNum=season_num,
#                               template=request_inputs.args,
#                               field_list=request_inputs.fields,
#                               limit=request_inputs.limit,
#                               offset=request_inputs.offset)

#     res = request_inputs.add_pagination(res)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp

# @app.route('/api/movies', methods=['GET'])
# def retrieve_movies():
#     request_inputs = rest_utils.RESTContext(request)
#     #print(request_inputs)
#     svc = service_factory['movies']

#     res = svc.get_resource_by_template(path=None,
#                                        template=request_inputs.args,
#                                        field_list=request_inputs.fields,
#                                        limit=request_inputs.limit,
#                                        offset=request_inputs.offset)

#     res = request_inputs.add_pagination(res)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp




if __name__ == '__main__':
    service_factory['users'] = Users()
    # service_factory['orders'] = Orders()
    # service_factory['person'] = Person()
    # service_factory['seasons'] = Seasons()
    # service_factory['episodes'] = Episodes()
    # service_factory['scenes'] = Scenes()
    # service_factory['movies'] = Movies()
    app.run(host="0.0.0.0", port=5003)
