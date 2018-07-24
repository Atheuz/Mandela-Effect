"""Quick little Mandela Effect flip-flop hashing."""
from datetime import date
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
             ('Chick-fil-A', 'Chic-fil-A'),
             ('Sex and the City', 'Sex in the City'),
             ('Life was like a box of chocolates',
              'Life is like a box of chocolates'),
             ('Monopoly man does not have a monocle', 'Monopoly man has a monocle'),
             ('JCPenney', 'JCPenny'),
             ('Mona Lisa smirks', 'Mona Lisa does not smirk'),
             ('KitKat', 'Kit-Kat'),
             ('Interview with the Vampire', 'Interview with a Vampire'),
             ('Magic Mirror on the Wall', 'Mirror, Mirror on the Wall'),
             ('Pikachu tail = all yellow', 'Pikachu tail = yellow with black tip'),
             ('Jif Peanut Butter', 'Jiffy Peanut Butter'),
             ('Im a barbie girl, in the barbie world',
              'Im a barbie girl, in a barbie world'),
             ('Daylight Saving Time', 'Daylight Savings Time'),
             ('Looney Tunes', 'Looney Toons'),
             ('Pixy Stix', 'Pixie Stix'),
             ('Chartreuse = Green', 'Chartreuse = Reddish'),
             ('Febreze', 'Febreeze'),
             ('Cup Noodles', 'Cup O Noodles'), ]


def main():
    """Main entry point."""
    h = blake2b(digest_size=20)
    # We only want to hash the left 'current' world-line.
    for flip, _ in FLIPFLOPS:
        h.update(flip.encode())
    hexdigest = h.hexdigest()
    now = datetime.now()
    msg = "dt: {0} - hash: {1}\n".format(now, hexdigest)
    with open("HASH-{}".format(date.today().isoformat()), "w") as f:
        print(msg)
        f.write(msg)


if __name__ == '__main__':
    main()
