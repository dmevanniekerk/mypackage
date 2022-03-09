from mypackage import myModule

def test_top_n():
    """
    This function is created with the intention to:
        make sure the function top_n works as intended
        give a few test cases with answers
        make sure (assert) the validity of the function
    """

    assert myModule.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert myModule.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myModule.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'
