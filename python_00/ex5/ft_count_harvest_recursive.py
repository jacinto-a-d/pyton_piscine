#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 20:13:02 by jabad-di            #+#    #+#            #
#   Updated: 2026/02/25 17:55:17 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    total_day = int(input("Days until harvest: "))

    def count_days(current):
        if (current <= total_day):
            print("Day", current)
            count_days(current + 1)
        else:
            print("Harvest time!")
    count_days(1)
