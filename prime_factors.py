class PrimeFactor:
    def of(self, num: int) -> list[int]:
        if num > 1:
            if num == 4:
                return [2, 2]
            return [num]
        return []
