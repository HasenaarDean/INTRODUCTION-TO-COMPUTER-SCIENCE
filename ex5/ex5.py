############################################################################
# FILE : ex5.py
# WRITER : Yulia Feldman , sfhr.8fy8_a , 313012809
#          Dean Hasenaar , hasenaar, 313584401
#
# EXERCISE : intro2cs ex5 2016-2017
# DESCRIPTION: This file contains several functions that activates
#              a graphic interface through which the user can compare food
#              baskets between different stores.
############################################################################

import xml.etree.ElementTree as ET
import copy

EMPTY_STRING = ''
FINE = 1.25


def get_attribute(store_db, ItemCode, tag):
    """
    Returns the attribute (tag)
    of an Item with code: Itemcode in the given store
    """

    return store_db[ItemCode][tag]


def string_item(item):
    """
    Textual representation of an item in a store.
    Returns a string in the format of '[ItemCode] (ItemName)'
    """
    return '[' + item['ItemCode'] + ']\t{' + item['ItemName'] + '}'

  
def string_store_items(store_db):
    """
    Textual representation of a store.
    Returns a string in the format of:
    string representation of item1
    string representation of item2
    """

    str_store = EMPTY_STRING

    for item in store_db:
        str_store += string_item(store_db[item])
        str_store += '\n'

    return str_store


def read_prices_file(filename):
    """
    Read a file of item prices into a dictionary.  The file is assumed to
    be in the standard XML format of "misrad haclcala".
    Returns a tuple: store_id and a store_db, 
    where the first variable is the store name
    and the second is a dictionary describing the store. 
    The keys in this db will be ItemCodes of the different items and the
    values smaller  dictionaries mapping attribute names to their values.
    Important attributes include 'ItemCode', 'ItemName', and 'ItemPrice'
    """
    store_db = dict()
    tree = ET.parse(filename)
    root = tree.getroot()

    # finding store's id in XML file according to 'StoreId' tag
    element = root.find('StoreId')
    store_id = element.text

    # finding all store's items in XML file according to 'Items' tag
    element = root.find('Items')

    for item in element.findall('Item'):

        item_code = item.find('ItemCode').text
        store_db[item_code] = {item[0].tag: item[0].text}

        # finding each item's attributes
        for attribute in item.findall('./'):
            store_db[item_code].update({attribute.tag: attribute.text})

    return store_id, store_db


def filter_store(store_db, filter_txt):
    """
    Create a new dictionary that includes only the items 
    that were filtered by user.
    I.e. items that text given by the user is part of their ItemName. 
    Args:
    store_db: a dictionary of dictionaries as created in read_prices_file.
    filter_txt: the filter text as given by the user.
    """
    new_db = dict()
    items = store_db.keys()
    for item in items:
        if filter_txt in store_db[item]['ItemName']:
            new_db[item] = store_db[item]

    return new_db


def create_basket_from_txt(basket_txt): 
    """
    Receives text representation of few items (and maybe some garbage 
    at the edges)
    Returns a basket- list of ItemCodes that were included in basket_txt
    """
    temp = EMPTY_STRING
    temp_list = list()

    basket_txt = basket_txt.replace('\t', EMPTY_STRING)
    basket_txt = basket_txt.replace('\n', EMPTY_STRING)

    for i in range(len(basket_txt)):
        if basket_txt[i] == '[':
            for j in range(i+1, len(basket_txt)):
                if basket_txt[j] != ']':
                    temp += basket_txt[j]

                elif basket_txt[j] == ']':
                    temp_list.append(temp)
                    temp = EMPTY_STRING
                    break
    return temp_list


def get_basket_prices(store_db, basket):
    """
    Arguments: a store - dictionary of dictionaries and a basket - 
    a list of ItemCodes
    Go over all the items in the basket and create a new list that describes
    the prices of store items
    In case one of the items is not part of the store, its price will be None.
    """
    temp_list = list()
    for item in basket:
        if item not in store_db:
            temp_list.append(None)
        else:
            temp_list.append(float(store_db[item]['ItemPrice']))

    return temp_list


def sum_basket(price_list):
    """
    Receives a list of prices.
    Returns a tuple - the sum of the list (when ignoring Nones) and the
    number of missing items (Number of Nones).
    """
    price_sum = 0
    missing_items = 0

    for price in price_list:
        if price is None:
            missing_items += 1
        else:
            price_sum += price

    return price_sum, missing_items


def basket_item_name(stores_db_list, ItemCode):
    """
    stores_db_list is a list of stores (list of dictionaries of 
    dictionaries)
    Find the first store in the list that contains the item and return its
    string representation (as in string_item())
    If the item is not available in any of the stores return only [ItemCode]
    """
    for store in stores_db_list:
        if ItemCode in store:
            return string_item(store[ItemCode])

    return '[' + ItemCode + ']'


def save_basket(basket, filename):
    """
    Save the basket into a file
    The basket representation in the file will be in the following format:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    """
    file = open(filename, 'a')
    for i in range(len(basket)):
        file.write("[" + basket[i] + "]" + '\n')

    file.close()


def load_basket(filename):
    """
    Create basket (list of ItemCodes) from the given file.
    The file is assumed to be in the format of:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    """
    file_txt = open(filename, 'r')
    items_basket = file_txt.read()
    new_basket = create_basket_from_txt(items_basket)
    file_txt.close()

    return new_basket


def best_basket(list_of_price_list):
    """
    Arg: list of lists, where each inner list is list of prices as created
    by get_basket_prices.
    Returns the cheapest store (index of the cheapest list) given that a 
    missing item has a price of its maximal price in the other stores *1.25
    """

    max_prices_list = [0] * len(list_of_price_list[0])

    for lst in list_of_price_list:
        for index in range(len(lst)):

            if lst[index] is not None:
                price = lst[index]
                if price > max_prices_list[index]:
                    max_prices_list[index] = price

    total_price_list = list()

    for lst in list_of_price_list:
        sum_list = 0
        new_lst = copy.deepcopy(lst)

        for index in range(len(lst)):

            # if the item does not exist, the item gets 125% the value of the
            # maximal price:
            if lst[index] is None:
                new_lst[index] = price
                price = FINE * max_prices_list[index]

            sum_list += price

        total_price_list.append(sum_list)

    minimal = min(total_price_list)

    for index2 in range(len(total_price_list)):
        if total_price_list[index2] == minimal:
            return index2

