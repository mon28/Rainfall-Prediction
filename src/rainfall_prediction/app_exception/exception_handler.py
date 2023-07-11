import os
import sys


class AppException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = AppException.error_message_detail(error_message, error_detail)


    @staticmethod
    def error_message_detail(error: Exception, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename

        error_message = f"Error occurred at [{filename}]" \
                        f" line number [{exc_tb.tb_lineno}] error message [{error}]"
        
        return error_message
    
    def __repr__(self):
        return AppException.__name__.str()
    
    
    def __str__(self):
        return self.error_message