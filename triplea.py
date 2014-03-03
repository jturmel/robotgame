import rg


class Robot:

    corners = [(6, 6), (12, 12)]

    def act(self, game):

        # if we're on one of the corners, guard
        if self.location in self.corners:
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]
                #elif rg.dist(loc, self.location) <= 2:
                #    new_loc = rg.toward(self.location,
                #                        loc)
                #    return ['move', new_loc]

        distances = {}
        for corner in self.corners:
            distances[corner] = rg.dist(self.location, corner)

        new_loc = rg.toward(self.location, min(distances, key=distances.get))

        if 'obstacle' in rg.loc_types(new_loc):
            return ['guard']
        else:
            return ['move', new_loc]
