def checkio(text):




if __name__ == '__main__':    
    print(checkio("$1.234.567,89"))
    print(checkio("$0,89"))
    print(checkio("Euro Style = $12.345,67, US Style = $12,345.67"))
    print(checkio("Us Style = $12,345.67, Euro Style = $12.345,67"))
    print(checkio("$1.234, $5.678 and $9"))
