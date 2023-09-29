import math
from tqdm import tqdm

def pollard_rho(N):
    # Polynomial function g(x) = (x^2 + 1) mod N
    def g(x):
        return (x**2 + 1) % N

    x = 2
    y = 2
    d = 1

    with tqdm(total=N) as progress:
        while d == 1:
            x = g(x)
            y = g(g(y))
            d = math.gcd(abs(x - y), N)
            progress.update(1)

    if d == N:
        return "Failure: No non-trivial factors found"
    else:
        return f"Found factor: {d}"

# Usage example
N = 75028926564243095350876556253054002059048724162557616616984189236507249837906571739103341249511617617686728055121809964555365800748123277977503402143848791135583759511900470314822144753821175349989759114593174302727420916174556594489335976199015832911621980456957179023125962485241644610617345637998571255579
result = pollard_rho(N)
print(result)
