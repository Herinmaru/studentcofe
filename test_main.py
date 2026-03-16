import pytest
import tempfile
import os
import csv
from main import calculate_median_coffee, read_all_files

def test_calculate_median():
    test_data = [
        ['Иван', 'дата', '500', '...'],
        ['Иван', 'дата', '600', '...'],
        ['Мария', 'дата', '200', '...'],
        ['Мария', 'дата', '300', '...'],
    ]
    
    result = calculate_median_coffee(test_data)
    
    assert len(result) == 2
    assert result[0][0] == 'Иван'  
    assert result[0][1] == 550.0    
    assert result[1][1] == 250.0   
def test_read_files():
    fd, path = tempfile.mkstemp(suffix='.csv', text=True)
    
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write("name,date,coffee\n")
            f.write("Иван,2024-01-01,500\n")
            f.write("Мария,2024-01-01,200\n")
        
        data = read_all_files([path])
        assert len(data) == 2
        assert data[0][0] == 'Иван'
        assert float(data[0][2]) == 500.0
    finally:
        os.unlink(path)

if __name__ == '__main__':
    pytest.main([__file__])
