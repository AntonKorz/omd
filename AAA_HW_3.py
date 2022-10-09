class CountVectorizer:
    """класс для кодирования текста"""

    def __init__(self):
        self.feature_names = []
        self.corpus = []

    def fit_transform(self, text: list) -> list:
        """функция принимает на вход корпус, составляет по нему словарь, который она сохраняет в атрибуты класса,
           затем кодирует корпус по полученному словарю"""

        slovarik = set()
        for fraze in text:                    # тут мы создаем словарик, приводим к нормальному виду наш корпус
            fraze = fraze.split()             # и сохраняем все в атрибуты класса
            self.corpus.append(fraze)
            slovarik = slovarik.union(fraze)
        self.feature_names = list(slovarik)

        count_matrix = [[0] * len(self.feature_names) for fraze in self.corpus]

        for i, fraze in enumerate(self.corpus):
            for j, feature in enumerate(self.feature_names):
                for word in fraze:
                    if word == feature:
                        count_matrix[i][j] += 1

        return count_matrix

    def get_feature_names(self):
        print(self.feature_names)


a = CountVectorizer()
print(a.fit_transform(['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste']))
a.get_feature_names()
