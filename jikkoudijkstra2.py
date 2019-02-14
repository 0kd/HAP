import dijkstra as dks


if __name__ == "__main__":
    edges2 = [
            ('10X1.counthapleft', '10X2.counthapleft', 0.022736545599999998), 
            ('10X1.counthapleft', '10X3.counthapleft', 0.0015585456000000004),
            ('10X2.counthapleft', '10X3.counthapleft', 0.021821999999999998), 
            ('10X1.counthapright', '10X2.counthapleft', 0.000124673238),
            ('10X10.counthapright', '10X3.counthapright', 0.010322),
            ('10X10.counthapleft', '10X2.counthapright', 0.0101),
            ('10X10.counthapleft', '10X3.counthapleft', 0.010322),
            ('10X2.counthapright', '10X3.counthapleft', 0.00042200000000000007),
            ('10X2.counthapright', '10X3.counthapright', 0.00042200000000000007)]

    edges = [
        ('A.a', "B", 0.00042200000000000007),
        ('A.a', "D", 0.00042200000000000007),
        ("B", "C", 0.8),
        ("B", "D", 0.9),
        ("B", "1E", 0.7),
        ("C", "1E", 0.5),
        ("D", "1E", 0.15),
        ("D", "F", 0.6),
        ("1E", "F", 0.8),
        ("1E", "G", 0.9),
        ("F", "G", 0.11)
    ]

    print (edges)
    print ('a to e')
    a=str('A.a')
    print (dks.dijkstra(edges, a, "1E"))
    print ("F -> G:")
    print (dks.dijkstra(edges2, "10X1.counthapleft", "10X3.counthapleft"))
