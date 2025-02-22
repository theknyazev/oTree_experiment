from otree.api import *
from .models import Constants, Subsession, Group, Player

class Introduction(Page):
    """Первая страница, опционально можно объяснить правила эксперимента."""
    def is_displayed(self):
        return self.round_number == 1


class Decision(Page):
    """Главная страница для каждого из 9 раундов, где участник укажет ставку налога."""
    form_model = 'player'
    form_fields = ['tax_rate']

    def vars_for_template(self):
        combo = self.participant.vars['combos_order'][self.round_number - 1]
        origin, size = combo
        self.player.wealth_origin = origin
        self.player.wealth_size = size

        return {
            'origin': origin,
            'size': size,
        }
import json

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        all_rounds = self.player.in_all_rounds()
        bar_data = []
        for p in all_rounds:
            label = f"{p.wealth_origin} / {p.wealth_size}"
            bar_data.append({
                'label': label,
                'tax_rate': p.tax_rate
            })
        bar_data_json = json.dumps(bar_data, ensure_ascii=False)
        size_mapping = {
            'Небольшое': 1,
            'Среднее': 2,
            'Большое': 3,
        }
        scatter_data = []
        for p in all_rounds:
            x_value = size_mapping[p.wealth_size] 
            y_value = p.tax_rate
            scatter_data.append({'x': x_value, 'y': y_value})
        scatter_data_json = json.dumps(scatter_data, ensure_ascii=False)

        average_tax = round(sum([p.tax_rate for p in all_rounds]) / len(all_rounds), 2)

        return {
            'bar_data_json': bar_data_json,
            'scatter_data_json': scatter_data_json,
            'average_tax': average_tax,
        }

page_sequence = [Introduction, Decision, Results]
