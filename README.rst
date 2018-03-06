==========
lightcheck
==========


.. image:: https://img.shields.io/pypi/v/lightcheck.svg
        :target: https://pypi.python.org/pypi/lightcheck

.. image:: https://img.shields.io/travis/FrauBoes/lightcheck.svg
        :target: https://travis-ci.org/FrauBoes/lightcheck

.. image:: https://readthedocs.org/projects/lightcheck/badge/?version=latest
        :target: https://lightcheck.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Lightcheck counts lights in a grid and r returns lights on.


* Free software: MIT license

Description
--------

COMP30670 Assignment 3
The Science Centre is installing a new display board which is constructed from LED lights.

The board is a square grid of LEDs which we control by sending commands to the unit to turn on or off certain rectangular regions.

The L×L lights can be modelled as a 2 dimensional grid with L rows of lights and L lights in each row and the LED's at each corner are (0, 0), (0, L−1), (L−1, L−1) and (L−1, 0).

The lights are either on or off.

The task of the application is to test the lights. We test them by sending instructions to turn on, turn off, or switch various inclusive ranges given as coordinate pairs. 
Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. 
The lights all start turned off.

Features
--------

After installing the app, you can run it using the following command:

lightcheck --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt
solve_led --input ./data/input_assign3.txt

The input is a file with instructions in the following format:

999
turn on 0,0 through 999,999
switch 0,0 through 999,0
turn off 499,499 through 500,500

The input can be a url or a local file (in this case the path has to be given)

The app returns the number of lights that are on after all instructions are executed.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
