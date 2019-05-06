# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return sorted(A) == A or sorted(A,reverse=True) == A