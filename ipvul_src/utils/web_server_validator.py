from urllib3.exceptions import HTTPError
from requests.exceptions import ConnectionError, TooManyRedirects
from ipvul_src.utils.request_handler import RequestHandler
from ipvul_src.utils.singleton import Singleton
from ipvul_src.utils.exceptions import WebServerValidatorException, RequestHandlerException


class WebServerValidator(metaclass=Singleton):

    def __init__(self):
        self.request_handler = RequestHandler()

    def validate_target_webserver(self, host):
        try:
            self.request_handler.send(
                "GET",
                timeout=20,
                url="{}://{}:{}".format(
                    host.protocol,
                    host.target,
                    host.port
                )
            )
            return True
        except RequestHandlerException:
            raise WebServerValidatorException
