#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/25 17:46:54 by jabad-di            #+#    #+#            #
#   Updated: 2026/02/25 17:51:42 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder():
    day = int(input("Days since last watering: "))
    if day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
