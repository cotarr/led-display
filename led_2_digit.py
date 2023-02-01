"""Raspberry Pi Sense Hat number display

This module will display a 2 digit integer value as 3 x 5 pixel 
numeric digits on the 8 x 8 LED display of a Raspberry Pi Sense Hat.
Valid integers range from -39 to 119. Out of range values will display EE"""

import time

from sense_hat import SenseHat
sense = SenseHat()

def small_letter(dig: int, xo: int, yo: int, red: int, grn: int, blu:int):
    """Print 1 digit integer number as 3x5 pixel digit.
    dig: one integer digit 0 to 9.
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""
    #
    #      * * *   0
    #      *   *   1
    #      *   *   2
    #      *   *   3
    #      * * *   4
    #
    #    0 1 2 3
    if dig == 0:

        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,red,grn,blu)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,red,grn,blu)
        sense.set_pixel(1+xo,4+yo,red,grn,blu)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,0,0,0)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,red,grn,blu)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,red,grn,blu)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,red,grn,blu)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #      *
    #      *
    #      *
    #      *
    #      *
    #
    if dig == 1:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,0,0,0)
        sense.set_pixel(1+xo,1+yo,0,0,0)
        sense.set_pixel(1+xo,2+yo,0,0,0)
        sense.set_pixel(1+xo,3+yo,0,0,0)
        sense.set_pixel(1+xo,4+yo,0,0,0)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,red,grn,blu)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,red,grn,blu)
        sense.set_pixel(2+xo,4+yo,red,grn,blu)

        sense.set_pixel(3+xo,0+yo,0,0,0)
        sense.set_pixel(3+xo,1+yo,0,0,0)
        sense.set_pixel(3+xo,2+yo,0,0,0)
        sense.set_pixel(3+xo,3+yo,0,0,0)
        sense.set_pixel(3+xo,4+yo,0,0,0)
    #
    #    * * *
    #        *
    #    * * *
    #    *
    #    * * *
    #
    if dig == 2:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,0,0,0)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,red,grn,blu)
        sense.set_pixel(1+xo,4+yo,red,grn,blu)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,red,grn,blu)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,red,grn,blu)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,0,0,0)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #    * * *
    #        *
    #    * * *
    #        *
    #    * * *
    #
    if dig == 3:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,0,0,0)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,0,0,0)
        sense.set_pixel(1+xo,4+yo,red,grn,blu)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,red,grn,blu)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,red,grn,blu)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,red,grn,blu)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #    *   *
    #    *   *
    #    * * *
    #        *
    #        *
    #
    if dig==4:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,red,grn,blu)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,0,0,0)
        sense.set_pixel(1+xo,4+yo,0,0,0)

        sense.set_pixel(2+xo,0+yo,0,0,0)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,0,0,0)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,red,grn,blu)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,red,grn,blu)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #    * * *
    #    *
    #    * * *
    #        *
    #    * * *
    #
    if dig == 5:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,red,grn,blu)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,0,0,0)
        sense.set_pixel(1+xo,4+yo,red,grn,blu)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,red,grn,blu)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,0,0,0)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,red,grn,blu)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #    *
    #    *
    #    * * *
    #    *   *
    #    * * *
    #
    if dig == 6:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,red,grn,blu)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,red,grn,blu)
        sense.set_pixel(1+xo,4+yo,red,grn,blu)

        sense.set_pixel(2+xo,0+yo,0,0,0)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,red,grn,blu)

        sense.set_pixel(3+xo,0+yo,0,0,0)
        sense.set_pixel(3+xo,1+yo,0,0,0)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,red,grn,blu)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #    * * *
    #        *
    #        *
    #        *
    #        *
    #
    if dig == 7:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,0,0,0)
        sense.set_pixel(1+xo,2+yo,0,0,0)
        sense.set_pixel(1+xo,3+yo,0,0,0)
        sense.set_pixel(1+xo,4+yo,0,0,0)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,0,0,0)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,0,0,0)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,red,grn,blu)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,red,grn,blu)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #    * * *
    #    *   *
    #    * * *
    #    *   *
    #    * * *
    #
    if dig == 8:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,red,grn,blu)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,red,grn,blu)
        sense.set_pixel(1+xo,4+yo,red,grn,blu)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,red,grn,blu)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,red,grn,blu)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,red,grn,blu)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #    * * *
    #    *   *
    #    * * *
    #        *
    #        *
    #
    if dig == 9:
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,red,grn,blu)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,0,0,0)
        sense.set_pixel(1+xo,4+yo,0,0,0)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,0,0,0)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,red,grn,blu)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,red,grn,blu)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)
    #
    #    * * *    E = Error
    #    *
    #    * * *
    #    *
    #    * * *
    #
    if (dig > 9) | (dig < 0):
        sense.set_pixel(0+xo,0+yo,0,0,0)
        sense.set_pixel(0+xo,1+yo,0,0,0)
        sense.set_pixel(0+xo,2+yo,0,0,0)
        sense.set_pixel(0+xo,3+yo,0,0,0)
        sense.set_pixel(0+xo,4+yo,0,0,0)

        sense.set_pixel(1+xo,0+yo,red,grn,blu)
        sense.set_pixel(1+xo,1+yo,red,grn,blu)
        sense.set_pixel(1+xo,2+yo,red,grn,blu)
        sense.set_pixel(1+xo,3+yo,red,grn,blu)
        sense.set_pixel(1+xo,4+yo,red,grn,blu)

        sense.set_pixel(2+xo,0+yo,red,grn,blu)
        sense.set_pixel(2+xo,1+yo,0,0,0)
        sense.set_pixel(2+xo,2+yo,red,grn,blu)
        sense.set_pixel(2+xo,3+yo,0,0,0)
        sense.set_pixel(2+xo,4+yo,red,grn,blu)

        sense.set_pixel(3+xo,0+yo,red,grn,blu)
        sense.set_pixel(3+xo,1+yo,0,0,0)
        sense.set_pixel(3+xo,2+yo,red,grn,blu)
        sense.set_pixel(3+xo,3+yo,0,0,0)
        sense.set_pixel(3+xo,4+yo,red,grn,blu)

def blank(xo: int, yo: int, red: int, grn: int, blu:int):
    """Print blank (no character)
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""
    #
    #            0
    #            1
    #            2
    #            3
    #            4
    #
    #  0 1 2 3
    sense.set_pixel(0+xo,0+yo,0,0,0)
    sense.set_pixel(0+xo,1+yo,0,0,0)
    sense.set_pixel(0+xo,2+yo,0,0,0)
    sense.set_pixel(0+xo,3+yo,0,0,0)
    sense.set_pixel(0+xo,4+yo,0,0,0)

    sense.set_pixel(1+xo,0+yo,0,0,0)
    sense.set_pixel(1+xo,1+yo,0,0,0)
    sense.set_pixel(1+xo,2+yo,0,0,0)
    sense.set_pixel(1+xo,3+yo,0,0,0)
    sense.set_pixel(1+xo,4+yo,0,0,0)

    sense.set_pixel(2+xo,0+yo,0,0,0)
    sense.set_pixel(2+xo,1+yo,0,0,0)
    sense.set_pixel(2+xo,2+yo,0,0,0)
    sense.set_pixel(2+xo,3+yo,0,0,0)
    sense.set_pixel(2+xo,4+yo,0,0,0)

    sense.set_pixel(3+xo,0+yo,0,0,0)
    sense.set_pixel(3+xo,1+yo,0,0,0)
    sense.set_pixel(3+xo,2+yo,0,0,0)
    sense.set_pixel(3+xo,3+yo,0,0,0)
    sense.set_pixel(3+xo,4+yo,0,0,0)

