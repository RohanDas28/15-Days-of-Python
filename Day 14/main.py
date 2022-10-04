#pip install AnilistPython
from AnilistPython import Anilist
anilist = Anilist()

def getAnime():
    animeName= input("Enter the name of the anime: ")
    anilist.print_anime_info(animeName)
def getManga():
    mangaName = input("Enter the name of the manga: ")
    anilist.print_manga_info(mangaName)
def getCharacter():
    characterName = input("Enter the name of the character: ")
    anilist.print_character_info(characterName)

def main():
    print("Welcome")
    print("1. Get Anime Info")
    print("2. Get Manga Info")
    print("3. Get Character Info")
    print("4. Exit")
    ch = input("Enter your choice: ")
    match ch:
        case "1":
            getAnime()
        case "2":
            getManga()
        case "3":
            getCharacter()
        case "4":
            exit()
        case _:
            print("Invalid choice")

main()

