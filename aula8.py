# Exemplo 1
try:
    pass
except Exception as e:
    raise
else:  # Executado se não houver exceção
    pass
finally:  # Executado sempre
    pass

# Exemplo 2
try:
    1/0
except (Exception, ZeroDivisionError) as e:
    print(e)
else:
    print('No exception')
finally:
    print('Finally')
