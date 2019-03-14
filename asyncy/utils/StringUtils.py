# -*- coding: utf-8 -*-


class StringUtils:
    @staticmethod
    def contains(string,pattern):
        pass
    @staticmethod
    def truncate(result, max_bytes: int):
        str_bytes = str(result).encode('utf-8', 'ignore')
        str_bytes_len = len(str_bytes)

        if str_bytes_len > max_bytes:
            truncated_len = str_bytes_len - max_bytes
            str_for_logging = str_bytes[:max_bytes] \
                .decode('utf-8', 'ignore')
            result = f'{str_for_logging} ... ' \
                     f'({truncated_len} bytes truncated)'

        return result
