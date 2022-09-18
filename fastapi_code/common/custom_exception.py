# class CustomException(Exception):
#     """
#     继承基础类
#     """
#     def __int__(self, error_info):
#         super().__init__()
#         self.error_info = error_info
#
#     def __str__(self):
#         return self.error_info
#
#
# class CustomValueError(ValueError):
#     def __int__(self, error_info):
#         super().__init__()
#         print(error_info)
#         self.error_info = error_info
#
#     def __str__(self):
#         print(self.error_info)
#         return str(self.error_info)
