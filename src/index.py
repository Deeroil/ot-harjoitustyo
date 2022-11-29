from grid import Grid
from minesweeper import Minesweeper

# TODO:
#     - uudelleennimeä grid_list englanniksi, ehkä ennemminkin joku_list?
#     - miten sliceet kivasti printattavasti taulukon, ehkä if index % row_len == 0?
#     - naapureiden laskenta, haluanko bound checking funktion erikseen?
#         - jokaiselle ruudulle: +1 joka naapuripommista, talleta ruutuun naapurien määrä
#         - pommin merkitseminen varmaan lukuna 9 tai 10
#     - tulosta grid_list jossa näkyy naapurit, tyhjät ja pommit
#         - 0: tyhjä
#         - 1-8: montako pomminaapuria
#         - 9: pommi/miina
#     - funktio jolla voi valita ("klikata") jonkun ruuduista: mitä tapahtuu?
#           - jos tyhjä: näytä vierekkäiset / return lista jossa vierekkäiset
#           - jos pommi: peli loppuu (aluksi esim: printtaa "Peli loppui")
#           - jos numero: return numero
#     - muista testit! toimiiko random.seed() kivasti, vai mielummin käsin tehdyt taulukot?
#     - onks se siistimpää selkeästi palauttaa grid_list vai muuttaa sitä funktion sisällä xd
#     - myös virheidenkäsittely!

# Note:
# there are still bugs with the neighbors, should rewrite bounds
if __name__ == "__main__":

    # repeat = True
    # while repeat:
        n = int(input(
            "Create a minesweeper grid of what size? (0 or negative will quit program) "))
        if n <= 0:
            # break
            quit()
        m = int(input("And how many mines? "))

        grid = Grid(n)
        grid.set_mines(m)
        grid.set_neighbors()

        # prints
        x = ""
        for i in range(grid.len):
            if i % grid.width == 0:
                x += "\n"
            x += f" {grid.grid[i]} "
        print(x)

        print("\n")

        msweep = Minesweeper(grid)

        while True:
          x_koord = int(input("Mikä x-koordinaatti?"))
          y_koord = int(input("Mikä y-koordinaatti?"))

          index = x_koord + y_koord*grid.width

          msweep.check_tile(index)
          msweep.add_shown_tiles(index)
          # msweep.add_shown_tiles(0)
          # ei oo lopetusehtoa paitsi miinaan osuminen

        
