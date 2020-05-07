"""
This module contains all API for the users.
"""
from flask import Blueprint,jsonify

from app.dao.usersDAO import get_all_users,get_all_students,get_user_by_id,get_all_companies

user_api_v1 = Blueprint("user_api_v1","user_api_v1",url_prefix="/api/v1/user")

@user_api_v1.route("/")
def api_get_all_users():
    """
    Get all users details.

    :returns: list of users with details
    :rtype: list
    """
    return jsonify(get_all_users())

@user_api_v1.route("/student")
def api_get_all_students():
    """
    Get all student details.

    :returns: list of students with details
    :rtype: list
    """
    return jsonify(get_all_students())

@user_api_v1.route("/<id>")
def api_get_user_by_id(id):
    """
    Get a particular user details by his id.
    
    :param id: Id of the user
    :type id: str
    :return: a dict containing user details
    :rtype: dict
    """
    return jsonify(get_user_by_id(id))

@user_api_v1.route("/company")
def api_get_all_companies():
    """
    Get all student details.
    :returns: a list of companies with details.
    :rtype: list
    """
    return jsonify(get_all_companies())

@user_api_v1.route("/register")
def register():
    pass

@user_api_v1.route("/login")
def login():
    pass

@user_api_v1.route("<id>/create_profile")
def create_profile():
    pass

@user_api_v1.route("/view_companies")
def api_get_approved_companies():
    """
    Get list of all approved copmanies
    :returns: a list of approved companies with details.
    :rtype: list
    """
    return jsonify(get_approved_companies())



