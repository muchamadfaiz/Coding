class TagCloud:
    # internally we make built in data strucuture for this example we create empty dictionary 
    # because we can get quickly the value of a key or a number of given tag
    def __init__(self):
        self.tags = {}
    # this function is to know if we have this tag in our dict? 
    # and if we don't have it we're going to set its value to 1
    # otherwise we're going to increment it by 1
    # def add(self, tag):
    #     self.tags[tag] = self.tags.get(tag, 0) + 1

    # next we're gonna make this dictionary smarter 
    # if we add with lower or upper case with same name its always increment the same (case sensitivity)
    #  so tags always convert first into lower case
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # next we gonna do read the count of the tag like this cloud['python']
    # to do this we need to use magic method called __getitem__ 
    def __getitem__ (self, tag):
        return self.tags.get(tag.lower(),0)

    # and then we gonna set item to the object with magic method called __setitem__
    def __setitem__ (self, tag, count):
        self.tags[tag.lower()] = count

    # and to count the data on dict
    def __len__ (self):
        return len(self.tags)

    # # and to make this iterable
    def __iter__ (self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Pawpaw")
cloud.add("Pawpaw")
cloud.add("pawpaw")
cloud.add("bilbil")
cloud.add("bilbil")
cloud.add("bilbil")
for a in cloud.tags:
    print(a)
# print(cloud.tags)