DOT_FILE = "friends.dot"

import re
from collections import defaultdict
from pprint import pprint

def parse_graph():
    """
    parses simple undirected graph dot file
    the file must have one line per edge, no styling
    """
    lines = []
    with open(DOT_FILE, 'r') as fp:
        for line in fp.readlines():
            lines.append(line)

    # check first and last line
    assert re.fullmatch(r'(\w+\s+){2}\{\s*', lines[0])
    assert re.fullmatch(r'\s*\}\s*', lines[-1])
    friends = defaultdict(set)
    for line in lines[1:-1]:
        words = re.findall(r'\w+', line)
        assert len(words) == 2 # assuming the first and last word are nodes
        for edge in [words, list(reversed(words))]:
            friends[edge[0]].add(edge[-1])
    return friends

def count_friends(friends):
    """
    counts friends per person
    """
    friend_count = dict((k, len(v)) for k, v in friends.items())
    pprint(friend_count)

    average_friend_count = sum(friend_count.values()) / len(friend_count)

    pprint("Friend counts:")
    pprint(friend_count)
    pprint("Average friend count per person")
    pprint(average_friend_count)
    return friend_count

def count_friend_of_friends(friends, friend_count):
    """
    counts everyone's friends' friends
    """
    friends_friends_avg = dict()
    for person in friends.keys():
        friends_friends_avg[person] = sum(friend_count[friend]
            for friend in friends[person]
        ) / friend_count[person]

    average_friend_of_friends = sum(friends_friends_avg.values()) / len(friends_friends_avg)

    pprint("Each person's friends' average friend count:")
    pprint(friends_friends_avg)
    pprint("Overall Average Friends' Average Friend count")
    pprint(average_friend_of_friends)
    return friends_friends_avg

if __name__ == '__main__':
    friends = parse_graph()
    count_friend_of_friends(friends, count_friends(friends))
