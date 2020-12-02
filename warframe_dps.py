print("\t\t\t\t\t\tПрограмма создана FiLLPeep и vladikar98")
print("\t\t\t\t\t\tДонат (Яндекс Деньги): 4100110262330929")

dmg_hit = float(input("Введите урон ударом: "))
dmg_piercing = float(input("Введите урон пронзанием: "))
dmg_cut = float(input("Введите урон разрезом: "))
dmg_status = float(input("Введите урон статуса: "))

crit_mult = float(input("Введите множитель крита: "))
speed_shot = float(input("Введите скорострельность(скорость атаки): "))

multi_shot = float(input("Введите мультивыстрел(если оружие ближнего боя, то 1): "))
multi_combo = int(input("Введите множитель комбо ((оружие ближнего боя), если нет, то 1): "))

dmg = dmg_hit + dmg_piercing + dmg_cut

if 1 <= multi_combo <= 12:
    def weeping_wounds(combo: int):
        """Стенающие раны"""
        res = (combo - 1) * 40
        percent = res / 100
        
        return res, percent

    def blood_rush(combo: int):
        """Приток крови"""
        res = (combo - 1) * 60
        percent = res / 100
        
        return res, percent

    melee_weapon_set = int(input("Это оружие ближнего боя? 0-нет, 1-да: "))
    
    if melee_weapon_set == 1:
        blood_rush_set = int(input("Установлен ли фулл Приток крови? 0-нет, 1-да: "))
        
        if blood_rush_set == 1:
            crit_new, percent = blood_rush(multi_combo)
            crit_mult += percent
            
            max_dmg = (dmg + dmg_status) * crit_mult * multi_shot * speed_shot
            aver_dmg = (dmg + max_dmg) / 2
            
            print(f"Крит увеличен на {crit_new}%")
            
            weeping_wounds_set = int(input("Установлен ли фулл Стенающие раны? 0-нет, 1-да: "))
            
            if weeping_wounds_set == 1:
                status_new, status_new_percent = weeping_wounds(multi_combo)
                dmg_status += status_new_percent
                
                max_dmg = (dmg + dmg_status) * crit_mult * multi_shot * speed_shot
                aver_dmg=(dmg+max_dmg)/2
                
                print(f"Статус увеличен на {status_new}%")
                print(f'Минимальный DPS: {dmg}\nСредний DPS: {aver_dmg}\nМаксимальный DPS: {max_dmg}')

            elif weeping_wounds_set==0: #Вопрос о Стенающих ранах
                max_dmg=(dmg+dmg_status)*crit_mult*multi_shot*speed_shot # Рассчёт максимального DPS
                aver_dmg=(dmg+max_dmg)/2  # Рассчёт среднего DPS
                print(f'Минимальный DPS: {dmg}\nСредний DPS: {aver_dmg}\nМаксимальный DPS: {max_dmg}')

            else: #Вопрос о Стенающих ранах
                print("Введены неверные данные")

        elif k==0: #Вопрос о Притоке крови
            weeping_wounds_set=int(input("Установлен ли фулл Стенающие раны? 0-нет, 1-да: "))

            if weeping_wounds_set==1: #Вопрос о Стенающих ранах

                p=weeping_wounds(multi_combo) #Формула увеличения статуса
                status_new_percent=stat (p) # Возвращает формулу выделения целой части статуса
                dmg_status=dmg_status+status_new_percent # Часть с магией где он должен убрать строчку с шансом и написать сразу с увеличенным множителем
                max_dmg=(dmg+dmg_status)*crit_mult*multi_shot*speed_shot # Рассчёт максимального DPS
                aver_dmg=(dmg+max_dmg)/2  # Рассчёт среднего DPS

                print(f"Статус увеличен на {p}%")
                print(f'Минимальный DPS: {dmg}\nСредний DPS: {aver_dmg}\nМаксимальный DPS: {max_dmg}')

            elif weeping_wounds_set==0: #Вопрос о Стенающих ранах
                max_dmg=(dmg+dmg_status)*crit_mult*multi_shot*speed_shot # Рассчёт максимального DPS
                aver_dmg=(dmg+max_dmg)/2  # Рассчёт среднего DPS
                print(f'Минимальный DPS: {dmg}\nСредний DPS: {aver_dmg}\nМаксимальный DPS: {max_dmg}')

            else: #Вопрос о Стенающих ранах
                print("Введены неверные данные")

        else: #Вопрос о Притоке крови
            print("Введены неверные данные")

    else:
        max_dmg=(dmg+dmg_status)*crit_mult*multi_shot*speed_shot # Рассчёт максимального DPS
        aver_dmg=(dmg+max_dmg)/2  # Рассчёт среднего DPS
        print(f'Минимальный DPS: {dmg}\nСредний DPS: {aver_dmg}\nМаксимальный DPS: {max_dmg}')

else: #Вопрос о множителе комбо
    print("Комбо не может быть больше 12 и меньше 1")
