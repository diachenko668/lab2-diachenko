"""Консольный анализатор чисел для лабораторной работы по Git."""

import argparse


def calculate_stats(numbers: list[float]) -> dict[str, float | int]:
    """Вычислить количество, сумму и среднее арифметическое чисел."""
    return {
        "count": len(numbers),
        "total": sum(numbers),
        "average": sum(numbers) / len(numbers),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Анализатор чисел")
    parser.add_argument("numbers", type=float, nargs="+", help="Числа для анализа")
    args = parser.parse_args()
    result = calculate_stats(args.numbers)
    print(f"Количество: {result['count']}")
    print(f"Сумма: {result['total']:g}")
    print(f"Среднее: {result['average']:g}")


if __name__ == "__main__":
    main()
