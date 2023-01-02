from todoapp.utils.app_exceptions import AppExceptionCase


class ServiceResult:
    def __init__(self, response, status_code):
        """

        :param response:
        :param status_code:
        """
        if isinstance(response, AppExceptionCase):
            self.success = False
            self.exception_case = response.exception_case
            self.status_code = status_code
        else:
            self.success = True
            self.status_code = status_code
        self.value = response

    def __str__(self):
        """

        :return:
        """
        if self.success:
            return "[Success]"
        return f'[Exception] "{self.exception_case}"'

    def __repr__(self):
        """

        :return:
        """
        if self.success:
            return "<ServiceResult Success>"
        return f"<ServiceResult AppException {self.exception_case}>"

    def __enter__(self):
        """

        :return:
        """
        return self.value

    def __exit__(self, *kwargs):
        """

        :param kwargs:
        :return:
        """
        pass
