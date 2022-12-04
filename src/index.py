from ui.cli import CLI
# TODO: kaikenlaista
#     - tulosta grid_list jossa näkyy naapurit, tyhjät ja pommit
#         - 0: tyhjä
#         - 1-8: montako pomminaapuria
#         - 9: pommi/miina
#     - muista testit! toimiiko random.seed() kivasti, vai mielummin käsin tehdyt taulukot?
#         - testaa kans bound checker
#     - myös virheidenkäsittely!

# Note:
# there are still bugs with the neighbors, should rewrite bounds
if __name__ == "__main__":
    game = CLI()
    game.play()
