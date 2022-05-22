from Analysis.RandomCalculatons import IsPrime


def AllowableUps(num_of_pts):
    factors = []
    if IsPrime(num_of_pts):
        return 0

    else:
        for i in range(2, num_of_pts):
            if num_of_pts % i == 0:
                factors.append(i)
    return factors
