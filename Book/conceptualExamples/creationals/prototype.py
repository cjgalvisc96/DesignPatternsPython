from typing import List
import copy


class SelfReferecingEntity:
    def __init__(self) -> None:
        self.parent = None

    def set_parent(self, *, parent) -> None:
        self.parent = parent


class SomeComponent:
    def __init__(
        self, *, some_int: int, some_list_of_objects: List, some_circular_ref
    ) -> None:
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self) -> object:
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(
            some_int=self.some_int,
            some_list_of_objects=some_list_of_objects,
            some_circular_ref=some_circular_ref,
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, *, memo={}) -> object:
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        new = self.__class__(
            some_int=self.some_int,
            some_list_of_objects=some_list_of_objects,
            some_circular_ref=some_circular_ref,
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new
