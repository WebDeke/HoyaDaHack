from abc import ABC, abstractmethod


class Base_Resource(ABC):

    def __init__(self):
        self.db_table = None
        self.db_schema = None

        # List of the fields, in order, that form the primary key
        self.primary_key_fields = None

    def get_full_table_name(self):
        return self.db_schema + "." + self.db_table

    @abstractmethod
    def get_resource_by_id(self, id):
        """

        :param id: The 'primary key' of the resource instance relative to the collection.
        :return: The resource or None if not found.
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass
