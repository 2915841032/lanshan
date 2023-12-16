# -*- coding: utf-8 -*-
# @File : 46.dataclass的使用.py
# @Author : 阿波
# @Time : 2023/9/9 23:16
# @Software: PyCharm
class InventoryItem:
    '''本类用于记录仓库中的一件物品.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def __init__(
            self,
            name: str,
            unit_price: float,
            quantity_on_hand: int = 0
    ) -> None:
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

    def __repr__(self) -> str:
        return (
            'InventoryItem('
            f'name={self.name!r}, unit_price={self.unit_price!r}, '
            f'quantity_on_hand={self.quantity_on_hand!r})')

    def __hash__(self) -> int:
        return hash((self.name, self.unit_price, self.quantity_on_hand))

    def __eq__(self, other) -> bool:
        if not isinstance(other, InventoryItem):
            return NotImplemented
        return (
                (self.name, self.unit_price, self.quantity_on_hand) ==
                (other.name, other.unit_price, other.quantity_on_hand))


inv = InventoryItem('麦叔的书', 38.8, 10)
inv2 = InventoryItem('麦叔的书', 38.8, 10)
print(inv)
print(inv == inv2)
# ?===========================================================================
from dataclasses import dataclass


@dataclass(unsafe_hash=False)
class InventoryItem2:
    '''本类用于记录仓库中的一件物品.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


inv3 = InventoryItem2('麦叔的书', 8.8, 10)
inv4 = InventoryItem2('麦叔的书', 8.8, 10)
print(inv3)
print(inv3 == inv4)