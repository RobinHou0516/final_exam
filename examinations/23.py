favorite_book = ['WSWW', 'sdgsdfg', 'sdfgb']

friend_book = favorite_book[:]

favorite_book.append("ybfs")
friend_book.append("sbsdfg")


print("My favorite types of book are:")
for book_item in favorite_book:
	print(book_item)


print("My friend's favorite types of book are:")
for book_item in friend_book:
	print(book_item)

print("ybfs" in favorite_book)
print("ybfs" not in friend_book)

print("sbsdfg" in friend_book)
print("sbsdfg" not in favorite_book)