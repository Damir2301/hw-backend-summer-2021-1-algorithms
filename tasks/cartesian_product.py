from typing import TypeVar

__all__ = ("cartesian_product",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def cartesian_product(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    """Определяет декартово произведение двух списков.

    Example:
        >> cartesian_product([1, 2], [3, 4])
        [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    two_lst = [(i, j) for i in arr1 for j in arr2 if (i, j)]
    return two_lst 
    
    raise NotImplementedError