def minus(xo: int, yo: int, red: int, grn: int, blu:int):
    """Print minus sign 
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""
    #
    #            0
    #            1
    #    * * *   2
    #            3
    #            4
    #
    #  0 1 2 3
    sense.set_pixel(0+xo,0+yo,0,0,0)
    sense.set_pixel(0+xo,1+yo,0,0,0)
    sense.set_pixel(0+xo,2+yo,0,0,0)
    sense.set_pixel(0+xo,3+yo,0,0,0)
    sense.set_pixel(0+xo,4+yo,0,0,0)

    sense.set_pixel(1+xo,0+yo,0,0,0)
    sense.set_pixel(1+xo,1+yo,0,0,0)
    sense.set_pixel(1+xo,2+yo,red,grn,blu)
    sense.set_pixel(1+xo,3+yo,0,0,0)
    sense.set_pixel(1+xo,4+yo,0,0,0)

    sense.set_pixel(2+xo,0+yo,0,0,0)
    sense.set_pixel(2+xo,1+yo,0,0,0)
    sense.set_pixel(2+xo,2+yo,red,grn,blu)
    sense.set_pixel(2+xo,3+yo,0,0,0)
    sense.set_pixel(2+xo,4+yo,0,0,0)

    sense.set_pixel(3+xo,0+yo,0,0,0)
    sense.set_pixel(3+xo,1+yo,0,0,0)
    sense.set_pixel(3+xo,2+yo,red,grn,blu)
    sense.set_pixel(3+xo,3+yo,0,0,0)
    sense.set_pixel(3+xo,4+yo,0,0,0)

def minusone(xo: int, yo: int, red: int, grn: int, blu:int):
    """Print minus sign on left and digit 1 on the right 
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""
    #
    #        *   0
    #        *   1
    #  * *   *   2
    #        *   3
    #        *   4
    #
    #  0 1 2 3
    sense.set_pixel(0+xo,0+yo,0,0,0)
    sense.set_pixel(0+xo,1+yo,0,0,0)
    sense.set_pixel(0+xo,2+yo,red,grn,blu)
    sense.set_pixel(0+xo,3+yo,0,0,0)
    sense.set_pixel(0+xo,4+yo,0,0,0)

    sense.set_pixel(1+xo,0+yo,0,0,0)
    sense.set_pixel(1+xo,1+yo,0,0,0)
    sense.set_pixel(1+xo,2+yo,red,grn,blu)
    sense.set_pixel(1+xo,3+yo,0,0,0)
    sense.set_pixel(1+xo,4+yo,0,0,0)

    sense.set_pixel(2+xo,0+yo,0,0,0)
    sense.set_pixel(2+xo,1+yo,0,0,0)
    sense.set_pixel(2+xo,2+yo,0,0,0)
    sense.set_pixel(2+xo,3+yo,0,0,0)
    sense.set_pixel(2+xo,4+yo,0,0,0)

    sense.set_pixel(3+xo,0+yo,red,grn,blu)
    sense.set_pixel(3+xo,1+yo,red,grn,blu)
    sense.set_pixel(3+xo,2+yo,red,grn,blu)
    sense.set_pixel(3+xo,3+yo,red,grn,blu)
    sense.set_pixel(3+xo,4+yo,red,grn,blu)

