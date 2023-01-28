import rest_utils
import pymysql
import json

from resources.base_resource import Base_Resource
from got_mongo import get_client

class Users():
    def __init__(self):
        super().__init__()
        self.db = "StudyUsers"
        self.db_col = "Users"

        self.primary_key_fields = ["email"]

    def _get_client(self):
        """
        # We will connect to the MongoDB database to retrieve Episode data from the
        # DFF TODO There are so many anti-patterns here I do not know where to begin.
        :return: client connection
        """

        # DFF TODO OMG. Did this idiot really put password information in source code?
        # Sure. Let's just commit this to GitHub and expose security vulnerabilities
        #
        client = get_client()
        return client

    def get_by_template(self,
                        path=None,
                        template=None,
                        field_list=None,
                        limit=None,
                        offset=None):
        """
        This is a logical abstraction of MongoDB Query statement.

        Ignore path for now.

        Assume that
            - template is a dictionary of parameters you want passed in.
                    for instance {'episodeTitle': 'The Kingsroad', 'episodeAirDate': '2011-04-24'}

            - field_list is ['customerNumber', 'orderNumber', 'status', 'orderDate']
            - Ignore limit for now
            - Ignore offset for now

        # Have to implement query parameter processing!! --> use get_by_template format

        This method would logically execute

        :param path: The relative path to the resource. Ignore for now.
        :param template: A dictionary of the form {key: value} to be converted to a where clause
        :param field_list: The subset of the fields to return.
        :param limit: Limit on number of rows to return.
        :param offset: Offset in the list of matching rows.
        :return: The rows matching the query.
        """
        client = self._get_client()
        mycol = client[self.db][self.db_col]
        list_res = []
        res = mycol.find(template)
        for doc in res:
            list_res.append(doc)
        return list_res

    def get_resource_all(self, seasonNum, episodeNum):
        """
        :return: a list of all person records
        """
        client = self._get_client()
        mycol = client[self.db][self.db_col]
        list_res = []
        res = mycol.find({})
        for doc in res:
            list_res.append(doc)
        return list_res

    def create(self, new_resource):
        """

        Assume that
            - new_resource is {'customerNumber': 101, 'status': 'Shipped'}
            - self.get_full_table_name() returns 'classicmodels.orders'

        This function would logically perform

        insert into classicmodels.orders(customerNumber, status)
            values(101, 'Shipped')

        :param new_resource: A dictionary containing the data to insert.
        :return: Returns the values of the primary key columns in the order defined.
            In this example, the result would be [101]
        """
        client = self._get_client()
        mycol = client[self.db][self.db_col]

        x = mycol.insert_one(new_resource)
        return x.inserted_id


    def update_resource_by_id(resource_id, data):
        """
            return 
        """
        ### TODO: implement this ###

    def get_resource_by_num(self, seasonNum, episodeNum, sceneNum):
        """
        :param id: The 'primary key' of the resource instance relative to the collection.
        :return: The resource or None if not found.
        """

        client = self._get_client()
        mycol = client[self.db][self.db_col]
        list_res = []
        res = mycol.find({"seasonNum": seasonNum, "episodeNum": episodeNum})
        for doc in res:
            list_res.append(doc)
        return list_res[0]["scenes"][sceneNum]

    # def get_by_template(self,
    #                     path=None,
    #                     template=None,
    #                     field_list=None,
    #                     limit=None,
    #                     offset=None):
    #     """
    #     This is a logical abstraction of an SQL SELECT statement.

    #     Ignore path for now.

    #     Assume that
    #         - template is {'customerNumber': 101, 'status': 'Shipped'}
    #         - field_list is ['customerNumber', 'orderNumber', 'status', 'orderDate']
    #         - self.get_full_table_name() returns 'classicmodels.orders'
    #         - Ignore limit for now
    #         - Ignore offset for now

    #     This method would logically execute

    #     select customerNumber, orderNumber, status, orderDate
    #         from classicmodels.orders
    #         where
    #             customerNumber=101 and status='Shipped'

    #     :param path: The relative path to the resource. Ignore for now.
    #     :param template: A dictionary of the form {key: value} to be converted to a where clause
    #     :param field_list: The subset of the fields to return.
    #     :param limit: Limit on number of rows to return.
    #     :param offset: Offset in the list of matching rows.
    #     :return: The rows matching the query.
    #     """


    #     db_table_full_name = self.get_full_table_name()
    #     field_str = 'customerNumber, orderNumber, status, orderDate'
    #     if len(field_list) == 1:
    #         field_str = field_list[0]
    #     else:
    #         field_str = ",".join(field_list)


    #     sql = "select " + field_str + " from " + \
    #           db_table_full_name + " where customerNumber=%s and status=%s"

    #     #print("DEBUG SQL: ", sql)

    #     conn = self._get_connection()
    #     cursor = conn.cursor()
    #     res = cursor.execute(sql, (template['customerNumber'], template['status']))


    #     if res > 0:
    #         result = cursor.fetchall()
    #     else:
    #         result = None

    #     #print("DEBUG RES: ", res)
    #     #print("DEBUG RESULT: ", result)
    #     #print("DEBUG FIELD_STR ", field_str)

    #     return result


if __name__ == "__main__":

    # order_res = Orders()
    # t_h = order_res.get_resource_by_id('10100')


    #print(t_h)               #json.dumps(t_h, indent=2))

    # mydict = { "name": "Peter", "address": "Lowstreet 27" }

    usr = Users()
    # id = usr.create(mydict)
    # print(id)


    id = usr.get_by_template(template={"name":"Peter"})
    print(id)

    print()

    client = usr._get_client()
    mycol = client[usr.db][usr.db_col]
    list_res = []
    res = mycol.find({})
    for doc in res:
        list_res.append(doc)
    print(list_res)

