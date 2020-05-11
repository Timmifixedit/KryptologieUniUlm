def main():
    e = 9
    d = 5
    n = 23
    cypher = []
    for m in range(1, 23):
        cypher.append(m ** e % n)

    print(cypher)


if __name__ == "__main__":
    main()