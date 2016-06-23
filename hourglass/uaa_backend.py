from social.backends.open_id import OpenIdConnectAuth
from social.utils import handle_http_errors

from hourglass.settings import (
    UAA_OAUTH_AUTH_URL, UAA_OAUTH_TOKEN_URL,  # UAA_OAUTH_CALLBACK_URL
)


class UAAOpenId(OpenIdConnectAuth):
    """UAA OpenID Connect authentication backend"""

    name = 'uaa'
    REDIRECT_STATE = False

    #                                       values when oidc-provider:
    AUTHORIZATION_URL = UAA_OAUTH_AUTH_URL  # 'http://localhost:3000/op/auth'
    ACCESS_TOKEN_URL = UAA_OAUTH_TOKEN_URL  # 'http://localhost:3000/op/token'
    ACCESS_TOKEN_METHOD = 'POST'

    # Override get_redirect_uri to return
    # the config value UAA_OAUTH_CALLBACK_URL
    # TODO: It seems like I shouldn't have to do this, but
    # I can't find any documentation on how to better accomplish this
    # def get_redirect_uri(self, state):
    #     return UAA_OAUTH_CALLBACK_URL

    # TODO: Not sure if we need to implement this
    # def user_data(self, access_token, *args, **kwargs):
    #     """Loads user data from somewhere"""
    #     pass

    # TODO: Not sure if we need to implement this
    # def get_user_details(self, response):
    #     print("-----------------------------")
    #     print(response)
    #     return {
    #         'email': 'whatever',
    #     }

    # TODO: This needs to be implemented
    # but it currently does not work
    # saving the association model is failing
    # https://github.com/omab/python-social-auth/blob/master/social/backends/open_id.py#L263
    @handle_http_errors
    def auth_complete(self, *args, **kwargs):
        self.process_error(self.data)
        response = self.request_access_token(
            self.ACCESS_TOKEN_URL,
            data=self.auth_complete_params(),
            headers=self.auth_headers(),
            method=self.ACCESS_TOKEN_METHOD
        )
        self.process_error(reponse)
        return self.do_auth(response['access_token'],
                            response=response,
                            *args, **kwargs)
