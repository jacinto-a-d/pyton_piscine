#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 18:56:51 by jabad-di            #+#    #+#            #
#   Updated: 2026/02/24 19:59:27 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age():
    plant_day = int(input("Enter plant age in days: "))
    if plant_day > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
