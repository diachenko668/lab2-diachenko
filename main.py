"""Консольный анализатор чисел для лабораторной работы по Git."""

import argparse
import math


def calculate_stats(numbers: list[float]) -> dict[str, float | int]:
    """Вычислить количество, сумму и среднее арифметическое чисел."""
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")
    if not all(math.isfinite(number) for number in numbers):
        raise ValueError("Все числа должны быть конечными")
    total = sum(numbers)
    if not math.isfinite(total):
        raise ValueError("Сумма чисел должна быть конечной")
    return {
        "count": len(numbers),
        "total": total,
        "average": total / len(numbers),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Анализатор чисел")
    parser.add_argument("numbers", type=float, nargs="+", help="Числа для анализа")
    args = parser.parse_args()
    try:
        result = calculate_stats(args.numbers)
    except ValueError as error:
        parser.error(str(error))
    print(f"Количество: {result['count']}")
    print(f"Сумма: {result['total']:g}")
    print(f"Среднее: {result['average']:g}")


if __name__ == "__main__":
    main()
