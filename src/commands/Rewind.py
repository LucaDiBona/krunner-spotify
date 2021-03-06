from .Command import Command
from Config import getCommandName


class Rewind(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("REWIND_COMMAND"), spotify)

    def Match(self, query: str):
        query = query.strip(" ")
        time = query.split(":")
        if all(x.isnumeric() for x in time):
            if len(time) == 1:
                return [(self.command + " " + time[0], "Rewind: " + time[0] + " sec", "Spotify", 100, 100, {})]
            if len(time) == 2:
                return [(self.command + " " + str(60*int(time[0]) + int(time[1])), "Rewind: " + time[0] + " min " + time[1] + " sec", "Spotify", 100, 100, {})]
            if len(time) == 3:
                return [(self.command + " " + str(60*60 * int(time[0]) + 60*int(time[1]) + int(time[2])), "Rewind: " + time[0] + " hr " + time[1] + " min " + time[2] + " sec", "Spotify", 100, 100, {})]
        else:
            return [(self.command + " 5", "Rewind 5 seconds.", "Spotify", 100, 100, {}),
                    (self.command + " 15", "Rewind 15 seconds.","Spotify", 90, 100, {}),
                    (self.command + " 60", "Rewind 1 minute", "Spotify", 80, 100, {}),
                    (self.command + " 300", "Rewind 5 minutes","Spotify", 70, 100, {}),
                    (self.command + " 600", "Rewind 10 minutes", "Spotify", 60, 100, {})]

    def Run(self, data: str):
        newProgress_ms = self.spotify.current_playback()["progress_ms"] - (int(data) * 1000)
        if newProgress_ms < 0:
            newProgress_ms = 0
        self.spotify.seek_track(newProgress_ms)
