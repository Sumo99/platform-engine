# -*- coding: utf-8 -*-
from frustum import Frustum

from .Config import Config


class Logger:

    events = [
        ('container-run', 'debug', 'Container {} run'),
        ('jwt-token', 'debug', 'Encoded token: {}'),
        ('story-parse', 'debug', 'Parsed story {}'),
        ('story-resolve', 'debug', 'Resolved {} to {}'),
        ('task-end', 'debug', 'Previous task ended'),
        ('task-start', 'debug', 'Start task for app {} with story {} id: {}'),
    ]

    def __init__(self):
        self.frustum = Frustum(verbosity=Config.get('logger.verbosity'))

    def register(self):
        for event in self.events:
            self.frustum.register_event(event[0], event[1], event[2])

    def log(self, event, *args):
        self.frustum.log(event, *args)