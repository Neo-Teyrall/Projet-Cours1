import sys
import math
import vector
from vector import Vector3


def calc_points(number_points : int, position : Vector3, angle = None):
    """reprise de l'algoryhtme de sphère de saff copié et modifié depuis le
    packet anti_lib_progs"""
    points = []
    use_angle = angle is not None
    if use_angle:
        ang = (angle * math.pi/180) % (2*math.pi)

    N = number_points
    for k in range(1, N + 1):
        h = -1 + 2 * (k - 1) / float(N - 1)
        theta = math.acos(h)
        if k == 1 or k == N:
            phi = 0
        elif use_angle:
            phi += ang
        else:
            phi += 3.6 / math.sqrt(N * (1 - h * h))

        points.append(Vector3(X = math.sin(phi) * math.sin(theta),
                              Y = math.cos(phi) * math.sin(theta),
                              Z = -math.cos(theta)) + position)
        phi %= 2*math.pi

    return points



if __name__ == "__main__" :
    points = calc_points(96, Vector3(10,10,10))
    for i, point in enumerate(points) :
        p = (point)
        print("{:6s}{:5d}{:^4s}{:1s}{:3s}{:1s}{:4d}{:1s}{:8.3f}{:8.3f}{:8.3f}\n"
              .format("HETATM", i, "O", "", "HOH", "A", i, "",
                      p[0], p[1], p[2]))
    
