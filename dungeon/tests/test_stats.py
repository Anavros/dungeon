# coding=utf-8
# Dungeon -> Tests -> Stats

import pytest
import dungeon.stats as stats

class TestTableBuilder:
    def test_defaults(s):
        table = stats.build_table()
        assert len(table.keys()) == 4
        assert table['HP'] == 0
        assert table['PW'] == 0
        assert table['DF'] == 0
        assert table['SP'] == 0

    def test_keyword_args(s):
        table = stats.build_table(5, 10, 5, 0)
        assert len(table.keys()) == 4
        assert table['HP'] == 5
        assert table['PW'] == 10
        assert table['DF'] == 5
        assert table['SP'] == 0

    def test_float_args(s):
        """If given non-integers, try to type cast. This rounds downwards."""
        table = stats.build_table(5.5, 4.4, 3.3, 2.2)
        assert len(table.keys()) == 4
        assert table['HP'] == 5
        assert table['PW'] == 4
        assert table['DF'] == 3
        assert table['SP'] == 2

    def test_string_args(s):
        table = stats.build_table('5', '4', '3', '2')
        assert len(table.keys()) == 4
        assert table['HP'] == 5
        assert table['PW'] == 4
        assert table['DF'] == 3
        assert table['SP'] == 2

    def test_bad_string_args(s):
        """If given arguments that can not be mapped to integers, 
        default to 0."""
        table = stats.build_table('Lots', 'ooo yes gimme that', 'x', 'z')
        assert len(table.keys()) == 4
        assert table['HP'] == 0
        assert table['PW'] == 0
        assert table['DF'] == 0
        assert table['SP'] == 0
        

class TestStacker:
    def test_normal_usage(s):
        base = stats.build_table(100, 10, 20, 20)
        item = stats.build_table(20, -5, 10, -10)
        assert stats.stack(base, item)['HP'] == 120
        assert stats.stack(base, item)['PW'] == 5
        assert stats.stack(base, item)['DF'] == 30
        assert stats.stack(base, item)['SP'] == 10

    def test_multiple_items(s):
        base = stats.build_table(100, 10, 20, 20)
        item = stats.build_table(20, -5, 10, 5)
        armor = stats.build_table(10, 0, 40, -10)
        potion = stats.build_table(120, 10, -5, 0)
        special = stats.build_table(0, 50, 0, 0)
        assert stats.stack(base, item, armor, potion, special)['HP'] == 250
        assert stats.stack(base, item, armor, potion, special)['PW'] == 65
        assert stats.stack(base, item, armor, potion, special)['DF'] == 65
        assert stats.stack(base, item, armor, potion, special)['SP'] == 15

    def test_negative_stack(s):
        base = stats.build_table(100, 10, 20, 5)
        item = stats.build_table(0, 0, 10, -10)
        assert stats.stack(base, item)['SP'] == 0


class TestExtracter:
    def test_normal_usage(s):
        table = stats.build_table(5, 4, 3, 2)
        assert stats.extract(table) == (5, 4, 3, 2)
