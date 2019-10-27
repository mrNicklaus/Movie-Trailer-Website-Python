import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Woody, Buzz Lightyear and the rest of the gang embark on a "
                        "road trip with Bonnie and a new toy named Forky.",
                        "https://img.yts.lt/assets/images/movies/toy_story_4_2019/medium-cover.jpg",
                        "https://youtu.be/LDXYRzerjzU")

# print(toy_story.storyline)
# toy_story.show_trailer()

avatar = media.Movie("Avatar",
                      "When his brother is killed in a robbery, paraplegic Marine Jake Sully decides "
                      "to take his place in a mission on the distant world of Pandora.",
                       "https://img.yts.lt/assets/images/movies/Avatar_2009/medium-cover.jpg",
                       "https://youtu.be/5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()

the_last_airbender = media.Movie("The Last Airbender",
                        "The world is divided into four kingdoms, each represented by the element they harness, "
                        "and peace has lasted throughout the realms of Water, Air, Earth, and Fire under the supervision of the Avatar, a link to the spirit world and the only being capable of mastering the use of all four elements.",
                        "https://img.yts.lt/assets/images/movies/The_Last_Airbender_2010/medium-cover.jpg",
                        "https://youtu.be/-egQ79OrYCs")

# print(the_last_airbender.storyline)
# the_last_airbender.show_trailer()

dolemite_is_my_name = media.Movie("Dolemite Is My Name",
                        "Eddie Murphy portrays real-life legend Rudy Ray Moore, a comedy and rap pioneer ",
                        "https://img.yts.lt/assets/images/movies/dolemite_is_my_name_2019/medium-cover.jpg",
                        "https://youtu.be/Ws1YIKsuTjQ")


fast_furious_presents_hobbs_shaw = media.Movie("Fast & Furious Presents: Hobbs & Shaw",
                        "Lawman Luke Hobbs and outcast Deckard Shaw form an unlikely alliance when a cyber-genetically enhanced villain threatens the future of humanity.",
                        "https://img.yts.lt/assets/images/movies/fast_furious_presents_hobbs_shaw_2019/medium-cover.jpg",
                        "https://youtu.be/9SA7FaKxZVI")


the_lion_king = media.Movie("The Lion King",
                        "After the murder of his father, a young lion prince flees his kingdom only to learn the true meaning of responsibility and bravery.",
                        "https://img.yts.lt/assets/images/movies/the_lion_king_2019/medium-cover.jpg",
                        "https://youtu.be/4CbLXeGSDxg")


the_secret_life_of_pets_2 = media.Movie("The Secret Life Of Pets 2",
                        "Max faces some major changes after his owner Katie gets married and now has a child",
                        "https://img.yts.lt/assets/images/movies/the_secret_life_of_pets_2_2019/medium-cover.jpg",
                        "https://youtu.be/pKLGUuJftl0")

movies = [toy_story, avatar, the_last_airbender, dolemite_is_my_name,
          fast_furious_presents_hobbs_shaw, the_lion_king, the_secret_life_of_pets_2]

fresh_tomatoes.open_movies_page(movies)
