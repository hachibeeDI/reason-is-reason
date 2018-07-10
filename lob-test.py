from itertools import cycle

power_def = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']


class Field:
    def __init__(self, players, winner_queue):
        self.card = None
        self.players = players
        self.winner_queue = winner_queue

    def wipe(self):
        self.card = None

    def add_winner(self, p):
        self.winner_queue.append(p)
        p.rank = len(self.winner_queue)

    def round(self):
        last_player_id = None
        for p in cycle(self.players):
            if last_player_id == p.id:
                last_player_id = None
                yield len(self.winner_queue) != len(self.players)
            if p.has_finished():
                continue

            dealed = p.deal(self)
            if dealed:
                last_player_id = p.id
            if p.has_finished():
                self.add_winner(p)

    def receive(self, player):
        self.card = player.cards.pop()

    def commendation(self):
        for p in self.players:
            print(p.rank)

    def start_match(self):
        round_generator = self.round()

        rounding = True
        while rounding:
            rounding = next(round_generator)
            self.wipe()
        round_generator.close()


class Player:
    def __init__(self, id, cards):
        self.id = id
        self.cards = cards
        self.rank = None

    def can_deal(self, field: Field):
        if field.card is None:
            return True
        field_power = power_def.index(field.card)
        hand_power = power_def.index(self.cards[0])
        return field_power < hand_power

    def deal(self, field: Field):
        if self.can_deal(field):
            field.receive(self)
            return True
        return False

    def has_finished(self):
        return not self.cards

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return '{self.id}: {self.cards}'.format(self=self)


if __name__ == '__main__':
    cards = input().split(' ')
    field = Field(
        players=list(map(lambda i_card: Player(i_card[0] + 1, [i_card[1]]), enumerate(cards))),
        winner_queue=[],
    )
    field.start_match()
    field.commendation()
