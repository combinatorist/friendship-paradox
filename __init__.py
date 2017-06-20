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
        assert len(words) in [2, 3] # assuming the first and last word are nodes
        for nodes in [words, words.reverse()]:
            friends[words[0]].add(words[-1])
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

def count_friend_of_friends():
    """
    counts everyone's friends' friends
    """
    pass

if __name__ == '__main__':
    count_friends(parse_graph())
