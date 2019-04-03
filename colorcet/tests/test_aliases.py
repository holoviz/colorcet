import pytest  # noqa
import colorcet as cc

def test_get_aliases():
    expected = ['kbc,  linear_blue_5_95_c73,  CET_L6,  linear_kbc_5_95_c73',
                'kbc,  CET_L6,  linear_blue_5_95_c73,  linear_kbc_5_95_c73']
    assert cc.get_aliases('kbc') in expected
    assert cc.get_aliases('linear_blue_5_95_c73') in expected
    assert cc.get_aliases('CET_L6') in expected
    assert cc.get_aliases('linear_kbc_5_95_c73') in expected

def test_all_original_names():
    assert len(cc.all_original_names()) == 79

def test_all_original_names_only_aliased():
    assert len(cc.all_original_names(only_aliased=True)) == 28

def test_all_original_names_nopic():
    assert len(cc.all_original_names(group='nopic')) == 10

def test_all_original_names_not_glasbey():
    assert len(cc.all_original_names(not_group='glasbey')) == 71

def test_all_original_names_nopic_and_only_aliased():
    assert len(cc.all_original_names(group='nopic', only_aliased=True)) == 2
