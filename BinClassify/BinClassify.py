from typing import Any
import math


class BinClassifyError(Exception):
    pass


class BinClassify:
    def __init__(self) -> None:
        self.val: bool = True
        self.varQuestion: int = 0

    def __valid_type(self, var: Any, var_type: type) -> None:
        if type(var) != var_type:
            raise TypeError(
                f"must be real {var_type.__name__} , not {type(var).__name__}"
            )

    def __valid_min(self, number: int, min_number: int) -> None:
        if number < min_number:
            raise ValueError(f"The number must be greater than {min_number}")

    def CoutGroups(self, nqustion: int) -> list:
        self.__valid_type(nqustion, int)
        self.__valid_min(nqustion, 1)
        if nqustion == 1:
            return [2, 2]
        else:
            nmin: int = 2 ** (nqustion - 1) + 1
            nmax: int = 2**nqustion
            return [nmin, nmax]

    def CoutQustion(self, number: int) -> int:
        self.__valid_type(number, int)
        self.__valid_min(number, 2)
        self.varHigh: int = number
        self.varQuestion = math.ceil(math.log(number, 2))
        self.val = False
        return self.varQuestion

    def Answer(self, arr: list) -> int:
        self.__valid_type(arr, list)
        if self.val:
            raise BinClassifyError("First you need to use the method CoutQustion")
        if len(arr) != self.varQuestion:
            raise ValueError(
                "The number of elements in the array does not match "
                + "the returned number of the CoutQustion method."
            )
        low: int = 1
        high: int = self.varHigh
        for i in arr:
            mid: int = (low + high) // 2
            if i == 0:
                high = mid
            elif i == 1:
                low = mid
            else:
                ValueError("One of the array elements is not binary (not 1, not 0)")
        return high