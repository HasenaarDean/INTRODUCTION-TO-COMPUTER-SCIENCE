#############################################################
# FILE : article.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex10 2016 - 2017
# DESCRIPTION: In this file we implemented the Article class.
#############################################################


class Article:

    """
    This class contains articles as objects and each article carries its
    name in a string form and a set of all its neighbors' articles.
    """

    def __init__(self, article_title):

        """
        This method gets as an input the name of an article and saves a set
        of its neighbors' articles.
        """

        self._article_title = article_title
        self._collection = set()

    def get_title(self):

        """
        This method returns the article's name.
        """

        return self._article_title

    def add_neighbor(self, neighbor):

        """
        Add neighbor to article.
        :param neighbor: Article object
        :return: An updated set of all article's neighbors.
        """

        self._collection.add(neighbor)

    def get_neighbors(self):

        """
        This method returns a list of all article's neighbors.
        """

        neighbors_list = []
        for neighbor in self._collection:
            neighbors_list.append(neighbor)
        return neighbors_list

    def __repr__(self):

        """
        This method returns a string representing the article's name,
        comma, and a list of all neighbors' names.
        """

        neighbors = []
        for neighb in self.get_neighbors():
            neighbors.append(neighb.get_title())
        return str((self._article_title, neighbors))

    def __len__(self):

        """
        This method returns the number of article's neighbors.
        """

        return len(self._collection)

    def __contains__(self, article):

        """
        This method gets an article object and returns whether or not the
        article object is an exiting neighbors.
        """

        return article in self._collection

