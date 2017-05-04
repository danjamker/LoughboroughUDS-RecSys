import math
import operator
from collections import Counter

class collabrative_filtering:

    def __init__(self):

        self.data = {"Adam":["Recommender Systems","Infomation Research", "Drag Queens - A Fab History"],
                     "Ben": ["Startreck", "Thomas the Tank Engine", "Micheal Palins Great Train Journies"],
                     "Chris": ["Recommender Systems", "Thomas the Tank Engine", "Vouge", "Social Network Journal", "Elle"],
                     "Daniel": ["Recommender Systems", "Social Network Journal", "Elle"],
                     "Edward": ["Harry Potter", "Infomation Research", "The Gaurdian"],
                     "Frank": ["Recommender Systems", "Harry Potter", "Huffingtonpost"],
                     "Greg": ["Gardians of the Galixy", "Infomation Research", "Huffingtonpost"],
                     "Haray": ["Startreck", "Starewars", "Gardians of the Galixy"],
                     "Patrick": ["Recommender Systems", "Infomation Research", "Startrack"]}



    def person_corrolations(self, person_1, person_2):
        #TODO compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)
        return 1

    def most_similar_user(self, person, number_of_users = 3):
        users = {}
        for u, v in self.data.iteritems():
            if u != person:
                users[u] = self.person_corrolations(self.data[person], self.data[u])

        return dict(sorted(users.iteritems(), key=operator.itemgetter(1), reverse=True)[:number_of_users])

    def user_recommendations(self, person):

        similar_users = self.most_similar_user(person)
        print similar_users

        recs = {}
        user_count = {}
        for u, w in similar_users.iteritems():
            for i in self.data[u]:
                if i not in self.data[person]:
                    recs[i] = recs.get(i, 0) + (1 * w)
                    user_count[i] = user_count.get(i, 0) + 1

        for k, v in recs.iteritems():
            recs[k] = v/user_count[k]

        return sorted(recs.items(), key=operator.itemgetter(1), reverse=True)

    def time_decay(self,v , c, t):
        pass

if __name__ == '__main__':

    cf = collabrative_filtering()

    print cf.user_recommendations("Daniel")

