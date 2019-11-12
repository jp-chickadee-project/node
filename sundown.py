import sys
import math
from datetime import datetime, timezone

logitudeWest = 87.397552
latitudeNorth = 46.543911

def getCurrentJulianDay(rnd):
    """Returns current julian day number including time.
    
    JDN = (1461*(year+4800+(month-14)/12))/4+(367*(month-2-12*((month-14)/12)))/12-3)3*
    ((year+4900+(month-14)/12)/100))/4+day-32075

    use previous day if caluclaulating an instant before 12pm UTC
    rnd is true if you want the JDN rounded to an integer
    """
    now = datetime.now(timezone.utc)
    if(now.hour < 12):
        now = now.replace(now.year, now.month, now.day - 1)#'''

    year, month, day = now.year, now.month, now.day
    a = int((1461 * (year + 4800 + int((month - 14) / 12))) / 4)
    b = int((367 * (month - 2 - 12 * int((month - 14) / 12 ))) / 12)
    c = int((3 * int((year + 4900 + int((month - 14) / 12)) / 100)) / 4)
    JDN = a + b - c + day - 32075
    JDN = JDN + ((now.hour - 12) / 24.0) + (now.minute / 1440.0) + (now.second / 86400.0) + 1.0
    #JDN = 2458799
    if rnd:
        return round(JDN)
    else:
        return JDN


def getjStar(n):
    return 2451545 + .0009 + (logitudeWest/360) + n


def getSolarMean(jStar):
    """M."""
    return (357.5291 + .98560028 * (jStar - 2451545)) % 360


def getCenter(Mrads):
    return (1.9148 * math.sin(Mrads)) + (.02 * math.sin(2 * Mrads) + (.0003 * math.sin(3 * Mrads)))


def getEclipLogi(M, C):
    return (M + 102.9372 + C + 180) % 360


def getjTransit(jStar, Mrads, lamRads):
    return jStar + (.0053 * math.sin(Mrads)) - (.0069 * math.sin(2 * lamRads))


def refineSolarMean(jTransit, M, jStar):
    newM = getSolarMean(jTransit)
    Mrads = math.radians(newM)
    C = getCenter(Mrads)
    lam = getEclipLogi(M, C)
    lamRads = math.radians(lam)
    jTransit = getjTransit(jStar, Mrads, lamRads)
    if M != newM:
        return refineSolarMean(jTransit, newM, jStar)
    else:
        return newM, Mrads, C, lam, lamRads, jTransit


def getHourAngle(lamRads):
    delta = math.asin(math.sin(lamRads) * math.sin(math.radians(23.45)))
    a = math.sin(math.radians(-.83))
    b = math.sin(math.radians(latitudeNorth))
    c = math.sin(delta)
    x = math.cos(math.radians(latitudeNorth))
    y = math.cos(delta)
    before = (a - b * c) / (x * y)
    return math.acos(before)


def getSunriseAndSunset(jDate=-1):
    jRise = []
    jSet = []
    if jDate == -1:
        jDate = getCurrentJulianDay(True)
        
    for i in range(14):
        n = round(jDate + i - 2451545 - 0.0009 - (logitudeWest/360))
        jStar = getjStar(n)
        M = getSolarMean(jStar)
        Mrads = math.radians(M)
        C = getCenter(Mrads)
        lam = getEclipLogi(M, C)
        lamRads = math.radians(lam)
        jTransit = getjTransit(jStar, Mrads, lamRads)
        M, Mrads, C, lam, lamRads, jTransit = refineSolarMean(jTransit, M, jStar)
        H = getHourAngle(lamRads)
        jStar = 2451545 + .0009 + ((math.degrees(H) + logitudeWest) / 360) + n
        jSet.append(jStar + (.0053 * math.sin(Mrads)) - (.0069 * math.sin(2 * lamRads)))
        jRise.append(jTransit - (jSet[i] - jTransit))

    return jRise, jSet
    

def testLib():
    jRise, jSet = getSunriseAndSunset(2458843)
    assert jRise[0] - 2458843.06389 > (5 / 14400), "\033[31m Sunrise calculations not within tollerance\033[39m"
    return True


def main():
    jRise, jSet = getSunriseAndSunset()
    print(jRise[0])
    testLib()


if __name__ =='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)


