def amdahl_law(p, n):
    """
    Amdahl Yasası'nı hesaplar.

     p: Paralelleştirilebilen kısmın oranı (0 ile 1 arasında)
    n: İşlemci veya paralel iş parçacığı sayısı
    :return: Hızlanma oranı (speedup)
    """
    if not (0 <= p <= 1):
        raise ValueError("'p' (paralelleştirilebilir oran) 0 ile 1 arasında olmalıdır.")
    if n <= 0:
        raise ValueError("'n' (işlemci sayısı) pozitif bir değer olmalıdır.")

    speedup = 1 / ((1 - p) + (p / n))
    return speedup

def main():
    print("Amdahl Yasası Hızlanma Hesaplayıcı")
    try:
        p = float(input("Paralelleştirilebilen kısmın oranını (0 ile 1 arasında) girin: "))
        n = int(input("İşlemci veya paralel iş parçacığı sayısını girin: "))

        speedup = amdahl_law(p, n)
        print(f"Hızlanma oranı: {speedup:.2f}")
    except ValueError as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()
