# -*- coding: utf-8 -*-
from asyncy.processing import Handler, Lexicon

from pytest import fixture


def test_handler_run(patch, logger, story):
    patch.many(story, ['line', 'start_line'])
    Handler.run(logger, '1', story)
    story.line.assert_called_with('1')
    story.start_line.assert_called_with('1')


def test_handler_run_run(patch, logger, story):
    patch.object(Lexicon, 'run')
    patch.object(story, 'line', return_value={'method': 'run'})
    result = Handler.run(logger, '1', story)
    Lexicon.run.assert_called_with(logger, story, story.line())
    assert result == Lexicon.run()


def test_handler_run_set(patch, logger, story):
    patch.object(Lexicon, 'set')
    patch.object(story, 'line', return_value={'method': 'set'})
    result = Handler.run(logger, '1', story)
    Lexicon.set.assert_called_with(logger, story, story.line())
    assert result == Lexicon.set()


def test_handler_run_if(patch, logger, story):
    patch.object(Lexicon, 'if_condition')
    patch.object(story, 'line', return_value={'method': 'if'})
    result = Handler.run(logger, '1', story)
    Lexicon.if_condition.assert_called_with(logger, story, story.line())
    assert result == Lexicon.if_condition()


def test_handler_run_for(patch, logger, story):
    patch.object(Lexicon, 'for_loop')
    patch.object(story, 'line', return_value={'method': 'for'})
    result = Handler.run(logger, 1, story)
    Lexicon.for_loop.assert_called_with(logger, story, story.line())
    assert result == Lexicon.for_loop()
