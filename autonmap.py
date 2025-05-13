import nmap
import time
from datetime import datetime

def сканировать_порт(хост, порт):
    """Сканирует один порт на хосте."""
    сканер = nmap.PortScanner()
    try:
        результат = сканер.scan(hosts=хост, ports=str(порт), arguments='-v -sS')
        return результат['scan'][хост]['tcp'][порт]['state']
    except Exception as e:
        return f"❌ Ошибка: {str(e)}"

def сканировать_хост(хост, порты='1-1024'):
    """Сканирует диапазон портов на хосте."""
    сканер = nmap.PortScanner()
    try:
        print(f"🔍 Сканирую {хост} (порты {порты})...")
        start_time = time.time()
        сканер.scan(hosts=хост, ports=порты, arguments='-v -sS')
        elapsed = time.time() - start_time
        
        print(f"\n🎯 Результаты сканирования {хост}:")
        for proto in сканер[хост].all_protocols():
            print(f"📡 Протокол: {proto}")
            ports = сканер[хост][proto].keys()
            for port in ports:
                state = сканер[хост][proto][port]['state']
                print(f"  Порт {port}: {state}")
        
        print(f"\n⏱ Время выполнения: {elapsed:.2f} сек.")
    except Exception as e:
        print(f"💢 Ошибка: {str(e)}")

def главное_меню():
    """Основное меню программы."""
    print("🎌 Добро пожаловать в Ниндзя-Сканер 3000")
    print(f"📅 Сегодня: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        print("\n⚔️ Выбери действие:")
        print("1. Сканировать один порт")
        print("2. Сканировать диапазон портов")
        print("3. Выйти")
        
        выбор = input("> ")
        
        if выбор == "1":
            хост = input("Введи IP или домен: ")
            порт = input("Введи порт: ")
            print(f"\n🔎 Статус порта {порт}: {сканировать_порт(хост, int(порт))}")
        
        elif выбор == "2":
            хост = input("Введи IP или домен: ")
            порты = input("Введи диапазон портов (например, 1-1000): ")
            сканировать_хост(хост, порты)
        
        elif выбор == "3":
            print("🌌 Сканер возвращается в тень...")
            break
        
        else:
            print("💢 Неверный выбор!")

if __name__ == "__main__":
    главное_меню()