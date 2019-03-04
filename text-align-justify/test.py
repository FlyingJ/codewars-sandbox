#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:31:21 2019

@author: ultra_jason
"""

test.assert_equals(justify('123 45 6', 7), '123  45\n6')
LONG_STRING = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.'
JUSTIFICATION = 30
LONG_STRING_JUSTIFIED = 'Lorem  ipsum  dolor  sit amet,\nconsectetur  adipiscing  elit.\nVestibulum    sagittis   dolor\nmauris,  at  elementum  ligula\ntempor  eget.  In quis rhoncus\nnunc,  at  aliquet orci. Fusce\nat   dolor   sit   amet  felis\nsuscipit   tristique.   Nam  a\nimperdiet   tellus.  Nulla  eu\nvestibulum    urna.    Vivamus\ntincidunt  suscipit  enim, nec\nultrices   nisi  volutpat  ac.\nMaecenas   sit   amet  lacinia\narcu,  non dictum justo. Donec\nsed  quam  vel  risus faucibus\neuismod.  Suspendisse  rhoncus\nrhoncus  felis  at  fermentum.\nDonec lorem magna, ultricies a\nnunc    sit    amet,   blandit\nfringilla  nunc. In vestibulum\nvelit    ac    felis   rhoncus\npellentesque. Mauris at tellus\nenim.  Aliquam eleifend tempus\ndapibus. Pellentesque commodo,\nnisi    sit   amet   hendrerit\nfringilla,   ante  odio  porta\nlacus,   ut   elementum  justo\nnulla et dolor.'
test.assert_equals(justify(LONG_STRING, JUSTIFICATION), LONG_STRING_JUSTIFIED)