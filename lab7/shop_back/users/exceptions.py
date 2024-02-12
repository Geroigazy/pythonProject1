from rest_framework.exceptions import APIException
from rest_framework import status

class UserNotFounded(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'username does not exists'
    default_code = 'username_not_founded'

    
class InvalidCrededntials(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'username or password are incorrect'
    default_code = 'invalid_credentials'
    