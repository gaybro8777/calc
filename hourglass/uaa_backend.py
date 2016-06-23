from social.backends.open_id import OpenIdConnectAuth, OpenIdConnectAssociation
from social.utils import handle_http_errors

from hourglass.settings import (
    UAA_OAUTH_AUTH_URL, UAA_OAUTH_TOKEN_URL,
)


class UAAOpenId(OpenIdConnectAuth):
    """UAA OpenID Connect authentication backend"""

    name = 'uaa'
    REDIRECT_STATE = False

    #                                       values when oidc-provider:
    AUTHORIZATION_URL = UAA_OAUTH_AUTH_URL  # 'http://localhost:3000/op/auth'
    ACCESS_TOKEN_URL = UAA_OAUTH_TOKEN_URL  # 'http://localhost:3000/op/token'
    ACCESS_TOKEN_METHOD = 'POST'

    # TODO: Not sure if we need to implement this
    # def user_data(self, access_token, *args, **kwargs):
    #     """Loads user data from somewhere"""
    #     pass

    # TODO: Not sure if we need to implement this
    # def get_user_details(self, response):
    #     return {
    #         'email': 'something',
    #     }

    # @handle_http_errors
    # def auth_complete(self, *args, **kwargs):
    #     """Completes login process, must return user instance"""
    #     state = self.validate_state()
    #
    #     # TODO: problem happens in the backends/oauth.py class here:
    #     # 400 Client Error: Bad Request for url: http://localhost:3000/op/token
    #     # It might be something as simple as having the wrong ACCESS_TOKEN_URL
    #     response = self.request_access_token(
    #         self.access_token_url(),
    #         data=self.auth_complete_params(state),
    #         headers=self.auth_headers(),
    #         auth=self.auth_complete_credentials(),
    #         method=self.ACCESS_TOKEN_METHOD
    #     )
    #     self.process_error(response)
    #     return self.do_auth(response['access_token'], response=response,
    #                         *args, **kwargs)
