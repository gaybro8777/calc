from social.backends.open_id import OpenIdConnectAuth

from hourglass.settings import (
    UAA_OAUTH_AUTH_URL, UAA_OAUTH_CALLBACK_URL
)


class UAAOpenId(OpenIdConnectAuth):
    """UAA OpenID Connect authentication backend"""

    name = 'uaa'
    REDIRECT_STATE = False

    AUTHORIZATION_URL = UAA_OAUTH_AUTH_URL

    # Override get_redirect_uri to return
    # the config value UAA_OAUTH_CALLBACK_URL
    # TODO: It seems like I shouldn't have to do this, but
    # I can't find any documentation on how to better accomplish this
    def get_redirect_uri(self, state):
        return UAA_OAUTH_CALLBACK_URL
