# -*- coding: utf-8 -*-

"""
- Código protegido por los derechos de autor según el Real Decreto Legislativo 1/1996, de 12 de abril, que aprueba el texto refundido de la Ley de Propiedad Intelectual de España.

- Copyright (©) 2023 [No-Reply]

- Todos los derechos reservados.

- Cualquier redistribución o modificación de este código sin la autorización expresa del autor está prohibida.

- Acorde a la Ley de Propiedad Intelectual, el autor tiene derechos morales (Articulos 14-16) y de explotación (Articulos 17-23) sobre la obra.

- Los derechos morales son inherentes al autor y son inalienables e irrenunciables.

- Los derechos de explotación permiten al autor realizar ciertos actos con respecto a la obra, como reproducirla, distribuirla, comunicarla públicamente y transformarla.

- Por lo tanto, cualquier uso de este código que viole estas prohibiciones estaría infringiendo los derechos de explotación del autor y sería ilegal.

- El autor no se hace responsable de ningún daño o perjuicio que pueda ocasionar por el uso inapropiado de este código.
"""

import sys
import pickle as pk
from colorama import Fore, Back, Style, init; init()
import os
import keyboard as kb
import time as t

class Error(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
        super().__init__(self.mensaje)

def wait_espace():
    
    print("\n" + cyan + "Se acabo, para cerrar el programa, pulse" + reset + green + ":" + reset + " " + blue + "Space" + reset)

    while True:
        stop_program = kb.is_pressed('space')

        if stop_program == True:
            sys.exit()

def re_intento_0():
    re_intento = input(intento_color)

    if re_intento == "Yes" or re_intento == "yes":
        pass
            
    else:
        wait_espace()


end_damage = 0

#def



data_dir = 'Data/'
attacks = 'Attacks/'
levels = 'Levels/'
general_stats = 'General_Stats/'
defenses = 'Defenses/'
resistances = 'Resistances/'
elemental_stats = 'Elemental_Stats/'

os.makedirs(data_dir, exist_ok = True)
os.makedirs(data_dir + attacks, exist_ok = True)
os.makedirs(data_dir + levels, exist_ok = True)
os.makedirs(data_dir + general_stats, exist_ok = True)
os.makedirs(data_dir + defenses, exist_ok = True)
os.makedirs(data_dir + resistances, exist_ok = True)
os.makedirs(data_dir + elemental_stats, exist_ok = True)

white = Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.BLACK
white_red = Style.BRIGHT + Fore.RED + Back.WHITE
red = Style.BRIGHT + Fore.RED + Back.BLACK + Fore.LIGHTRED_EX
cyan = Style.BRIGHT + Fore.GREEN + Back.CYAN
blue = Back.BLUE
green = Style.BRIGHT + Fore.GREEN
reset = Style.RESET_ALL

error_color_0 = "\n" + cyan + "Error" + reset + green + ": " + white + blue
error_color_1 = reset + "\n"

intento_color = cyan + "¿" + reset + blue + "Quieres intentarlo de nuevo" + reset + cyan + "?" + reset + " " + cyan + "(" + reset + blue + "Yes" + reset + cyan + "/" + reset + blue + "No" + reset + cyan + ")" + reset + " " + cyan + "(" + reset + blue + "Cualquier otra respuesta que no sea" + reset + " " + cyan + "'" + reset + blue + "Yes" + reset + cyan + "'" + reset + " " + blue + "o" + reset + " " + cyan + "'" + reset + blue + "yes" + reset + cyan + "'" + reset + " " + blue + "Sera tomada como" + reset + cyan + ":" + reset + " " + blue + "No" + reset + cyan + ".)" + reset + " " + green + "--> " + reset


def list_of_data():

    print("\n")

    with open(data_dir + attacks + 'natural_attack.txt', 'rb') as file:
        print(blue + "Ataque natural --> " + cyan, pk.load(file), reset)

    with open(data_dir + attacks + 'weapon_attack.txt', 'rb') as file:
        print(blue + "Ataque del arma --> " + cyan, pk.load(file), reset)

    with open(data_dir + attacks + 'base_attack.txt', 'rb') as file:
        print(blue + "Ataque base --> " + cyan, pk.load(file), reset)

    with open(data_dir + attacks + 'artifact_attacks_list.txt', 'rb') as file:
        a_a_l = pk.load(file)
        print(blue + "Ataque plano de los artefactos --> " + cyan, a_a_l, "--> " + "[" + str(sum(a_a_l)) + "]" + reset)

    with open(data_dir + attacks + 'artifact_porcentual_attacks_list.txt', 'rb') as file:
        a_p = pk.load(file)

        print(blue + "Ataque porcentual de los artefactos --> " + cyan, end = ""); print(" [", end = "")

        for item_0 in a_p:

            if item_0 == a_p[-1]:
                print(str(item_0) + "%", end = "")
                break

            print(str(item_0) + "%, ", end = "")

        print("] --> ", end = "")

        with open(data_dir + attacks + 'base_attack.txt', 'rb') as file:
            atk_base_0 = pk.load(file)

            print("[", end = "")

            for item_1 in a_p:

                if item_1 == a_p[-1]:
                    print(str(round(((item_1 * atk_base_0) / 100), 5)), end = "")
                    break

                print(str(round(((item_1 * atk_base_0) / 100), 5)) + ", ", end = "")

            print("] --> ", end = "")
            print("[", end = ""); print(round(((sum(a_p) * atk_base_0) / 100), 5), end = ""); print("]", reset)


    with open(data_dir + attacks + 'general_attack.txt', 'rb') as file:
        print(blue + "Ataque general --> " + cyan, pk.load(file), reset)

    with open(data_dir + levels + 'level_character.txt', 'rb') as file:
        print(blue + "Nivel de tu personaje (En uso) --> " + cyan, pk.load(file), reset)

    with open(data_dir + levels + 'level_enemy.txt', 'rb') as file:
        print(blue + "Nivel del enemigo --> " + cyan, pk.load(file), reset)
    
    with open(data_dir + general_stats + 'elemental_bonus.txt', 'rb') as file:
        b_e = pk.load(file)
        print(blue + "Bono elemental --> " + cyan, str(round(b_e * 100, 4)) + "% -->", round(b_e, 4), reset)

    with open(data_dir + elemental_stats + 'elemental_maestry.txt', 'rb') as file:
        print(blue + "Maestria elemental --> " + cyan, pk.load(file), reset)

    with open(data_dir + general_stats + 'critical_multiplier.txt', 'rb') as file:
        m_c = pk.load(file)
        print(blue + "Daño critico --> " + cyan, str(round(m_c * 100, 4)) + "% -->", round(m_c, 4), reset)

    with open(data_dir + general_stats + 'energy_charge.txt', 'rb') as file:
        e_c = pk.load(file)
        print(blue + "Recarga de energia --> " + cyan, str(round(e_c * 100, 4)) + "% -->", round(e_c, 4), reset)

    with open(data_dir + defenses + 'defense_enemy.txt', 'rb') as file:
        print(blue + "Defensa del enemigo --> " + cyan, pk.load(file), reset)

    with open(data_dir + defenses + 'defense_reduction.txt', 'rb') as file:
        d_r = pk.load(file)
        print(blue + "Reduccion de la defensa del enemigo --> " + cyan, str(round(d_r * 100, 4)) + "% -->", round(d_r, 4), reset)

    with open(data_dir + defenses + 'defense_ignored.txt', 'rb') as file:
        d_i = pk.load(file)
        print(blue + "Defensa ignorada del enemigo --> " + cyan, str(round(d_i * 100, 4)) + "% -->", round(d_i, 4), reset)
   
    with open(data_dir + defenses + 'defense_multiplier.txt', 'rb') as file:
        d_m = pk.load(file)
        print(blue + "Multiplicador de la defensa del enemigo --> " + cyan, str(round(d_m * 100, 4)) + "% -->", round(d_m, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_fisic_base_enemy.txt', 'rb') as file:
        e_r_b_e = pk.load(file)
        print(blue + "Resistencia elemental fisica del enemigo --> " + cyan, str(round(e_r_b_e * 100, 4)) + "% -->", round(e_r_b_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_cryo_base_enemy.txt', 'rb') as file:
        e_r_b_e = pk.load(file)
        print(blue + "Resistencia elemental cryo del enemigo --> " + cyan, str(round(e_r_b_e * 100, 4)) + "% -->", round(e_r_b_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_hydro_base_enemy.txt', 'rb') as file:
        e_r_b_e = pk.load(file)
        print(blue + "Resistencia elemental hydro del enemigo --> " + cyan, str(round(e_r_b_e * 100, 4)) + "% -->", round(e_r_b_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_pyro_base_enemy.txt', 'rb') as file:
        e_r_b_e = pk.load(file)
        print(blue + "Resistencia elemental pyro del enemigo --> " + cyan, str(round(e_r_b_e * 100, 4)) + "% -->", round(e_r_b_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_dendro_base_enemy.txt', 'rb') as file:
        e_r_b_e = pk.load(file)
        print(blue + "Resistencia elemental dendro del enemigo --> " + cyan, str(round(e_r_b_e * 100, 4)) + "% -->", round(e_r_b_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_geo_base_enemy.txt', 'rb') as file:
        e_r_b_e = pk.load(file)
        print(blue + "Resistencia elemental geo del enemigo --> " + cyan, str(round(e_r_b_e * 100, 4)) + "% -->", round(e_r_b_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_electro_base_enemy.txt', 'rb') as file:
        e_r_b_e = pk.load(file)
        print(blue + "Resistencia elemental electro del enemigo --> " + cyan, str(round(e_r_b_e * 100, 4)) + "% -->", round(e_r_b_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_anemo_base_enemy.txt', 'rb') as file:
        e_r_b_e = pk.load(file)
        print(blue + "Resistencia elemental anemo del enemigo --> " + cyan, str(round(e_r_b_e * 100, 4)) + "% -->", round(e_r_b_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_debuffed_enemy.txt', 'rb') as file:
        e_r_d_e = pk.load(file)
        print(blue + "Resistencia elemental reducida del enemigo --> " + cyan, str(round(e_r_d_e * 100, 4)) + "% -->", round(e_r_d_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_fisic_enemy.txt', 'rb') as file:
        e_r_f_e = pk.load(file)
        print(blue + "Resistencia elemental del enemigo --> " + cyan, str(round(e_r_f_e * 100, 4)) + "% -->", round(e_r_f_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_cryo_enemy.txt', 'wb') as file:        
        e_r_c_e = pk.load(file)
        print(blue + "Resistencia elemental del enemigo --> " + cyan, str(round(e_r_c_e * 100, 4)) + "% -->", round(e_r_c_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_hydro_enemy.txt', 'wb') as file:        
        e_r_h_e = pk.load(file)
        print(blue + "Resistencia elemental del enemigo --> " + cyan, str(round(e_r_h_e * 100, 4)) + "% -->", round(e_r_h_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_pyro_enemy.txt', 'wb') as file:        
        e_r_p_e = pk.load(file)
        print(blue + "Resistencia elemental del enemigo --> " + cyan, str(round(e_r_p_e * 100, 4)) + "% -->", round(e_r_p_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_dendro_enemy.txt', 'wb') as file:        
        e_r_d_e = pk.load(file)
        print(blue + "Resistencia elemental del enemigo --> " + cyan, str(round(e_r_d_e * 100, 4)) + "% -->", round(e_r_d_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_geo_enemy.txt', 'wb') as file:        
        e_r_g_e = pk.load(file)
        print(blue + "Resistencia elemental del enemigo --> " + cyan, str(round(e_r_g_e * 100, 4)) + "% -->", round(e_r_g_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_electro_enemy.txt', 'wb') as file:        
        e_r_e_e = pk.load(file)
        print(blue + "Resistencia elemental del enemigo --> " + cyan, str(round(e_r_e_e * 100, 4)) + "% -->", round(e_r_e_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_anemo_enemy.txt', 'wb') as file:        
        e_r_a_e = pk.load(file)
        print(blue + "Resistencia elemental del enemigo --> " + cyan, str(round(e_r_a_e * 100, 4)) + "% -->", round(e_r_a_e, 4), reset)

    with open(data_dir + resistances + 'elemental_resistance_multiplier_enemy.txt', 'rb') as file:
        e_r_m_e = pk.load(file)
        print(blue + "Multiplicador de la resistencia elemental del enemigo --> " + cyan, str(round(e_r_m_e * 100, 4)) + "% -->", round(e_r_m_e, 4), reset)

    with open(data_dir + elemental_stats + 'vaporize_reaction_bonus.txt', 'rb') as file:
        v_r_b = pk.load(file)
        print(blue + "Boño de daño por la reaccion de vaporizacion --> " + cyan, str(round(v_r_b * 100, 4)) + "% -->", round(v_r_b, 4), reset)

    with open(data_dir + elemental_stats + 'melted_reaction_bonus.txt', 'rb') as file:
        m_r_b = pk.load(file)
        print(blue + "Boño de daño por la reaccion de derretido --> " + cyan, str(round(m_r_b * 100, 4)) + "% -->", round(m_r_b, 4), reset)

    with open(data_dir + elemental_stats + 'overloaded_reaction_bonus.txt', 'rb') as file:
        o_r_b = pk.load(file)
        print(blue + "Boño de daño por la reaccion de sobrecargado --> " + cyan, str(round(o_r_b * 100, 4)) + "% -->", round(o_r_b, 4), reset)

    with open(data_dir + elemental_stats + 'superconducting_reaction_bonus.txt', 'rb') as file:
        s_r_b = pk.load(file)
        print(blue + "Boño de daño por la reaccion de superconductor --> " + cyan, str(round(s_r_b * 100, 4)) + "% -->", round(s_r_b, 4), reset)

    with open(data_dir + elemental_stats + 'electrocharged_reaction_bonus.txt', 'rb') as file:
        e_r_b = pk.load(file)
        print(blue + "Boño de daño por la reaccion de electrocargado --> " + cyan, str(round(e_r_b * 100, 4)) + "% -->", round(e_r_b, 4), reset)

    with open(data_dir + elemental_stats + 'icebreaker_reaction_bonus.txt', 'rb') as file:
        i_r_b = pk.load(file)
        print(blue + "Boño de daño por la reaccion de rompehielo --> " + cyan, str(round(i_r_b * 100, 4)) + "% -->", round(i_r_b, 4), reset)

    with open(data_dir + elemental_stats + 'whirlwind_reaction_bonus.txt', 'rb') as file:
        w_r_b = pk.load(file)
        print(blue + "Boño de daño por la reaccion de torbellino --> " + cyan, str(round(w_r_b * 100, 4)) + "% -->", round(w_r_b, 4), reset)

    with open(data_dir + elemental_stats + 'crystallization_bonus.txt', 'rb') as file:
        c_r_b = pk.load(file)
        print(blue + "Boño de daño por la reaccion de cristalizado --> " + cyan, str(round(c_r_b * 100, 4)) + "% -->", round(c_r_b, 4), reset)

    with open(data_dir + elemental_stats + 'overloaded_damage.txt', 'rb') as file:
        o_d = pk.load(file)
        print(blue + "Daño del sobrecargado --> " + cyan, o_d, reset)

    return None

def obt_atk_nature():
    try:
        try:
            atk_natural = float(input("\nAtaque natural --> "))
        except ValueError:
            raise Error(error_color_0 + "0.0" + error_color_1)
       
        if atk_natural <= 0:
            raise Error(error_color_0 + "0.1" + error_color_1)

    except Error as e_0:
        print(e_0)
        
        re_intento_0()
        obt_atk_nature()

    with open(data_dir + attacks + 'natural_attack.txt', 'wb') as file:
        pk.dump(atk_natural, file)
            
def obt_atk_weapon():
    try:
        try:
            atk_arma = float(input("\nAtaque del arma --> "))
        except ValueError:
            raise Error(error_color_0 + "0.2" + error_color_1)

        if atk_arma <= 0:
            raise Error(error_color_0 + "0.3" + error_color_1)

    except Error as e_1:
        print(e_1)
        
        re_intento_0()
        obt_atk_weapon()

    with open(data_dir + attacks + 'weapon_attack.txt', 'wb') as file:
            pk.dump(atk_arma, file)

def obt_atk_art():
    atk_extra_0 = []

    for _ in range(5):
        try:
            try:
                recipiente_de_daño_0 = int(input("\nAtaque que tengas en cada artefaco (Consejo: Puedes empezar desde el casco hasta la flor) (Si no tienes ataque en el artefacto; pon '0') --> "))
            except ValueError:
                raise Error(error_color_0 + "0.4" + error_color_1)
        
            if recipiente_de_daño_0 < 0:
                raise Error(error_color_0 + "0.5" + error_color_1)
            
            atk_extra_0.append(recipiente_de_daño_0)

        except Error as e_2:
            print(e_2)
            
            re_intento_0()
            obt_atk_art()

    with open(data_dir + attacks + 'artifact_attacks_list.txt', 'wb') as file:
        pk.dump(atk_extra_0, file)

def obt_atk_p_art():
    atk_extra_1 = []

    for _ in range(5):
        recipiente_de_daño_1 = input("\nAtaque porcentual que tengas en cada artefaco (Consejo: Puedes empezar desde el casco hasta la flor) (Si no tienes ataque porcentual en el artefacto; pon '0') --> ")

        recipiente_de_daño_1 = recipiente_de_daño_1.replace('%', ''); recipiente_de_daño_1 = recipiente_de_daño_1.replace(',', '.')

        try:
            try:
                recipiente_de_daño_1 = float(recipiente_de_daño_1)
            except ValueError:
                raise Error(error_color_0 + "0.6" + error_color_1)
        
            if recipiente_de_daño_1 < 0:
                raise Error(error_color_0 + "0.7" + error_color_1)
            
            atk_extra_1.append(recipiente_de_daño_1)

        except Error as e_3:
            print(e_3)
            
            re_intento_0()
            obt_atk_p_art()

    with open(data_dir + attacks + 'artifact_porcentual_attacks_list.txt', 'wb') as file:
        pk.dump(atk_extra_1, file)

def obt_atk_base_and_general():

    obt_atk_nature()

    obt_atk_weapon()

    with open(data_dir + attacks + 'natural_attack.txt', 'rb') as file_0:
        atk_natural = pk.load(file_0)

    with open(data_dir + attacks + 'weapon_attack.txt', 'rb') as file_1:
        atk_arma = pk.load(file_1)

    atk_base = atk_natural + atk_arma

    obt_atk_art()

    obt_atk_p_art()
    
    with open(data_dir + attacks + 'base_attack.txt', 'wb') as file:
        pk.dump(atk_base, file)

    with open(data_dir + attacks + 'artifact_attacks_list.txt', 'rb') as file_0:
        atk_extra_0 = pk.load(file_0)

    with open(data_dir + attacks + 'artifact_porcentual_attacks_list.txt', 'rb') as file_1:
        atk_extra_1 = pk.load(file_1)

    atk_general = atk_base + sum(atk_extra_0) + ((sum(atk_extra_1) * atk_base) / 100)

    with open(data_dir + attacks + 'general_attack.txt', 'wb') as file:
        pk.dump(atk_general, file)

def obt_character_level():
    try:
        try:
            character_level = int(input("\nNivel de tu personaje (En uso) --> "))
        except ValueError:
            raise Error(error_color_0 + "0.8" + error_color_1)

        if character_level < 1 or character_level > 90:
            raise Error(error_color_0 + "0.9" + error_color_1)
        
    except Error as e_4:
        print(e_4)
        
        re_intento_0()
        obt_character_level()

    with open(data_dir + levels  + 'level_character.txt', 'wb') as file:
            pk.dump(character_level, file)

def obt_enemy_level():
    try:
        try:
            enemy_level = int(input("\nNivel del mounstro enemigo --> "))
        except ValueError:
            raise Error(error_color_0 + "1.0" + error_color_1)
        
        if enemy_level < 1:
            raise Error(error_color_0 + "1.1" + error_color_1)
    
    except Error as e_5:
        print(e_5)
        
        re_intento_0()
        obt_enemy_level()

    with open(data_dir + levels + 'level_enemy.txt', 'wb') as file:
            pk.dump(enemy_level, file)

def obt_elemental_bonus():
    
    try:
        try:
            bono_elemental = input("\nBono elemental --> ")
            bono_elemental = bono_elemental.replace('%', ''); bono_elemental = bono_elemental.replace(',', '.')
            
            bono_elemental = float(bono_elemental)
            bono_elemental = bono_elemental / 100
        except ValueError:
            raise Error(error_color_0 + "1.2" + error_color_1)
        
        if bono_elemental < 0:
            raise Error(error_color_0 + "1.3" + error_color_1)

    except Error as e_6:
        print(e_6)
        
        re_intento_0()
        obt_elemental_bonus()

    with open(data_dir + general_stats + 'elemental_bonus.txt', 'wb') as file:
            pk.dump(bono_elemental, file)

def obt_maestria_elemental():
    try:
        try:
            maestria_elemental = int(input("\nMaestria elemental --> "))
        except ValueError:
            raise Error(error_color_0 + "1.4" + error_color_1)
        
        if maestria_elemental < 0:
            raise Error(error_color_0 + "1.5" + error_color_1)

    except Error as e_7:
        print(e_7)
        
        re_intento_0()
        obt_maestria_elemental()

    with open(data_dir + elemental_stats + 'elemental_maestry.txt', 'wb') as file:
            pk.dump(maestria_elemental, file)

def obt_mul_crit():
    try:
        try:
            multiplicador_critico = input("\nDaño critico --> ")
            multiplicador_critico = multiplicador_critico.replace('%', ''); multiplicador_critico = multiplicador_critico.replace(',', '.')

            multiplicador_critico = float(multiplicador_critico)
            multiplicador_critico = multiplicador_critico / 100
        except ValueError:
            raise Error(error_color_0 + "1.6" + error_color_1)
        
        if multiplicador_critico < 0:
            raise Error(error_color_0 + "1.7" + error_color_1)
        
    except Error as e_8:
        print(e_8)

        re_intento_0()
        obt_mul_crit()

    with open(data_dir + general_stats + 'critical_multiplier.txt', 'wb') as file:
            pk.dump(multiplicador_critico, file)

def obt_energy_charge():
    try:
        try:
            recarga_de_energia = input("\nRecarga de energia --> ")
            recarga_de_energia = recarga_de_energia.replace('%', ''); recarga_de_energia = recarga_de_energia.replace(',', '.')
            
            recarga_de_energia = float(recarga_de_energia)
            recarga_de_energia = recarga_de_energia / 100
        except ValueError:
            raise Error(error_color_0 + "1.8" + error_color_1)
        
        if recarga_de_energia < 0:
            raise Error(error_color_0 + "1.9" + error_color_1)
        
    except Error as e_9:
        print(e_9)

        re_intento_0()
        obt_energy_charge()

    with open(data_dir + general_stats + 'energy_charge.txt', 'wb') as file:
            pk.dump(recarga_de_energia, file)

def calc_def_enemy():
    try:
        try:
            with open(data_dir + levels + 'level_enemy.txt', 'rb') as file_0:
                e_l = pk.load(file_0)
        except FileNotFoundError:
            raise Error(error_color_0 + "2.0" + error_color_1)
        
    except Error as e_10:
        print(e_10)
        wait_espace()
        
    def_enemy = 5 * e_l + 500

    with open(data_dir + defenses + 'defense_enemy.txt', 'wb') as file_1:
        pk.dump(def_enemy, file_1)

def obt_def_reduction():
    try:
        try:
            def_reduction = input("\nPorcentaje de defensa reducida --> ")

            def_reduction = def_reduction.replace('%', '')
            def_reduction = def_reduction.replace(',', '.')

            def_reduction = float(def_reduction)
            def_reduction = def_reduction / 100
        
        except ValueError:
            raise Error(error_color_0 + "2.1" + error_color_1)
        
        if def_reduction < 0:
            raise Error(error_color_0 + "2.2" + error_color_1)
        
    except Error as e_11:
        print(e_11)

        re_intento_0()
        obt_def_reduction()
    
    with open(data_dir + defenses + 'defense_reduction.txt', 'wb') as file:
        pk.dump(def_reduction, file)
        
def obt_def_ignored():
    try:
        try:
            def_ignored = input("\nPorcentaje de defensa ignorada --> ")

            def_ignored = def_ignored.replace('%', '')
            def_ignored = def_ignored.replace(',', '.')

            def_ignored = float(def_ignored)
            def_ignored = def_ignored / 100
        except ValueError:
            raise Error(error_color_0 + "2.3" + error_color_1)
        
        if def_ignored < 0:
            raise Error(error_color_0 + "2.4" + error_color_1)
        
    except Error as e_12:
        print(e_12)

        re_intento_0()
        obt_def_ignored()

    with open(data_dir + defenses + 'defense_ignored.txt', 'wb') as file:
        pk.dump(def_ignored, file)

def calc_mul_def_enemy():
    try:
        try:
            try:
                try:
                    try:
                        with open(data_dir + levels + 'level_character.txt', 'rb') as file_0:
                            level_character = pk.load(file_0)
                    except FileNotFoundError:
                        raise Error(error_color_0 + "2.5" + error_color_1)
                
                    with open(data_dir + levels + 'level_enemy.txt', 'rb') as file_1:
                        level_enemy = pk.load(file_1)
                except FileNotFoundError:
                    raise Error(error_color_0 + "2.6" + error_color_1)
            
                with open(data_dir + defenses + 'defense_reduction.txt', 'rb') as file_2:
                    defense_reduction = pk.load(file_2)
            except FileNotFoundError:
                raise Error(error_color_0 + "2.7" + error_color_1)
        
            with open(data_dir + defenses + 'defense_ignored.txt', 'rb') as file_3:
                defense_ignored = pk.load(file_3)

        except FileNotFoundError:
            raise Error(error_color_0 + "2.8" + error_color_1)

    except Error as e_13:
        print(e_13)
        wait_espace()

    def_multiplier = (level_character + 100) / ((1 - defense_reduction) * (1 - defense_ignored) * (level_enemy + 100) + level_character + 100)

    with open(data_dir + defenses + 'defense_multiplier.txt', 'wb') as file_4:
        pk.dump(def_multiplier, file_4)

def obt_elemental_resistance_fisic_enemy():
    try:
        try:
            res_elemental_base = input("\nResistencia elemental fisica del enemigo --> ")

            res_elemental_base = res_elemental_base.replace('%', '')
            res_elemental_base = res_elemental_base.replace(',', '.')

            res_elemental_base = float(res_elemental_base)
            res_elemental_base = res_elemental_base / 100

        except ValueError:
            raise Error(error_color_0 + "2.9" + error_color_1)

    except Error as e_14:
        print(e_14)

        re_intento_0()
        obt_elemental_resistance_fisic_enemy()
    
    with open(data_dir + resistances + 'elemental_resistance_fisic_base_enemy.txt', 'wb') as file:
                pk.dump(res_elemental_base, file)

def obt_elemental_resistance_cryo_enemy():
    try:
        try:
            res_elemental_base = input("\nResistencia elemental cryo del enemigo --> ")

            res_elemental_base = res_elemental_base.replace('%', '')
            res_elemental_base = res_elemental_base.replace(',', '.')

            res_elemental_base = float(res_elemental_base)
            res_elemental_base = res_elemental_base / 100

        except ValueError:
            raise Error(error_color_0 + "2.9" + error_color_1)

    except Error as e_14:
        print(e_14)

        re_intento_0()
        obt_elemental_resistance_cryo_enemy()
    
    with open(data_dir + resistances + 'elemental_resistance_cryo_base_enemy.txt', 'wb') as file:
                pk.dump(res_elemental_base, file)

def obt_elemental_resistance_hydro_enemy():
    try:
        try:
            res_elemental_base = input("\nResistencia elemental hydro del enemigo --> ")

            res_elemental_base = res_elemental_base.replace('%', '')
            res_elemental_base = res_elemental_base.replace(',', '.')

            res_elemental_base = float(res_elemental_base)
            res_elemental_base = res_elemental_base / 100

        except ValueError:
            raise Error(error_color_0 + "2.9" + error_color_1)

    except Error as e_14:
        print(e_14)

        re_intento_0()
        obt_elemental_resistance_hydro_enemy()

    with open(data_dir + resistances + 'elemental_resistance_hydro_base_enemy.txt', 'wb') as file:
                pk.dump(res_elemental_base, file)

def obt_elemental_resistance_pyro_enemy():
    try:
        try:
            res_elemental_base = input("\nResistencia elemental pyro del enemigo --> ")

            res_elemental_base = res_elemental_base.replace('%', '')
            res_elemental_base = res_elemental_base.replace(',', '.')

            res_elemental_base = float(res_elemental_base)
            res_elemental_base = res_elemental_base / 100

        except ValueError:
            raise Error(error_color_0 + "2.9" + error_color_1)

    except Error as e_14:
        print(e_14)

        re_intento_0()
        obt_elemental_resistance_pyro_enemy()

    with open(data_dir + resistances + 'elemental_resistance_pyro_base_enemy.txt', 'wb') as file:
                pk.dump(res_elemental_base, file)
    
def obt_elemental_resistance_dendro_enemy():
    try:
        try:
            res_elemental_base = input("\nResistencia elemental dendro del enemigo --> ")

            res_elemental_base = res_elemental_base.replace('%', '')
            res_elemental_base = res_elemental_base.replace(',', '.')

            res_elemental_base = float(res_elemental_base)
            res_elemental_base = res_elemental_base / 100

        except ValueError:
            raise Error(error_color_0 + "2.9" + error_color_1)

    except Error as e_14:
        print(e_14)

        re_intento_0()
        obt_elemental_resistance_dendro_enemy()

    with open(data_dir + resistances + 'elemental_resistance_dendro_base_enemy.txt', 'wb') as file:
                pk.dump(res_elemental_base, file)
    
def obt_elemental_resistance_geo_enemy():
    try:
        try:
            res_elemental_base = input("\nResistencia elemental geo del enemigo --> ")

            res_elemental_base = res_elemental_base.replace('%', '')
            res_elemental_base = res_elemental_base.replace(',', '.')

            res_elemental_base = float(res_elemental_base)
            res_elemental_base = res_elemental_base / 100

        except ValueError:
            raise Error(error_color_0 + "2.9" + error_color_1)

    except Error as e_14:
        print(e_14)

        re_intento_0()
        obt_elemental_resistance_geo_enemy()

    with open(data_dir + resistances + 'elemental_resistance_geo_base_enemy.txt', 'wb') as file:
                pk.dump(res_elemental_base, file)
    
def obt_elemental_resistance_electro_enemy():
    try:
        try:
            res_elemental_base = input("\nResistencia elemental electro del enemigo --> ")

            res_elemental_base = res_elemental_base.replace('%', '')
            res_elemental_base = res_elemental_base.replace(',', '.')

            res_elemental_base = float(res_elemental_base)
            res_elemental_base = res_elemental_base / 100

        except ValueError:
            raise Error(error_color_0 + "2.9" + error_color_1)

    except Error as e_14:
        print(e_14)

        re_intento_0()
        obt_elemental_resistance_electro_enemy()
    
    with open(data_dir + resistances + 'elemental_resistance_electro_base_enemy.txt', 'wb') as file:
                pk.dump(res_elemental_base, file)

def obt_elemental_resistance_anemo_enemy():
    try:
        try:
            res_elemental_base = input("\nResistencia elemental anemo del enemigo --> ")

            res_elemental_base = res_elemental_base.replace('%', '')
            res_elemental_base = res_elemental_base.replace(',', '.')

            res_elemental_base = float(res_elemental_base)
            res_elemental_base = res_elemental_base / 100

        except ValueError:
            raise Error(error_color_0 + "2.9" + error_color_1)

    except Error as e_14:
        print(e_14)

        re_intento_0()
        obt_elemental_resistance_anemo_enemy()

    with open(data_dir + resistances + 'elemental_resistance_anemo_base_enemy.txt', 'wb') as file:
                pk.dump(res_elemental_base, file)

def obt_elemental_resistance_base_enemys():
    obt_elemental_resistance_fisic_enemy()
    obt_elemental_resistance_cryo_enemy()
    obt_elemental_resistance_hydro_enemy()
    obt_elemental_resistance_pyro_enemy()
    obt_elemental_resistance_dendro_enemy()
    obt_elemental_resistance_geo_enemy()
    obt_elemental_resistance_electro_enemy()
    obt_elemental_resistance_anemo_enemy()

def obt_elemental_resistance_debuff_enemy():
    try:
        try:
            elemental_resistance_debuff_enemy = input("\nResistencia elemental reducida/bajada --> ")

            elemental_resistance_debuff_enemy = elemental_resistance_debuff_enemy.replace('%', '')
            elemental_resistance_debuff_enemy = elemental_resistance_debuff_enemy.replace(',', '.')

            elemental_resistance_debuff_enemy = float(elemental_resistance_debuff_enemy)
            elemental_resistance_debuff_enemy = elemental_resistance_debuff_enemy / 100

        except ValueError:
            raise Error(error_color_0 + "3.0" + error_color_1)
        
    except Error as e_15:
        print(e_15)

        re_intento_0()
        obt_elemental_resistance_debuff_enemy()

    with open(data_dir + resistances + 'elemental_resistance_debuffed_enemy.txt', 'wb') as file:
        pk.dump(elemental_resistance_debuff_enemy, file)

def calc_elemental_resistance_enemy():
    try:
        try:
            try:
                with open(data_dir + resistances + 'elemental_resistance_fisic_base_enemy.txt', 'rb') as file_0:
                    elemental_resistance_fisic_enemy = pk.load(file_0)
                    
                with open(data_dir + resistances + 'elemental_resistance_cryo_base_enemy.txt', 'rb') as file_1:
                    elemental_resistance_cryo_enemy = pk.load(file_1)
                    
                with open(data_dir + resistances + 'elemental_resistance_hydro_base_enemy.txt', 'rb') as file_2:
                    elemental_resistance_hydro_enemy = pk.load(file_2)

                with open(data_dir + resistances + 'elemental_resistance_pyro_base_enemy.txt', 'rb') as file_3:
                    elemental_resistance_pyro_enemy = pk.load(file_3)

                with open(data_dir + resistances + 'elemental_resistance_dendro_base_enemy.txt', 'rb') as file_4:
                    elemental_resistance_dendro_enemy = pk.load(file_4)

                with open(data_dir + resistances + 'elemental_resistance_geo_base_enemy.txt', 'rb') as file_5:
                    elemental_resistance_geo_enemy = pk.load(file_5)

                with open(data_dir + resistances + 'elemental_resistance_electro_base_enemy.txt', 'rb') as file_6:
                    elemental_resistance_electro_enemy = pk.load(file_6)

                with open(data_dir + resistances + 'elemental_resistance_anemo_base_enemy.txt', 'rb') as file_7:
                    elemental_resistance_anemo_enemy = pk.load(file_7)

            except FileNotFoundError:
                raise Error(error_color_0 + "3.1" + error_color_1)
            
            
            with open(data_dir + resistances + 'elemental_resistance_debuffed_enemy.txt', 'rb') as file_1:
                elemental_resistance_debuffed_enemy = pk.load(file_1)
        except FileNotFoundError:
            raise Error(error_color_0 + "3.2" + error_color_1)
        
    except Error as e_16:
        print(e_16)
        wait_espace()

    elemental_resistance_fisic_enemy = elemental_resistance_fisic_enemy - elemental_resistance_debuffed_enemy
    
    elemental_resistance_cryo_enemy = elemental_resistance_cryo_enemy - elemental_resistance_debuffed_enemy

    elemental_resistance_hydro_enemy = elemental_resistance_hydro_enemy - elemental_resistance_debuffed_enemy

    elemental_resistance_pyro_enemy = elemental_resistance_pyro_enemy - elemental_resistance_debuffed_enemy

    elemental_resistance_dendro_enemy = elemental_resistance_dendro_enemy - elemental_resistance_debuffed_enemy

    elemental_resistance_geo_enemy = elemental_resistance_geo_enemy - elemental_resistance_debuffed_enemy

    elemental_resistance_electro_enemy = elemental_resistance_electro_enemy - elemental_resistance_debuffed_enemy

    elemental_resistance_anemo_enemy = elemental_resistance_anemo_enemy - elemental_resistance_debuffed_enemy


    with open(data_dir + resistances + 'elemental_resistance_fisic_enemy.txt', 'wb') as file_0:
        pk.dump(elemental_resistance_fisic_enemy, file_0)

    with open(data_dir + resistances + 'elemental_resistance_cryo_enemy.txt', 'wb') as file_1:
        pk.dump(elemental_resistance_cryo_enemy, file_1)

    with open(data_dir + resistances + 'elemental_resistance_hydro_enemy.txt', 'wb') as file_2:
        pk.dump(elemental_resistance_hydro_enemy, file_2)

    with open(data_dir + resistances + 'elemental_resistance_pyro_enemy.txt', 'wb') as file_3:
        pk.dump(elemental_resistance_pyro_enemy, file_3)

    with open(data_dir + resistances + 'elemental_resistance_dendro_enemy.txt', 'wb') as file_4:
        pk.dump(elemental_resistance_dendro_enemy, file_4)

    with open(data_dir + resistances + 'elemental_resistance_geo_enemy.txt', 'wb') as file_5:
        pk.dump(elemental_resistance_geo_enemy, file_5)

    with open(data_dir + resistances + 'elemental_resistance_electro_enemy.txt', 'wb') as file_6:
        pk.dump(elemental_resistance_electro_enemy, file_6)

    with open(data_dir + resistances + 'elemental_resistance_anemo_enemy.txt', 'wb') as file_7:
        pk.dump(elemental_resistance_anemo_enemy, file_7)

def cacl_mul_elemental_resistance_enemy():
    try:
        try:
            with open(data_dir + resistances + 'elemental_resistance_fisic_enemy.txt', 'rb') as file_0:
                elemental_resistance_fisic_enemy = pk.load(file_0)

            with open(data_dir + resistances + 'elemental_resistance_cryo_enemy.txt', 'rb') as file_1:
                elemental_resistance_cryo_enemy = pk.load(file_1)

            with open(data_dir + resistances + 'elemental_resistance_hydro_enemy.txt', 'rb') as file_2:
                elemental_resistance_hydro_enemy = pk.load(file_2)

            with open(data_dir + resistances + 'elemental_resistance_pyro_enemy.txt', 'rb') as file_3:
                elemental_resistance_pyro_enemy = pk.load(file_3)

            with open(data_dir + resistances + 'elemental_resistance_dendro_enemy.txt', 'rb') as file_4:
                elemental_resistance_dendro_enemy = pk.load(file_4)

            with open(data_dir + resistances + 'elemental_resistance_geo_enemy.txt', 'rb') as file_5:
                elemental_resistance_geo_enemy = pk.load(file_5)

            with open(data_dir + resistances + 'elemental_resistance_electro_enemy.txt', 'rb') as file_6:
                elemental_resistance_electro_enemy = pk.load(file_6)

            with open(data_dir + resistances + 'elemental_resistance_anemo_enemy.txt', 'rb') as file_7:
                elemental_resistance_anemo_enemy = pk.load(file_7)
            
        except FileNotFoundError:
            raise Error(error_color_0 + "3.3" + error_color_1)

    except Error as e_17:
        print(e_17)
        wait_espace()

    if elemental_resistance_fisic_enemy < 0:
        elemental_resistance_multiplier_fisic_enemy = 1 - (elemental_resistance_fisic_enemy / 2)
    
    elif elemental_resistance_fisic_enemy >= 0 and elemental_resistance_fisic_enemy < 0.75:
        elemental_resistance_multiplier_fisic_enemy = 1 - elemental_resistance_fisic_enemy

    elif elemental_resistance_fisic_enemy >= 0.75:
        elemental_resistance_multiplier_fisic_enemy = 1 / ((4 * elemental_resistance_fisic_enemy) + 1)

    
    if elemental_resistance_cryo_enemy < 0:
        elemental_resistance_multiplier_cryo_enemy = 1 - (elemental_resistance_cryo_enemy / 2)
    
    elif elemental_resistance_cryo_enemy >= 0 and elemental_resistance_cryo_enemy < 0.75:
        elemental_resistance_multiplier_cryo_enemy = 1 - elemental_resistance_cryo_enemy

    elif elemental_resistance_cryo_enemy >= 0.75:
        elemental_resistance_multiplier_cryo_enemy = 1 / ((4 * elemental_resistance_cryo_enemy) + 1)
        

    if elemental_resistance_hydro_enemy < 0:
        elemental_resistance_multiplier_hydro_enemy = 1 - (elemental_resistance_hydro_enemy / 2)
    
    elif elemental_resistance_hydro_enemy >= 0 and elemental_resistance_hydro_enemy < 0.75:
        elemental_resistance_multiplier_hydro_enemy = 1 - elemental_resistance_hydro_enemy

    elif elemental_resistance_hydro_enemy >= 0.75:
        elemental_resistance_multiplier_hydro_enemy = 1 / ((4 * elemental_resistance_hydro_enemy) + 1)

    if elemental_resistance_pyro_enemy < 0:
        elemental_resistance_multiplier_pyro_enemy = 1 - (elemental_resistance_pyro_enemy / 2)
    
    elif elemental_resistance_pyro_enemy >= 0 and elemental_resistance_pyro_enemy < 0.75:
        elemental_resistance_multiplier_pyro_enemy = 1 - elemental_resistance_pyro_enemy

    elif elemental_resistance_pyro_enemy >= 0.75:
        elemental_resistance_multiplier_pyro_enemy = 1 / ((4 * elemental_resistance_pyro_enemy) + 1)
        

    if elemental_resistance_dendro_enemy < 0:
        elemental_resistance_multiplier_dendro_enemy = 1 - (elemental_resistance_dendro_enemy / 2)
    
    elif elemental_resistance_dendro_enemy >= 0 and elemental_resistance_dendro_enemy < 0.75:
        elemental_resistance_multiplier_dendro_enemy = 1 - elemental_resistance_dendro_enemy

    elif elemental_resistance_dendro_enemy >= 0.75:
        elemental_resistance_multiplier_dendro_enemy = 1 / ((4 * elemental_resistance_dendro_enemy) + 1)

    if elemental_resistance_geo_enemy < 0:
        elemental_resistance_multiplier_geo_enemy = 1 - (elemental_resistance_geo_enemy / 2)
    
    elif elemental_resistance_geo_enemy >= 0 and elemental_resistance_geo_enemy < 0.75:
        elemental_resistance_multiplier_geo_enemy = 1 - elemental_resistance_geo_enemy

    elif elemental_resistance_geo_enemy >= 0.75:
        elemental_resistance_multiplier_geo_enemy = 1 / ((4 * elemental_resistance_geo_enemy) + 1)

    if elemental_resistance_electro_enemy < 0:
        elemental_resistance_multiplier_electro_enemy = 1 - (elemental_resistance_electro_enemy / 2)
    
    elif elemental_resistance_electro_enemy >= 0 and elemental_resistance_electro_enemy < 0.75:
        elemental_resistance_multiplier_electro_enemy = 1 - elemental_resistance_electro_enemy

    elif elemental_resistance_electro_enemy >= 0.75:
        elemental_resistance_multiplier_electro_enemy = 1 / ((4 * elemental_resistance_electro_enemy) + 1)

    if elemental_resistance_anemo_enemy < 0:
        elemental_resistance_multiplier_anemo_enemy = 1 - (elemental_resistance_anemo_enemy / 2)
    
    elif elemental_resistance_anemo_enemy >= 0 and elemental_resistance_anemo_enemy < 0.75:
        elemental_resistance_multiplier_anemo_enemy = 1 - elemental_resistance_anemo_enemy

    elif elemental_resistance_anemo_enemy >= 0.75:
        elemental_resistance_multiplier_anemo_enemy = 1 / ((4 * elemental_resistance_anemo_enemy) + 1)
        

    with open(data_dir + resistances + 'elemental_resistance_multiplier_fisic_enemy.txt', 'wb') as file_0:
        pk.dump(elemental_resistance_multiplier_fisic_enemy, file_0)

    with open(data_dir + resistances + 'elemental_resistance_multiplier_cryo_enemy.txt', 'wb') as file_1:
        pk.dump(elemental_resistance_multiplier_cryo_enemy, file_1)

    with open(data_dir + resistances + 'elemental_resistance_multiplier_hydro_enemy.txt', 'wb') as file_2:
        pk.dump(elemental_resistance_multiplier_hydro_enemy, file_2)

    with open(data_dir + resistances + 'elemental_resistance_multiplier_pyro_enemy.txt', 'wb') as file_3:
        pk.dump(elemental_resistance_multiplier_pyro_enemy, file_3)

    with open(data_dir + resistances + 'elemental_resistance_multiplier_dendro_enemy.txt', 'wb') as file_4:
        pk.dump(elemental_resistance_multiplier_dendro_enemy, file_4)

    with open(data_dir + resistances + 'elemental_resistance_multiplier_geo_enemy.txt', 'wb') as file_5:
        pk.dump(elemental_resistance_multiplier_geo_enemy, file_5)

    with open(data_dir + resistances + 'elemental_resistance_multiplier_electro_enemy.txt', 'wb') as file_6:
        pk.dump(elemental_resistance_multiplier_electro_enemy, file_6)

    with open(data_dir + resistances + 'elemental_resistance_multiplier_anemo_enemy.txt', 'wb') as file_7:
        pk.dump(elemental_resistance_multiplier_anemo_enemy, file_7)

def cacl_elemental_bonus():
    try:
        try:
            with open(data_dir + elemental_stats + 'elemental_maestry.txt', 'rb') as file:
                elemental_maestry = pk.load(file)

        except FileNotFoundError:
            raise Error(error_color_0 + "3.4" + error_color_1)

    except Error as e_18:
        print(e_18)
        wait_espace()

    vaporized_and_melted = (278 * (elemental_maestry / (elemental_maestry + 1400)) / 100)
    overloaded_superconducting_electrocharged_icebreaker_whirlwind = (1600 * (elemental_maestry / (elemental_maestry + 2000)) / 100)
    crystallization = (444 * (elemental_maestry / (elemental_maestry + 1400))) / 100

    with open(data_dir + elemental_stats + 'vaporize_reaction_bonus.txt', 'wb') as file:
        pk.dump(vaporized_and_melted, file)

    with open(data_dir + elemental_stats + 'melted_reaction_bonus.txt', 'wb') as file:
        pk.dump(vaporized_and_melted, file)

    with open(data_dir + elemental_stats + 'overloaded_reaction_bonus.txt', 'wb') as file:
        pk.dump(overloaded_superconducting_electrocharged_icebreaker_whirlwind, file)

    with open(data_dir + elemental_stats + 'superconducting_reaction_bonus.txt', 'wb') as file:
        pk.dump(overloaded_superconducting_electrocharged_icebreaker_whirlwind, file)

    with open(data_dir + elemental_stats + 'electrocharged_reaction_bonus.txt', 'wb') as file:
        pk.dump(overloaded_superconducting_electrocharged_icebreaker_whirlwind, file)

    with open(data_dir + elemental_stats + 'icebreaker_reaction_bonus.txt', 'wb') as file:
        pk.dump(overloaded_superconducting_electrocharged_icebreaker_whirlwind, file)

    with open(data_dir + elemental_stats + 'whirlwind_reaction_bonus.txt', 'wb') as file:
        pk.dump(overloaded_superconducting_electrocharged_icebreaker_whirlwind, file)

    with open(data_dir + elemental_stats + 'crystallization_bonus.txt', 'wb') as file:
        pk.dump(crystallization, file)

def calc_overloaded_reaction():
    try:
        try:
            try:
                try:
                    with open(data_dir + elemental_stats + 'overloaded_reaction_bonus.txt', 'rb') as file:
                        overloaded_bonus = pk.load(file)
            
                except FileNotFoundError:
                    raise Error(error_color_0 + "3.5" + error_color_1)

                with open(data_dir + levels + 'level_character.txt', 'rb') as file:
                    character_level = pk.load(file)

            except FileNotFoundError:
                raise Error(error_color_0 + "3.6" + error_color_1)
            
            with open(data_dir + resistances + 'elemental_resistance_multiplier_enemy.txt', 'rb') as file:
                elemental_resistance_multiplier_enemy = pk.load(file)

        except FileNotFoundError:
            raise Error(error_color_0 + "3.7" + error_color_1)
    
    except Error as e_19:
        print(e_19)
        wait_espace()

    if character_level >= 1 and character_level < 10:
        overloaded = 34 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 10 and character_level < 20:
        overloaded = 68 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 20 and character_level < 30:
        overloaded = 161 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 30 and character_level < 40:
        overloaded = 273 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 40 and character_level < 50:
        overloaded = 415 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 50 and character_level < 60:
        overloaded = 647 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 60 and character_level < 70:
        overloaded = 979 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 70 and character_level < 80:
        overloaded = 1533 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 80 and character_level < 90:
        overloaded = 2159 * overloaded_bonus * elemental_resistance_multiplier_enemy
    elif character_level >= 90 and character_level < 100:
        overloaded = 2901 * overloaded_bonus * elemental_resistance_multiplier_enemy

    with open(data_dir + elemental_stats + 'overloaded_damage.txt', 'wb') as file:
        pk.dump(overloaded, file)

def main_0():
    obt_atk_base_and_general()
    obt_character_level()
    obt_enemy_level()
    obt_elemental_bonus()
    obt_maestria_elemental()
    obt_mul_crit()
    obt_energy_charge()
    calc_def_enemy()
    obt_def_reduction()
    obt_def_ignored()
    calc_mul_def_enemy()
    obt_elemental_resistance_base_enemys()
    obt_elemental_resistance_debuff_enemy()
    calc_elemental_resistance_enemy()
    cacl_mul_elemental_resistance_enemy()
    cacl_elemental_bonus()
    calc_overloaded_reaction()
    list_of_data()
    wait_espace()

if __name__ == "__main__":

    main_0()
