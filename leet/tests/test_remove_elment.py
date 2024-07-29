from leet.scripts.remove_element import Solution

SOL = Solution()
def test_remove_elemnt():

    k,nums = SOL.removeElement([3,2,2,1,3],3)
    assert k == 3
    assert 3 not in nums

def test_remove_dups():
    k = SOL.removeDuplicates([1,1,2])
    assert k == 2