def resource_allocation(tasks, resources):
    allocation = []

    for i, task in enumerate(tasks):
        resource = resources[i % len(resources)]

        energy = task * resource["energy_factor"]
        cost = task * resource["cost_factor"]

        allocation.append({
            "task": i + 1,
            "resource": resource["name"],
            "energy": energy,
            "cost": cost
        })

    return allocation
