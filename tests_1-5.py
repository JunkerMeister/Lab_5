import pytest
import zd1, zd2, zd3, zd4, ZD5

@pytest.mark.parametrize('str, expected_result', [('спорстмен спор спорт', 'спор'),
                                                  ('sadas sdfg fee', ''),
                                                  ('ff спор спорт', '')])
def test_for_zd1_max_prefix(str, expected_result):
    assert zd1.max_prefix(str.split()) == expected_result

@pytest.mark.parametrize('a, b, ans', [([106, 182, 278, 333, 333, 432, 591, 595, 895, 922], [106, 333, 922, 591, 333, 595, 432, 895, 182], 278),
                                      ([111, 143, 407, 420, 504, 589, 760, 788, 867, 991], [111, 867, 407, 760, 589, 420, 991, 788, 504], 143)])
def test_for_zd2_rand_list(a, b, ans):
    assert zd2.rand_list(a, b) == ans


@pytest.mark.parametrize('x, res', [('MDCXI', 1611),
                                    ('IMD', 1499),
                                    ('LXV', 65)])
def test_for_zd3_roman_to_arabic(x, res):
    assert zd3.roman_to_arabic(x) == res


@pytest.mark.parametrize('s, bool', [('череп переч', True),
                                    ('sadas sdfg', False)])
def test_for_zd4_t_or_f(s, bool):
    assert zd4.t_or_f(s.split()) == bool

@pytest.mark.parametrize('number, result', [(3, 2),
                                    (56, 225851433717),
                                    (656, 55770816383141016535164708206647562140783249332538645580921636439479656844023258024264103536233305161016374523542751829753465427753697280)])
def test_for_ZD_5_fibonaci(number, result):
    assert ZD5.fibonaci(number) == result