import argparse
import csv
from statistics import median
from tabulate import tabulate

def read_all_files(file_paths):
    """Читает все CSV файлы"""
    all_rows = []
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, skipinitialspace=True)
                next(reader)
                
                for row in reader:
                    if row:
                        all_rows.append(row)
        except FileNotFoundError:
            print(f"Ошибка: Файл {file_path} не найден")
            return None
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
    
    return all_rows

def calculate_median_coffee(data):
    """Считает медиану трат на кофе"""
    student_spends = {}
    
    for row in data:
        name = row[0]
        coffee = float(row[2])
        
        if name not in student_spends:
            student_spends[name] = []
        
        student_spends[name].append(coffee)
    
    result = []
    for name, spends in student_spends.items():
        med = median(spends)
        result.append([name, round(med, 2)])
    
    
    result.sort(key=lambda x: x[1], reverse=True)
    
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--report', required=True)
    
    args = parser.parse_args()
    
    if args.report != 'median-coffee':
        print("Поддерживается только отчет median-coffee")
        return
    
    print("Читаю файлы:", args.files)
    data = read_all_files(args.files)
    
    if data is None or not data:
        print("Нет данных")
        return
    
    result = calculate_median_coffee(data)
    
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ:")
    print("="*50)
    print(tabulate(result, 
                   headers=['Студент', 'Медиана трат'],
                   tablefmt='grid',
                   floatfmt='.2f'))

if __name__ == '__main__':
    main()
