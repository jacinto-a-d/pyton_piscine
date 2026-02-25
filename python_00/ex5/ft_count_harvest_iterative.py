#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 20:12:29 by jabad-di            #+#    #+#            #
#   Updated: 2026/02/25 17:54:18 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    count_day = int(input("Days until harvest: "))
    for i in range(1, count_day + 1):
        print("Day", i)
    print("Harvest time!")
