import pytest
import zd1, zd2
#zd3, zd4, ZD5

@pytest.mark.parametrize('str, expected_result', [('спорстмен спор спорт', 'спор'),
                                                  ('fff dgdsadf aaaa', ''),
                                                  ('ff спор спорт', '')])
def test_for_zd1_max_prefix(str, expected_result):
    assert zd1.max_prefix(str.split()) == expected_result

@pytest.mark.parametrize('a, b, ans', [([106, 182, 278, 333, 333, 432, 591, 595, 895, 922], [106, 333, 922, 591, 333, 595, 432, 895, 182], 278),
                                                   ([111, 143, 407, 420, 504, 589, 760, 788, 867, 991], [111, 867, 407, 760, 589, 420, 991, 788, 504], 143)])
def test_for_zd2_rand_list(a, b, ans):
    assert zd2.rand_list(a, b) == ans