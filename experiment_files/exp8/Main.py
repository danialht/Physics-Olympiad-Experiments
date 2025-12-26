from scipy.integrate import quad
from scipy.constants import epsilon_0
import math
from math import sqrt
from math import cos
from math import sin
from math import asinh


# Rho and z are the point's cylindrical coordinates in the disc's plane.
def calculate_integral(z, rho, radius) -> float:
    def integrand(phi) -> float:
        if phi == 0 or phi == math.pi:
            return 0.0

        return (sqrt(z ** 2 + rho ** 2 + radius ** 2 - 2 * rho * radius * cos(phi)) - sqrt(z ** 2 + rho ** 2)
                + rho * cos(phi) * (
                        asinh((radius - rho * cos(phi)) / sqrt(z ** 2 + (rho * sin(phi)) ** 2))
                        + asinh((rho * cos(phi)) / sqrt(z ** 2 + (rho * sin(phi)) ** 2))))

    def calculate() -> float:
        a, b = 0, math.pi * 2
        singular_points = [0, math.pi]
        result_arr = quad(integrand, a, b, points=singular_points, epsabs=1E-9, epsrel=1E-9)
        return result_arr[0]

    # A problematic singularity point hard coded to avoid any possible problems.
    return 2 * math.pi * radius if rho == 0 and z == 0 else calculate()


# Calculates rho then z
def calculate_distances(coords: list[float]) -> list[float]:
    # The plane's equation is: 1.456x-2.333y+1.000z = 1.000 aka: ax + by + cz = 1
    a, b, c = 1.456, -2.333, 1.0

    x, y, z = coords

    dist_to_center = round(
        sqrt((x - center_coords[0]) ** 2 + (y - center_coords[1]) ** 2 + (z - center_coords[2]) ** 2), 3)

    z_ans = round(math.fabs(a * x + b * y + c * z - 1) / sqrt(a ** 2 + b ** 2 + c ** 2), 3)

    try:
        rho_ans = sqrt(dist_to_center ** 2 - z_ans ** 2)
    except:  # Handles the extreme edge case of floating point errors causing the sqrt argument to be negative.
        rho_ans = 0.0

    return [rho_ans, z_ans]


def clamp(start, end, value):
    return max(min(value, end), start)


def experiment_mode_a():
    measurement_coordinates: list[float] = [0, 0, 0]
    print("Note that all coordinates must be between 0.0 and 10.0")
    while True:
        try:
            measurement_coordinates[0] = float(input("Enter measurement coordinate x in meters: "))
            measurement_coordinates[1] = float(input("Enter measurement coordinate y in meters: "))
            measurement_coordinates[2] = float(input("Enter measurement coordinate z in meters: "))
        except TypeError:
            print("Please enter valid numbers!")
            continue
        break
    measurement_coordinates[0] = clamp(0, cube_length, measurement_coordinates[0])
    measurement_coordinates[1] = clamp(0, cube_length, measurement_coordinates[1])
    measurement_coordinates[2] = clamp(0, cube_length, measurement_coordinates[2])
    rho, z = calculate_distances(measurement_coordinates)
    result = calculate_integral(z, rho, radius)
    result *= (sigma / (4 * math.pi * epsilon_0))
    print(f"Electric Potential in Volts: {result:.3e}")


def experiment_mode_b():
    while True:
        try:
            print("Input number of measurements on each axis:\n"
                  "Warning: trying to take more than 4000 measurements will take a long time!")
            num_x = int(input("x axis: "))
            num_y = int(input("y axis: "))
            num_z = int(input("z axis: "))
        except TypeError:
            print("Please enter valid integers!")
            continue
        break

    with open("result.txt", "a") as file:
        file.write("------------------------------------------\n")
        file.write("X\tY\tZ\tV\n")

    for i in range(num_x):
        for j in range(num_y):
            for k in range(num_z):
                x = i * cube_length / num_x
                y = j * cube_length / num_y
                z = k * cube_length / num_z
                rho, z_ans = calculate_distances([x, y, z])
                result = calculate_integral(z_ans, rho, radius)
                result *= (sigma / (4 * math.pi * epsilon_0))
                with open("result.txt", "a") as file:
                    file.write(str(round(x, 3)) + "\t" + str(round(y, 3)) + "\t" + str(round(z, 3)) + "\t" + str(result) + "\n")
    print("Results saved to result.txt")


if __name__ == '__main__':
    # All in SI units.
    radius: float = 0.221
    sigma: float = 1.365E-8
    cube_length: float = 10
    # (x, y, z)
    center_coords = (4.231, 5.166, 6.892)
    # The plane's equation is: 1.456x-2.333y+1.000z = 1.000
    while True:
        try:
            experiment_mode = input("Please enter the experiment mode: (A for single data, B for auto measure) ")
            if experiment_mode != "A" and experiment_mode != "B":
                raise ValueError
        except ValueError:
            print("Please enter a valid input")
            continue
        break

    if experiment_mode == "A":
        experiment_mode_a()
    else:
        experiment_mode_b()
