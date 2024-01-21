#!/usr/bin/env python3

def calculate_automatization(minutes_to_automate, minutes_to_perform, amount_of_time_done):
    print(f'Minutos que llevaria la automatización => [{minutes_to_automate}]')
    print(f'El proceso normal tarda => [{minutes_to_perform}] minutos, se ejecuta semanalmente => [{amount_of_time_done}] veces, semanalmente tadas las ejecuciones tardarian => [{minutes_to_perform * amount_of_time_done}] minutos')
    print(f'Tiempo automatizacion [{minutes_to_automate}] / Tiempo ejecucion semanal [{amount_of_time_done}] => No. Semanas [{minutes_to_automate / minutes_to_perform}]')
    if [minutes_to_automate < (minutes_to_perform * amount_of_time_done)]:        
        return "Vale la pena automatizar el proceso"
    else:
        return "No vale la pena automatizar el proceso"
    
print(calculate_automatization(40*60, 10, 1))
