def merge_intervals(intervalos):
    if not intervalos:
        return []

    intervalos.sort(key=lambda x: x[0])

    merged = [intervalos[0]]

    for atual in intervalos[1:]:
        last_merged = merged[-1]
        if atual[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], atual[1])
        else:
            merged.append(atual)

    return merged
