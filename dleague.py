import rg


class Robot:
    def act(self, game):
        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        new_location = rg.toward(self.location, rg.CENTER_POINT)

        # TODO determine if there are any obstacles between me and the center
        # and adjust accordingly

        # move toward the center
        return ['move', new_location]
