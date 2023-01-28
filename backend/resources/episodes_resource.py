import rest_utils
import pymysql
import json

from resources.base_resource import Base_Resource
from got_mongo import get_client

class Episodes():
    def __init__(self):
        super().__init__()
        self.db = "GoT"
        self.db_col = "episodes"

    def _get_client(self):
        """
        # We will connect to the MongoDB database to retrieve Episode data from the loaded GoT dataset.
        # DFF TODO There are so many anti-patterns here I do not know where to begin.
        :return: client connection
        """

        # DFF TODO OMG. Did this idiot really put password information in source code?
        # Sure. Let's just commit this to GitHub and expose security vulnerabilities
        #
        client = get_client()
        return client

    def get_resource_by_template(self,
                                 seasonNum,
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
        template["seasonNum"] = seasonNum
        #print(template)
        res = mycol.find(template)
        for doc in res:
            list_res.append(doc)
        return list_res

    def get_resource_by_num(self, season_num, episode_num):
        """
        :param id: The 'primary key' of the resource instance relative to the collection.
        :return: The resource or None if not found.
        """

        client = self._get_client()
        mycol = client[self.db][self.db_col]
        list_res = []
        res = mycol.find({"seasonNum": season_num, "episodeNum": episode_num})
        for doc in res:
            list_res.append(doc)
        return list_res

    def get_by_template(self,
                        path=None,
                        template=None,
                        field_list=None,
                        limit=None,
                        offset=None):
        """
        This is a logical abstraction of an SQL SELECT statement.

        Ignore path for now.

        Assume that
            - template is {'customerNumber': 101, 'status': 'Shipped'}
            - field_list is ['customerNumber', 'orderNumber', 'status', 'orderDate']
            - self.get_full_table_name() returns 'classicmodels.orders'
            - Ignore limit for now
            - Ignore offset for now

        This method would logically execute

        select customerNumber, orderNumber, status, orderDate
            from classicmodels.orders
            where
                customerNumber=101 and status='Shipped'

        :param path: The relative path to the resource. Ignore for now.
        :param template: A dictionary of the form {key: value} to be converted to a where clause
        :param field_list: The subset of the fields to return.
        :param limit: Limit on number of rows to return.
        :param offset: Offset in the list of matching rows.
        :return: The rows matching the query.
        """


        db_table_full_name = self.get_full_table_name()
        field_str = 'customerNumber, orderNumber, status, orderDate'
        if len(field_list) == 1:
            field_str = field_list[0]
        else:
            field_str = ",".join(field_list)


        sql = "select " + field_str + " from " + \
              db_table_full_name + " where customerNumber=%s and status=%s"

        #print("DEBUG SQL: ", sql)

        conn = self._get_connection()
        cursor = conn.cursor()
        res = cursor.execute(sql, (template['customerNumber'], template['status']))


        if res > 0:
            result = cursor.fetchall()
        else:
            result = None

        #print("DEBUG RES: ", res)
        #print("DEBUG RESULT: ", result)
        #print("DEBUG FIELD_STR ", field_str)

        return result

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

        db_table_full_name = self.get_full_table_name()
        ##new_resource_tup = ",".join(new_resource)

        #print("DEBUG NEW_RESOURCE ", new_resource)

        values_str = "(orderNumber, orderDate, customerNumber, status, requiredDate)"
        #values_str = "%s, \' %s\' " % (new_resource['customerNumber'], new_resource['status'])
        sql = "insert into " + db_table_full_name + values_str + "values (%s, %s, %s, %s, %s)"
        conn = self._get_connection()
        cursor = conn.cursor()
        res = cursor.execute(sql, ('11570', '2022-03-18', new_resource['customerNumber'], new_resource['status'], '2022-03-24'))

        return new_resource['customerNumber']


    def update_resource_by_id(self, id, new_values):
        """
        This is a logical abstraction of an SQL UPDATE statement.

        Assume that
            - id is 30100
            - new_values is {'customerNumber': 101, 'status': 'Shipped'}
            - self.get_full_table_name() returns 'classicmodels.orders'

        This method would logically execute.

        update classicmodels.orders
            set customerNumber=101, status=shipped
            where
                orderNumber=30100


        :param id: The 'primary key' of the resource to update
        :new_values: A dictionary defining the columns to update and the new values.
        :return: 1 if a resource was updated. 0 otherwise.
        """

        db_table_full_name = self.get_full_table_name()
        sql = "update " + db_table_full_name + " set customerNumber=%s, status=%s where orderNumber=%s"
        conn = self._get_connection()
        cursor = conn.cursor()
        #print("DEBUG SQL UPDATE = ", cursor.mogrify(sql, (new_values['customerNumber'], new_values['status'], id)))

        res = cursor.execute(sql, (new_values['customerNumber'], new_values['status'], id))

        return res


    def delete_resource_by_id(self, id):
        """
        This is a logical abstraction of an SQL DELETE statement.

        Assume that
            - id is 30100
            - new_values is {'customerNumber': 101, 'status': 'Shipped'}

        This method would logically execute.

        delete from classicmodels.orders
            where
                orderNumber=30100


        :param id: The 'primary key' of the resource to delete
        :return: 1 if a resource was deleted. 0 otherwise.
        """

        db_table_full_name = self.get_full_table_name()
        sql = "delete from " + db_table_full_name + " where orderNumber=%s"
        conn = self._get_connection()
        cursor = conn.cursor()

        #print("DEBUG SQL DELETE = ", cursor.mogrify(sql, (id)))

        res = cursor.execute(sql, (id))

        return res


if __name__ == "__main__":

    order_res = Orders()
    t_h = order_res.get_resource_by_id('10100')

    print(t_h)               #json.dumps(t_h, indent=2))