#
#    * * *  0
#        *  1
#  *   * *  2
#    *      3
#    * * *  4
#  0 1 2 3
def minustwo(xo: int, yo: int, red: int, grn: int, blu:int):
    """Print minus sign on left and digit 2 on the right 
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""
    sense.set_pixel(0+xo,0+yo,0,0,0)
    sense.set_pixel(0+xo,1+yo,0,0,0)
    sense.set_pixel(0+xo,2+yo,red,grn,blu)
    sense.set_pixel(0+xo,3+yo,0,0,0)
    sense.set_pixel(0+xo,4+yo,0,0,0)

    sense.set_pixel(1+xo,0+yo,red,grn,blu)
    sense.set_pixel(1+xo,1+yo,0,0,0)
    sense.set_pixel(1+xo,2+yo,00,00,00)
    sense.set_pixel(1+xo,3+yo,red,grn,blu)
    sense.set_pixel(1+xo,4+yo,red,grn,blu)

    sense.set_pixel(2+xo,0+yo,red,grn,blu)
    sense.set_pixel(2+xo,1+yo,0,0,0)
    sense.set_pixel(2+xo,2+yo,red,grn,blu)
    sense.set_pixel(2+xo,3+yo,0,0,0)
    sense.set_pixel(2+xo,4+yo,red,grn,blu)

    sense.set_pixel(3+xo,0+yo,red,grn,blu)
    sense.set_pixel(3+xo,1+yo,red,grn,blu)
    sense.set_pixel(3+xo,2+yo,red,grn,blu)
    sense.set_pixel(3+xo,3+yo,0,0,0)
    sense.set_pixel(3+xo,4+yo,red,grn,blu)

#
#    * * *  0
#        *  1
#  *   * *  2
#        *  3
#    * * *  4
#  0 1 2 3
def minusthree(xo: int, yo: int, red: int, grn: int, blu:int):
    """Print minus sign on left and digit 3 on the right 
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""
    sense.set_pixel(0+xo,0+yo,0,0,0)
    sense.set_pixel(0+xo,1+yo,0,0,0)
    sense.set_pixel(0+xo,2+yo,red,grn,blu)
    sense.set_pixel(0+xo,3+yo,0,0,0)
    sense.set_pixel(0+xo,4+yo,0,0,0)

    sense.set_pixel(1+xo,0+yo,red,grn,blu)
    sense.set_pixel(1+xo,1+yo,0,0,0)
    sense.set_pixel(1+xo,2+yo,0,0,0)
    sense.set_pixel(1+xo,3+yo,0,0,0)
    sense.set_pixel(1+xo,4+yo,red,grn,blu)

    sense.set_pixel(2+xo,0+yo,red,grn,blu)
    sense.set_pixel(2+xo,1+yo,0,0,0)
    sense.set_pixel(2+xo,2+yo,red,grn,blu)
    sense.set_pixel(2+xo,3+yo,0,0,0)
    sense.set_pixel(2+xo,4+yo,red,grn,blu)

    sense.set_pixel(3+xo,0+yo,red,grn,blu)
    sense.set_pixel(3+xo,1+yo,red,grn,blu)
    sense.set_pixel(3+xo,2+yo,red,grn,blu)
    sense.set_pixel(3+xo,3+yo,red,grn,blu)
    sense.set_pixel(3+xo,4+yo,red,grn,blu)    

