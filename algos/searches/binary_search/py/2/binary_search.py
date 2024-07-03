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
target = 40

# print(Binary_Search.target_is_in_list(scope, target))

print(Binary_Search.get_index_of_target(scope, target))
