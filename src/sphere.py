import sys
import math
import vector
from vector import Vector3
from point import Point

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

        new_point = Point(X = math.sin(phi) * math.sin(theta),
                              Y = math.cos(phi) * math.sin(theta),
                              Z = -math.cos(theta))
        new_point.position += position
        points.append(new_point)
        phi %= 2*math.pi

    return points



if __name__ == "__main__" :
    points = calc_points(200, Vector3(0,0,0))
    for i, ipoint in enumerate(points) :
        for j , jpoint in enumerate(points[i+1:]):
            d =  ipoint.dist_to(jpoint)
            if d < 0.3:
                ipoint.connect(jpoint)
    for i, point in enumerate(points) :
        p=point.position
        print("{:6s}{:5d}{:^4s}{:1s}{:3s} {:1s}{:4d}{:>4s}{:8.3f}{:8.3f}{:8.3f}"
              .format("HETATM", point.num_point, "O", "", "HOH", "A", point.num_point , "  ",
                      p.x, p.y, p.z))

    for i, point in enumerate(points):
        if len(point.voisins) == 0 :
            continue
        print("CONECT",end = "")
        print("{:>5}".format(point.num_point), end ="")
        for j, voisin in enumerate(point.voisins):
            print("{:>5}".format(voisin.num_point), end = "")
        print()