#
#  * * * *  0
#  * *   *  1
#  * *   *  2
#  * *   *  3
#  * * * *  4
#  0 1 2 3
def onezero(xo: int, yo: int, red: int, grn: int, blu:int):
    """Print digit 1 on left and digit 0 on the right 
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""

    sense.set_pixel(0+xo,0+yo,red,grn,blu)
    sense.set_pixel(0+xo,1+yo,red,grn,blu)
    sense.set_pixel(0+xo,2+yo,red,grn,blu)
    sense.set_pixel(0+xo,3+yo,red,grn,blu)
    sense.set_pixel(0+xo,4+yo,red,grn,blu)

    sense.set_pixel(1+xo,0+yo,red,grn,blu)
    sense.set_pixel(1+xo,1+yo,red,grn,blu)
    sense.set_pixel(1+xo,2+yo,red,grn,blu)
    sense.set_pixel(1+xo,3+yo,red,grn,blu)
    sense.set_pixel(1+xo,4+yo,red,grn,blu)

    sense.set_pixel(2+xo,0+yo,red,grn,blu)
    sense.set_pixel(2+xo,1+yo,0,0,0)
    sense.set_pixel(2+xo,2+yo,0,0,0)
    sense.set_pixel(2+xo,3+yo,0,0,0)
    sense.set_pixel(2+xo,4+yo,red,grn,blu)

    sense.set_pixel(3+xo,0+yo,red,grn,blu)
    sense.set_pixel(3+xo,1+yo,red,grn,blu)
    sense.set_pixel(3+xo,2+yo,red,grn,blu)
    sense.set_pixel(3+xo,3+yo,red,grn,blu)
    sense.set_pixel(3+xo,4+yo,red,grn,blu)  

#
#    *   *   0
#    *   *   1
#    *   *   2
#    *   *   3
#    *   *   4
#  0 1 2 3
def oneone(xo: int, yo: int, red: int, grn: int, blu:int):
    """Print digit 1 on left and digit 1 on the right 
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""

    sense.set_pixel(0+xo,0+yo,0,0,0)
    sense.set_pixel(0+xo,1+yo,0,0,0)
    sense.set_pixel(0+xo,2+yo,0,0,0)
    sense.set_pixel(0+xo,3+yo,0,0,0)
    sense.set_pixel(0+xo,4+yo,0,0,0)

    sense.set_pixel(1+xo,0+yo,red,grn,blu)
    sense.set_pixel(1+xo,1+yo,red,grn,blu)
    sense.set_pixel(1+xo,2+yo,red,grn,blu)
    sense.set_pixel(1+xo,3+yo,red,grn,blu)
    sense.set_pixel(1+xo,4+yo,red,grn,blu)

    sense.set_pixel(2+xo,0+yo,0,0,0)
    sense.set_pixel(2+xo,1+yo,0,0,0)
    sense.set_pixel(2+xo,2+yo,0,0,0)
    sense.set_pixel(2+xo,3+yo,0,0,0)
    sense.set_pixel(2+xo,4+yo,0,0,0)

    sense.set_pixel(3+xo,0+yo,red,grn,blu)
    sense.set_pixel(3+xo,1+yo,red,grn,blu)
    sense.set_pixel(3+xo,2+yo,red,grn,blu)
    sense.set_pixel(3+xo,3+yo,red,grn,blu)
    sense.set_pixel(3+xo,4+yo,red,grn,blu)  

