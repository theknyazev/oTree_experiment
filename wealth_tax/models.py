from otree.api import *

import random

sizes = ['Небольшое', 'Среднее', 'Большое']

class Constants(BaseConstants):
    name_in_url = 'two_factor'
    players_per_group = None
    num_rounds = 9

    origins = ['Природные ресурсы', 'Инвестиции', 'IT-стартап']
    sizes = ['Небольшое', 'Среднее', 'Большое']

    combos = [(o, s) for o in origins for s in sizes]


class Subsession(BaseSubsession):
    def creating_session(self):
        """Этот метод вызывается один раз при создании сессии.
        Здесь мы случайно перемешиваем 9 комбинаций для каждого участника."""
        for player in self.get_players():
            randomized_combos = random.sample(Constants.combos, len(Constants.combos))
            player.participant.vars['combos_order'] = randomized_combos


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    wealth_origin = models.StringField()
    wealth_size = models.StringField()

    tax_rate = models.IntegerField(
        label='Какую ставку налога на наследство Вы считаете справедливой (0–100)?',
        min=0,
        max=100
    )
