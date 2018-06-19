"""Quick little Mandela Effect flip-flop hashing."""
from datetime import datetime
from hashlib import blake2b

FLIPFLOPS = [("Houston, we've had a problem", 'Houston, we have a problem'),
             ('Froot Loops', 'Fruit Loops'),
             ('Hillary Clinton', 'Hilary Clinton'),
             ('Flintstones', 'Flinstone'),
             ('Tidy Cats', 'Tidy Cat'),
             ('Rice Krispies', 'Rice Crispy'),
             ('Bud light', 'Bud lite'),
             ('Reba McEntire', 'Reba McIntyre'),
             ('Chick-fil-A', 'Chic-fil-A'), ]


def main():
    """Main entry point."""
    h = blake2b(digest_size=20)
    # We only want to hash the left 'current' world-line.
    for flip, _ in FLIPFLOPS:
        h.update(flip.encode())
    hexdigest = h.hexdigest()
    now = datetime.now()
    msg = "dt: {0} - hash: {1}\n".format(now, hexdigest)
    with open("HASH", "w") as f:
        print(msg)
        f.write(msg)


if __name__ == '__main__':
    main()
