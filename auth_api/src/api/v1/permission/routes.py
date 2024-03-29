from http import HTTPStatus

from core.containers import Container
from core.settings import config
from core.utils import authenticate, rate_limit
from dependency_injector.wiring import Provide, inject
from flask import Blueprint, Response, jsonify, make_response, request
from flask_jwt_extended import jwt_required
from services.permission import PermissionService

permission = Blueprint('permission', __name__, url_prefix='/permission')


@permission.route('/', methods=['GET'])
@jwt_required()
@authenticate()
@rate_limit(config.user_max_request_rate)
@inject
def get_permissions(
        user_id: str,
        perm_service: PermissionService = Provide[Container.perm_service]):
    perm_service.check_superuser_authorization(user_id)
    perm_list = perm_service.get_permission_list()
    result = [{'uuid': perm.permission_id,
               'permission_name': perm.permission_name} for perm in perm_list]
    return jsonify(result)


@permission.route('/', methods=['POST'])
@jwt_required()
@authenticate()
@rate_limit(config.user_max_request_rate)
@inject
def create_permission(
        user_id: str,
        perm_service: PermissionService = Provide[Container.perm_service]):
    create_request = perm_service.validate_request(request)
    if isinstance(create_request, Response):
        return create_request

    perm_service.check_superuser_authorization(user_id)
    new_perm = perm_service.create_permission(
        create_request.permission_name
    )

    return make_response(
        jsonify(uuid=new_perm.permission_id,
                permission_name=new_perm.permission_name),
        HTTPStatus.OK
    )


@permission.route('/<uuid:perm_uuid>', methods=['PATCH'])
@jwt_required()
@authenticate()
@rate_limit(config.user_max_request_rate)
@inject
def edit_permission(user_id: str, perm_uuid: str,
                    perm_service: PermissionService = Provide[
                        Container.perm_service]):
    edit_request = perm_service.validate_request(request)
    if isinstance(edit_request, Response):
        return edit_request
    perm_service.check_superuser_authorization(user_id)
    edited_perm = perm_service.edit_permission(
        permission_id=perm_uuid,
        permission_name=edit_request.permission_name
    )
    return make_response(
        jsonify(uuid=edited_perm.permission_id,
                permission_name=edited_perm.permission_name),
        HTTPStatus.OK
    )


@permission.route('/<uuid:perm_uuid>', methods=['DELETE'])
@jwt_required()
@authenticate()
@rate_limit(config.user_max_request_rate)
@inject
def delete_permission(user_id: str, perm_uuid: str,
                      perm_service: PermissionService = Provide[
                          Container.perm_service]):
    perm_service.check_superuser_authorization(user_id)
    deleted_perm = perm_service.delete_permission(permission_id=perm_uuid)
    return make_response(
        jsonify(uuid=deleted_perm.permission_id,
                permission_name=deleted_perm.permission_name),
        HTTPStatus.OK
    )
