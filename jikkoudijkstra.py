import dijkstra as dks


if __name__ == "__main__":
    edges = [
        ("A", "B", 0.0000000000007),
        ("A", "D", 0.5),
        ("B", "C", 0.8),
        ("B", "D", 0.9),
        ("B", "E", 0.7),
        ("C", "E", 0.5),
        ("D", "E", 0.15),
        ("D", "F", 0.6),
        ("E", "F", 0.8),
        ("E", "G", 0.9),
        ("F", "G", 0.11)
    ]

    print (edges)
    print ('a to e')
    a=str('A')
    print (dks.dijkstra(edges, a, "E"))
    print ("F -> G:")
    print (dks.dijkstra(edges, "F", "G"))
