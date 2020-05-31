#############################################################
# FILE : wikinetwork.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex10 2016 - 2017
# DESCRIPTION: In this file we implemented the WikiNetwork
# class and its methods.
#############################################################

from article import Article

# Magic Numbers:

NEW_LINE = '\n'
TAB_SEPARATING = '\t'


def read_article_links(file_name):

    """
    This function gets a string of the file's name and returns
    a list of all couples of articles, while each couple is a tuple of
    two names of the articles.
    """

    f = open(file_name, 'r')
    text = f.read()
    f.close()
    links = text.split(NEW_LINE)
    links.pop(-1)
    tuple_list = []
    for link in links:
        tuple_list.append(tuple(link.split(TAB_SEPARATING)))
    return tuple_list


class WikiNetwork:

    """
    This class represents the Wikipedia Network, contains all the articles'
    objects in a dictionary while the value of each article is an article
    object which is an exiting neighbor of the original article.
    """

    def __init__(self, link_list=[]):

        """
        This method gets a list of all the couples in a file and creates
        a dictionary of the articles' objects while the value of each article
        is an article object which is an exiting neighbor of the original
        article.
        """

        self._links = {}
        self.update_network(link_list)

    def update_network(self, link_list):

        """
        This method gets a list of couples of articles and updates the Network
        accordingly.
        """

        for art, neighb in link_list:
            if art not in self._links:
                self._links[art] = Article(art)
            if neighb not in self._links:
                self._links[neighb] = Article(neighb)
            self._links[art].add_neighbor(self._links[neighb])

    def get_articles(self):

        """
        This method returns a list of all the Articles objects of all the
        articles in the Network.
        """

        articles_lst = [article for article in self._links.values()]
        return articles_lst

    def get_titles(self):

        """
        This method returns a list of names of all the articles in the Network.
        """

        titles_name = [title for title in self._links]
        return titles_name

    def __contains__(self, title):

        """
        This method returns whether or not an article exists in the Network
        according to its name.
        """

        return title in self._links

    def __len__(self):

        """
        This method returns the number of the articles in the Network.
        """

        return len(self._links)

    def __repr__(self):

        """
        This method returns a string representing the Network: the string
        represents a dictionary which its keys are the articles' names, and
        its values are the articles.
        """

        return str(self._links)

    def __getitem__(self, title):

        """
        This method gets article's name and returns the object of the article
        which suits its name.
        """

        if self.__contains__(title):
            for art in self.get_articles():
                if title == art.get_title():
                    return art

    def page_rank(self, iters, d=0.9):

        """
        This method gets an int in param iters which represents the number
        of iterations that page_rank will be played, and also gets a real
        number 'd' between 0 to 1 which represents the size of donation to
        the neighbors articles. The method returns a list of the articles'
        names sorted firstly by size from biggest to smallest value and
        secondly by lexicographic order from smallest to biggest.
        """

        scores_dic = {}
        trans_dic = {}
        for key in self.get_titles():
            scores_dic[key] = 1.0
            trans_dic[key] = 0.0
        for _ in range(iters):
            for art in self._links.values():
                neighb_num = len(art)
                give = scores_dic[art.get_title()] * d / neighb_num
                scores_dic[art.get_title()] = 1.0 - d
                # Here we use the formula of Page Rank

                for neighb in art.get_neighbors():
                    trans_dic[neighb.get_title()] += give
            for key in scores_dic:
                scores_dic[key] += trans_dic[key]
                trans_dic[key] = 0
        page_list = [item[0] for item in sorted(scores_dic.items(),
                                                key=lambda artic: (-artic[1],
                                                                   artic[0]))]
        return page_list

    def jaccard_index(self, article_title):

        """
        This method gets article's name and returns a sorted list of all the
        sorted articles firstly by the index jaccard value from biggest to
        smallest value, and secondly by lexicographic order from smallest to
        biggest. if the article's name does not exist in the Network, nor the
        article in the Network has no exiting neighbors - then the method will
        return None.
        """

        jacc_dic = {}
        if article_title not in self._links:
                return None
        if len(self._links[article_title]) == 0:
            return None
        for title in self._links:
            article_neighbors = self._links[title].get_neighbors()
            title_neighbors = self._links[article_title].get_neighbors()
            intersection = set(title_neighbors) & set(article_neighbors)
            union = set(title_neighbors) | set(article_neighbors)
            jaccard_num = len(intersection) / len(union)
            jacc_dic[title] = jaccard_num
            # Here we used the formula of Jaccard

        jacc_sorted = [item[0] for item in sorted(jacc_dic.items(),
                                                  key=lambda artic:
                                                  (-artic[1], artic[0]))]
        return jacc_sorted

    def travel_path_iterator(self, article_title):

        """
        This method gets article's name and returns an iterator of all the
        articles' names in the path, according to an order. the path goes
        from the article through its exiting neighbors in the Network,
        while the order goes this way: first sort: each pace we choose
        the article with the highest entrance rank of other articles.
        second sort: we choose the article lexicographically, from
        lowest value to highest value.
        """

        if article_title not in self._links:
            return iter([])
        yield article_title
        rank_dic = {}
        for title in self._links:
            for neighb in self._links[title].get_neighbors():
                if neighb.get_title() in rank_dic:
                    rank_dic[neighb.get_title()] += 1
                else:
                    rank_dic[neighb.get_title()] = 1
        while self._links[article_title].get_neighbors():
            new_dic = {}
            for neighb in self._links[article_title].get_neighbors():
                if neighb.get_title() in rank_dic:
                    new_dic[neighb.get_title()] = rank_dic[neighb.get_title()]
                else:
                    new_dic[neighb.get_title()] = 0
            sorted_lst = [item[0] for item in sorted(new_dic.items(),
                                                     key=lambda artic:
                                                     (-artic[1], artic[0]))]
            article_title = sorted_lst[0]
            yield article_title

        return

    def friends_by_depth_helper(self, article, depth, friends_set):

        """
        This method helps us to implement the friends_by_depth method
        by using a recursion. the method gets an article, a depth positive
        integer (or 0) of closeness to other articles in the Network, and all
        the friends set (neighbors) of the article, and updates the friends
        set. The recursion stops when the depth of closeness becomes to 0,
        and of course the article itself also includes in the set.
        """

        if article in friends_set:
            return
        friends_set.add(article.get_title())
        if depth <= 0:
            return
        for neighbor in article.get_neighbors():
            self.friends_by_depth_helper(neighbor, depth-1, friends_set)

    def friends_by_depth(self, article_title, depth):

        """
        This method gets an article's name and a depth integer of closeness
        to other articles in the Network (positive integer or 0), and returns
        a list of all the friends' names in distance 'd' (depth param) from it.
        If the article's name does not exist in the Network, the method will
        return None.
        """

        if article_title not in self._links:
            return None
        article = self._links[article_title]
        friends_set = set()
        self.friends_by_depth_helper(article, depth, friends_set)
        return friends_set
