class StringCalculator:
    def add(self, numbers_str: str) -> int:
        if not numbers_str:
            return 0

        # Refactored for cleaner sum calculation
        parts = numbers_str.split(',')
        return sum(int(part) for part in parts)