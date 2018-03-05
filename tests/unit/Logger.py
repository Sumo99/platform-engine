# -*- coding: utf-8 -*-
from asyncy.Logger import Logger

from frustum import Frustum

from pytest import fixture


@fixture
def logger(patch, config):
    patch.object(Frustum, '__init__', return_value=None)
    return Logger(config)


def test_logger_init(logger, config):
    name = config.logger_name
    level = config.logger_level
    Frustum.__init__.assert_called_with(name, level)


def test_logger_events_github_autherr(logger):
    message = 'Github authentication for app {} and installation {} failed'
    assert logger.events[0] == ('github-autherr', 'error', message)


def test_logger_events_container_start(logger):
    message = 'Container {} is running'
    assert logger.events[1] == ('container-start', 'info', message)


def test_logger_events_container_end(logger):
    message = 'Container {} has finished'
    assert logger.events[2] == ('container-end', 'info', message)


def test_logger_events_story_start(logger):
    message = 'Start processing story "{}" for app {} with id {}'
    assert logger.events[3] == ('story-start', 'info', message)


def test_logger_events_story_save(logger):
    message = 'Saved results of story "{}" for app {}'
    assert logger.events[4] == ('story-save', 'info', message)


def test_logger_events_story_end(logger):
    message = 'Finished processing story "{}" for app {} with id {}'
    assert logger.events[5] == ('story-end', 'info', message)


def test_logger_events_task_received(logger):
    message = 'Received task for app {} with story "{}"'
    assert logger.events[6] == ('task-received', 'info', message)


def test_logger_events_container_volume(logger):
    message = 'Created volume {}'
    assert logger.events[7] == ('container-volume', 'debug', message)


def test_logger_events_container_environment(logger):
    message = 'Made environment "{}"'
    assert logger.events[8] == ('container-environment', 'debug', message)


def test_logger_events_jwt_token(logger):
    assert logger.events[9] == ('jwt-token', 'debug', 'Encoded token: {}')


def test_logger_events_story_parse(logger):
    assert logger.events[10] == ('story-parse', 'debug', 'Parsed story {}')


def test_logger_events_story_resolve(logger):
    message = 'Resolved "{}" to "{}"'
    assert logger.events[11] == ('story-resolve', 'debug', message)


def test_logger_start(patch, logger):
    patch.object(Frustum, 'register_event')
    patch.object(Frustum, 'start_logger')
    logger.events = [('event', 'level', 'message')]
    logger.start()
    Frustum.register_event.assert_called_with('event', 'level', 'message')
    Frustum.start_logger.assert_called_with()


def test_logger_log(patch, logger):
    patch.object(Frustum, 'log')
    logger.log('my-event')
    Frustum.log.assert_called_with('my-event')


def test_logger_log_args(patch, logger):
    patch.object(Frustum, 'log')
    logger.log('my-event', 'extra', 'args')
    Frustum.log.assert_called_with('my-event', 'extra', 'args')