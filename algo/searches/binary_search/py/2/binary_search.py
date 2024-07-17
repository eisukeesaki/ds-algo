class Binary_Search:
    @staticmethod
    def target_is_in_list(l, tgt):
        first = 0
        last = len(l) - 1
        while first <= last:
            mid = int((last + first) / 2)
            if l[mid] == tgt:
                return True
            elif l[mid] < tgt:
                first = mid + 1
            elif l[mid] > tgt:
                last = mid - 1
        return False

    @staticmethod
    def exists_(l: list[int], tgt: int, first: int, last: int) -> bool:
        # recursive
        if first > last:
            return False
        while first <= last:
            mid = int((first + last) / 2)
            if l[mid] == tgt:
                return True
            elif l[mid] < tgt:
                first = mid + 1
                return Binary_Search.exists_(l, tgt, first, last)
            elif l[mid] > tgt:
                last = mid - 1
                return Binary_Search.exists_(l, tgt, first, last)

    @staticmethod
    def get_index_of_target(l: list[int], tgt: int) -> int:
        """
        Returns:
            - index of the search target
            - -1 to indicate not found
        """
        first = 0
        last = len(l) - 1
        while first <= last:
            mid = int((first + last) / 2)
            if l[mid] == tgt:
                return mid
            elif l[mid] < tgt:
                first = mid + 1
            elif l[mid] > tgt:
                last = mid - 1
        return -1

scope = [10, 20, 30, 40, 50]
target = 100

# print(Benary_Search.target_is_in_list(scope, target))

# print(Benary_Search.get_index_of_target(scope, target))

print(Binary_Search.exists_(scope, target, first=0, last=len(scope) - 1))

