# coding=utf-8
# Dungeon -> Tests -> Interface

import pytest
import dungeon.interface as interface

class TestKeywordInput:
    pass


class TestComparisonCheck:
    def test_included(s):
        assert interface.included('KEY', ['KEY', 'OTHERKEY', 'three'])
        assert interface.included('key', ['KEY', 'otherkey', 'THREE'])
        assert interface.included('keY', ['kEy', 'OthERkEY', 'three'])

    def test_not_included(s):
        assert not interface.included('NOKEY', ['KEY', 'OTHERKEY', 'three'])
        assert not interface.included('nokey', ['KEY', 'otherkey', 'THREE'])
        assert not interface.included('NokeY', ['kEy', 'OthERkEY', 'three'])

    def test_scalar_options(s):
        assert interface.included('key', 'KEY')
        assert not interface.included('nokey', 'KEY')
