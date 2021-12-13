import re
import requests

from common import const


def pet_shop_login(user=const.DEFAULT_USER, connector=requests):
    """
    Login user and get session id
    :return: session id
    """

    # Set URL
    url = const.BASIC_API + '/user/login/'

    # Sel query string
    login_str = '?username=%s&password=%s' % (user['username'], user['password'])

    # Set headers
    headers = {'Content-Type': 'application/json'}

    # Send GET request
    response = requests.get(url + login_str, headers=headers)
    sessionId = re.search(r'\d+', str(response.content)).group(0)
    return response


def pet_shop_logout(connector=requests):
    """
        Logout current user
        """

    # Set URL
    url = const.BASIC_API + '/user/logout/'

    # Send GET request
    response = requests.get(url)
    return response
