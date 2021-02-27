import pytest  # noqa
import colorcet as cc

def test_get_aliases():
    expected = {'kbc', 'linear_blue_5_95_c73', 'linear_kbc_5_95_c73'}
    assert set(cc.get_aliases('kbc').split(",  ")) == expected
    assert set(cc.get_aliases('linear_blue_5_95_c73').split(",  ")) == expected
    assert set(cc.get_aliases('linear_kbc_5_95_c73').split(",  ")) == expected

def test_all_original_names():
    assert len(cc.all_original_names()) == 107

def test_all_original_names_only_aliased():
    assert len(cc.all_original_names(only_aliased=True)) == 28

def test_all_original_names_nopic():
    assert len(cc.all_original_names(group='nopic')) == 10

def test_all_original_names_not_glasbey():
    assert len(cc.all_original_names(not_group='glasbey')) == 94

def test_all_original_names_nopic_and_only_aliased():
    assert len(cc.all_original_names(group='nopic', only_aliased=True)) == 2
