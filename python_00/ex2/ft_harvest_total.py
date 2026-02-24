#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 18:46:57 by jabad-di            #+#    #+#            #
#   Updated: 2026/02/24 18:55:06 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    one_day = int(input("Day 1 harvest: "))
    two_day = int(input("Day 2 harvest: "))
    three_day = int(input("Day 3 harvest: "))
    print("Total harvest:", one_day + two_day + three_day)
