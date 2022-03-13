import numpy as np

def outliers_iqr_mod(data, feature, left=1.5, right=1.5, log_scale=False) -> tuple:
    """
    Давайте немного модифицируем нашу функцию outliers_iqr(). 
    Добавьте в нее параметры left и right, которые задают число IQR влево и вправо от границ ящика 
    (пусть по умолчанию они равны 1.5).
    Функция, как и раньше должна возвращать потенциальные выбросы и очищенный DataFrame.
    """
    if log_scale:
        x = np.log(data[feature])
    else:
        x = data[feature]
    quartile1, quartile3 = x.quantile(0.25), x.quantile(0.75)
    # IQR = Q3 - Q1
    iqr = quartile3 - quartile1
    
    # b_lower = Q1 - 1.5IQR
    # b_upper = Q3 + 1.5IQR
    lower_bound = quartile1 - (left*iqr)
    upper_bound = quartile3 + (right*iqr)
    
    # Формируем очищенный df и df с выбросами
    outliers = data[(x<lower_bound) | (x>upper_bound)]
    cleaned = data[(x>lower_bound) & (x<upper_bound)]

    return outliers, cleaned

def outliers_z_score_mod(data, feature, log_scale=False, left=3, right=3) -> tuple:
    """
    Давайте расширим правило 3ех сигм, чтобы иметь возможность учитывать ассиметричность данных.
    Добавьте в функцию outliers_z_score() параметры left и right, которые будут задавать число сигм (стандартных отклонений) 
    влево и вправо соответственно, которые определяют границы метода z-отклонения. 
    По умолчанию оба параметры равны 3
    """
    
    if log_scale:
        x = np.log(data[feature])
    else:
        x = data[feature]
    # Вычислить мат ожидание и СО
    mu = x.mean() 
    sigma = x.std()
    
    # Вычислить границы
    low_b = mu - (left*sigma)
    high_b = mu + (right*sigma)
    
    # Найти значения в заданных диапазонах
    out = data[(x<low_b) | (x>high_b)]
    cln = data[(x>low_b) & (x<high_b)] 
    
    return out, cln 