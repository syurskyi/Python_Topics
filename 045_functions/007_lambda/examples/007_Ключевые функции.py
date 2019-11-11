ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids))  # Lexicographic sort
# ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Integer sort
print(sorted_ids)
# ['id1', 'id2', 'id3', 'id22', 'id30', 'id100']
