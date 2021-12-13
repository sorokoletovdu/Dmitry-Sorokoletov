from pprint import pprint

import pytest
import requests
import json
import re
import datetime
import pytz
from common import const
from common import user
from common import req_resp_format as rrf


def test_login():
    """
    Login user and get session id
    :return: session id
    """
    # Set expected X-Expire-After header
    expectedExpireTime = datetime.datetime.now() + datetime.timedelta(hours=1)
    formattedExpectedExpireTime = expectedExpireTime.astimezone(pytz.UTC).strftime('%a %b %d %H:%M:%S GMT %Y')

    with requests.Session() as s:
        # Send GET request
        response = user.pet_shop_login(const.DEFAULT_USER, s)

        # Check response HTTP code equals 200
        assert response.status_code == 200

        # Check headers consist X-Rate-Limit=5000 and X-Expires-After equals current time plus one hour UTC
        assert response.headers['X-Rate-Limit'] == '5000'
        assert response.headers['X-Expires-After'] == formattedExpectedExpireTime


def test_logout():
    """
        Logout current user
    """

    with requests.Session() as s:
        # Send GET request
        response = user.pet_shop_logout(s)

        # Check response HTTP code equals 200
        assert response.status_code == 200

        # Check response consist "User logged out"
        assert re.search(r'User logged out', str(response.content)).group(0)


def test_create_user():
    """
    Create new user. And login new user.
    """
    with requests.Session() as s:
        user.pet_shop_login(const.DEFAULT_USER, s)

        # Set URL
        url = const.BASIC_API + '/user'

        # Set headers
        headers = {'Content-Type': 'application/json'}

        # Send POST request
        response = s.post(url, headers=headers, data=json.dumps(const.USER_1, indent=4))

        # Check response HTTP code equals 200
        assert response.status_code == 200

        # Check response equals request
        resp_body = response.json()
        assert resp_body == const.USER_1

        # Print request and response
        rrf.pprint_req(response.request)
        rrf.pprint_res(response)

        # Logout current user
        user.pet_shop_logout(s)

        # Check new user can log in
        resp = user.pet_shop_login(const.USER_1, s)
        assert resp.status_code == 200

        # Print new user request and response
        rrf.pprint_req(resp.request)
        rrf.pprint_res(resp)

        user.pet_shop_logout(s)


def test_create_user_with_list():
    """
    Create two new users. And login both new users.
    """
    with requests.Session() as s:
        user.pet_shop_login(const.DEFAULT_USER, s)

        # Set URL
        url = const.BASIC_API + '/user/createWithList'

        # Set headers
        headers = {'Content-Type': 'application/json'}

        # Set list of users
        req_data = [const.USER_2, const.USER_3]

        # Send POST request
        response = s.post(url, headers=headers, data=json.dumps(req_data, indent=4))

        # Check response HTTP code equals 200
        assert response.status_code == 200

        # Check response equals request
        resp_body = response.json()
        assert resp_body == req_data

        # Print request and response
        rrf.pprint_req(response.request)
        rrf.pprint_res(response)

        # Logout current user
        user.pet_shop_logout(s)

        # Check the first new user can log in
        resp = user.pet_shop_login(const.USER_2, s)
        assert resp.status_code == 200

        # Print new user request and response
        rrf.pprint_req(resp.request)
        rrf.pprint_res(resp)

        # Logout current user
        user.pet_shop_logout(s)

        # Check the second new user can log in
        resp = user.pet_shop_login(const.USER_3, s)
        assert resp.status_code == 200

        # Print new user request and response
        rrf.pprint_req(resp.request)
        rrf.pprint_res(resp)

        user.pet_shop_logout(s)


def test_get_user_info():
    """
    Get user info by username
    """
    with requests.Session() as s:
        # Set URL
        url = const.BASIC_API + '/user/%s' % (const.USER_1['username'])

        # Set headers
        headers = {'Content-Type': 'application/json'}

        # Send GET request
        response = s.get(url, headers=headers)
        assert response.status_code == 200

        resp_body = response.json()

        assert resp_body == const.USER_1

        # Print new user request and response
        rrf.pprint_req(response.request)
        rrf.pprint_res(response)


def test_update_user():
    """
    Update existing user Name
    """
    with requests.Session() as s:
        # Set URL
        url = const.BASIC_API + '/user/%s' % (const.USER_1_UPDATED['username'])

        # Set headers
        headers = {'Content-Type': 'application/json'}

        user.pet_shop_login(const.DEFAULT_USER, s)
        # Send PUT request
        response = s.put(url, headers=headers, data=json.dumps(const.USER_1_UPDATED, indent=4))
        assert response.status_code == 200

        resp_body = response.json()

        assert resp_body == const.USER_1_UPDATED

        # Print new user request and response
        rrf.pprint_req(response.request)
        rrf.pprint_res(response)


def test_delete_user():
    """
    Delete existing user
    """
    with requests.Session() as s:
        # Set URL
        url = const.BASIC_API + '/user/%s' % (const.USER_3['username'])

        user.pet_shop_login(const.DEFAULT_USER, s)
        # Send DELETE request
        response = s.delete(url)
        assert response.status_code == 200
