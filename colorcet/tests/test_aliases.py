import pytest  # noqa
import colorcet as cc

def test_get_aliases():
    names = {'kbc', 'linear_blue_5_95_c73', 'CET_L6', 'linear_kbc_5_95_c73'}
    assert set(cc.get_aliases('kbc').split(",  ")) == names
    assert set(cc.get_aliases('linear_blue_5_95_c73').split(",  ")) == names
    assert set(cc.get_aliases('CET_L6').split(",  ")) == names
    assert set(cc.get_aliases('linear_kbc_5_95_c73').split(",  ")) == names

def test_all_original_names():
    assert len(cc.all_original_names()) == 98

def test_all_original_names_only_aliased():
    assert len(cc.all_original_names(only_aliased=True)) == 48

def test_all_original_names_nopic():
    assert len(cc.all_original_names(group='nopic')) == 15

def test_all_original_names_not_glasbey():
    assert len(cc.all_original_names(not_group='glasbey')) == 90

def test_all_original_names_nopic_and_only_aliased():
    assert len(cc.all_original_names(group='nopic', only_aliased=True)) == 2