def show_2_digits(dig: int,xo: int, yo: int, red: int, grn: int, blu: int):
    """Print 2 digit integer number as 3x5 pixel digit.
    dig: one integer digit 0 to 9.
    xo, yo: offset in pixel from upper left, 0,0 is upper left.
    red,grn,blu: brightness 0-255."""
 
    if (dig >= 0)&(dig<=99):
        digtmp = dig
        dig1=int(digtmp/10)
        dig2=int(digtmp-(dig1*10))
        if dig1 >= 1:
            small_letter(dig1,0+xo,yo,red,grn,blu)
        else:
            blank(xo,yo,red,grn,blu)
        small_letter(dig2,4+xo,yo,red,grn,blu)

    if (dig > 99) & (dig <=109):
        digtmp = dig - 100
        dig1=int(digtmp/10)
        dig2=int(digtmp-(dig1*10))
        onezero(xo,yo,red,grn,blu)
        small_letter(dig2,4+xo,yo,red,grn,blu)

    if (dig > 109) & (dig <=119):
        digtmp = dig - 100
        dig1=int(digtmp/10)
        dig2=int(digtmp-(dig1*10))
        oneone(xo,yo,red,grn,blu)
        small_letter(dig2,4+xo,yo,red,grn,blu)

    if (dig < 0) & (dig > -10):
        dig2 = int((dig * -1) )
        minus(xo,yo,red,grn,blu)
        small_letter(dig2,4+xo,yo,red,grn,blu)

    if (dig <= -10) & (dig > -20):
        dig2 = int((dig * -1) -10)
        minusone(xo,yo,red,grn,blu)
        small_letter(dig2,4+xo,yo,red,grn,blu)

    if (dig <= -20) & (dig > -30):
        dig2 = int((dig * -1) -20)
        minustwo(xo,yo,red,grn,blu)
        small_letter(dig2,4+xo,yo,red,grn,blu)

    if (dig <= -30) & (dig > -40):
        dig2 = int((dig * -1) -30)
        minusthree(xo,yo,red,grn,blu)
        small_letter(dig2,4+xo,yo,red,grn,blu)

    if (dig <= -40) | (dig > 119):
        small_letter(1000,0+xo,yo,red,grn,blu)
        small_letter(1000,4+xo,yo,red,grn,blu)

def set_activity(x: int, brightness: int):
    """Show one LED in lower row as green activity indicator
    x: position in bottom row, 0 is left, 7 is right
    brightness: integer 0 to 255"""
    if x < 0 or x > 7:
        x = 7
    red = 0;
    grn = brightness;
    blu = 0;
    sense.set_pixel(x,7,red,grn,blu)

def set_error(x: int, brightness: int):
    """Show one LED in lower row as red error indicator
    x: position in bottom row, 0 is left, 7 is right"""
    if x < 0 or x > 7:
        x = 7
    red = brightness;
    grn = 0;
    blu = 0;
    sense.set_pixel(x,7,red,grn,blu)

def clear_activity(x: int):
    """Clear the activity LED indicator
    x: position in bottom row, 0 is left, 7 is right"""
    sense.set_pixel(x,7,0,0,0)

# On program start...
sense.clear();
sense.set_rotation(0)

if __name__ == '__main__':
    # For debug, cycle through each value
    #
    sense.clear()
    
    t = -40
    while t < 120:        
        show_2_digits(t,0,1,100,100,100)
        t += 1
        time.sleep(0.5)

    sense.clear()