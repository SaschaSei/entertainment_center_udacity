import media
import fresh_tomatoes

""" Creating the movies and assigning values to: title, stroyline,
    poster_image_url, trailer_youtube_url
"""
toy_story = media.Movie(
    "Toy Stroy", "A story of a boy and his toys come to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar", "Marine on an alien planet.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=1FcaRebb-bM")

pulp_fiction = media.Movie(
    "Pulp Fiction", "",
    "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

school_of_rock = media.Movie(
    "School of Rock", "Jack Black teaching Rock",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

lucky_number_slevin = media.Movie(
    "Lucky Number S7evin",
    "Two underworld bosses, a mysterious hitman, and some guy in between",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/Lucky_Number_Slevin_Theater_Poster.JPG",
    "https://www.youtube.com/watch?v=fVIUEcizkPc")

full_metal_jacket = media.Movie(
    "Full Metal Jacket",
    "The story of young Americans who become soldiers in the Vietnam war.",
    "https://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",
    "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

movies = [toy_story, avatar, pulp_fiction, school_of_rock, lucky_number_slevin,
    full_metal_jacket]

fresh_tomatoes.open_movies_page(movies)
