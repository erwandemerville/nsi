#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from turtle import penup, pendown, goto

g = 9.81  # intensité de pesanteur terrestre

class Projectile:  # déclarer une classe Projectile
    pass

balle = Projectile()  # créer un objet
balle.x = 0  # affecter son attribut x,
balle.y = 0  # son attribut y,
balle.vx = 10  # son attribut vx,
balle.vy = 20  # et son attribut vy