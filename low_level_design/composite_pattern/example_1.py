"""
Link-1(Bangla) : https://software-engineering-notes-in-bangla.blogspot.com/2019/05/composite-design-pattern.html
"""

"""
The following example description belongs to Link-1.
"""

from abc import ABC, abstractmethod

class IComponent(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def set_playback_speed(self, speed: float):
        pass

    @abstractmethod
    def get_name(self):
        pass


class Song(IComponent):
    def __init__(self, song_name: str, artist: str):
        self.song_name = song_name
        self.artist = artist
        self.speed = 1.0

    def play(self):
        print(f'Playing the song : {self.song_name}')

    def set_playback_speed(self, speed: float):
        self.speed = speed

    def get_name(self):
        return self.song_name

    def get_artist(self):
        return self.artist


class Playlist(IComponent):
    def __init__(self, playlist_name: str):
        self.playlist_name = playlist_name
        self.playlist = []

    def play(self):
        for component in self.playlist:
            component.play()

    def set_playback_speed(self, speed: float):
        for component in self.playlist:
            component.set_playback_speed(speed)

    def get_name(self):
        return self.playlist_name

    def add(self, component: IComponent):
        self.playlist.append(component)

    def remove(self, component: IComponent):
        self.playlist.remove(component)

"""
Q : কেন এখানে component: Song এর বদলে component: IComponent ব্যবহার করা হয়েছে?
-> যদি মেথডটি এমন হতো— add(component: Song), তবে playlist-এ শুধু Song যোগ করা যেত। কিন্তু বাস্তব জীবনে একটি playlist-এর ভেতর 
আরেকটি ছোট playlist ও থাকতে পারে। যেহেতু Song এবং Playlist উভয়ই IComponent-এর অংশ, তাই type হিসেবে IComponent ব্যবহার করলে 
playlist-এর ভেতরে Song এবং playlist উভয়কেই রাখা সম্ভব হয়।

program যখন IComponent দেখে, সে ধরে নেয় এর ভেতরে অবশ্যই play() বা get_name() মেথডগুলো আছে। তাই তাকে আলাদা করে বলতে হয় না যে 
এটি Song নাকি playlist। সে শুধু মেথডটি call করে এবং object-টি তার নিজের মতো করে কাজ করে।
"""

s1 = Song("Like a Rolling Stone", "Bob Dylan")
s2 = Song("Imagine", "John Lennon")

sub_list = Playlist("Favorite Collection")
sub_list.add(s2)

main_list = Playlist("Music Library")
main_list.add(s1)
main_list.add(sub_list)

if __name__ == '__main__':
    main_list.play()
