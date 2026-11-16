import matplotlib.pyplot as plt


def demand_supply_simulation():
    # Demand parameters
    a = 100
    b = 2

    # Supply parameters
    c = 10
    d = 3

    # Price range
    prices = range(0, 51)

    # Calculate demand and supply
    demand = []
    supply = []

    for price in prices:
        qd = max(0, a - b * price)
        qs = max(0, c + d * price)

        demand.append(qd)
        supply.append(qs)

    # Calculate equilibrium
    equilibrium_price = (a - c) / (b + d)
    equilibrium_quantity = a - b * equilibrium_price

    print("Market Equilibrium")
    print("------------------")
    print("Equilibrium Price:", equilibrium_price)
    print("Equilibrium Quantity:", equilibrium_quantity)

    # Plot demand and supply curves
    plt.figure(figsize=(9, 5))

    plt.plot(prices, demand, label="Demand", color="blue")
    plt.plot(prices, supply, label="Supply", color="red")

    plt.scatter(equilibrium_price, equilibrium_quantity,
                color="green", s=100,
                label="Equilibrium Point")

    plt.axvline(equilibrium_price, linestyle="--",
                color="gray")

    plt.axhline(equilibrium_quantity, linestyle="--",
                color="gray")

    plt.title("Demand and Supply Simulation")
    plt.xlabel("Price")
    plt.ylabel("Quantity")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    demand_supply_simulation()