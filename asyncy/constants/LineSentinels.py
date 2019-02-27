# -*- coding: utf-8 -*-


_ALL_SENTINELS = set()
"""
Collection of all sentinels. Handy when trying to know if a result
is a sentinel or not.
"""


class _Sentinel:
    def __init__(self, keyword):
        self.keyword = keyword
        _ALL_SENTINELS.add(self)

    def __str__(self):
        return f'_Sentinel#{self.keyword}'


class LineSentinels:
    """
    A collection for all sentinels, which are used as special line numbers
    during the execution of certain constructs, such as foreach, return, etc.

    How sentinels are used:
    During the flow of execution, they will almost always break
    the normal flow of execution in some manner. For example,
    Lexicon.for_loop calls Story.execute_block in order to execute the same
    block multiple times. When Story.execute_block returns the BREAK
    sentinel, Lexicon.for_loop knows that it's time to stop looping.

    Sentinels are used to control the flow of execution. The other approach
    was to start throwing exceptions during execution, but that is a horrible,
    horrible idea because:
    1. Incurs a runtime performance hit
    2. It's an exception, which is not what it was designed to do
    """
    BREAK = _Sentinel('break')
    RETURN = _Sentinel('return')

    @staticmethod
    def is_sentinel(result):
        return result in _ALL_SENTINELS

    @staticmethod
    def is_not_sentinel(result):
        return not LineSentinels.is_sentinel(result)
