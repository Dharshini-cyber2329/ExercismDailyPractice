"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    # If ticket is express
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue


def find_my_friend(queue, friend_name):
    # Return index of friend
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    # Insert at given index
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    # Remove by name
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    # Count occurrences
    return queue.count(person_name)


def remove_the_last_person(queue):
    # Remove last person and return name
    return queue.pop()


def sorted_names(queue):
    # Return sorted copy (do NOT change original)
    return sorted(queue)