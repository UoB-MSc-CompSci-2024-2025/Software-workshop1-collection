class User:
    def __init__(self, user_id, name, is_premium=False):
        self.user_id = user_id
        self.name = name
        self.is_premium = is_premium
        self.play_history = []

    def play_song(self, song):
        print(f"Now playing {song.title} by {song.artist}")
        self.play_history.append(song)
        song.increment_song_count()

    def view_history(self):
        if not self.play_history:
            print("No songs played yet.")
        else:
            print(f"Play history for {self.name}:")
            for history in self.play_history:
                print(history)

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Premium: {self.is_premium}"


class FreeUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, is_premium=False)

    def play_song(self, song):
        print("Enjoy uninterrupted music by upgrading to premium!")
        super().play_song(song)


class PremiumUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, is_premium=True)

    def download_song(self, song):
        print(f"{song.title} by {song.artist} has been downloaded.")


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.play_count = 0

    def increment_song_count(self):
        self.play_count += 1

    def __str__(self):
        return f"{self.title} by {self.artist} (Plays: {self.play_count})"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song in self.songs:
            print(f"{song.title} is already in the playlist '{self.name}'.")
        else:
            self.songs.append(song)
            print(f"Added {song.title} to playlist '{self.name}'.")

    def view_songs(self):
        print(f"Playlist: {self.name}")
        if not self.songs:
            print("No songs in this playlist yet.")
        else:
            for song in self.songs:
                print(song)


class Admin:
    def __init__(self, admin_id, name, library):
        self.admin_id = admin_id
        self.name = name
        self.users = {}
        self.library = library
        self.playlists = {}

    def add_user(self, user):
        self.users[user.user_id] = user
        print(f"User {user.name} (ID: {user.user_id}) added.")

    def view_users(self):
        print("All Users:")
        for user in self.users:
            print(user)

    def add_playlist(self, playlist):
        if playlist.name in self.playlists:
            print(f"A playlist named '{playlist.name}' already exists.")
        else:
            self.playlists[playlist.name] = playlist
            print(f"Playlist '{playlist.name}' has been created.")

    def view_playlists(self):
        if not self.playlists:
            print("No playlists available.")
        else:
            print("Available Playlists:")
            for key in self.playlists.keys():
                print(f'These are the playlists you have - {key}')


class Library:
    def __init__(self):
        self.songs = []

    def add_song_library(self, song):
        if song in self.songs:
            print(F"{song.title} by {song.artist} is already in the library")
        else:
            self.songs.append(song)
            print(f"Song {song.title} by {song.artist} added to the library.")

        print(self.songs)

    def view_library(self):
        print("All the songs in the Library:")
        if not self.songs:
            print("There are no songs in the library")
        else:
            for song in self.songs:
                print(song)



def validate_user_type(user_id):
    if user_id is not None and user_id[0] == 'F':
        return FreeUser
    else:
        return PremiumUser


def create_user(user_id, name):
    if validate_user_type(user_id):
        return FreeUser(user_id, name)
    else:
        return PremiumUser(user_id, name)


def song_choice():
    which_song = input("Enter the number of the song to add: ")
    if which_song == '':
        print('please enter the number of the song')
    else:
        which_song = int(which_song)

    return which_song


def main():
    library = Library()
    admin = Admin(admin_id="admin1", name="SuperAdmin", library=library)
    playlist = None

    while True:
        try:
            choice = int(input(
                "\nMusic Streaming App\n"
                "1. Create a User\n"
                "2. Add a Song to the library\n"
                "3. Create a Playlist and Add Songs\n"
                "4. Play a Song\n"
                "5. View Playlist\n"
                "6. View User History\n"
                "7. Admin: View All Songs\n"
                "8. Admin: View All Users\n"
                "9. Exit\n"
                "Enter your choice: "
            ))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match choice:
            case 1:
                user_id = input("Enter User ID: ")
                name = input("Enter Name: ")

                user = create_user(user_id, name)
                admin.add_user(user)
                # check the type of the user for programmer confirmation
                print(type(admin.users[user_id]))

            case 2:
                song_id = input("Enter Song ID: ")
                title = input("Enter Song Title: ")
                artist = input("Enter Song Artist: ")
                library.add_song_library(Song(song_id, title, artist))

            case 3:
                if not admin.users:
                    print("No users available. Create a user first.")
                    continue

                playlist_name = input("Enter Playlist Name: ")
                if playlist_name in admin.playlists:
                    print(f"A playlist named '{playlist_name}' already exists.")
                    playlist = admin.playlists[playlist_name]
                else:
                    playlist = Playlist(playlist_name)
                    admin.add_playlist(playlist)

                while True:
                    add_more = input("Add a song to the playlist? (yes/no): ").lower()
                    if add_more == "no":
                        break

                    if not admin.library.songs:
                        print("No songs in the library to add to the playlist")
                        break

                    for i, song in enumerate(admin.library.songs, 1):
                        print(f"{i}. {song}")

                    song_choice_by_user = song_choice()
                    if 0 < song_choice_by_user <= len(admin.library.songs):
                        playlist.add_song(admin.library.songs[song_choice_by_user - 1])
                        print(playlist.songs)
                    else:
                        print('choose the number from the songs shown')

            case 4:
                if not admin.users:
                    print("No users available. Create a user first.")
                    continue
                user_id = input("Enter your User ID: ")
                user = admin.users.get(user_id)

                if not user:
                    print("User not found. Please try again.")
                    continue
                if not playlist or not playlist.songs:
                    print("No playlist or songs available. Create one first.")
                    continue
                temp = {}
                for i, song in enumerate(playlist.songs, 1):
                    print(f"{i}. {song}")
                    temp[i] = song

                song_choice_by_user = song_choice()
                if 0 < song_choice_by_user <= len(playlist.songs):
                    user.play_song(temp[song_choice_by_user])

                else:
                    print('choose the number from the songs shown')

            case 5:
                if not admin.playlists:
                    print('No playlist available')
                    continue

                admin.view_playlists()
                playlist_name = input("Enter the playlist name to view songs: ")
                playlist = admin.playlists.get(playlist_name)
                if not playlist:
                    print('The searched play list is not available')
                else:
                    playlist.view_songs()


            case 6:
                user_id = input("Enter your User ID: ")
                user = admin.users.get(user_id)
                if not user:
                    print('The user is not available')
                else:
                    user.view_history()

            case 7:
                admin.library.view_library()

            case 8:
                admin.view_users()

            case 9:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
