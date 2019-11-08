from datetime import datetime

def main():
    """docstring placeholder.
    
    write more stuff here
    """
    sys.exit(0)


""" Calculate current Julian day (n) """

""" Calculate mean solar noon (J*) - uses n """

""" Calculate solar mean anomaly (M) - uses J* """

""" Calculate equation of center (C) - uses M """

""" Calculate ecliptic longitude (lambda) - uses M and C """

""" Calculate declination of the sun (delta) - uses lambda """

""" Calculate hour angle (lower omega (w)) - uses lat & long of Marquette """

""" Calculate solar transit (Jtransit) - uses J*, M, 2(lambda) """

"""  Calculate Jrise and Jset (sunrise and sunset) - uses Jtransit, lowerOmega(w) """

if __name__ == '__main__':
    try():
        main()
    except KeyboardInterrupt:
        sys.exit(1)


